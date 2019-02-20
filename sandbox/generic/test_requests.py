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

import urllib3
import requests


urllib3.disable_warnings()

url = 'http://teste.brerp.com.br/ADInterface/services/ModelADService'
headers = {
    'user-agent': 'my-app/0.0.1',
    'content-type': 'text/xml; charset=UTF-8'
}


def test_xml():
    xml = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:_0="http://idempiere.org/ADInterface/1_0">
    <soapenv:Header/>
    <soapenv:Body>
    <_0:queryData>
    <_0:ModelCRUDRequest>
    <_0:ModelCRUD>
    <_0:serviceType>QueryBPartnerTest</_0:serviceType>
    </_0:ModelCRUD>
    <_0:ADLoginRequest>
    <_0:user>superuser @ brerp.com.br</_0:user>
    <_0:pass>Sua Senha Aqui</_0:pass>
    <_0:ClientID>1000000</_0:ClientID>
    <_0:RoleID>1000000</_0:RoleID>
    </_0:ADLoginRequest>
    </_0:ModelCRUDRequest>
    </_0:queryData>
    </soapenv:Body>
    </soapenv:Envelope>
    """
    return xml


def test_xml_file():
    test_file = open('../../documents/CreateBPartnerTest_request.xml', 'r')
    return test_file.read()


request = test_xml()
print('Request:' + request)

# timeout on seconds
try:
    r = requests.post(url, data=request, headers=headers,
                      verify=False, timeout=2)
except Exception as e:
    print(e)
else:
    print('Status: {}'.format(str(r.status_code)))
    print('Headers: {}'.format(str(r.headers)))
    print('Response: {}'.format(str(r.text)))
