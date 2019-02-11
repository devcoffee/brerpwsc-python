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

from brerpwsc.request import CreateDataRequest
from brerpwsc.request import CompositeOperationRequest
from brerpwsc.request import SetDocActionRequest
from brerpwsc.base import LoginRequest
from brerpwsc.base import Operation
from brerpwsc.enums import WebServiceResponseStatus
from brerpwsc.net import WebServiceConnection
from brerpwsc.base import Field
from brerpwsc.enums import DocAction
import traceback

url = 'http://localhost:8031'
urls = 'https://localhost:8431'

login = LoginRequest()
login.client_id = 11
login.org_id = 0
login.role_id = 102
login.password = 'System'
login.user = 'SuperUser'

ws1 = CreateDataRequest()
ws1.web_service_type = 'CreateMovementTest'
ws1.data_row = [
    Field('C_DocType_ID', 143),
    Field('MovementDate', '2015-10-25 00:00:00'),
    Field('AD_Org_ID', '11')
]

ws2 = CreateDataRequest()
ws2.web_service_type = 'CreateMovementLineTest'
ws2.data_row = [
    Field('M_Movement_ID', '@M_Movement.M_Movement_ID'), 
    Field('M_Product_ID', '138'),
    Field('MovementQty', '1'), 
    Field('M_Locator_ID', '50001'), 
    Field('M_LocatorTo_ID', '50000'),
    Field('AD_Org_ID', '11')
]

ws3 = SetDocActionRequest()
ws3.web_service_type = 'DocActionMovementTest'
ws3.doc_action = DocAction.Complete
ws3.record_id_variable = '@M_Movement.M_Movement_ID'

ws0 = CompositeOperationRequest()
ws0.login = login
ws0.operations.append(Operation(ws1))
ws0.operations.append(Operation(ws2))
ws0.operations.append(Operation(ws3))
ws0.web_service_type = 'CompositeMovementTest'

wsc = WebServiceConnection()
wsc.url = urls
wsc.attempts = 3
wsc.app_name = 'Test from python'

try:
    response = wsc.send_request(ws0)
    wsc.print_xml_request()
    wsc.print_xml_response()

    if response.status == WebServiceResponseStatus.Error:
        print('Error: ' + response.error_message)
    else:
        print('Response: ' + str(response.web_service_response_model()))
        for res in response.responses:
            print('Response: ' + str(res.web_service_response_model()))
        print('---------------------------------------------')
        print('Web Service Type: ' + ws0.web_service_type)
        print('Attempts: ' + str(wsc.attempts_request))
        print('Time: ' + str(wsc.time_request))
except:
    traceback.print_exc()
