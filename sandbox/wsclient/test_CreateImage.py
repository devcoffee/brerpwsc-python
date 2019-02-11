# -*- encoding: utf-8 -*-
"""
Produto: BrERP Web Service Client - Python                                                    
Copyright (C) 2018  devCoffee Sistemas de Gestão Integrada                 
                                                                           
Este arquivo é parte do DocxSimplifier que é software livre; você pode     
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

from brerpwsc.base import LoginRequest
from brerpwsc.base import Operation
from brerpwsc.base import Field
from brerpwsc.request import CreateDataRequest
from brerpwsc.request import CompositeOperationRequest
from brerpwsc.enums import WebServiceResponseStatus
from brerpwsc.net import WebServiceConnection
from random import randint

import traceback

url = 'https://test.idempiere.org'
urls = 'https://test.idempiere.org'

# CREATE LOGIN
login = LoginRequest()
login.client_id = 11
login.org_id = 0
login.role_id = 102
login.warehouse_id = 50002

# CREATE WEBSERVICE FOR IMAGE
path_image = '../documents/idempiere-logo.png'

ws1 = CreateDataRequest()
ws1.web_service_type = 'CreateImageTest'
ws1.data_row.append(Field('Name', 'idempiere-logo.png'))
ws1.data_row.append(
    Field('Description', 'Test Create BPartner and Logo with Python'))

# CREATE BINARY FIELD
binary_field = Field('BinaryData')
with open(path_image, 'rb') as file:
    binary_field.set_byte_value(file.read())
ws1.data_row.append(binary_field)

# CREATE WEBSERVICE FOR BPARTNER
ws2 = CreateDataRequest()
ws2.web_service_type = 'CreateBPartnerTest'
ws2.data_row.append(Field('Name', 'Business Partner Test'))
ws2.data_row.append(Field('Value', str(randint(1000000, 10000000))))
# ws2.data_row.append(Field('TaxID', '987654321'))
ws2.data_row.append(Field('Logo_ID', '@AD_Image.AD_Image_ID'))

# CREATE COMPOSITE
ws0=CompositeOperationRequest()
ws0.login=login
ws0.operations.append(Operation(ws1))
ws0.operations.append(Operation(ws2))
ws0.web_service_type='CompositeBPartnerTest'

# CREATE CONNECTION
wsc=WebServiceConnection()
wsc.url=url
wsc.attempts=3
wsc.app_name='Test from python'

# SEND CONNECTION
try:
    response=wsc.send_request(ws0)
    wsc.print_xml_request()
    wsc.print_xml_response()

# GET THE RESPONSE
    if response.status == WebServiceResponseStatus.Error:
        print('Error: ', response.error_message)
    else:
        print('Response: ', str(response.web_service_response_model()))
        for res in response.responses:
            print('Response: ', str(res.web_service_response_model()))
        print('-' * 45)
        print('Web Service Type: ', ws0.web_service_type)
        print('Attempts: ', str(wsc.attempts_request))
        print('Time: ', str(wsc.time_request))
except:
    traceback.print_exc()
