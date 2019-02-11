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

from brerpwsc.net import WebServiceConnection

url = 'http://dev11.devcoffee.com.br/ADInterface/services/ModelADService'
urls = 'https://localhost:8431/ADInterface/services/ModelADService'


def test_xml():
    test_file = open('../documents/ReadBPartnerTest_request.xml', 'r')
    return test_file.read()


wsc = WebServiceConnection()
wsc.url = url
wsc.attempts = 3
try:
    response = wsc.send_request(test_xml())
except Exception as e:
    print('Error', str(e))
else:
    wsc.print_xml_response()
finally:
    print(wsc.attempts_request)
    print(wsc.time_request)
    print(wsc.response_status)
