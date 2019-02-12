# BrERP Web Service Connector - Python

![logo-brerp](documents/logo_brerp-300x86.png)

O BrERP Web Service Connector tem como objetivo facilitar as requisições SOAP para os webservices do BrERP em sua aplicação **Python**. Com sua arquitetura model oriented, não é necessário tratar os arquivos  XML de *request* e *response* **manualmente**. Desta forma, com o auxílio desta biblioteca, é possível realizar facilmente tarefas como:

- CRUDs, em qualquer tabela do sistema;
- Extrair informações de views;
- Executar Doc Actions em qualquer documento do BrERP;
- Executar processos.

## Compatibilidade

Este repositório conta com uma solução **Python**, **compatível com Python 2 e Python 3**. Porém, é **altamente recomendada** a utilização de **Python 3**, visto que **Python 2** será **descontinuado** no começo de 2020.

## Arquitetura

O repositório está dividido em 3 diretórios:

- **brerpwsc**:
  - Este diretório contém o **código fonte** da biblioteca **brerpwsc**, que é compilada e inserida nos pacotes do **pip**;
- **sandbox**:
  - Este diretório contém uma série de *classes de teste* e **classes de exemplo**, que podem ser utilizadas como base para a utilização dessa biblioteca em sua *aplicação Python*.
- **documents**:
  - Este diretório contém arquivos utilizados pelos testes, como *xmls* de exemplo, ou arquivos *.png*

## Instalação

Para instalar o **brerpwsc-python** é necessário clonar este repositório para um diretório **brerpwsc**. Para isso:

```shell
git clone https://github.com/devcoffee/brerpwsc-python brerpwsc
```

Feito isso, basta utilizar o próprio **pip** para instalar o plugin em seu **ambiente python**:

```shell
pip install -e --user brerpwsc
```

## Exemplo prático: Criando um Parceiro de Negócios com Imagem de Logo

Para podermos utilizar os webservices no **BrERP**, é necessário realizar uma configuração inicial, que deve informar o sistema sobre quais parâmetros esperar em um **request** e quais parâmetros enviar na **response**.
Neste exemplo, criaremos uma aplicação capaz de **Criar um parceiro de negócios com uma imagem de logo anexada**. Para isso, será necessário utilizar três *Web Services*, um para o envio da imagem, outro para a criação do parceiro de negócios, com o *record_id* da imagem referenciado e por fim, um **Web Service Composto** que nos permite enviar todas as informações em **uma única requisição**.

### Configurando os Webservices no BrERP

Para **exportar** ou **importar** dados no **BrERP**, *nenhuma linha de  código precisa ser escrita*. Basta que sejam feitas algumas simples configurações na janela de ***Segurança de Serviços Web***.

#### Segurança de Serviços Web

Esta é a janela de configuração dos Web Services, e possui 4 abas de configuração, sendo elas:

- **Parâmetros  de Serviço Web**:
  - Esta aba é de **importância vital** para o funcionamento do Web Service, uma vez que nela são configuradas as ações do Web Service, como a tabela a ser utilizada, a ação a ser realizada, entre outros.
- **Entradas de Serviço Web**:
  - Aqui é informado os parâmetros de entrada do Web Service, ou seja, quais informações serão consumidas por ele. É comum que os parâmetros sejam classificados em conformidade com os nomes da coluna da tabela manipulada.
- **Resultado de Serviço Web**:
  - Essa coluna diz respeito as informações que serão retornadas pelo Web Service, também tendo conformidade com o nome das colunas da tabela
- **Acesso de Serviço Web**:
  - Nessa aba são configuradas as permissões de Login do Web Service, ou seja, quais perfis terão permissão para utiliza-lo.

![SegurancaDeServicosWeb](/documents/SegurancaDeServicosWeb.png)

### Criando o Web Service CreateImageTest

# Em Construção