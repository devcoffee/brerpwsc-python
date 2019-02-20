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

class WebServiceException(Exception):
    def __init__(self, message, cause=None):
        if cause:
            super(WebServiceException, self).__init__(u'{message}, caused by: {cause}'.format(
                message=message, 
                cause=repr(cause)
            ))
        else:
            super(WebServiceException, self).__init__(message)

        self.cause = cause

class WebServiceTimeoutException(Exception):
    def __init__(self, message, cause=None):
        if cause:
            super(WebServiceTimeoutException, self).__init__(u'{message}, caused by: {cause}'.format(
                message=message, 
                cause=repr(cause)
            ))
        else:
            super(WebServiceTimeoutException, self).__init__(message)
        
        self.cause = cause
