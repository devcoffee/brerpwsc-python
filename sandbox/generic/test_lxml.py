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

from lxml import etree

prefix_0 = "_0"
namespace_0 = "http://idempiere.org/ADInterface/1_0"
prefix_soapenv = "soapenv"
namespace_soapenv = "http://schemas.xmlsoap.org/soap/envelope/"

attribute_xmlns = "xmlns"
namespace_xmlns = "http://www.w3.org/2000/xmlns/"

url = 'http://localhost:8031/ADInterface/services/ModelADService'
urls = 'https://localhost:8431/ADInterface/services/ModelADService'
headers = {'user-agent': 'my-app/0.0.1', 'content-type': 'text/xml; charset=UTF-8'}

root = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope",
                     nsmap={prefix_0: namespace_0, prefix_soapenv: namespace_soapenv})
root.append(etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Header"))
body = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Body")
root.append(body)
body.append(etree.Element("{http://idempiere.org/ADInterface/1_0}createData"))
body.set('hi','hello')
print(etree.tostring(root, pretty_print=True))

root2 = etree.parse("../../documents/CreateBPartnerTest_request.xml")
print(etree.tostring(root2, pretty_print=True))
