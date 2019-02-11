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

# root = etree.parse("../../documents/QueryBPartnerTest_response.xml")
root = etree.parse("../../documents/StandardResponseError_Example.xml")
fault = etree.parse("../../documents/Fault_response.xml")
print(etree.tostring(root, pretty_print=True))
print(etree.tostring(fault, pretty_print=True))


def check_fault(xml):
    for element in xml.iter():
        temp_tag = element.tag.rsplit('}', 1)[-1]
        temp_text = element.text
        if temp_tag in ('Fault',):
            continue
        print(temp_tag)
        print(temp_text)


def find_elements_0(root, name):
    return root.findall('.//{%s}%s' % (namespace_0, name))


# CHECK FAULT
for element in fault.iter():
    temp_tag = element.tag.rsplit('}', 1)[-1]
    if temp_tag in ('Envelope', 'Body'):
        continue

    if temp_tag in ('Fault',):
        check_fault(element)
        break

print("")

for element in root.iter():
    temp_tag = element.tag.rsplit('}', 1)[-1]
    if temp_tag in ('Envelope', 'Body'):
        continue

    print(find_elements_0(element, 'StandardResponse')[0].get('RecordIDe'))
    break
