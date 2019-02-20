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

from brerpwsc import base
from brerpwsc import enums
import datetime
import lxml.etree
import sys


class CompositeOperationRequest(base.CompositeRequest):
    """
    BrERP Web Service Composite
    """

    def __init__(self):
        super(CompositeOperationRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.CompositeResponse

    def web_service_method(self):
        return enums.WebServiceMethod.compositeOperation

    def web_service_definition(self):
        return enums.WebServiceDefinition.compositeInterface


class CreateDataRequest(base.ModelCRUDRequest):
    """
    BrERP Web Service CreateData
    """

    def __init__(self):
        super(CreateDataRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return enums.WebServiceMethod.createData

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class CreateUpdateDataRequest(base.ModelCRUDRequest):
    """
    BrERP Web Service CreateUpdateData
    """

    def __init__(self):
        super(CreateUpdateDataRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return enums.WebServiceMethod.createUpdateData

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class DeleteDataRequest(base.ModelCRUDRequest):
    """
    BrERP Web Service DeleteDataRequest
    """

    def __init__(self):
        super(DeleteDataRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return enums.WebServiceMethod.deleteData

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class UpdateDataRequest(base.ModelCRUDRequest):
    """
    BrERP Web Service UpdateDataRequest
    """

    def __init__(self):
        super(UpdateDataRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return enums.WebServiceMethod.updateData

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class ReadDataRequest(base.ModelCRUDRequest):
    """
    BrERP Web Service ReadDataRequest
    """

    def __init__(self):
        super(ReadDataRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.WindowTabDataResponse

    def web_service_method(self):
        return enums.WebServiceMethod.readData

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class QueryDataRequest(base.ModelCRUDRequest):
    """
    BrERP Web Service QueryDataRequest
    """

    def __init__(self):
        super(QueryDataRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.WindowTabDataResponse

    def web_service_method(self):
        return enums.WebServiceMethod.queryData

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class GetListRequest(base.ModelGetListRequest):
    """
    BrERP Web Service GetListRequest
    """

    def __init__(self):
        super(GetListRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.WindowTabDataResponse

    def web_service_method(self):
        return enums.WebServiceMethod.getList

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class RunProcessRequest(base.ModelRunProcessRequest):
    """
    BrERP Web Service RunProcessRequest
    """

    def __init__(self):
        super(RunProcessRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.RunProcessResponse

    def web_service_method(self):
        return enums.WebServiceMethod.runProcess

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class SetDocActionRequest(base.ModelSetDocActionRequest):
    """
    BrERP Web Service SetDocActionRequest
    """

    def __init__(self):
        super(SetDocActionRequest, self).__init__()

    def web_service_response_model(self):
        return enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return enums.WebServiceMethod.setDocAction

    def web_service_definition(self):
        return enums.WebServiceDefinition.ModelADService


class RequestFactory(object):
    """
    RequestFactory. Class for build de Web Service Xml Document
    """
    PREFIX_0 = "_0"
    NAMESPACE_0 = "http://idempiere.org/ADInterface/1_0"
    PREFIX_SOAPENV = "soapenv"
    NAMESPACE_SOAPENV = "http://schemas.xmlsoap.org/soap/envelope/"
    ATTRIBUTE_XMLNS = "xmlns"
    NAMESPACE_XMLNS = "http://www.w3.org/2000/xmlns/"
    NSMAP = {PREFIX_0: NAMESPACE_0, PREFIX_SOAPENV: NAMESPACE_SOAPENV}

    def create_element_0(self, name, text=None):
        """
        Create element NAMESPACE_0 = "http://idempiere.org/ADInterface/1_0"
        :param name: Node
        :param text: Node text
        :return: Element
        """
        element = lxml.etree.Element('{%s}%s' % (self.NAMESPACE_0, name))
        if text:
            element.text = str(text)
        return element

    def create_element_soapenv(self, name, text=None):
        """
        Create element NAMESPACE_SOAPENV = "http://schemas.xmlsoap.org/soap/envelope/"
        :param name: Node
        :param text: Node text
        :return: Element
        """
        element = lxml.etree.Element('{%s}%s' % (self.NAMESPACE_SOAPENV, name))
        if text:
            element.text = str(text)
        return element

    def create_request(self, wsr):
        """
        Create request
        :param wsr: Web Service
        :return: Xml Request
        """
        return self.build_document(wsr)

    def build_document(self, wsr):
        """
        Build xml document
        :param wsr: Web Service
        :return: Xml Request
        """
        doc = lxml.etree.Element('{%s}%s' % (self.NAMESPACE_SOAPENV, 'Envelope'), nsmap=self.NSMAP)
        doc.append(self.create_element_soapenv('Header'))
        node_body = self.create_element_soapenv('Body')
        node_request = self.create_element_0(wsr.web_service_method().value)
        node_request.append(self.build_request(wsr))
        node_body.append(node_request)
        doc.append(node_body)
        return doc

    def build_request(self, wsr):
        """
        Build especific request
        :param wsr: Web Service
        :return: Xml Request
        """
        request = self.create_element_0(wsr.web_service_request_model().value)

        if wsr.web_service_request_model() == enums.WebServiceRequestModel.CompositeRequest:
            request.append(self.create_element_0('serviceType', wsr.web_service_type))

        request.append(self.build_model(wsr))

        if wsr.login:
            request.append(self.build_login(wsr.login))
        return request

    def build_login(self, log):
        """
        Build xml login
        :param log: Login request
        :return: Xml login
        """
        login = self.create_element_0('ADLoginRequest')

        if log.user:
            login.append(self.create_element_0('user', log.user))

        if log.password:
            login.append(self.create_element_0('pass', log.password))

        if log.lang:
            if isinstance(log.lang, enums.Language):
                temp_lang = log.lang.value
            else:
                temp_lang = log.lang
            login.append(self.create_element_0('lang', temp_lang))

        if log.client_id:
            login.append(self.create_element_0('ClientID', log.client_id))

        if log.role_id:
            login.append(self.create_element_0('RoleID', log.role_id))

        if log.org_id:
            login.append(self.create_element_0('OrgID', log.org_id))

        if log.warehouse_id:
            login.append(self.create_element_0('WarehouseID', log.warehouse_id))

        if log.stage:
            login.append(self.create_element_0('stage', log.stage))

        return login

    def build_model(self, wsr):
        """
        Build model for request
        :param wsr: Web Services
        :return: Xml Model
        """
        if wsr.web_service_request_model() == enums.WebServiceRequestModel.CompositeRequest:
            model = self.create_element_0('operations')
            if wsr.operations:
                for i in wsr.operations:
                    model.append(self.build_operation(i))
            return model
        elif wsr.web_service_request_model() == enums.WebServiceRequestModel.ModelCRUDRequest:
            model = self.create_element_0('ModelCRUD')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.table_name:
                model.append(self.create_element_0('TableName', wsr.table_name))

            if wsr.record_id:
                model.append(self.create_element_0('RecordID', wsr.record_id))

            if wsr.record_id_variable:
                model.append(self.create_element_0('recordIDVariable', wsr.record_id_variable))

            if wsr.action:
                model.append(self.create_element_0('Action', wsr.action))

            if wsr.filter:
                model.append(self.create_element_0('Filter', wsr.filter))

            if wsr.limit:
                model.append(self.create_element_0('Limit', wsr.limit))

            if wsr.offset:
                model.append(self.create_element_0('Offset', wsr.offset))

            if wsr.data_row:
                model.append(self.build_data_row(wsr.data_row))

            return model
        elif wsr.web_service_request_model() == enums.WebServiceRequestModel.ModelGetListRequest:
            model = self.create_element_0('ModelGetList')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.filter:
                model.append(self.create_element_0('Filter', wsr.filter))

            if wsr.ad_reference_id:
                model.append(self.create_element_0('AD_Reference_ID', wsr.ad_reference_id))

            return model
        elif wsr.web_service_request_model() == enums.WebServiceRequestModel.ModelRunProcessRequest:
            model = self.create_element_0('ModelRunProcess')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.ad_process_id:
                model.set('AD_Process_ID', wsr.ad_process_id)

            if wsr.ad_menu_id:
                model.set('AD_Menu_ID', wsr.ad_menu_id)

            if wsr.ad_record_id:
                model.set('AD_Record_ID', wsr.ad_record_id)

            if wsr.doc_action:
                model.set('DocAction', wsr.doc_action)

            if wsr.param_values:
                model.append(self.build_param_values(wsr.param_values))

            return model
        elif wsr.web_service_request_model() == enums.WebServiceRequestModel.ModelSetDocActionRequest:
            model = self.create_element_0('ModelSetDocAction')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.table_name:
                model.append(self.create_element_0('tableName', wsr.table_name))

            if wsr.record_id:
                model.append(self.create_element_0('recordID', wsr.record_id))

            if wsr.record_id_variable:
                model.append(self.create_element_0('recordIDVariable', wsr.record_id_variable))

            if wsr.doc_action:
                if isinstance(wsr.doc_action, enums.DocAction):
                    model.append(self.create_element_0('docAction', str(wsr.doc_action.value)))
                else:
                    model.append(self.create_element_0('docAction', str(wsr.doc_action)))

            return model
        return self.create_element_0('NoModel')

    def build_operation(self, oper):
        """
        Build operation xml for Composite
        :param oper: Operation
        :return: Xml operation
        """
        operation = self.create_element_0('operation')
        operation.set('preCommit', str(oper.pre_commit).lower())
        operation.set('postCommit', str(oper.post_commit).lower())
        operation.append(self.create_element_0('TargetPort', oper.web_service.web_service_method().value))
        operation.append(self.build_model(oper.web_service))
        return operation

    def build_data_row(self, row):
        """
        Build row
        :param row: Data for row
        :return: Xml Row
        """
        data_row = self.create_element_0('DataRow')
        for i in row:
            data_row.append(self.build_field(i))
        return data_row

    def build_param_values(self, params):
        """
        Build row for params
        :param params: Params
        :return: Xml for params
        """
        param_values = self.create_element_0('ParamValues')
        for i in params:
            param_values.append(self.build_field(i))
        return param_values

    def build_field(self, f):
        """
        Build fields
        :param f: Field
        :return: Xml Field
        """
        field = self.create_element_0('field')

        if f.column:
            field.set('column', f.column)

        if f.type:
            field.set('type', f.type)

        if f.lval:
            field.set('lval', f.lval)

        if f.disp is not None:
            field.set('disp', f.disp)

        if f.edit is not None:
            field.set('edit', f.edit)

        if f.error is not None:
            field.set('error', f.error)

        if f.error_val:
            field.set('errorVal', f.error_val)

        if f.value:
            value = f.value
            temp_value = ''
            if isinstance(value, bool):
                temp_value = 'Y' if value else 'N'
            elif isinstance(value, datetime.datetime):
                temp_value = datetime.datetime.strftime(value, '%Y-%m-%d %H:%M:%S')
            elif isinstance(value, enums.DocAction):
                temp_value = value.value
            elif isinstance(value, enums.DocStatus):
                temp_value = value.value
            else:
                if sys.version_info[0] == '2':
                    temp_value = str(value).decode('UTF-8')
                else:
                    # Python 3 Code, sys.version_info[0] == '3'
                    temp_value = str(value)

            field.append(self.create_element_0('val', temp_value))

        return field
