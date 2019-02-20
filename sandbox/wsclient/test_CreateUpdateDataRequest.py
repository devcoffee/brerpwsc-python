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

from brerpwsc.request import CreateUpdateDataRequest
from brerpwsc.base import LoginRequest
from brerpwsc.enums import WebServiceResponseStatus
from brerpwsc.net import WebServiceConnection
from brerpwsc.base import Field
import traceback
import random

url = 'https://teste.brerp.com.br'

login = LoginRequest()
login.client_id = 1000000
login.org_id = 5000003
login.role_id = 1000000
login.warehouse_id = 5000007
login.password = 'sua senha aqui'
login.user = 'superuser @ brerp.com.br'

ws = CreateUpdateDataRequest()
ws.web_service_type = 'CreateUpdateBPartnerTest'
ws.login = login

ws.data_row = [
    Field('Name', 'Test BPartner Update'), 
    Field('Value', 9515330),
    Field('TaxID', '987654321')
]

wsc = WebServiceConnection()
wsc.url = url
wsc.attempts = 3
wsc.app_name = 'Test from python'

try:
    response = wsc.send_request(ws)
    wsc.print_xml_request()
    wsc.print_xml_response()

    if response.status == WebServiceResponseStatus.Error:
        print('Error: ', response.error_message)
    else:
        print('RecordID: ', str(response.record_id))
        for field in response.output_fields:
            print('{}: {}'.format(
                str(field.column),
                str(field.value)
            ))
        print('-' * 45)
        print('Web Service Type: ', ws.web_service_type)
        print('Attempts: ', str(wsc.attempts_request))
        print('Time: ', str(wsc.time_request))
except:
    traceback.print_exc()
