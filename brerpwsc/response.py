# -*- encoding: utf-8 -*-
"""
Produto: BrERP Web Service Client - Python                                                    
Copyright (C) 2018  devCoffee Sistemas de Gestão Integrada                 
                                                                           
Este arquivo é parte do BrERP Web Service Client - Python que é software livre; você pode     
redistribuí-lo e/ou modificá-lo sob os termos da Licença Pública Geral GNU,
conforme publicada pela Free Software Foundation; tanto a versão 3 da      
Licença como (a seu critério) qualquer versão mais nova.                   
                                                                           
                                                                           
Este programa é distribuído na expectativa de ser útil, mas SEM            
QUALQUER GARANTIA; sem mesmo a garantia implícita de                       
COMERCIALIZAÇÃO ou de ADEQUAÇÃO A QUALQUER PROPÓSITO EM                    
PARTICULAR. Consulte a Licença Pública Geral GNU para obter mais           
detalhes.                                                                  
                                                                           
Você deve ter recebido uma cópia da Licença Pública Geral GNU              
junto com este programa; se não, escreva para a Free Software              
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA                   
02111-1307, USA  ou para devCoffee Sistemas de Gestão Integrada,           
Rua Paulo Rebessi 665 - Cidade Jardim - Leme/SP - Brasil.                           
"""

"""
Contributor: @pozzisan <pedropozzif@gmail.com>
"""

import brerpwsc.base
import brerpwsc.enums
import lxml.etree
import copy


class CompositeResponse(brerpwsc.base.WebServiceResponse):
    """
    Composite class response 
    """

    def __init__(self):
        super(CompositeResponse, self).__init__()
        self.responses = []

    def web_service_response_model(self):
        return brerpwsc.enums.WebServiceResponseModel.CompositeResponse


class RunProcessResponse(brerpwsc.base.WebServiceResponse):
    """
    Run process class response
    """

    def __init__(self):
        super(RunProcessResponse, self).__init__()
        self.log_info = ''
        self.summary = ''

    def web_service_response_model(self):
        return brerpwsc.enums.WebServiceResponseModel.RunProcessResponse


class StandardResponse(brerpwsc.base.WebServiceResponse):
    """
    Standard response class
    """

    def __init__(self):
        super(StandardResponse, self).__init__()
        self.record_id = 0
        self.output_fields = []

    def web_service_response_model(self):
        return brerpwsc.enums.WebServiceResponseModel.StandardResponse


class WindowTabDataResponse(brerpwsc.base.WebServiceResponse):
    """
    Window tab response class for query
    """

    def __init__(self):
        super(WindowTabDataResponse, self).__init__()
        self.num_rows = 0
        self.total_rows = 0
        self.start_row = 0
        self.data_set = []

    def web_service_response_model(self):
        return brerpwsc.enums.WebServiceResponseModel.WindowTabDataResponse


class ResponseFactory():
    """
    ResponseFactory. Class for build responses
    """
    NAMESPACE_0 = "http://idempiere.org/ADInterface/1_0"
    RESPONSE_DEFINITION = ('compositeOperationResponse', 'createDataResponse', 'createUpdateDataResponse',
                           'deleteDataResponse', 'setDocActionResponse', 'getListResponse', 'queryDataResponse',
                           'readDataResponse', 'runProcessResponse', 'updateDataResponse')
    FAULT_DEFINITION = ('Fault')
    BODY_DEFINITION = ('Envelope', 'Body')

    def find_elements_0(self, root, name):
        """
        Find elements into xml document
        :param root: Xml element
        :param name: Element to find
        :return: Elements
        """
        return root.findall('.//{%s}%s' % (self.NAMESPACE_0, name))

    def create_response(self, response_model, xml_response):
        """
        Create response from xml document
        :param response_model: Response object
        :param xml_response: xml raw
        :return: Response object
        """

        if response_model == brerpwsc.enums.WebServiceResponseModel.StandardResponse:
            operation = self.create_standard_response
            response = StandardResponse()
        elif response_model == brerpwsc.enums.WebServiceResponseModel.CompositeResponse:
            operation = self.create_composite_response
            response = CompositeResponse()
        elif response_model == brerpwsc.enums.WebServiceResponseModel.RunProcessResponse:
            operation = self.create_run_process_response
            response = RunProcessResponse()
        elif response_model == brerpwsc.enums.WebServiceResponseModel.WindowTabDataResponse:
            operation = self.create_window_tab_data_response
            response = WindowTabDataResponse()

        for element in xml_response.iter():
            temp_tag = element.tag.rsplit('}', 1)[-1]

            if temp_tag in self.BODY_DEFINITION:
                continue

            if temp_tag in self.FAULT_DEFINITION:
                return self.has_fault_error(response, element)

            if temp_tag in self.RESPONSE_DEFINITION:
                return operation(response, element)

        return None

    def has_fault_error(self, response, xml_response):
        """
        Find fault error from xml
        :param response: Response object
        :param xml_response: Raw xml
        :return: Response
        """
        response.status = brerpwsc.enums.WebServiceResponseStatus.Error

        for element in xml_response.iter():
            temp_tag = element.tag.rsplit('}', 1)[-1]
            temp_text = element.text

            if temp_tag in self.FAULT_DEFINITION:
                continue

            if temp_tag == 'faultstring':
                response.error_message = temp_text

        return response

    def create_standard_response(self, response, xml_response):
        """
        Creates standard response object
        :param response: Response object
        :param xml_response: Raw xml
        :return: StandardResponse
        """
        standard_responses = self.find_elements_0(xml_response, 'StandardResponse')

        if len(standard_responses) <= 0:
            return response

        standard_response = standard_responses[0]
        response.record_id = standard_response.get('RecordID')
        is_error = True if str(standard_response.get('IsError')).lower() in ('true', 'yes') else False

        if is_error:
            response.status = brerpwsc.enums.WebServiceResponseStatus.Error
            errors = self.find_elements_0(standard_response, 'Error')
            if len(errors) > 0:
                response.error_message = errors[0].text
        else:
            out_fields = self.find_elements_0(standard_response, 'outputField')
            for i in out_fields:
                field = brerpwsc.base.Field()
                field.column = i.get('column')
                field.value = i.get('value')
                response.output_fields.append(field)
        return response

    def create_composite_response(self, response, xml_response):
        """
        Build composite response
        :param response: Response object
        :param xml_response: Raw xml
        :return: CompositeResponse
        """
        standard_responses = self.find_elements_0(xml_response, 'StandardResponse')

        for sr in standard_responses:
            wtd_responses = self.find_elements_0(sr, 'WindowTabData')
            process_responses = self.find_elements_0(xml_response, 'RunProcessResponse')

            if len(wtd_responses) > 0:
                temp_element = lxml.etree.Element("temp")
                temp_element.append(copy.deepcopy(wtd_responses[0]))
                partial_response = self.create_window_tab_data_response(WindowTabDataResponse(), temp_element)
            elif len(process_responses) > 0:
                temp_element = lxml.etree.Element("temp")
                temp_element.append(copy.deepcopy(wtd_responses[0]))
                partial_response = self.create_run_process_response(RunProcessResponse(), temp_element)
            else:
                temp_element = lxml.etree.Element("temp")
                temp_element.append(copy.deepcopy(sr))
                partial_response = self.create_standard_response(StandardResponse(), temp_element)

            if not partial_response or partial_response.status == brerpwsc.enums.WebServiceResponseStatus.Error:
                response.status = brerpwsc.enums.WebServiceResponseStatus.Error
                response.error_message = partial_response.error_message

            response.responses.append(partial_response)

        return response

    def create_run_process_response(self, response, xml_response):
        """
        Build run process response
        :param response: Response object
        :param xml_response: Raw xml
        :return: RunProcessResponse
        """
        process_responses = self.find_elements_0(xml_response, 'RunProcessResponse')

        if len(process_responses) <= 0:
            return response

        process_response = process_responses[0]
        is_error = True if str(process_response.get('IsError')).lower() in ('true', 'yes') else False

        if is_error:
            response.status = brerpwsc.enums.WebServiceResponseStatus.Error
            errors = self.find_elements_0(process_response, 'Error')
            if len(errors) > 0:
                response.error_message = errors[0].text
        else:
            summarys = self.find_elements_0(process_response, 'Summary')
            infos = self.find_elements_0(process_response, 'LogInfo')

            if len(summarys) > 0:
                response.summary = summarys[0].text

            if len(infos) > 0:
                response.log_info = infos[0].text

        return response

    def create_window_tab_data_response(self, response, xml_response):
        """
        Build windows tab response for query request
        :param response: Response object
        :param xml_response: Raw xml
        :return: WindowTabResponse
        """
        wtd_responses = self.find_elements_0(xml_response, 'WindowTabData')

        if len(wtd_responses) <= 0:
            return response

        wtd_response = wtd_responses[0]
        errors = self.find_elements_0(wtd_response, 'Error')

        if len(errors) > 0:
            response.status = brerpwsc.enums.WebServiceResponseStatus.Error
            response.error_message = errors[0].text
        else:
            successs = self.find_elements_0(wtd_response, 'Success')
            if len(successs) > 0:
                if successs[0].text.lower() in ('false', 'no'):
                    response.status = brerpwsc.enums.WebServiceResponseStatus.Unsuccessful
                    return response

            num_rows = int(wtd_response.get('NumRows')) or 0
            response.num_rows = num_rows

            start_row = int(wtd_response.get('StartRow')) or 0
            response.start_row = start_row

            total_rows = int(wtd_response.get('TotalRows')) or 0
            response.total_rows = total_rows

            rows = self.find_elements_0(wtd_response, 'DataRow')

            for row in rows:
                fields = self.find_elements_0(row, 'field')
                temp_row = []
                response.data_set.append(temp_row)
                for f in fields:
                    field = brerpwsc.base.Field()
                    field.column = f.get('column')
                    values = self.find_elements_0(f, 'val')
                    if len(values) > 0:
                        field.value = values[0].text
                    temp_row.append(field)

        return response
