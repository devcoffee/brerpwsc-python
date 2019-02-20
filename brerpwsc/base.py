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

from abc import ABCMeta
from abc import abstractmethod
from base64 import b64encode
from base64 import b64decode
from datetime import datetime
from brerpwsc import enums
from sys import version_info


class LoginRequest(object):
    """
    Class to abstract the BrERP Web Service Login
    """

    def __init__(self):
        self.user = ''
        self.password = ''
        self.lang = enums.Language.en_US
        self.client_id = 0
        self.role_id = 0
        self.org_id = 0
        self.warehouse_id = 0
        self.stage = 0


class Field(object):
    """
    Class to abstract the BrERP Web Service Login
    """

    def __init__(self, column='', value=''):
        self.value = value
        self.column = column
        self.type = ''
        self.lval = ''
        self.disp = None
        self.edit = None
        self.error = None
        self.error_val = ''

    def set_byte_value(self, val=None):
        """
        Convert byte to unicode String
        :param val: Value to unicode String
        :return: None
        """
        if val:
            if version_info[0] == '2':
                self.value = b64encode(val)
            else:
                b64value = b64encode(val)
                self.value = b64value.decode('utf-8', 'xmlcharrefreplace')

    def get_byte_value(self):
        """
        Return decoded Base64 Byte Value
        :return: Bytes
        """
        return b64decode(self.value) if self.value else False

    def get_boolean_value(self):
        """
        Convert value to boolean
        :return: Boolean
        """
        if self.value:
            temp_value = str(self.value).upper()

            return True if temp_value in ('Y', 'YES') else False
        return False

    def get_type(self):
        """
        Gets de type of value
        :return: Type of value
        """
        return type(self.value)

    def get_date_value(self):
        """
        Convert the value to Date
        :return: Date
        """
        if self.value:
            temp_value = str(self.value)
            return datetime.strptime(temp_value, '%Y-%m-%d %H:%M:%S')
        return None

    def get_doc_status_value(self):
        """
        Convert the value to DocStatus
        :return: DocStatus
        """
        if self.value:
            temp_value = str(self.value)
            return enums.DocStatus(temp_value)
        return None

    def get_doc_action_value(self):
        """
        Convert the value to DocAction
        :return: DocAction
        """
        if self.value:
            temp_value = str(self.value)
            return enums.DocAction(temp_value)
        return None


class Operation(object):
    """
    Operation For composite operation
    """

    def __init__(self, web_service=None, pre_commit=False, post_commit=False):
        self.web_service = web_service
        self.pre_commit = pre_commit
        self.post_commit = post_commit


class WebServiceResponse(object):
    """
    Class to abstract the BrERP response
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.error_message = ''
        self.web_service_type = ''
        self.status = enums.WebServiceResponseStatus.Successful

    @abstractmethod
    def web_service_response_model(self):
        pass


class WebServiceRequest(object):
    """
    Class to abstract the BrERP request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.login = LoginRequest()
        self.web_service_type = ''

    @abstractmethod
    def web_service_response_model(self):
        pass

    @abstractmethod
    def web_service_request_model(self):
        pass

    @abstractmethod
    def web_service_method(self):
        pass

    @abstractmethod
    def web_service_definition(self):
        pass


class ModelCRUDRequest(WebServiceRequest):
    """
    ModelCRUDRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelCRUDRequest, self).__init__()
        self.data_row = []
        self.offset = 0
        self.limit = 0
        self.filter = ''
        self.action = None
        self.record_id = 0
        self.record_id_variable = ''
        self.table_name = ''

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelCRUDRequest


class ModelGetListRequest(WebServiceRequest):
    """
    ModelGetListRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelGetListRequest, self).__init__()
        self.ad_reference_id = 0
        self.filter = ''

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelGetListRequest


class ModelRunProcessRequest(WebServiceRequest):
    """
    ModelRunProcessRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelRunProcessRequest, self).__init__()
        self.param_values = []
        self.doc_action = None
        self.ad_record_id = 0
        self.ad_menu_id = 0
        self.ad_process_id = 0

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelRunProcessRequest


class ModelSetDocActionRequest(WebServiceRequest):
    """
    ModelSetDocActionRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelSetDocActionRequest, self).__init__()
        self.table_name = ''
        self.record_id = 0
        self.record_id_variable = ''
        self.doc_action = None

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelSetDocActionRequest


class CompositeRequest(WebServiceRequest):
    """
    CompositeRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(CompositeRequest, self).__init__()
        self.operations = []

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.CompositeRequest
