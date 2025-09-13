<!-- image -->

## PREFEITURA DE SãO PAULO

## Nota Fiscal de Serviços Eletrônica -NFS-e

## Manual de Utilização Web Service

## Versão 3.2

## ÍNDICE

| 1. INTRODUÇÃO.................................................................................................................................................... 4                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2. INTERFACES DISPONÍVEIS.................................................................................................................................. 4                                                                                                                                     |
| 2.1. INTERFACES SÍNCRONAS....................................................................................................................................4                                                                                                                                    |
| 2.1.1. ENVIO DE RPS .............................................................................................................................................4                                                                                                                                |
| 2.1.2. ENVIO DE LOTE DE RPS...............................................................................................................................4                                                                                                                                       |
| 2.1.3. TESTE DE ENVIO DE LOTE DE RPS...............................................................................................................4                                                                                                                                              |
| 2.1.4. CONSULTA DE NF-E ....................................................................................................................................5                                                                                                                                     |
| 2.1.5. CONSULTA DE NF-E RECEBIDAS..................................................................................................................5                                                                                                                                              |
| 2.1.6. CONSULTA DE NF-E EMITIDAS....................................................................................................................5                                                                                                                                             |
| 2.1.7. CONSULTA DE LOTE....................................................................................................................................5                                                                                                                                      |
| 2.1.8. CONSULTA INFORMAÇÕES DO LOTE..........................................................................................................5                                                                                                                                                    |
| 2.1.9. CANCELAMENTO DE NF-E...........................................................................................................................5                                                                                                                                           |
| 2.1.10. CONSULTA DE CNPJ..................................................................................................................................5                                                                                                                                       |
| 2.2 INTERFACES ASSÍNCRONAS.................................................................................................................................5                                                                                                                                      |
| 2.2.1 ENVIO DE LOTE DE RPS - ASSÍNCRONO .......................................................................................................5                                                                                                                                                  |
| 2.2.2 CONSULTA SITUAÇÃO LOTE ASSÍNCRONO..................................................................................................5                                                                                                                                                        |
| 2.2.3 TESTE ENVIO DE LOTE RPS - ASSÍNCRONO..................................................................................................6                                                                                                                                                     |
| 2.2.4 EMISSÃO DE GUIA - ASSÍNCRONO...............................................................................................................6                                                                                                                                                |
| 2.2.5 CONSULTA SITUAÇÃO GUIA ........................................................................................................................6                                                                                                                                            |
| 2.2.6 CONSULTA GUIA..........................................................................................................................................6                                                                                                                                    |
| 3. ARQUITETURA DE COMUNICAÇÃO.................................................................................................................... 7                                                                                                                                               |
| 3.1. MODELOCONCEITUAL.......................................................................................................................................7                                                                                                                                     |
| 3.2. PADRÕESTÉCNICOS...........................................................................................................................................8                                                                                                                                  |
| 3.2.1. Padrão de Comunicação.............................................................................................................................8                                                                                                                                        |
| 3.2.2. Padrão de Certificado Digital......................................................................................................................8                                                                                                                                       |
| 3.2.3. Padrão de Assinatura Digital ......................................................................................................................9                                                                                                                                       |
| 3.2.4. Validação de Assinatura Digital pelo Sistema de NF-e .............................................................................10                                                                                                                                                       |
| 3.2.5. Resumo dos Padrões Técnicos .................................................................................................................10                                                                                                                                            |
| 3.3. MODELOOPERACIONAL...................................................................................................................................11                                                                                                                                       |
| 3.3.1. Serviços.....................................................................................................................................................11                                                                                                                            |
| 3.4. PADRÃODASMENSAGENSXML.......................................................................................................................12 3.4.1. Validação da estrutura das Mensagens XML............................................................................................13 |

## Manual de Utilização

Web Service

| 3.4.2. Schemas XML (arquivos XSD) ...................................................................................................................13                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.4.3. Versão dos Schemas XML.........................................................................................................................14                    |
| 3.4.4. Regras de preenchimento dos campos ....................................................................................................15                            |
| 3.4.5. Tratamento de caracteres especiais no texto de XML .............................................................................16                                   |
| 4. WEB SERVICE LOTE NFE....................................................................................................................................16               |
| 4.1. WSDL................................................................................................................................................................17 |
| 4.2. TIPOS UTILIZADOS............................................................................................................................................17         |
| 4.2.1. Tipos Simples............................................................................................................................................18          |
| 4.2.2. Tipos Complexos.......................................................................................................................................24             |
| 4.3.SERVIÇOSEMÉTODOSSÍNCRONOS .................................................................................................................34                           |
| 4.3.1. Regras Gerais............................................................................................................................................34          |
| 4.3.2. Envio de RPS.............................................................................................................................................35          |
| 4.3.3. Envio de Lote de RPS (EnvioLoteRPS).......................................................................................................39                         |
| 4.3.4. Teste de Envio de Lote de RPS (TesteEnvioLoteRPS)................................................................................42                                  |
| 4.3.5. Pedido de Consulta de NF-e (ConsultaNFe) .............................................................................................42                             |
| 4.3.6. Pedido de Consulta de NF-e Recebidas (ConsultaNFeRecebidas)............................................................44                                            |
| 4.3.7. Pedido de Consulta de NF-e Emitidas (ConsultaNFeEmitidas).................................................................47                                         |
| 4.3.8. Pedido de Consulta de Lote (ConsultaLote) .............................................................................................48                            |
| 4.3.9. Pedido de Informações do Lote (ConsultaInformacoesLote)...................................................................50                                         |
| 4.3.10. Pedido de Cancelamento de NF-e (CancelamentoNFe) .........................................................................51                                        |
| 4.3.11. Pedido de Consulta de CNPJ (ConsultaCNPJ) .........................................................................................54                               |
| 4.4.SERVIÇOSEMÉTODOSASSÍNCRONOS .............................................................................................................56                             |
| 4.4.1. Regras Gerais............................................................................................................................................57          |
| 4.4.2. Envio de Lote de RPS (EnvioLoteRpsAsync)..............................................................................................57                             |
| 4.4.3. Teste de Envio de Lote de RPS Assíncrono (TesteEnvioLoteRpsAsync)....................................................59                                              |
| 4.4.4. Pedido de Consulta da Situação do Lote RPS Assíncrono (ConsultaSituacaoLote) ..................................59                                                    |
| 4.4.5. Emissão de Guia de forma Assíncrona (EmissaoGuiaAsync) ....................................................................61                                        |
| 4.4.6. Pedido de Consulta da Situação da Emissão de Guia Assíncrona (ConsultaSituacaoGuia) ......................63                                                         |
| 4.4.7. Pedido de Consulta de Guia (ConsultaGuia).............................................................................................65                             |
| 4.5. TABELA DE ERROS E ALERTAS...........................................................................................................................66                 |
| 4.5.1. Erros .........................................................................................................................................................67    |
| 4.5.2. Alertas ......................................................................................................................................................72     |
| 5. ARQUIVOS DE EXEMPLOS.................................................................................................................................73                  |
| 6. ATUALIZAÇÕES ( CHANGELOG )..........................................................................................................................74                   |

## 1. INTRODUÇÃO

Este manual tem como objetivo apresentar a definição das especificações e critérios técnicos necessários para  utilização  do  Web  Service  disponibilizado  pela  Prefeitura  de  São  Paulo  para  as  empresas prestadoras, tomadoras ou intermediárias de serviços.

Por meio do Web Service as empresas poderão integrar seus próprios sistemas de informações com o Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo. Desta forma, consegue-se automatizar o processo de emissão, consulta e cancelamento de NF-e.

|   Manual Versão | Alterações                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Data        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
|             3.2 | Novos campos para a Reforma Tributária 2026 ATENÇÃO: Os arquivos XSD versão 2.0 com os novos campos já estão disponíveis para consulta. No entanto, os Webservices ainda não estão habilitados para receber esses novos campos. Recomendamos que, por enquanto, os sistemas continuem utilizando os campos atualmente suportados pelos Webservices em produção. Assim que os serviços forem atualizados para aceitar os novos campos, comunicaremos oficialmente. Alteração: No xml "PedidoEnvioLoteRPS" foram adicionados os novos campos para a Reforma Tributária 2026. Orientações: no cabeçalho, o campo 'Versao' deverá ser igual a 2. Verificar o tpRPS, em que constam os novos campos. Os tipos complexos possuem a descrição: "(complemento para a versão 2.0)" Alterado o tpNFE, na Consulta, no cabeçalho, o campo 'Versao' deverá ser igual a 2. Verificar o tpNFE, em que constam os novos campos. Os tipos complexos possuem a descrição: "(complemento para a versão 2.0)" | Agosto/2025 |

## 2. INTERFACES DISPONÍVEIS

Por meio do Web Service, o Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo, disponibiliza uma série de interfaces que poderão ser acessadas pelos sistemas dos usuários. A seguir, estão resumidas as interfaces disponíveis e suas respectivas funcionalidades básicas.

## 2.1. INTERFACES SÍNCRONAS

## 2.1.1. ENVIO DE RPS

Através desta interface, os prestadores de serviços poderão enviar um RPS emitido por seu sistema para que  seja  substituído  por  uma  Nota  Fiscal  Eletrônica.  Esta  interface  destina-se  aos  prestadores  que desejam  emitir  NF-e  online  e  individualmente.  Para  emissões  de  grandes  volumes  recomendamos  a utilização da interface Envio de Lote de RPS.

## 2.1.2. ENVIO DE LOTE DE RPS

Através  desta  interface,  os  prestadores  de  serviços  poderão  enviar  lotes  de  RPS  emitidos  por  seus sistemas  para  que  sejam  substituídos  por  Notas  Fiscais  Eletrônicas.  Esta  interface  destina-se  aos prestadores que desejam emitir NF-e em grandes volumes.

## 2.1.3. TESTE DE ENVIO DE LOTE DE RPS

O  uso  desta  interface  é  opcional.  A  interface  de  Envio  de  Lote  de  RPS  faz  exatamente  as  mesmas verificações, entretanto na interface de Teste, nenhuma NF-e é gerada. Esta interface deverá ser usada apenas na fase de adaptação dos sistemas dos contribuintes. Nos casos de sistemas já adaptados, seu uso resulta em duplicidade de esforços desnecessários.

## 2.1.4. CONSULTA DE NF-E

Esta interface permite aos prestadores de serviços consultarem as NF-e emitidas por ele.

## 2.1.5. CONSULTA DE NF-E RECEBIDAS

Esta interface possibilita aos tomadores, intermediários e/ou prestadores de serviços consultarem as NFe  que  tiverem  sido  emitidas  para  eles,  possibilitando,  por  exemplo,  a  alimentação  automática  de  seu módulo de contas a pagar.

## 2.1.6. CONSULTA DE NF-E EMITIDAS

Esta interface possibilita aos prestadores de serviços consultarem as NF-e que tiverem sido emitidas por eles.

## 2.1.7. CONSULTA DE LOTE

Após o envio bem-sucedido de um Lote de RPS, o Web Service retorna diversas informações, entre elas o número do lote processado. Com esta interface, basta informar o número do lote desejado para receber as informações de todas as NF-e geradas neste lote.

## 2.1.8. CONSULTA INFORMAÇÕES DO LOTE

Após o envio bem-sucedido de um Lote de RPS, o Web Service retorna diversas informações, entre elas o número do lote processado. Com esta interface, basta informar o número do lote desejado para receber informações  resumidas:  data/hora  de  envio  do  lote,  quantidade  de  notas  processadas,  tempo  de processamento etc.

Para ter informações das notas processadas, deve-se usar a interface de Consulta de Lote.

## 2.1.9. CANCELAMENTO DE NF-E

Com esta interface, os prestadores de serviços poderão cancelar as NF-e emitidas por eles, informando apenas os números da NF-e que deverão ser cancelados.

## 2.1.10. CONSULTA DE CNPJ

Esta interface possibilita aos tomadores, intermediários e/ou prestadores de serviços consultarem quais Inscrições  Municipais  (CCM)  estão  vinculadas  a  um  determinado  CNPJ  e  se  estes  Contribuintes  já possuem autorização para emissão de NFS-e.

## 2.2 INTERFACES ASSÍNCRONAS

## 2.2.1 ENVIO DE LOTE DE RPS - ASSÍNCRONO

Através  desta  interface,  os  prestadores  de  serviços  poderão  enviar  lotes  de  RPS  emitidos  por  seus sistemas de forma assíncrona para que sejam substituídos por Notas Fiscais Eletrônicas. É semelhante à interface síncrona, contudo, ao invés de retornar as informações do lote, é retornado um protocolo, para posterior consulta da situação. Esta interface destina-se aos prestadores que desejam emitir NF-e em grandes volumes e que não necessitam da NF-e na mesma comunicação.

## 2.2.2 CONSULTA SITUAÇÃO LOTE ASSÍNCRONO

Esta interface permite aos prestadores de serviços acompanharem a situação do lote enviado de forma assíncrona. Através do protocolo devolvido na interface de envio de lote assíncrono, será possível verificar se o lote foi processado, se está em processamento ou se foi invalidado.

## 2.2.3 TESTE ENVIO DE LOTE RPS - ASSÍNCRONO

O uso desta interface é opcional. Assim como na interface de Envio de Lote de RPS, faz exatamente as mesmas verificações, entretanto na interface de Teste, nenhuma NF-e é gerada. Esta interface deverá ser usada apenas na fase de adaptação dos sistemas dos contribuintes. Nos casos de sistemas já adaptados, seu uso resulta em duplicidade de esforços desnecessários. Nesta interface um número de protocolo é devolvido para posterior consulta à situação do lote.

## 2.2.4 EMISSÃO DE GUIA - ASSÍNCRONO

Através  desta  interface,  os  prestadores  de  serviços  poderão  emitir  guias  por  incidência,  de  forma assíncrona. Esta interface devolve um protocolo para posterior consulta a situação da emissão da guia. Esta  interface  destina-se  aos  prestadores  que  desejam  emitir  guias  de  incidência  com  grandes quantidades de notas.

## 2.2.5 CONSULTA SITUAÇÃO GUIA

Esta interface permite aos prestadores de serviços acompanharem a situação da emissão de guia enviada assincronamente. Através do protocolo devolvido na interface de envio de Emissão de guia assíncrono, será possível verificar se a guia foi emitida, se está em processamento ou se foi invalidada.

## 2.2.6 CONSULTA GUIA

Através desta interface, os prestadores de serviços poderão consultar as guias emitidas por eles, através do número da guia.

## 3. ARQUITETURA DE COMUNICAÇÃO

## 3.1. MODELO CONCEITUAL

O  Web  Service  síncrono  do  Sistema  de  Notas  Fiscais  Eletrônicas®  da  Prefeitura  de  São  Paulo  irá disponibilizar as seguintes funcionalidades:

- A. Envio de RPS;
- B. Envio de Lote de RPS;
- C. Teste de Envio de Lote de RPS;
- D. Consulta de NF-e;
- E. Consulta de NF-e Recebidas;
- F. Consulta de NF-e Emitidas;
- G. Consulta de Lote;
- H. Consulta de Informações de Lote;
- I. Cancelamento de NF-e;
- J. Consulta de CNPJ.

O Web Service assíncrono  do Sistema de Notas Fiscais Eletrônicas®  da  Prefeitura  de  São  Paulo  irá disponibilizar as seguintes funcionalidades:

- K. Envio de Lote de RPS - Assíncrono;
- L. Consulta Situação de Lote de RPS (referente ao serviço K);
- M.  Teste de Envio de Lote de RPS - Assíncrono;
- N. Emissão de Guia - Assíncrono;
- O. Consulta Situação Emissão de Guia (referente ao serviço N);
- P. Consulta Guia;

Existirá um único Web Service síncrono com todos os serviços apresentados acima de A a J, e um único Web Service assíncrono com todos os serviços apresentados acima de K a P. O fluxo de comunicação é sempre iniciado pelo sistema do contribuinte através do envio de uma mensagem XML ao Web Service com o pedido do serviço desejado.

No Web Service síncrono, o pedido de serviço será atendido na mesma conexão (todos os serviços deste Web Service serão síncronos). O processamento do pedido do serviço é concluído na mesma conexão, com a devolução de uma mensagem XML contendo o retorno do processamento do serviço pedido.

No Web Service assíncrono, os pedidos de serviço 'Envio de Lote RPS', 'Teste de Envio de Lote de RPS', e, 'Emissão de Guia' são enviados para uma fila e retornam uma mensagem XML contendo um protocolo, que  deverá  ser  guardado  pelo  solicitante  a  fim  de  utilizar  para  consulta  da  situação  do  pedido posteriormente. Os demais pedidos do Web Service assíncrono serão atendidos na mesma conexão, com

a  devolução  de  uma  mensagem  XML  contendo  o  retorno  do  processamento  do  protocolo  ou  serviço pedido.

O diagrama a seguir ilustra o fluxo conceitual de comunicação entre o sistema do contribuinte e o Sistema de Notas Fiscais Eletrônicas da Prefeitura de São Paulo:

<!-- image -->

## 3.2. PADRÕES TÉCNICOS

## 3.2.1. Padrão de Comunicação

A comunicação entre os sistemas de informações dos contribuintes e o Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo será baseada em um Web Service síncrono, e um Web Service assíncrono, disponibilizados no Sistema de Notas Fiscais de Serviços Eletrônicas. O meio físico de comunicação utilizado será a Internet, com o uso do protocolo SSL, que além de garantir um duto de comunicação seguro na Internet, permite a identificação do servidor e do cliente através de certificados digitais, eliminando a necessidade de identificação do usuário através de nome ou código de usuário e senha.

O modelo de comunicação segue o padrão de Web Services definido pelo WS-I Basic Profile. A troca de mensagens entre o Web Service do Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo e o sistema do contribuinte será realizada no padrão SOAP, com troca de mensagens XML no padrão  Style/Enconding:  Document/Literal,  wrapped.  A  opção  'wrapped'  representa  a  chamada  aos métodos disponíveis com a passagem de mais de um parâmetro.

## 3.2.2. Padrão de Certificado Digital

Os certificados digitais utilizados no Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo serão emitidos por Autoridade Certificadora credenciada pela Infraestrutura de Chaves Públicas Brasileira -ICP-Brasil, tipo A1, A3 ou A4, devendo conter o CNPJ do proprietário do certificado digital.

Os certificados digitais serão exigidos no mínimo* em dois (2) momentos distintos:

- A. Assinatura de Mensagens XML:

Quem pode assinar a Mensagem XML:

- Todas as Mensagens XML podem ser assinadas pelo próprio contribuinte. Neste caso o certificado digital utilizado deverá conter o CNPJ do contribuinte que gerou a mensagem XML;

- As Mensagens XML de consulta de NF-e Emitidas, NF-e Recebidas e Informações de lote, podem ser assinadas pelo contador (desde que cadastrado na tela de 'Configurações do Perfil do Contribuinte') ou por um terceiro (ex.: funcionário da empresa contribuinte), desde que o contribuinte tenha concedido a esta permissão de acesso a consultas (através do menu 'Gerenciamento de Usuários' do Sistema de Notas Fiscais Eletrônicas). Neste caso  o  certificado  digital  utilizado  deverá  conter  o  CPF/CNPJ  do  contador  /  usuário autorizado.

Todas as mensagens XML deverão conter o CPF/CNPJ de quem estará autorizado a efetuar a sua transmissão (TAG CPFCNPJRemetente). No caso de as Mensagens XML serem transmitidas por quem as gerou o CPF/CNPJ informado deverá ser o do próprio.

- B. Autenticação na transmissão das mensagens entre os servidores do contribuinte e da Prefeitura de São Paulo: O certificado digital utilizado para identificar essa função deverá conter o CPF/CNPJ do  responsável  pela  transmissão  das  mensagens.  Este  CPF/CNPJ  deverá  ser  o  mesmo  que consta na TAG CPFCNPJRemetente da mensagem XML.

* Adicionalmente os certificados digitais também poderão ser exigidos conforme a necessidade específica de cada serviço (exemplo: itens 4.3.2 e 4.3.10).

## 3.2.3. Padrão de Assinatura Digital

As mensagens enviadas ao Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo são documentos eletrônicos elaborados no padrão XML e devem ser assinados digitalmente utilizando certificado digital, descrito no item 3.2.2.

Os elementos abaixo estão presentes dentro do Certificado do contribuinte tornando desnecessária a sua representação  individualizada  na  mensagem  XML.  Portanto,  a  mensagem  XML  não  deve  conter  os elementos:

- &lt;X509SubjectName&gt;
- &lt;X509IssuerSerial&gt;
- &lt;X509IssuerName&gt;
- &lt;X509SerialNumber&gt;
- &lt;X509SKI&gt;

Analogamente, as TAGs abaixo não deverão ser informadas, pois as informações serão obtidas a partir do Certificado do emitente:

- &lt;KeyValue&gt;
- &lt;RSAKeyValue&gt;
- &lt;Modulus&gt;
- &lt;Exponent&gt;

Para o processo de assinatura, o contribuinte não deve fornecer a Lista de Certificados Revogados, já que a mesma será montada e validada pelo Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo.

A assinatura digital do documento eletrônico deverá atender aos seguintes padrões adotados:

- A. Padrão de assinatura: 'XML Digital Signature', utilizando o formato 'Enveloped' (http://www.w3c.org/TR/xmldsig-core/);
- B. Certificado digital: Emitido por AC credenciada no ICP-Brasil (http://www.w3c.org/2000/09/xmldsig#X509Data);
- C. Cadeia de Certificação: EndCertOnly (Incluir na assinatura apenas o certificado do usuário final);
- D. Tipo do certificado: A1, A3 ou A4 (o uso de HSM é recomendado);
- E. Tamanho da Chave Criptográfica: Compatível com os certificados A1 e A3 (1024bits) ou A4 (2048 bits);
- F. Função criptográfica assimétrica: RSA (http://www.w3c.org/2000/09/xmldsig#rsa-sha1);
- G. Função de 'message digest': SHA -1 (http://www.w3c.org/2000/09/xmldsig#sha1);

- H. Codificação: Base64 (http://www.w3c.org/2000/09/xmldsig#base64);
- I. Transformações exigidas: Útil para realizar a canonicalização do  XML enviado para realizar  a validação correta da Assinatura Digital. São elas:
- (1)  Enveloped (http://www.w3c.org/2000/09/xmldsig#enveloped-signature);
- (2)  C14N (http://www.w3c.org/TR/2001/REC-xml-c14n-20010315).

## 3.2.4. Validação de Assinatura Digital pelo Sistema de NF-e

Para a validação da assinatura digital, seguem as regras que serão adotadas pelo Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo:

- A. Extrair  a  chave  pública  do  certificado  digital  e  não  utilizar  a  chave  indicada  na  TAG  XML (ds:KeyValue);
- B. Verificar o prazo de validade do certificado utilizado;
- C. Montar  e  validar  a  cadeia  de  confiança  dos  certificados  validando  também  a  LCR  (Lista  de Certificados Revogados) de cada certificado da cadeia;
- D. Validar o uso da chave utilizada (Assinatura Digital) de tal forma a aceitar certificados somente do tipo A (não serão aceitos certificados do tipo S);
- E. Garantir que o certificado utilizado é de um usuário final e não de uma Autoridade Certificadora;
- F. Adotar as regras definidas pelo RFC 3280 para LCRs e cadeia de confiança;
- G. Validar a integridade de todas as LCR utilizadas pelo sistema;
- H. Prazo de validade de cada LCR utilizada (verificar data inicial e final).

A forma de conferência da LCR pelo Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo pode ser feita de 2 (duas) maneiras: On-line ou Download periódico. As assinaturas digitais das mensagens serão verificadas considerando o horário fornecido pelo Observatório Nacional.

## 3.2.5. Resumo dos Padrões Técnicos

A tabela a seguir resume os principais padrões de tecnologia utilizados:

| CARACTERÍSTICA               | DESCRIÇÃO                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------|
| Web Services                 | Padrão definido pelo WS-I Basic Profile 1.1 (http://www.wsi.org/Profiles/BasicProfile-1.1-2004-08-24.html). |
| Meio lógico de comunicação   | Web Service, disponibilizados pelo Sistema de NF-e da Prefeitura de São Paulo.                              |
| Meio físico de comunicação   | Internet                                                                                                    |
| Protocolo Internet           | TLS versão 1.2, com autenticação mútua através de certificados digitais.                                    |
| Padrão de troca de mensagens | SOAP versão 1.2.                                                                                            |
| Padrão da mensagem XML       | XML no padrão Style/Encoding: Document/Literal, wrapped.                                                    |

| CARACTERÍSTICA                  | DESCRIÇÃO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão de certificado digital   | X.509 versão 3, emitido por Autoridade Certificadora credenciada pela Infra- estrutura de Chaves Públicas Brasileira - ICP-Brasil, do tipo A1, A3 ou A4, devendo conter o CNPJ do proprietário do certificado digital. Para assinatura de mensagens, utilizar o certificado digital do estabelecimento emissor da NF-e (no caso de Consulta de NF-e Recebidas utilizar o certificado digital do tomador). Opcionalmente as Mensagens XML de consulta de NF-e Emitidas, NF-e Recebidas e Informações de lote, podem ser assinadas pelo contador (desde que cadastrado na tela de 'Configurações do Perfil do Contribuinte') ou por um terceiro (ex.: funcionário da empresa contribuinte), desde que o contribuinte tenha concedido a este permissão de acesso a consultas (através do menu 'Gerenciamento de Usuários' do Sistema de Notas Fiscais Eletrônicas). Neste caso o certificado digital utilizado deverá conter o CPF/CNPJ do contador / usuário autorizado. Para autenticação, utilizar o certificado digital do responsável pela transmissão. |
| Padrão de assinatura digital    | XML Digital Signature, Enveloped, com certificado digital X.509 versão 3, com chave privada de 1024 bits (A1 / A3) ou 2048 bits (A4), com padrões de criptografia assimétrica RSA, algoritmo message digest SHA-1 e utilização das transformações Enveloped e C14N.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Validação de assinatura digital | Será validada, além da integridade e autoria, a cadeia de confiança com a validação das LCRs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Padrões de preenchimento XML    | • Campos não obrigatórios do Schema que não possuam conteúdo terão suas tags suprimidas na mensagem XML. • Máscara de números decimais e datas estão definidas no Schema XML. • Nos campos numéricos inteiro, não incluir a vírgula ou ponto decimal. • Nos campos numéricos com casas decimais, utilizar o 'ponto decimal' na separação da parte inteira.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 3.3. MODELO OPERACIONAL

A forma de processamento dos pedidos de serviços do Web Service do Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo poderá ser síncrona, atendendo ao pedido de serviço na mesma conexão, ou, poderá ser assíncrona, necessitando um pedido de consulta utilizando o protocolo recebido na primeira comunicação.

## 3.3.1. Serviços

## I.  Síncrono

Os pedidos de serviços são processados imediatamente e o resultado do processamento é obtido em uma única conexão.

Abaixo, o fluxo simplificado de funcionamento:

<!-- image -->

Etapas do processo ideal:

1. O sistema do contribuinte inicia a conexão enviando uma mensagem XML de pedido do serviço para o Web Service;
2. O Web Service recebe a mensagem XML de pedido do serviço e encaminha ao sistema da NFe;
3.  O  sistema  da  NF-e  recebe  a  mensagem  XML  de  pedido  do  serviço  e  realiza  o  processamento*, devolvendo uma mensagem XML de retorno ao Web Service;
4. O Web Service recebe a mensagem XML de retorno e a encaminha ao sistema do contribuinte;
5. O sistema do contribuinte recebe a mensagem XML de retorno e encerra a conexão.

## II. Assíncrono

Os pedidos de serviços são alocados em um repositório para processamento gerando um protocolo que é devolvido na mesma conexão. O resultado do processamento é obtido através de uma segunda conexão utilizando o protocolo recebido na primeira conexão.

Abaixo, o fluxo simplificado de funcionamento:

<!-- image -->

Etapas do processo ideal:

## 1ª Parte:

1. O sistema do contribuinte inicia a conexão enviando uma mensagem XML de pedido de serviço para o Web Service;
2. O Web Service recebe a mensagem XML de pedido do serviço, enfileira para processamento no sistema da NFe, gera um protocolo, e devolve uma mensagem XML de retorno com o protocolo;
3. O sistema do contribuinte recebe a mensagem XML de retorno com o protocolo e encerra a conexão.

## 2ª Parte:

1. O sistema do contribuinte inicia a conexão enviando uma mensagem XML de pedido de serviço, com o protocolo recebido anteriormente, para o Web Service;
2. O Web Service recebe a mensagem XML do pedido do serviço e consulta junto ao sistema da NFe se o pedido foi processado;
3. O Web Service recebe a mensagem XML de retorno e a encaminha ao sistema do contribuinte;
4. O sistema do contribuinte recebe a mensagem XML de retorno e encerra a conexão.

## 3.4. PADRÃO DAS MENSAGENS XML

A especificação adotada para as mensagens XML é a recomendação W3C para XML 1.0, disponível em www.w3.org/TR/REC-xml e a codificação dos caracteres será em UTF-8.

## 3.4.1. Validação da estrutura das Mensagens XML

Para garantir minimamente a integridade das informações prestadas e a correta formação das mensagens XML, o contribuinte deverá submeter cada uma das mensagens XML de pedido de serviço para validação pelo seu respectivo arquivo XSD (XML Schema Definition, definição de esquemas XML) antes de seu envio. Neste manual utilizaremos a nomenclatura Schema XML para nos referir a arquivo XSD.

Um Schema XML define o conteúdo de uma mensagem XML, descrevendo os seus atributos, elementos e a sua organização, além de estabelecer regras de preenchimento de conteúdo e de obrigatoriedade de cada elemento ou grupo de informação.

A validação da estrutura da mensagem XML é realizada por um analisador sintático (parser) que verifica se a mensagem XML atende às definições e regras de seu respectivo Schema XML.

Qualquer  divergência  da  estrutura  da  mensagem  XML  em  relação  ao  seu  respectivo  Schema  XML, provoca um erro de validação do Schema XML. Neste caso o conteúdo da mensagem XML de pedido do serviço não poderá ser processado.

A primeira condição para que a mensagem XML seja validada com sucesso é que ela seja submetida ao Schema XML correto. Assim, os sistemas de informação dos contribuintes devem estar preparados para gerar mensagens XML em seus respectivos Schemas XML em vigor.

## 3.4.2. Schemas XML (arquivos XSD)

O Schema XML (arquivo XSD) correspondente a cada uma das mensagens XML de pedido e de retorno utilizadas pelo Web Service LoteNFe (serviço síncrono) pode ser obtido na internet acessando o Portal do Sistema de Notas Fiscais Eletrônicas da Prefeitura de São Paulo. Para obter os Schemas XML do Web Service da NF-e acione o navegador Web (Firefox, Google Chrome, por exemplo) e digite o endereço a seguir:

## a) NFS-e emitidas até 22/02/2015

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-v01-0.zip

## b) NFS-e emitidas a partir de 23/02/2015 (fato gerador até 31/12/2025)

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-v01-1.zip

- c) NFS-e emitidas pelo serviço assíncrono

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-assincrono-v01-1.zip

- d) NFS-e -Reforma tributária 2026 (serviços síncronos e assíncronos)

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-reformatributaria-v02-0.zip

## 3.4.3. Versão dos Schemas XML

Toda mudança de layout das mensagens XML do Web Service implica na atualização do seu respectivo Schema XML. A identificação da versão dos Schemas XML será realizada com o acréscimo do número da versão no nome do arquivo XSD precedida da literal '\_v', como segue:

- PedidoEnvioLoteRPS\_v02.xsd (Schema XML de Envio de Lote de RPS, versão 2);
- RetornoEnvioLoteRPS\_v03.xsd (Schema XML do Retorno de Envio de Lote de RPS, versão 3);
- TiposNFe\_v01.xsd (Schema XML dos tipos básicos da NF-e, versão 1).

A maioria dos Schemas XML definidos para a utilização do Web Service do Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo utiliza as definições de tipos simples ou tipos complexos que estão definidos  em outros Schemas XML (ex.: TiposNFe.xsd e xmldsig-core-schema.xsd), nestes casos, a modificação de versão do Schema básico será repercutida no Schema principal.

Por exemplo, o tipo RPS (tpRPS) utilizado no Schema PedidoEnvioLoteRPS\_V04.xsd está definido no Schema TiposNFe\_V01.xsd, caso ocorra alguma modificação na definição deste tipo, e um conseqüente incremento da versão do Schema TiposNFe\_V01.xsd para TiposNFe\_V02.xsd o Schema PedidoEnvioLoteRPS\_V04.xsd  (bem  como  todos  os  Schemas  que  utilizam  o  tipo  RPS)  deve  ter  a declaração 'import' atualizada com o nome do Schema TiposNFe\_V02.xsd e a versão atualizada para PedidoEnvioLoteRPS\_V05.xsd.

## Exemplo de Schema XML de Pedido de Envio de Lote de RPS (arquivo PedidoEnvioLoteRPS\_v01.xsd):

```
<?xml version="1 _ 0" encoding= utf-8"2> http:/ prefeitura sp gov.br / nfe xmlns:tipos= http prefeitura sp.gov.br / nfe/tipos xmlns:xs= 'http: org/ 2001/XMLSchema xmlns:ds="http: w3.org/ 2000/09/xmldsig# import namespace= http:/ prefeitura br / nfe/tipos schemaLocation= IiposNFe_vÛl.Isd" <Xs: import namespace= http org/ 2000/09 xmldsigf schemaLocation= xmldsig-core-schema v01 <xs:element name 'PedidoEnvioLoteRPS" <xs:annotation> <xs:documentation? Schema utilizado para PEDIDO de envio de lote de RPS <xs:documentation> <xs:documentation)Este Schema XML utilizado pelos prestadores de serviços para substituição em lote de RPS por NF-e </xs:documentation> annotation> <xs:complexIype> <xs:element name= Cabecalho" minoccurs= maxOccurs=" 1" > annotation? documentation) Cabeçalho do pedido.< / xs:documentation> comp lexType> sequence? <xs:element name CPFCNP JRemetente type= tipos:tpCPFCNPJ" minOccurs= maxOccurs= annotation? documentation>Informe CPF CNPJ do Remetente autorizado transmitir Mensagem </xs:element <xs:element name transacao type Xs boolean minOccurs= 1" maxOccurs=" 1" > annotation? documentation> Informe se 05 RPS serem substituídos por NF =e farão parte de uma mesma transação True Os RPS serão substituidos por NF-e se não ocorrer nenhum evento de erro durante processamento de todo lote; False Os RPS válidos serão substituidos por NF-e, mesmo que ocorran eventos de erro durante processamento de outros RPS deste lote.< / xs:documentation> <xs:element name= dt Inicio" typez minOccurs="]" maxOccurs="1" > annotation> documentation?Informe data de inicio do periodo transmitido (AAAA-MMDD) </xs:element>
```

```
<xs :element name dtFim" type Xs:date maxOccurs=" 1" > annotation) documentation>Informe data final do período transmitido DD) <xs:annotation> </ xs:element> <xs:element name QtdRPS" tipos:tpQuantidade maxoccur 5= annotation? documentation> Informe total de RPS contidos na </xs:element> <xs:element name ValorTotalServicos type tipos tpValor minoccurs= maxOccurs="1" > annotation? documentation>Informe valor total dos serviços prestados dos RPS contidos na mensagem XML </xs:element <xs :element name ValorTotalDeducoes" type "tipos:tpValor minoccurs= 0 " maxOccurs=" 1" > annotation) valor total das deduçães dos RPS contidos na mensagem XML . < / xs :documentation> <xs:annotation? Xs:element> </ Xs : sequence attribute name Versao type="tipos:tpVersao" use= required" annotation> documentation Informe Versão do Schema XML </xs: complexIype> </xs:element> <xs:element name RPS" type="tipos:tpRPS" minOccurs= 1" maxOccurs= 50"> annotation? <xs: documentation>Informe 05 RPS Seren substituidos por </ xs:annotation? </xs:element> <xs:element ref="ds Signature maxoccurs=" 1 annotation> <xs:documentation Assinatura digital emissor dos RPS <lxs:documentation> </xs:annotation> Xs sequence? <s comp lexIype> </xs schema
```

As modificações de layout das mensagens XML do Web Service podem ser causadas por necessidades técnicas ou em razão da modificação de alguma legislação. As modificações decorrentes de alteração da legislação deverão ser implementadas nos prazos previstos no ato normativo que introduziu a alteração. As  modificações  de  ordem  técnica  serão  divulgadas  pela  Prefeitura  de  São  Paulo  e  poderão  ocorrer sempre que se fizerem necessárias.

## 3.4.4. Regras de preenchimento dos campos

- Campos que representam CPF e CNPJ (respectivamente 11 e 14 caracteres) devem ser informados com o tamanho fixo previsto, sem formatação e com o preenchimento dos zeros não significativos;
- Campos numéricos que representam valores e quantidades são de tamanho variável, respeitando o tamanho  máximo  previsto  para  o  campo  e  a  quantidade  de  casas  decimais  (quando  houver).  O preenchimento de zeros não significativos causa erro de validação do Schema XML.
- Os campos numéricos devem ser informados sem o separador de milhar, com uso do ponto decimal para indicar a parte fracionária (quando houver) respeitando-se a quantidade de dígitos prevista no layout;
- As datas devem ser informadas no formato 'AAAA -MMDD'.

Para  reduzir  o  tamanho  final  das  mensagens  XML  alguns  cuidados  de  programação  deverão  ser assumidos:

- Na  geração  das  mensagens  XML,  excetuados  os  campos  identificados  como  obrigatórios  no respectivo Schema XML, não incluir as TAGs de campos zerados (para campos tipo numérico) ou vazios (para campos tipo caractere);
- Não incluir "espaços" no início e/ou no final de campos alfanuméricos;
- Não incluir comentários na mensagem XML;
- Não incluir anotação e documentação na mensagem XML (TAG annotation e TAG documentation);
- Não incluir caracteres de formatação na mensagem XML: 'LF' (Line Feed ou salto de linha, caractere ASCII 10), "CR" (Carriage Return ou retorno do carro, caractere ASCII 13), "tab", caractere de "espaço" entre as TAGs).

## 3.4.5. Tratamento de caracteres especiais no texto de XML

Todos os textos de uma mensagem XML passam por uma análise do 'parser' específico da linguagem. Alguns caracteres afetam o funcionamento deste 'parser', não podendo aparecer no texto de uma forma não controlada. Estes caracteres devem ser substituídos conforme a tabela a seguir:

| CARACTERES QUE AFETAM O'PARSER'   | DESCRIÇÃO          | SUBSTITUIR POR   |
|-----------------------------------|--------------------|------------------|
| >                                 | Sinal de maior     | &gt;             |
| <                                 | Sinal de menor     | &lt;             |
| &                                 | E-comercial        | &amp;            |
| '                                 | Aspas              | &quot;           |
| '                                 | Sinal de apóstrofe | &apos;           |

## 4. Web Service Lote NFe

Os Web Services LoteNFe e LoteNFeAsync, do Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo, disponibilizam os serviços que serão utilizados pelos sistemas de informação dos contribuintes.

O mecanismo de utilização do Web Service LoteNFe segue as seguintes premissas:

Será disponibilizado um Web Service (LoteNFe) para todos os serviços síncronos, existindo um método Web para cada tipo de serviço.

Os serviços disponibilizados neste Web Service serão síncronos, portanto o envio da mensagem XML de pedido do serviço e a obtenção da mensagem XML de retorno serão realizados na mesma conexão através de um único método.

Já o mecanismo de utilização do Web Service LoteNFeAsync segue as seguintes premissas:

Será disponibilizado um Web Service (LoteNFeAsync) para os serviços assíncronos, existindo métodos Web para cada tipo de serviço.

Os serviços disponibilizados neste Web Service serão assíncronos, ou seja, o envio da mensagem XML de pedido de serviço será feita em uma conexão através de um método específico, e a obtenção da mensagem  XML  de  retorno  será  feita  através  de  uma  segunda  conexão,  através  de  um  método  de consulta.

Para finalidade de rastrear o pedido feito na primeira conexão, o Web Service retorna, neste primeiro contato, um protocolo único e exclusivo, de 32 caracteres no formato GUID (do inglês Globally Unique Identifier ,  ou,  Identificador  Único  Global),  no  qual  deverá  ser  armazenado  pelo  contribuinte  para  ser utilizado nos métodos de consulta da mensagem de retorno.

Este tipo de Web Service é ideal para uma entrega mais rápida dos pedidos de serviço, já que não depende da espera do final do processamento para entregar uma resposta ao contribuinte.

Para ambos os Web Services, as mensagens XML de pedido de serviço que excederem o tamanho limite previsto (500 KB) obterão como retorno uma mensagem XML de erro. Portanto os sistemas de informação dos contribuintes não poderão permitir a geração de mensagens XML com tamanho superior a 500 KB.

Primeiramente cada mensagem  XML  de  pedido  de serviço será recebida pelo Web  Service correspondente para validação de seu respectivo Schema XML (arquivo XSD). Caso ocorram erros de validação do Schema XML, o conteúdo da mensagem XML não será processado e será retornada uma mensagem XML contendo o(s) erro(s) ocorrido(s).

## 4.1. WSDL

Para que os sistemas de informação dos contribuintes saibam quais parâmetros enviar aos Web Services LoteNFe e LoteNFeAsync, e quais parâmetros serão retornados, os contribuintes deverão utilizar o arquivo WSDL (Web Service Description Language, linguagem de descrição de serviço Web). Trata-se de um arquivo  XML  que  configura  como  ocorrerá  a  interação  entre  um  Web  Service  e  seus  consumidores (sistemas de informação dos contribuintes).

O WSDL é uma linguagem baseada em XML, com a finalidade de documentar as mensagens XML que o Web Service aceita (pedidos de serviço) e gera (retornos). Esse mecanismo padrão facilita a interpretação dos contratos pelos desenvolvedores e ferramentas de desenvolvimento.

Para enxergar o valor do WSDL, imagine que um contribuinte quer invocar um dos métodos que é fornecido pelo Web Service LoteNFe. O contribuinte pode pedir alguns exemplos de mensagens XML de pedido e de retorno e escrever sua aplicação para produzir e consumir mensagens XML que se parecem com os exemplos, mas isso pode gerar muitos erros. Por exemplo, o contribuinte pode assumir que um campo é um inteiro, quando de fato é uma string. O WSDL especifica o que a mensagem XML de pedido deve conter e como vai ser a mensagem XML de retorno, em uma notação não ambígua.

A notação que o arquivo WSDL usa para descrever o formato das mensagens é baseada no padrão XML, o  que  significa  que  é  uma  linguagem  de  programação  neutra  e  baseada  em  padrões,  o  que  a  torna adequada para descrever as interfaces dos Web services, que são acessíveis por uma grande variedade de plataformas e linguagens de programação. Além de descrever o conteúdo das mensagens, o WSDL define onde o serviço está disponível e quais protocolos de comunicação são usados para conversar com o serviço. Isso significa que o arquivo WSDL define tudo que é necessário para escrever um programa que utilize o XML Web service. Há várias ferramentas disponíveis para ler o arquivo WSDL e gerar o código para comunicar com o XML Web service.

A documentação do WSDL pode ser obtida na internet acessando o endereço do Web Service do Sistema de Notas Fiscais de Serviços Eletrônicas da Prefeitura de São Paulo.

Para obter o WSDL do Web Service da NF-e acione o navegador Web (Firefox, Google Chrome, por exemplo) e digite o endereço a seguir:

## Web Service síncrono LoteNFe:

https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx?WSDL

## Web Service assíncrono LoteNFeAsync:

https://nfews.prefeitura.sp.gov.br/lotenfeasync.asmx?WSDL

## 4.2. TIPOS UTILIZADOS

A seguir são apresentados os tipos Simples e Complexos utilizados nos Schemas XML de pedido e de retorno. Estes tipos estão definidos no Schema XML de TiposNF-e (arquivo TiposNFe\_V01.xsd).

Para obter a versão mais recente do Schema XML de TiposNF-e (bem como os demais Schemas XML) acesse o link:

## a) NFS-e emitidas até 22/02/2015

Versão do Manual: 3

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-v01-0.zip

- b) NFS-e emitidas a partir de 23/02/2015 (fato gerador até 31/12/2025)

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-v01-1.zip

- c) NFS-e emitidas pelo serviço assíncrono

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-assincrono-v01-1.zip

- d) NFS-e -Reforma tributária 2026 (serviços síncronos e assíncronos)

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-reformatributaria-v02-0.zip

## 4.2.1. Tipos Simples

Descrição dos nomes e abreviações utilizados nas colunas de cabeçalho do layout da tabela de Tipos Simples:

| NOME DO TIPO   | DESCRIÇÃO (tipo utilizado para informar...)   | TIPO BASE   |   TAMANHO | DEC   | OBSERVAÇÃO                                                                                                         |
|----------------|-----------------------------------------------|-------------|-----------|-------|--------------------------------------------------------------------------------------------------------------------|
| tpCidade       | Código da cidade de endereço.                 | N           |         7 |       | O código informado deverá pertencer à Tabela de Municípios (do IBGE) disponibilizada pela Prefeitura de São Paulo. |

- A. Coluna Nome do Tipo: Nome do tipo simples;
- B. Coluna Descrição: Descrição do tipo simples;
- C. Coluna Tipo Base: tipo base utilizado na criação do tipo simples.
4. B -boolean;
5. Base64Binary;
6. C -campo alfanumérico;
7. D -campo data;
8. N -campo numérico;
- D. Coluna Tamanho: x-y, onde x indica o tamanho mínimo e y o tamanho máximo; a existência de um  único  valor  indica  que  o  campo  tem  tamanho  fixo,  devendo-se  informar  a  quantidade  de caracteres exigidos, preenchendo-se os zeros não significativos; tamanhos separados por vírgula indicam que o campo deve ter um dos tamanhos fixos da lista;
- E. Coluna Dec: indica a quantidade máxima de casas decimais do campo.

## Tabelas de tipos simples

| NOME DO TIPO   | DESCRIÇÃO (tipo utilizado para informar...)   | TIPO BASE   | TAMANHO   |   DEC | OBSERVAÇÃO                                     |
|----------------|-----------------------------------------------|-------------|-----------|-------|------------------------------------------------|
| tpAliquota     | Valor da alíquota do serviço                  | N           | 3-5       |     4 | Exemplo: 5% - 0.05 2,5% - 0.025 1,75% - 0.0175 |

| NOME DO TIPO             | DESCRIÇÃO (tipo utilizado para informar...)    | TIPO BASE     | TAMANHO   | DEC   | OBSERVAÇÃO                                                                                                                 |
|--------------------------|------------------------------------------------|---------------|-----------|-------|----------------------------------------------------------------------------------------------------------------------------|
| tpAssinatura             | Assinatura digital de NF-e / RPS               | Base64 Binary |           |       | Cadeia de caracteres (com informações do RPS emitido) assinada conforme descrito no item 4.3.2.                            |
| tpAssinaturaCancelamento | Assinatura Digital de Cancelamento de NF-e.    | Base64 Binary |           |       | Cadeia de caracteres (com informações do RPS emitido) assinada conforme descrito no item 4.3.10.                           |
| tpBairro                 | Bairro do endereço                             | C             | 0-30      |       | Bairro                                                                                                                     |
| tpCEP                    | CEP do endereço                                | N             | 7-8       |       | CEP                                                                                                                        |
| tpCidade                 | Código da cidade do endereço                   | N             | 7         |       | O código informado deverá pertencer à Tabela de Municípios (do IBGE) disponibilizada pela Prefeitura de São Paulo.         |
| tpCNPJ                   | Número no Cadastro Nacional da Pessoa Jurídica | C             | 14        |       |                                                                                                                            |
| tpCodigoServico          | Códigos de Serviço                             | N             | 4-5       |       | O código informado deverá pertencer à Tabela de Serviços disponibilizada pela Prefeitura de São Paulo.                     |
| tpCodigoEvento           | Código do Evento                               | N             | 3-4       |       | O código informado deverá pertencer à Tabela de Erros ou à Tabela de Alertas disponibilizada pela Prefeitura de São Paulo. |
| tpCodigoVerificacao      | Código de Verificação da NF-e                  | C             | 8         |       | Código de verificação da NF-e gerado pelo Sistema de Notas Fiscais Eletrônicas.                                            |
| tpComplementoEndereco    | Complemento do Endereço                        | C             | 0-30      |       |                                                                                                                            |
| tpCPF                    | Número no Cadastro de Pessoas Físicas          | C             | 11        |       |                                                                                                                            |
| tpDescricaoEvento        | Descrição do Evento                            | C             | 0-300     |       | Descrição correspondente ao código do evento ocorrido.                                                                     |

| NOME DO TIPO         | DESCRIÇÃO (tipo utilizado para informar...)   | TIPO BASE   | TAMANHO   | DEC   | OBSERVAÇÃO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------|-----------------------------------------------|-------------|-----------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tpDiscriminacao      | Discriminação dos Serviços                    | C           | 0-2000    |       | Texto contínuo descritivo dos serviços. O conjunto de caracteres correspondentes ao código ASCII 13 e ASCII 10 deverá ser substituído pelo caracter | (pipe ou barra vertical. ASCII 124). Exemplo: Digitado na NF 'Lavagem de carro com lavagem de motor' Preenchimento do arquivo: 'Lavagem de carro|com lavagem de motor' Não devem ser colocados espaços neste campo para completar seu tamanho máximo, devendo o campo ser preenchido apenas com conteúdo a ser processado /armazenado. (*) Este campo é impresso num retângulo com 95 caracteres (largura) e 24 linhas (altura). É permitido (não recomendável), o uso de mais de 2000 caracteres. Caso seja ultrapassado o limite de 24 linhas, o conteúdo será truncado durante a impressão |
| tpEmail              | E-mail                                        | C           | 0-75      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tpInscricaoEstadual  | Inscrição Estadual                            | N           | 1-19      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tpInscricaoMunicipal | Inscrição Municipal                           | N           | 8         |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tpLogradouro         | Endereço                                      | C           | 0-50      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tpNumero             | Número                                        | N           | 1-12      |       | Tipo utilizado para informar número de NF-e, número de RPS, número de Guia, número de Lote, número de página, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| tpNumeroEndereco     | Número do Endereço                            | C           | 0-10      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tpOpcaoSimples       | Opção pelo Simples                            | C           | 1         |       | Opção pelo Simples: 0 - Normal ou Simples Nacional (DAMSP); 1 - Optante pelo Simples Federal (Alíquota de 1,0%); 2 - Optante pelo Simples Federal (Alíquota de 0,5%); 3 - Optante pelo Simples Municipal. 4 - Optante pelo Simples Nacional (DAS).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tpQuantidade         | Tipo Quantidade                               | N           | 1-15      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tpRazaoSocial        | Tipo Razão Social                             | C           | 0-75      |       | Nome / Razão Social                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| tpSerieRPS           | Tipo Série do RPS                             | C           | 1-5       |       | Série do RPS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| tpStatusNFe          | Status da NF-e                                | C           | 1         |       | Status da NF-e: N - Normal; C - Cancelada                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

| NOME DO TIPO         | DESCRIÇÃO (tipo utilizado para informar...)                                                                    | TIPO BASE   | TAMANHO   | DEC   | OBSERVAÇÃO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------|----------------------------------------------------------------------------------------------------------------|-------------|-----------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tpSucesso            | O conteúdo deste campo indica se o pedido do serviço obteve sucesso ou não (conforme descrito no item (4.3.1). | B           |           |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tpTempoProcessamento | Tempo de processamento (segundos).                                                                             | N           | 1-15      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tpTipoLogradouro     | Tipo de endereço.                                                                                              | C           | 0-3       |       | Rua, Av, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| tpTipoRPS            | Tipo do RPS.                                                                                                   | C           | 1         |       | Tipo do RPS: RPS - Recibo Provisório de Serviços; RPS-M - Recibo Provisório de Serviços proveniente de Nota Fiscal Conjugada (Mista);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tpTributacaoNFe      | Tipo de Tributação                                                                                             | C           | 1         |       | RPS-C - Cupom. a) NFS-e emitidas até 22/02/2015: poderá ser preenchido com: T - Tributação no município de São Paulo; F - Tributação fora do município de São Paulo; I - Isento/Imune; J - ISS Suspenso por Decisão Judicial. b) NFS-e emitidas a partir de 23/02/2015: poderá ser preenchido com: T - Tributado em São Paulo F - Tributado Fora de São Paulo A - Tributado em São Paulo, porém Isento B - Tributado Fora de São Paulo, porém Isento D - Tributado em São Paulo com isenção parcial M - Tributado em São Paulo, porém com indicação de imunidade subjetiva N - Tributado Fora de São Paulo, porém com indicação de imunidade subjetiva R - Tributado em São Paulo, porém com indicação de imunidade objetiva S - Tributado fora de São Paulo, porém com indicação de imunidade objetiva X - Tributado em São Paulo, porém Exigibilidade Suspensa V - Tributado Fora de São Paulo, porém Exigibilidade Suspensa P - Exportação de Serviços |
| tpUF                 | Sigla da UF do endereço.                                                                                       | C           | 2         |       | Sigla da UF do endereço.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tpValor              | Valores                                                                                                        | N           | 0-15      | 2     | Tipo utilizado para valores com 15 dígitos, sendo 13 de corpo e 2 decimais. Exemplo: R$ 500,85 - 500.85 R$ 826,00 - 826                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| NOME DO TIPO                 | DESCRIÇÃO (tipo utilizado para informar...)               | TIPO BASE   | TAMANHO   | DEC   | OBSERVAÇÃO                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------|-----------------------------------------------------------|-------------|-----------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tpVersao                     | Versão                                                    | N           | 1-3       |       | O conteúdo deste campo indica a versão do Schema XML utilizado. Exemplo: Versão 1 - 1 Versão 10 - 10 Versão 100 - 100                                                                                                                                                                                                                                                    |
| tpPercentualCargaTributari a | Percentual da carga tributária                            | N           | 7         | 4     | Exemplo: 5% - 0.05 2,5% - 0.025 1,75% - 0.0175                                                                                                                                                                                                                                                                                                                           |
| tpFonteCargaTributaria       | Fonte de informação da carga tributária                   | C           | 0-10      |       | Exemplo: IBPT                                                                                                                                                                                                                                                                                                                                                            |
| tpNumeroProtocoloAsync       | Número do protocolo devolvido nos serviços assíncronos    | C           | 32        |       | Formato GUID, conforme informado no Item 4                                                                                                                                                                                                                                                                                                                               |
| tpIncidencia                 | Incidência                                                | C           | 7         |       | Formato AAAA-MM                                                                                                                                                                                                                                                                                                                                                          |
| tpSituacaoLote               | Situações do processamento do Lote Assíncrono             | C           | 1         |       | Tipos da Situação: enviado - 0 invalidado - 1 verificado - 2 processado - 3                                                                                                                                                                                                                                                                                              |
| tpSituacaoGuia               | Situações do processamento da Guia por serviço Assíncrono | C           | 1         |       | Tipos da Situação: solicitada - 0 invalidada - 1 verificada - 2 processada - 3                                                                                                                                                                                                                                                                                           |
| tpEmissaoGuia                | Tipos de Emissão da Guia                                  | N           | 1         |       | Tipos: 1-Guia de NFS-e emitidas 2-Guia de NFS-e recebidas (exceto rejeitadas) 3-Guia de NFS-e Emitidas e Recebidas (exceto rejeitadas) 4-Guia de NFS-e recebidas aceitas 5-Guia de NFS-e recebidas sem manifestação do tomador 6-Guia de NFS-e recebidas rejeitadas 7-Guia de NFTS emitidas 8-Todas (NFS-e emitidas, NFTS emitidas e NFS-e recebidas, exceto rejeitadas) |
| tpSituacaoGuia               | Tipos de Situação da Guia                                 | N           | 1         |       | Tipos: 1 - Guias pendentes de pagamento 2 - Guias quitadas 3 - Guias canceladas 4 - Guias pendente de emissão                                                                                                                                                                                                                                                            |

| NOME DO TIPO                    | DESCRIÇÃO (tipo utilizado para informar...)                                                                                                                        | TIPO BASE   |   TAMANHO | DEC   | OBSERVAÇÃO                                                                                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| tpStatusGuiaEnum                | Tipos de Situação de pagamento da Guia                                                                                                                             | N           |         1 |       | Tipos: 0 - Normal 1 - Cancelada 2 - Quitada 3 - Aproveitada 4 - Alterada 5 - Quitada Por RDT 6 - Quitada por Substituição 7 - Quitada por Retificação |
| tpExigibilidadeSuspensa         | Tipo emissão com exigibilidade suspensa                                                                                                                            | C           |         1 |       | 0 = Não 1 = Sim                                                                                                                                       |
| tpOnerosidade                   | Tipo de serviço                                                                                                                                                    | C           |         1 |       | 0 = Não onerosa 1 = Onerosa                                                                                                                           |
| tpPagamentoParceladoAnt ecipado | Tipo do indicador de nota fiscal de pagamento parcelado antecipado (realizado antes do fornecimento)                                                               | C           |         1 |       | 0 = Não 1 = Sim                                                                                                                                       |
| tpCodigoNCM                     | Código da lista de Nomenclatura Comum do Mercosul (NCM)                                                                                                            | C           |         8 |       | Exemplo: 3404.90.29 - 34049029                                                                                                                        |
| tpCodigoPaisISO                 | Tipo Código do País segundo tabela ISO                                                                                                                             | C           |         2 |       | Exemplo: CA - Canadá                                                                                                                                  |
| tpCodigoNBS                     | Código da lista de Nomenclatura Brasileira de Serviços (NBS)                                                                                                       | C           |         9 |       | Exemplo: 1.1805.40.00 - 118054000                                                                                                                     |
| tpReferencia                    | Tipo de referência da Nota                                                                                                                                         | C           |         1 |       | 0 - Nota fiscal referenciada para emissão de nota de multa e juros 1 - Nota fiscal de pagamento parcelado antecipado                                  |
| tpTipoNotaReferenciada          | Tipo de nota fiscal referenciada.                                                                                                                                  | C           |         1 |       | 0 - NFS-e 1 - NFTS                                                                                                                                    |
| tpCClassTribIBSCBS              | Código de classificação Tributária do IBS e da CBS principal                                                                                                       | N           |         6 |       | Exemplo: 550016                                                                                                                                       |
| tpCClassTribReg                 | Código de classificação Tributária do IBS e da CBS secundário, que informa a tributação original ser utilizada caso os requisitos da suspensão não sejam cumpridos | N           |         6 |       | Exemplo: 200045                                                                                                                                       |
| tpEnteGov                       | Tipo do ente da compra governamental                                                                                                                               | C           |         1 |       | 1 - União 2 - Estados 3 - Distrito Federal 4 - Municípios                                                                                             |
| tpEstadoProvinciaRegiao         | Estado, província ou região                                                                                                                                        | C           |        60 |       | Estado, província ou região                                                                                                                           |
| tpIndicadorCompraGov            | Tipo do indicador de compra governamental.                                                                                                                         | C           |         1 |       | 0 - Não 1 - Sim                                                                                                                                       |
| tpNaoNIF                        | Tipo do motivo para não informação do NIF.                                                                                                                         | C           |         1 |       | 0 - Não informado na nota de origem 1 - Dispensado do NIF 2 - Não exigência do NIF                                                                    |

| NOME DO TIPO           | DESCRIÇÃO (tipo utilizado para informar...)                                                                 | TIPO BASE   |   TAMANHO | DEC   | OBSERVAÇÃO                        |
|------------------------|-------------------------------------------------------------------------------------------------------------|-------------|-----------|-------|-----------------------------------|
| tpNIF                  | Tipo NIF (Número de Identificação Fiscal) - fornecido por um órgão de administração tributária no exterior. | C           |        40 |       |                                   |
| tpCCIB                 | Cadastro de imóveis.                                                                                        | C           |         8 |       |                                   |
| tpModoPrestacaoServico | Tipo Modo de prestação do serviço.                                                                          | C           |         1 |       | 1 - Presencial 2 - Não presencial |
| tpNomeCidade           | Nome da Cidade                                                                                              | C           |        60 |       |                                   |

## 4.2.2. Tipos Complexos

Layout da tabela utilizada para representar a estrutura XML dos Tipos Complexos:

| <Nome do tipo complexo>                      | <Nome do tipo complexo>         | <Nome do tipo complexo>      | <Nome do tipo complexo>      | <Nome do tipo complexo>      |
|----------------------------------------------|---------------------------------|------------------------------|------------------------------|------------------------------|
| <Descrição do tipo complexo>                 | <Descrição do tipo complexo>    | <Descrição do tipo complexo> | <Descrição do tipo complexo> | <Descrição do tipo complexo> |
| Nome do Elemento                             | Nome do Elemento                | Tipo do Elemento             | Ocorrência*                  | Descrição                    |
| <Nome do elemento1>                          | <Nome do elemento1>             | <Tipo do elemento 1>         | x-y                          | <Descrição do elemento 1>    |
| <Nome do elemento...>                        | <Nome do elemento...>           | <Tipo do elemento ...>       | x-y                          | <Descrição do elemento ...>  |
| Elemento que deriva de uma escolha (Choice). | <Nome do elemento de escolha a> | <Tipo do elemento a>         | x-y                          | <Descrição do elemento a>    |
| Elemento que deriva de uma escolha (Choice). | <Nome do elemento de escolha b> | <Tipo do elemento b>         | x-y                          | <Descrição do elemento b>    |
| Elemento que deriva de uma escolha (Choice). | <Nome do elemento de escolha c> | <Tipo do elemento c>         | x-y                          | <Descrição do elemento c>    |
| <Nome do elemento N>                         | <Nome do elemento N>            | <Tipo do elemento N>         | x-y                          | <Descrição do elemento N>    |

* Ocorrência: x - y, onde x indica a ocorrência mínima e y a ocorrência máxima.

| tpEvento                                                                                                                                               | tpEvento   | tpEvento          | tpEvento   | tpEvento                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-------------------|------------|----------------------------------------------------------------------------------------|
| Tipo que representa a ocorrência de eventos de erro/alerta                                                                                             | Elemento   | Tipo do Elemento  | Ocorrência | Descrição                                                                              |
| Codigo                                                                                                                                                 | Codigo     | tpCodigoEvento    | 1-1        | Código do evento ocorrido.                                                             |
| Descricao                                                                                                                                              | Descricao  | tpDescricaoEvento | 0-1        | Descrição do evento ocorrido.                                                          |
| (Choice) Caso o evento tenha sido gerado durante o processamento de uma NF-e (ou RPS), o tpEvento tambem retorna a chave da NF-e (ou RPS) que o gerou. | ChaveNFe   | tpChaveNFe        | 0-1        | Chave de identificação da NF-e que gerou o evento (ver detalhes na tabela tpChaveNFe). |
| (Choice) Caso o evento tenha sido gerado durante o processamento de uma NF-e (ou RPS), o tpEvento tambem retorna a chave da NF-e (ou RPS) que o gerou. | ChaveRPS   | tpChaveRPS        | 0-1        | Chave de identificação do RPS que gerou o evento (ver detalhes na tabela tpChaveRPS).  |

| tpCPFCNPJ                       | tpCPFCNPJ                       | tpCPFCNPJ                       | tpCPFCNPJ                       | tpCPFCNPJ                                       |
|---------------------------------|---------------------------------|---------------------------------|---------------------------------|-------------------------------------------------|
| Tipo que representa um CPF/CNPJ | Tipo que representa um CPF/CNPJ | Tipo que representa um CPF/CNPJ | Tipo que representa um CPF/CNPJ | Tipo que representa um CPF/CNPJ                 |
| Nome do Elemento                | Nome do Elemento                | Tipo do Elemento                | Ocorrência                      | Descrição                                       |
| (Choice)                        | CPF                             | tpCPF                           | 1-1                             | Número no Cadastro de Pessoas Físicas.          |
| (Choice)                        | CNPJ                            | tpCNPJ                          | 1-1                             | Número no Cadastro Nacional da Pessoa Jurídica. |

| tpChaveNFeRPS                                                                   | tpChaveNFeRPS                                                                   | tpChaveNFeRPS                                                                   | tpChaveNFeRPS                                                                           |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Tipo que representa a Chave de uma NF-e e a Chave do RPS que a mesma substitui. | Tipo que representa a Chave de uma NF-e e a Chave do RPS que a mesma substitui. | Tipo que representa a Chave de uma NF-e e a Chave do RPS que a mesma substitui. | Tipo que representa a Chave de uma NF-e e a Chave do RPS que a mesma substitui.         |
| Nome do Elemento                                                                | Tipo do Elemento                                                                | Ocorrência                                                                      | Descrição                                                                               |
| ChaveNFe                                                                        | tpChaveNFe                                                                      | 1-1                                                                             | Chave de identificação da NF-e que substitui o RPS (ver detalhes na tabela tpChaveNFe). |
| ChaveRPS                                                                        | tpChaveRPS                                                                      | 1-1                                                                             | Chave de identificação do RPS substituído (ver detalhes na tabela tpChaveRPS).          |

| tpChaveNFe                              | tpChaveNFe                              | tpChaveNFe                              | tpChaveNFe                                          |
|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------------------|
| Tipo que representa a chave de uma NF-e | Tipo que representa a chave de uma NF-e | Tipo que representa a chave de uma NF-e | Tipo que representa a chave de uma NF-e             |
| Nome do Elemento                        | Tipo do Elemento                        | Ocorrência                              | Descrição                                           |
| InscricaoPrestador                      | tplnscricaoMunicipal                    | 1-1                                     | Inscrição Municipal do Prestador que emitiu a NF-e. |
| Numero                                  | tpNumero                                | 1-1                                     | Número da NF-e.                                     |
| CodigoVerificacao                       | tpCodigoVerificacao                     | 0-1                                     | Código de Verificação da NF-e.                      |

| tpChaveRPS                                       | tpChaveRPS                                       | tpChaveRPS                                       | tpChaveRPS                                         |
|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|----------------------------------------------------|
| Tipo que define a chave identificadora de um RPS | Tipo que define a chave identificadora de um RPS | Tipo que define a chave identificadora de um RPS | Tipo que define a chave identificadora de um RPS   |
| Nome do Elemento                                 | Tipo do Elemento                                 | Ocorrência                                       | Descrição                                          |
| InscricaoPrestador                               | tplnscricaoMunicipal                             | 1-1                                              | Inscrição Municipal do Prestador que emitiu o RPS. |
| SerieRPS                                         | tpSerieRPS                                       | 0-1                                              | Série do RPS.                                      |
| NumeroRPS                                        | tpNumero                                         | 1-1                                              | Número do RPS.                                     |

| tpEndereco                      | tpEndereco                      | tpEndereco                      | tpEndereco                         |
|---------------------------------|---------------------------------|---------------------------------|------------------------------------|
| Tipo que representa um Endereço | Tipo que representa um Endereço | Tipo que representa um Endereço | Tipo que representa um Endereço    |
| Nome do Elemento                | Tipo do Elemento                | Ocorrência                      | Descrição                          |
| TipoLogradouro                  | tpTipoLogradouro                | 0-1                             | Tipo do endereço.                  |
| Logradouro                      | tpLogradouro                    | 0-1                             | Endereço.                          |
| NumeroEndereco                  | tpNumeroEndereco                | 0-1                             | Número do endereço.                |
| ComplementoEndereco             | tpComplementoEndereco           | 0-1                             | Complemento do endereço.           |
| Bairro                          | tpBairro                        | 0-1                             | Bairro do endereço.                |
| Cidade                          | tpCidade                        | 0-1                             | Código IBGE da cidade do endereço. |
| UF                              | tpUF                            | 0-1                             | Sigla da UF do endereço.           |

.2

| tpEndereco                      | tpEndereco                      | tpEndereco                      | tpEndereco                      |
|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| Tipo que representa um Endereço | Tipo que representa um Endereço | Tipo que representa um Endereço | Tipo que representa um Endereço |
| Nome do Elemento                | Tipo do Elemento                | Ocorrência                      | Descrição                       |
| CEP                             | tpCEP                           | 0-1                             | CEP do endereço.                |

| tpEndereco (complemento para a versão 2.0)            | tpEndereco (complemento para a versão 2.0)            | tpEndereco (complemento para a versão 2.0)            | tpEndereco (complemento para a versão 2.0)            |
|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Acréscimo no tpEndereco para Reforma tributária 2026. | Acréscimo no tpEndereco para Reforma tributária 2026. | Acréscimo no tpEndereco para Reforma tributária 2026. | Acréscimo no tpEndereco para Reforma tributária 2026. |
| Nome do Elemento                                      | Tipo do Elemento                                      | Ocorrência                                            | Descrição                                             |
| EnderecoExterior                                      | tpEnderecoExterior                                    | 0-1                                                   | Tipo endereço no exterior.                            |

| tplnformacoesLote                                     | tplnformacoesLote                                     | tplnformacoesLote                                     | tplnformacoesLote                                             |
|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------|
| Tipo que representa as informações do lote processado | Tipo que representa as informações do lote processado | Tipo que representa as informações do lote processado | Tipo que representa as informações do lote processado         |
| Nome do Elemento                                      | Tipo do Elemento                                      | Ocorrência                                            | Descrição                                                     |
| NumeroLote                                            | tpNumero                                              | 0-1                                                   | Número do lote.                                               |
| InscricaoPrestador                                    | tplnscricaoMunicipal                                  | 1-1                                                   | Inscrição Municipal do prestador dos RPS contidos no lote.    |
| CPFCNPJRemetente                                      | tpCPFCNPJ                                             | 1-1                                                   | CPF/CNPJ do remetente autorizado a transmitir a mensagem XML. |
| DataEnvioLote                                         | dateTime                                              | 1-1                                                   | Data/Hora do envio do lote (AAAA-MM- DDThh:mm:ss).            |
| QtdNotas                                              | tpQuantidade                                          | 1-1                                                   | Quantidade de RPS contidos no lote.                           |
| TempoProcessamento                                    | tpTempoProcessamento                                  | 1-1                                                   | Tempo de processamento do lote.                               |
| ValorTotalServicos                                    | tpValor                                               | 1-1                                                   | Valor total dos serviços dos RPS contidos na mensagem XML.    |
| ValorTotalDeducoes                                    | tpValor                                               | 0-1                                                   | Valor total das deduções dos RPS contidos na mensagem XML.    |

| tpNFe                        | tpNFe                        | tpNFe                        | tpNFe                                                                     |
|------------------------------|------------------------------|------------------------------|---------------------------------------------------------------------------|
| Tipo que representa uma NF-e | Tipo que representa uma NF-e | Tipo que representa uma NF-e | Tipo que representa uma NF-e                                              |
| Nome do Elemento             | Tipo do Elemento             | Ocorrênci a                  | Descrição                                                                 |
| Assinatura                   | tpAssinatura                 | 0-1                          | Assinatura do RPS que gerou a NF-e (conforme especificado no Item 4.3.2). |
| ChaveNFe                     | tpChaveNFe                   | 1-1                          | Chave de identificação da NF-e (ver detalhes na tabela tpChaveNFe).       |
| DataEmissaoNFe               | dateTime                     | 1-1                          | Data/Hora da emissão da NF-e (AAAA-MM- DDThh:mm:ss).                      |
| NumeroLote                   | tpNumero                     | 0-1                          | Número do lote que gerou a NF-e.                                          |
| ChaveRPS                     | tpChaveRPS                   | 0-1                          | Chave de identificação do RPS (ver detalhes na tabela tpChaveRPS).        |
| TipoRPS                      | tpTipoRPS                    | 0-1                          | Tipo do RPS.                                                              |
| DataEmissaoRPS               | date                         | 0-1                          | Data da emissão do RPS.                                                   |
| DataFatoGeradorNFe           | dateTime                     | 1-1                          | Data do fato gerador da NF-e                                              |
| CPFCNPJPrestador             | tpCPFCNPJ                    | 1-1                          | CPF/CNPJ do prestador.                                                    |
| RazaoSocialPrestador         | tpRazaoSocial                | 1-1                          | Nome / Razão Social do prestador.                                         |
| EnderecoPrestador            | tpEndereco                   | 1-1                          | Endereço do prestador.                                                    |
| EmailPrestador               | tpEmail                      | 0-1                          | E-mail do prestador.                                                      |
| StatusNFe                    | tpStatusNFe                  | 1-1                          | Status da NF-e.                                                           |

| tpNFe                            | tpNFe                        | tpNFe                        | tpNFe                                                                                                                |
|----------------------------------|------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Tipo que representa uma NF-e     | Tipo que representa uma NF-e | Tipo que representa uma NF-e | Tipo que representa uma NF-e                                                                                         |
| Nome do Elemento                 | Tipo do Elemento             | Ocorrênci a                  | Descrição                                                                                                            |
| DataCancelamento                 | date                         | 0-1                          | Se a NF-e tiver sido cancelada, este campo será preenchido com a data de cancelamento da NF-e (AAAA-MM-DDThh:mm:ss). |
| TributacaoNFe                    | tpTributacaoNFe              | 1-1                          | Tipo de tributação da NF-e.                                                                                          |
| OpcaoSimples                     | tpOpcaoSimples               | 1-1                          | Tipo de opção pelo Simples.                                                                                          |
| NumeroGuia                       | tpNumero                     | 0-1                          | Número da guia vinculada a NF-e.                                                                                     |
| DataQuitacaoGuia                 | Date                         | 0-1                          | Data de quitação da guia vinculada a NF-e.                                                                           |
| ValorServicos                    | tpValor                      | 1-1                          | Valor dos serviços em R$.                                                                                            |
| ValorDeducoes                    | tpValor                      | 0-1                          | Valor das deduções em R$.                                                                                            |
| ValorPIS                         | tpValor                      | 0-1                          | Valor da retenção do PIS em R$.                                                                                      |
| ValorCOFINS                      | tpValor                      | 0-1                          | Valor da retenção do COFINS em R$.                                                                                   |
| ValorINSS                        | tpValor                      | 0-1                          | Valor da retenção do INSS em R$.                                                                                     |
| ValorIR                          | tpValor                      | 0-1                          | Valor da retenção do IR em R$.                                                                                       |
| ValorCSLL                        | tpValor                      | 0-1                          | Valor da retenção do CSLL em R$.                                                                                     |
| CodigoServico                    | tpCodigo                     | 1-1                          | Código do serviço prestado.                                                                                          |
| AliquotaServicos                 | tpAliquota                   | 1-1                          | Alíquota do serviço prestado.                                                                                        |
| ValorISS                         | tpValor                      | 1-1                          | Valor do ISS em R$.                                                                                                  |
| ValorCredito                     | tpValor                      | 1-1                          | Valor do crédito gerado.                                                                                             |
| ISSRetido                        | Boolean                      | 1-1                          | Retenção do ISS. Preencher com: "true" - para NF-e com ISS Retido; "false" - para NF-e sem ISS Retido                |
| CPFCNPJTomador                   | tpCPFCNPJ                    | 0-1                          | CPF/CNPJ do tomador.                                                                                                 |
| InscricaoMunicipalTomador        | tpInscricaoMunicipal         | 0-1                          | Inscrição Municipal do tomador.                                                                                      |
| InscricaoEstadualTomador         | tpInscricaoEstadual          | 0-1                          | Inscrição Estadual do tomador.                                                                                       |
| RazaoSocialTomador               | tpRazaoSocial                | 0-1                          | Nome / Razão Social do tomador.                                                                                      |
| EnderecoTomador                  | tpEndereco                   | 0-1                          | Endereço do tomador.                                                                                                 |
| EmailTomador                     | tpEmail                      | 0-1                          | E-mail do tomador.                                                                                                   |
| CPFCNPJIntermediario             | tpCPFCNPJ                    | 0-1                          | CPF/CNPJ do intermediário                                                                                            |
| InscricaoMunicipalIntermediari o | tpInscricaoMunicipal         | 0-1                          | Inscrição Municipal do intermediário.                                                                                |
| ISSRetidoIntermediario           | Boolean                      | 0-1                          | 'true' - para NF-e com ISS Retido pelo Intermediário 'false' - para NF-e sem retenção pelo Intermediário             |
| EmailIntermediario               | tpEmail                      | 0-1                          | E-mail do intermediário                                                                                              |
| ValorCargaTributaria             | tpValor                      | 0-1                          | Valor da carga tributária total em R$.                                                                               |
| PercentualCargaTributaria        | tpPercentualCargaTributari a | 0-1                          | Valor percentual da carga tributária                                                                                 |
| FonteCargaTributaria             | tpFonteCargaTributaria       | 0-1                          | Fonte de informação da carga tributária                                                                              |
| CodigoCEI                        | tpNumero                     | 0-1                          | Código do CEI - Cadastro específico do INSS                                                                          |
| MatriculaObra                    | tpNumero                     | 0-1                          | Número da matrícula de obra.                                                                                         |

| tpNFe                        | tpNFe                        | tpNFe                        | tpNFe                                                                                                                  |
|------------------------------|------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Tipo que representa uma NF-e | Tipo que representa uma NF-e | Tipo que representa uma NF-e | Tipo que representa uma NF-e                                                                                           |
| Nome do Elemento             | Tipo do Elemento             | Ocorrênci a                  | Descrição                                                                                                              |
| MunicipioPrestacao           | tpCidade                     | 0-1                          | Código do município onde ocorreu a prestação do serviço, conforme tabela de Códigos de Municípios elaborada pelo IBGE. |
| NumeroEncapsulamento         | tpNumero                     | 0-1                          | Código do encapsulamento de notas dedutoras.                                                                           |
| ValorTotalRecebido           | tpValor                      | 0-1                          | Valor Total Recebido em R$ (inclusive valores repassados a terceiros).                                                 |
| Discriminacao                | tpDiscriminacao              | 1-1                          | Discriminação dos serviços.                                                                                            |

| tpNFE (complemento para a versão 2.0)                                                                                                                           | tpNFE (complemento para a versão 2.0)                                                                                                                           | tpNFE (complemento para a versão 2.0)                                                                                                                           | tpNFE (complemento para a versão 2.0)                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Atenção: utilizar como complemento da versão 1.0 do tpNFE, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. | Atenção: utilizar como complemento da versão 1.0 do tpNFE, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. | Atenção: utilizar como complemento da versão 1.0 do tpNFE, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. | Atenção: utilizar como complemento da versão 1.0 do tpNFE, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. |
| Nome do Elemento                                                                                                                                                | Tipo do Elemento                                                                                                                                                | Ocorrência                                                                                                                                                      | Descrição                                                                                                                                                       |
| ValorInicialCobrado                                                                                                                                             | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor Inicial.                                                                                                                                                  |
| ValorFinalCobrado                                                                                                                                               | tpValor                                                                                                                                                         | 1-1                                                                                                                                                             | Valor total cobrado pela prestação do serviço.                                                                                                                  |
| ValorMulta                                                                                                                                                      | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor da multa.                                                                                                                                                 |
| ValorJuros                                                                                                                                                      | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor dos juros.                                                                                                                                                |
| ValorDeducaoCIBS                                                                                                                                                | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor de dedução da base de cálculo do IBS e CBS.                                                                                                               |
| ValorIPI                                                                                                                                                        | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor IPI                                                                                                                                                       |
| ExigibilidadeSuspensa                                                                                                                                           | tpExigibilidadeSuspensa                                                                                                                                         | 1-1                                                                                                                                                             | Informe se é uma emissão com exigibilidade suspensa. 0 - Não 1 - Sim                                                                                            |
| Onerosidade                                                                                                                                                     | tpOnerosidade                                                                                                                                                   | 1-1                                                                                                                                                             | Informe se o serviço é oneroso.                                                                                                                                 |
| PagamentoParceladoAntecipado                                                                                                                                    | tpPagamentoParceladoAntecipado                                                                                                                                  | 1-1                                                                                                                                                             | Informe se a nota teve pagamento parcelado antecipado.                                                                                                          |
| NCM                                                                                                                                                             | tpCodigoNCM                                                                                                                                                     | 0-1                                                                                                                                                             | Informe o número NCM (Nomenclatura Comum do Mercosul).                                                                                                          |
| NBS                                                                                                                                                             | tpCodigoNBS                                                                                                                                                     | 0-1                                                                                                                                                             | Informe o número NBS (Nomenclatura Brasileira de Serviços).                                                                                                     |
| NotaReferenciada                                                                                                                                                | tpNotaReferenciada                                                                                                                                              | 0-1                                                                                                                                                             | Informações da nota referenciada.                                                                                                                               |
| IBSCBS                                                                                                                                                          | tpIBSCBS                                                                                                                                                        | 0-1                                                                                                                                                             | Informações declaradas pelo emitente referentes ao IBS e à CBS.                                                                                                 |

| TpRPS                   | TpRPS                   | TpRPS                   | TpRPS                                                              |
|-------------------------|-------------------------|-------------------------|--------------------------------------------------------------------|
| Tipo que representa RPS | Tipo que representa RPS | Tipo que representa RPS | Tipo que representa RPS                                            |
| Nome do Elemento        | Tipo do Elemento        | Ocorrência              | Descrição                                                          |
| Assinatura              | tpAssinatura            | 1-1                     | Assinatura do RPS emitido (conforme especificado no Item 4.3.2).   |
| ChaveRPS                | tpChaveRPS              | 1-1                     | Chave de identificação do RPS (ver detalhes na tabela tpChaveRPS). |
| TipoRPS                 | tpTipoRPS               | 1-1                     | Tipo do RPS.                                                       |
| DataEmissao             | date                    | 1-1                     | Data da emissão do RPS.                                            |
| StatusRPS               | tpStatusNFe             | 1-1                     | Status do RPS.                                                     |
| TributacaoRPS           | tpTributacaoNFe         | 1-1                     | Tipo de tributação do RPS.                                         |
| ValorServicos           | tpValor                 | 1-1                     | Valor dos serviços em R$.                                          |
| ValorDeducoes           | tpValor                 | 1-1                     | Valor das deduções em R$.                                          |
| ValorPIS                | tpValor                 | 0-1                     | Valor da retenção do PIS em R$.                                    |
| ValorCOFINS             | tpValor                 | 0-1                     | Valor da retenção do COFINS em R$.                                 |
| ValorINSS               | tpValor                 | 0-1                     | Valor da retenção do INSS em R$.                                   |

| TpRPS                            | TpRPS                        | TpRPS                   | TpRPS                                                                                                                                                                                                                                                                                                        |
|----------------------------------|------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipo que representa RPS          | Tipo que representa RPS      | Tipo que representa RPS | Tipo que representa RPS                                                                                                                                                                                                                                                                                      |
| Nome do Elemento                 | Tipo do Elemento             | Ocorrência              | Descrição                                                                                                                                                                                                                                                                                                    |
| ValorIR                          | tpValor                      | 0-1                     | Valor da retenção do IR em R$.                                                                                                                                                                                                                                                                               |
| ValorCSLL                        | tpValor                      | 0-1                     | Valor da retenção do CSLL em R$.                                                                                                                                                                                                                                                                             |
| CodigoServico                    | tpCodigo                     | 1-1                     | Código do serviço prestado.                                                                                                                                                                                                                                                                                  |
| AliquotaServicos                 | tpAliquota                   | 1-1                     | Alíquota do serviço prestado.                                                                                                                                                                                                                                                                                |
| ISSRetido                        | Boolean                      | 1-1                     | Retenção do ISS. Preencher com: "true" - para NF-e com ISS Retido; "false" - para NF-e sem ISS Retido                                                                                                                                                                                                        |
| CPFCNPJTomador                   | tpCPFCNPJ                    | 0-1                     | CPF/CNPJ do tomador do serviço.                                                                                                                                                                                                                                                                              |
| InscricaoMunicipalTomador        | tpInscricaoMunicip al        | 0-1                     | Inscrição Municipal do tomador. ATENÇÃO 1: Este elemento só deverá ser preenchido para tomadores estabelecidos no município de São Paulo (CCM). ATENÇÃO 2: O preenchimento deste elemento implica na obrigatoriedade do preenchimento do elemento CPFCNPJTomador. Será verificado se o CNPJ vinculado ao CCM |
| InscricaoEstadualTomador         | tpInscricaoEstadual          | 0-1                     | Inscrição Estadual do tomador.                                                                                                                                                                                                                                                                               |
| RazaoSocialTomador               | tpRazaoSocial                | 0-1                     | Nome / Razão Social do tomador.                                                                                                                                                                                                                                                                              |
| EnderecoTomador                  | tpEndereco                   | 0-1                     | Endereço do tomador.                                                                                                                                                                                                                                                                                         |
| EmailTomador                     | tpEmail                      | 0-1                     | E-mail do tomador.                                                                                                                                                                                                                                                                                           |
| CPFCNPJIntermediario             | tpCPFCNPJ                    | 0-1                     | CPF/CNPJ do intermediário do serviço.                                                                                                                                                                                                                                                                        |
| InscricaoMunicipalIntermediari o | tpInscricaoMunicip al        | 0-1                     | Inscrição Municipal do intermediário. ATENÇÃO 1: Este elemento só deverá ser preenchido para intermediários estabelecidos no município de São Paulo (CCM). Será verificado se o CNPJ vinculado ao CCM corresponde ao CNPJ informado no elemento                                                              |
| ISSRetidoIntermediario           | Boolean                      | 0-1                     | 'true' - para NF-e com ISS Retido pelo Intermediário 'false' - para NF-e sem retenção pelo Intermediário Caso o Intermediário não seja identificado, essa tag não deverá ocorrer.                                                                                                                            |
| EmailIntermediario               | tpEmail                      | 0-1                     | E-mail do intermediário                                                                                                                                                                                                                                                                                      |
| Discriminacao                    | tpDiscriminacao              | 1-1                     | Discriminação dos serviços.                                                                                                                                                                                                                                                                                  |
| ValorCargaTributaria             | tpValor                      | 0-1                     | Valor da carga tributária total em R$.                                                                                                                                                                                                                                                                       |
| PercentualCargaTributaria        | tpPercentualCarga Tributaria | 0-1                     | Valor percentual da carga tributária                                                                                                                                                                                                                                                                         |
| FonteCargaTributaria             | tpFonteCargaTribut aria      | 0-1                     | Fonte de informação da carga tributária                                                                                                                                                                                                                                                                      |
| CodigoCEI                        | tpNumero                     | 0-1                     | Código do CEI - Cadastro específico do INSS                                                                                                                                                                                                                                                                  |
| MatriculaObra                    | tpNumero                     | 0-1                     | Número da matrícula de obra.                                                                                                                                                                                                                                                                                 |

| TpRPS                   | TpRPS                   | TpRPS                   | TpRPS                                                                                                                  |
|-------------------------|-------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| Tipo que representa RPS | Tipo que representa RPS | Tipo que representa RPS | Tipo que representa RPS                                                                                                |
| Nome do Elemento        | Tipo do Elemento        | Ocorrência              | Descrição                                                                                                              |
| MunicipioPrestacao      | tpCidade                | 0-1                     | Código do município onde ocorreu a prestação do serviço, conforme tabela de Códigos de Municípios elaborada pelo IBGE. |
| ValorTotalRecebido      | tpValor                 | 0-1                     | Valor Total Recebido em R$ (inclusive valores repassados a terceiros).                                                 |
| NumeroEncapsulamento    | tpNumero                | 0-1                     | Código do encapsulamento de notas dedutoras.                                                                           |

| tpRPS (complemento para a versão 2.0)                                                                                                                           | tpRPS (complemento para a versão 2.0)                                                                                                                           | tpRPS (complemento para a versão 2.0)                                                                                                                           | tpRPS (complemento para a versão 2.0)                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Atenção: utilizar como complemento da versão 1.0 do tpRPS, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. | Atenção: utilizar como complemento da versão 1.0 do tpRPS, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. | Atenção: utilizar como complemento da versão 1.0 do tpRPS, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. | Atenção: utilizar como complemento da versão 1.0 do tpRPS, são os campos adicionados que correspondem à versão 2.0 para atendimento da Reforma Tributária 2026. |
| Nome do Elemento                                                                                                                                                | Tipo do Elemento                                                                                                                                                | Ocorrência                                                                                                                                                      | Descrição                                                                                                                                                       |
| ValorInicialCobrado                                                                                                                                             | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor Inicial.                                                                                                                                                  |
| ValorFinalCobrado                                                                                                                                               | tpValor                                                                                                                                                         | 1-1                                                                                                                                                             | Valor total cobrado pela prestação do serviço.                                                                                                                  |
| ValorMulta                                                                                                                                                      | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor da multa.                                                                                                                                                 |
| ValorJuros                                                                                                                                                      | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor dos juros.                                                                                                                                                |
| ValorDeducaoCIBS                                                                                                                                                | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor de dedução da base de cálculo do IBS e CBS.                                                                                                               |
| ValorIPI                                                                                                                                                        | tpValor                                                                                                                                                         | 0-1                                                                                                                                                             | Valor IPI                                                                                                                                                       |
| ExigibilidadeSuspensa                                                                                                                                           | tpExigibilidadeSuspensa                                                                                                                                         | 1-1                                                                                                                                                             | Informe se é uma emissão com exigibilidade suspensa. 0 - Não 1 - Sim                                                                                            |
| Onerosidade                                                                                                                                                     | tpOnerosidade                                                                                                                                                   | 1-1                                                                                                                                                             | Informe se o serviço é oneroso.                                                                                                                                 |
| PagamentoParceladoAntecipado                                                                                                                                    | tpPagamentoParceladoAntecipado                                                                                                                                  | 1-1                                                                                                                                                             | Informe se a nota teve pagamento parcelado antecipado.                                                                                                          |
| NCM                                                                                                                                                             | tpCodigoNCM                                                                                                                                                     | 0-1                                                                                                                                                             | Informe o número NCM (Nomenclatura Comum do Mercosul).                                                                                                          |
| NBS                                                                                                                                                             | tpCodigoNBS                                                                                                                                                     | 0-1                                                                                                                                                             | Informe o número NBS (Nomenclatura Brasileira de Serviços).                                                                                                     |
| NotaReferenciada                                                                                                                                                | tpNotaReferenciada                                                                                                                                              | 0-1                                                                                                                                                             | Informações da nota referenciada.                                                                                                                               |
| IBSCBS                                                                                                                                                          | tpIBSCBS                                                                                                                                                        | 0-1                                                                                                                                                             | Informações declaradas pelo emitente referentes ao IBS e à CBS.                                                                                                 |

r (v2)

| tpEventoAsync                                                                                                | tpEventoAsync                                                                                                | tpEventoAsync                                                                                                | tpEventoAsync                                                                                                |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Tipo que representa a ocorrência de eventos durante o processamento da mensagem XML nos serviços assíncronos | Tipo que representa a ocorrência de eventos durante o processamento da mensagem XML nos serviços assíncronos | Tipo que representa a ocorrência de eventos durante o processamento da mensagem XML nos serviços assíncronos | Tipo que representa a ocorrência de eventos durante o processamento da mensagem XML nos serviços assíncronos |
| Nome do Elemento                                                                                             | Tipo do Elemento                                                                                             | Ocorrência                                                                                                   | Descrição                                                                                                    |
| Codigo                                                                                                       | tpCodigoEvento                                                                                               | 1-1                                                                                                          | Código do evento ocorrido.                                                                                   |
| Descricao                                                                                                    | tpDescricaoEvento                                                                                            | 0-1                                                                                                          | Descrição do evento ocorrido.                                                                                |

| tpInformacoesLoteAsync                                                    | tpInformacoesLoteAsync                                                    | tpInformacoesLoteAsync                                                    | tpInformacoesLoteAsync                                                    |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Tipo que representa as informações do lote processado de forma assíncrona | Tipo que representa as informações do lote processado de forma assíncrona | Tipo que representa as informações do lote processado de forma assíncrona | Tipo que representa as informações do lote processado de forma assíncrona |
| Nome do Elemento                                                          | Tipo do Elemento                                                          | Ocorrência                                                                | Descrição                                                                 |
| NumeroProtocolo                                                           | tpNumeroProtocoloAsync                                                    | 1-1                                                                       | Número do protocolo do lote.                                              |
| DataRecebimento                                                           | date                                                                      | 1-1                                                                       | Data/hora de envio do lote.                                               |

| tpInformacoesGuiaAsync                                                    | tpInformacoesGuiaAsync                                                    | tpInformacoesGuiaAsync                                                    | tpInformacoesGuiaAsync                                                    |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Tipo que representa as informações da guia processada de forma assíncrona | Tipo que representa as informações da guia processada de forma assíncrona | Tipo que representa as informações da guia processada de forma assíncrona | Tipo que representa as informações da guia processada de forma assíncrona |
| Nome do Elemento                                                          | Tipo do Elemento                                                          | Ocorrência                                                                | Descrição                                                                 |
| NumeroProtocolo                                                           | tpNumeroProtocoloAsync                                                    | 1-1                                                                       | Número do protocolo do pedido de processamento da guia.                   |
| DataRecebimento                                                           | date                                                                      | 1-1                                                                       | Data/hora de envio do lote.                                               |

| tpGuia                                     | tpGuia                                     | tpGuia                                     | tpGuia                                                  |
|--------------------------------------------|--------------------------------------------|--------------------------------------------|---------------------------------------------------------|
| Tipo que representa as informações da guia | Tipo que representa as informações da guia | Tipo que representa as informações da guia | Tipo que representa as informações da guia              |
| Nome do Elemento                           | Tipo do Elemento                           | Ocorrência                                 | Descrição                                               |
| InscricaoPrestador                         | tpInscricaoMunicipal                       | 1-1                                        | Número do protocolo do pedido de processamento da guia. |
| NumeroGuia                                 | tpNumero                                   | 0-1                                        | Data/hora de envio do lote.                             |
| Incidencia                                 | tpIncidencia                               | 1-1                                        | Incidência da guia                                      |
| ValorTotal                                 | tpValor                                    | 0-1                                        | Valor total da guia                                     |
| ValorIss                                   | tpValor                                    | 0-1                                        | Valor do ISS                                            |
| ValorTotalPagamento                        | tpValor                                    | 0-1                                        | Valor total de pagamento                                |
| Status                                     | tpStatusGuia                               | 0-1                                        | Situação de pagamento a guia                            |
| Situacao                                   | tpSituacaoGuia                             | 1-1                                        | Situação da guia                                        |
| Referencia                                 | tpEmissaoGuia                              | 0-1                                        | Situação do tipo de notas da emissão da guia            |
| DataEmissao                                | date                                       | 0-1                                        | Data de emissão da guia                                 |
| DataVencimento                             | date                                       | 0-1                                        | Data de vencimento da guia                              |
| DataPagamento                              | date                                       | 0-1                                        | Data de pagamento da guia                               |
| DataQuitacao                               | date                                       | 0-1                                        | Data de quitação da guia                                |
| DataCancelamento                           | date                                       | 0-1                                        | Data de cancelamento da guia                            |
| LinhaDigitavel                             | Alfanumérico                               | 0-1                                        | Linha numérica para pagamento                           |

| tpStatusGuia                                                              | tpStatusGuia                                                              | tpStatusGuia                                                              | tpStatusGuia                                                              |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Tipo que representa as informações da guia processada de forma assíncrona | Tipo que representa as informações da guia processada de forma assíncrona | Tipo que representa as informações da guia processada de forma assíncrona | Tipo que representa as informações da guia processada de forma assíncrona |
| Nome do Elemento                                                          | Tipo do Elemento                                                          | Ocorrência                                                                | Descrição                                                                 |
| -                                                                         | tpStatusGuiaEnum                                                          | 1-1                                                                       | Tipo do Status da Guia                                                    |

| tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)   |
|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF            |
| Nome do Elemento                               | Nome do Elemento                               | Tipo do Elemento                               | Ocorrência                                     | Descrição                                      |
| (Choice)                                       | CPF                                            | tpCPF                                          | 1-1                                            | Número no Cadastro de Pessoas Físicas.         |
|                                                | CNPJ                                           | tpCNPJ                                         | 1-1                                            | Número no Cadastro de Pessoa Jurídica          |

| tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)   | tpCPFCNPJNIF (complemento para a versão 2.0)                                                                                  |
|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF            | Tipo que representa um CPF/CNPJ/NIF                                                                                           |
| Nome do Elemento                               | Nome do Elemento                               | Tipo do Elemento                               | Ocorrência                                     | Descrição                                                                                                                     |
|                                                | NIF                                            | tpNIF                                          | 1-1                                            | Tipo NIF (Número de Identificação Fiscal) - fornecido por um órgão de administração tributária no exterior.                   |
|                                                | NaoNIF                                         | tpNaoNIF                                       | 1-1                                            | Tipo do motivo para não informação do NIF. 0 - Não informado na nota de origem 1 - Dispensado do NIF 2 - Não exigência do NIF |

| tpEnderecoExterior (complemento para a versão 2.0)   | tpEnderecoExterior (complemento para a versão 2.0)   | tpEnderecoExterior (complemento para a versão 2.0)   | tpEnderecoExterior (complemento para a versão 2.0)                               |
|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------|
| Tipo endereço no exterior                            | Tipo endereço no exterior                            | Tipo endereço no exterior                            | Tipo endereço no exterior                                                        |
| Nome do Elemento                                     | Tipo do Elemento                                     | Ocorrência                                           | Descrição                                                                        |
| cPais                                                | tpCodigoPaisISO                                      | 1-1                                                  | Código do país (Tabela de Países ISO)                                            |
| cEndPost                                             | tpCodigoEndPostal                                    | 1-1                                                  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. |
| xCidade                                              | tpNomeCidade                                         | 1-1                                                  | Nome da cidade no exterior do prestador do serviço.                              |
| xEstProvReg                                          | tpEstadoProvinciaRegiao                              | 1-1                                                  | Estado, província ou região da cidade no exterior do prestador do serviço.       |

| tpInformacoesPessoa (complemento para a versão 2.0)   | tpInformacoesPessoa (complemento para a versão 2.0)   | tpInformacoesPessoa (complemento para a versão 2.0)   | tpInformacoesPessoa (complemento para a versão 2.0)   | tpInformacoesPessoa (complemento para a versão 2.0)                                                                           |
|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Tipo de informações de pessoa                         | Tipo de informações de pessoa                         | Tipo de informações de pessoa                         | Tipo de informações de pessoa                         | Tipo de informações de pessoa                                                                                                 |
| Nome do Elemento                                      | Nome do Elemento                                      | Tipo do Elemento                                      | Ocorrência                                            | Descrição                                                                                                                     |
| (Choice)                                              | CPF                                                   | tpCPF                                                 | 1-1                                                   | Número no Cadastro de Pessoas Físicas.                                                                                        |
| (Choice)                                              | CNPJ                                                  | tpCNPJ                                                | 1-1                                                   | Número no Cadastro de Pessoa Jurídica                                                                                         |
| (Choice)                                              | NIF                                                   | tpNIF                                                 | 1-1                                                   | Tipo NIF (Número de Identificação Fiscal) - fornecido por um órgão de administração tributária no exterior.                   |
| (Choice)                                              | NaoNIF                                                | tpNaoNIF                                              | 1-1                                                   | Tipo do motivo para não informação do NIF. 0 - Não informado na nota de origem 1 - Dispensado do NIF 2 - Não exigência do NIF |
| xNome                                                 | xNome                                                 | tpRazaoSocial                                         | 1-1                                                   | Razão Social                                                                                                                  |
| end                                                   | end                                                   | tpEndereco                                            | 0-1                                                   | Endereço                                                                                                                      |
| email                                                 | email                                                 | tpEmail                                               | 0-1                                                   | Endereço eletrônico                                                                                                           |

| tpServico (complemento para a versão 2.0)   | tpServico (complemento para a versão 2.0)   | tpServico (complemento para a versão 2.0)   | tpServico (complemento para a versão 2.0)   | tpServico (complemento para a versão 2.0)              |
|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|--------------------------------------------------------|
| Tipo com as informações do serviço          | Tipo com as informações do serviço          | Tipo com as informações do serviço          | Tipo com as informações do serviço          | Tipo com as informações do serviço                     |
| Nome do Elemento                            | Nome do Elemento                            | Tipo do Elemento                            | Ocorrência                                  | Descrição                                              |
| modoPrestServ                               | modoPrestServ                               | tpModoPrestacaoServico                      | 1-1                                         | Tipo Modo de prestação do serviço.                     |
| (Choice)                                    | clocalPrestServ                             | tpCidade                                    | 1-1                                         | Código da cidade do município da prestação do serviço. |
|                                             | cPaisPrestServ                              | tpCodigoPaisISO                             | 1-1                                         | Informar quando o serviço é prestado fora do país.     |
| cCIB                                        | cCIB                                        | tpCCIB                                      | 0-1                                         | Código do cadastro de imóveis.                         |
| indCompGov                                  | indCompGov                                  | tpIndicadorCompraGov                        | 1-1                                         | Tipo do indicador de compra governamental              |
| tpEnteGov                                   | tpEnteGov                                   | tpEnteGov                                   | 0-1                                         | Tipo do ente da compra governamental.                  |

| tpGIBSCBS (complemento para a versão 2.0)   | tpGIBSCBS (complemento para a versão 2.0)   | tpGIBSCBS (complemento para a versão 2.0)   | tpGIBSCBS (complemento para a versão 2.0)                                                                                                                           |
|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Informações relacionadas ao IBS e à CBS.    | Informações relacionadas ao IBS e à CBS.    | Informações relacionadas ao IBS e à CBS.    | Informações relacionadas ao IBS e à CBS.                                                                                                                            |
| Nome do Elemento                            | Tipo do Elemento                            | Ocorrência                                  | Descrição                                                                                                                                                           |
| cClassTribIBSCBS                            | tpCClassTribIBSCBS                          | 1-1                                         | Informações relacionadas aos tributos IBS e à CBS.                                                                                                                  |
| CClassTribReg                               | tpCClassTribReg                             | 0-1                                         | Código de classificação Tributária do IBS e da CBS secundário, que informa a tributação original ser utilizada caso os requisitos da suspensão não sejam cumpridos. |

Versão do Manual: 3 .2

pág. 33

| tpTrib (complemento para a versão 2.0)                                     | tpTrib (complemento para a versão 2.0)                                     | tpTrib (complemento para a versão 2.0)                                     | tpTrib (complemento para a versão 2.0)                                     |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Informações relacionadas aos valores do serviço prestado para IBS e à CBS. | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. |
| Nome do Elemento                                                           | Tipo do Elemento                                                           | Ocorrência                                                                 | Descrição                                                                  |
| gIBSCBS                                                                    | tpGIBSCBS                                                                  | 1-1                                                                        | Informações relacionadas aos tributos IBS e à CBS.                         |

| tpValores (complemento para a versão 2.0)                                  | tpValores (complemento para a versão 2.0)                                  | tpValores (complemento para a versão 2.0)                                  | tpValores (complemento para a versão 2.0)                                  |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Informações relacionadas aos valores do serviço prestado para IBS e à CBS. | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. |
| Nome do Elemento                                                           | Tipo do Elemento                                                           | Ocorrência                                                                 | Descrição                                                                  |
| trib                                                                       | tpTrib                                                                     | 1-1                                                                        | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. |

| tpIBSCBS (complemento para a versão 2.0)   | tpIBSCBS (complemento para a versão 2.0)   | tpIBSCBS (complemento para a versão 2.0)   | tpIBSCBS (complemento para a versão 2.0)                                   |
|--------------------------------------------|--------------------------------------------|--------------------------------------------|----------------------------------------------------------------------------|
| Tipo das informações do IBS/CBS            | Tipo das informações do IBS/CBS            | Tipo das informações do IBS/CBS            | Tipo das informações do IBS/CBS                                            |
| Nome do Elemento                           | Tipo do Elemento                           | Ocorrência                                 | Descrição                                                                  |
| dest                                       | tpInformacoesPessoa                        | 0-1                                        | Informações do destinatário                                                |
| adq                                        | tpInformacoesPessoa                        | 0-1                                        | Informações do adquirente                                                  |
| serv                                       | tpServico                                  | 1-1                                        | Informações relativas ao serviço prestado para IBS/CBS.                    |
| valores                                    | tpValores                                  | 1-1                                        | Informações relacionadas aos valores do serviço prestado para IBS e à CBS. |

| tpNotaReferenciada (complemento para a versão 2.0)   | tpNotaReferenciada (complemento para a versão 2.0)   | tpNotaReferenciada (complemento para a versão 2.0)   | tpNotaReferenciada (complemento para a versão 2.0)                                                                                                 |
|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipo de informações da nota referenciada.            | Tipo de informações da nota referenciada.            | Tipo de informações da nota referenciada.            | Tipo de informações da nota referenciada.                                                                                                          |
| Nome do Elemento                                     | Tipo do Elemento                                     | Ocorrência                                           | Descrição                                                                                                                                          |
| TipoReferencia                                       | tpReferencia                                         | 1-1                                                  | Tipo de referência da nota. 0 = Nota fiscal referenciada para emissão de nota de multa e juros. 1 = Nota fiscal de pagamento parcelado antecipado. |
| TipoNotaReferenciada                                 | tpTipoNotaReferenciada                               | 1-1                                                  | Tipo de nota fiscal referenciada 0 = NFS-e 1 = NFTS                                                                                                |
| NumeroNFe                                            | tpNumero                                             | 1-1                                                  | Número da NFS-e ou Número da NFTS, depende do TipoNotaReferenciada informado.                                                                      |
| CodigoVerificacao                                    | tpCodigoVerificacao                                  | 1-1                                                  | Código de verificação da NFS-e ou da NFTS, depende do TipoNotaReferenciada informado.                                                              |

## 4.3. SERVIÇOS E MÉTODOS SÍNCRONOS

A seguir são descritos cada um dos serviços disponibilizados pelo Web Service LoteNFe, bem como seus respectivos métodos e schemas XML de pedido e de retorno do serviço.

## 4.3.1. Regras Gerais

## Parâmetros

Todos os métodos de pedido de serviço disponíveis recebem dois parâmetros conforme o exemplo: &lt;Nome do Método&gt;(&lt;Parâmetro VersaoSchema &gt;, &lt;Parâmetro MensagemXML &gt;).

## Onde,

Parâmetro VersaoSchema : Versão do Schema XML utilizado para montar a mensagem XML de pedido do serviço (tipo de dado: Integer);

Parâmetro MensagemXML : Mensagem XML de pedido do serviço (tipo de dado: String).

Observações do parâmetro MensagemXML : basicamente existem duas formas mais comuns de informar a mensagem XML neste parâmetro: 1) Informar o XML com os caracteres especiais tratados conforme item 3.4.5 deste manual; ou, 2) Informar o XML dentro de uma seção CDATA:

Exemplo: &lt;MensagemXML&gt;&lt;![CDATA[MENSAGEM  XML  DE  PEDIDO  AQUI]]&gt;&lt;/MensagemXML&gt;

Todos os métodos retornam uma mensagem XML de retorno no respectivo Schema XML de retorno do serviço pedido (string).  Todos os Schemas XML de retorno contem uma TAG chamada 'Sucesso' no cabeçalho. Esta TAG indica se o pedido foi atendido com sucesso (true) ou não (false) conforme descrito a seguir:

## ▪ Sucesso: True

Caso todo o pedido do serviço tenha sido processado sem que ocorram eventos de erro. Sendo assim,  o  Web  Service  transmitirá  uma  mensagem  XML  de  retorno  do  respectivo  serviço informando o sucesso da operação (TAG sucesso = true) e as demais informações pertinentes ao respectivo Schema de Retorno. Caso ocorram eventos de alerta durante o processamento, os alertas  gerados  serão  apresentados  na  mensagem  XML  de  retorno. Eventos  de  alerta  não impedem que o pedido seja atendido com sucesso.

- Sucesso: False

Caso ocorra algum evento de erro durante o processamento do pedido do serviço. Sendo assim, o Web Service transmitirá uma mensagem XML de retorno do respectivo serviço informando o não sucesso  da  operação  (TAG  sucesso  =  false)  e  as  demais  Informações  sobre  os  eventos  de erro/alerta ocorridos.

## Observações:

Descrição dos nomes e abreviações utilizados no cabeçalho das tabelas que representam a estrutura definida nos schemas XML:

| <nome do arquivo.xsd>   | <nome do arquivo.xsd>   | <nome do arquivo.xsd>                      | <nome do arquivo.xsd>   | <nome do arquivo.xsd>   | <nome do arquivo.xsd>   | <nome do arquivo.xsd>   | <nome do arquivo.xsd>   |
|-------------------------|-------------------------|--------------------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| #                       | Campo                   | Descrição                                  | Ele                     | Pai                     | Tipo                    | Ocorr.                  | Observação              |
| P1                      | Cabecalho               | TAG de grupo das informações do cabeçalho. | G                       | -                       | -                       | 1-1                     |                         |
|                         | Versao                  | Versão do XML                              | A                       | P1                      | tpVersao                | 1-1                     |                         |
|                         | dtInicio                | Data de início do período transmitido.     | E                       | P1                      | D                       | 1-1                     | (AAAA-MM-DD)            |

- A. Coluna  #:  Código  de  identificação  do  campo.  Este  código  é  utilizado  por  um  elemento  'filho' identificar seu elemento 'pai' na coluna 'Pai';
- B. Coluna Descrição: Descrição do campo;
- C. Coluna Ele.:

A - indica que o campo é um atributo do Elemento anterior;

E - indica que o campo é um Elemento;

CE -indica que o campo é um Elemento que deriva de uma Escolha (Choice);

G -indica que o campo é um Elemento de Grupo;

CG - indica que o campo é um Elemento de Grupo que deriva de uma Escolha (Choice);

- D. Coluna Pai: Indica qual é o elemento pai;
- E. Coluna Tipo:

Tipos Base:

N -campo numérico;

- C -campo alfanumérico;
- D -campo data;

Tipos Simples e Tipos Complexos:

- F. Coluna Ocorr.: x - y, onde x indica a ocorrência mínima e y a ocorrência máxima.

Para obter a versão mais recente dos Schemas XML acesse o link:

- a) NFS-e emitidas até 22/02/2015

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-v01-0.zip

- b) NFS-e emitidas a partir de 23/02/2015 (fato gerador até 31/12/2025)

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-v01-1.zip

- c) NFS-e emitidas pelo serviço assíncrono

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-assincrono-v01-1.zip

- d) NFS-e -Reforma tributária 2026 (serviços síncronos e assíncronos)

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/schemas-reformatributaria-v02-0.zip

## 4.3.2. Envio de RPS

<!-- image -->

- I.  Descrição:  Este  método  é  responsável  por  atender  aos  pedidos  de  Envio  Individual  de  RPS  para substituição por NF-e.

II. Método: EnvioRPS.

III. Mensagem XML: O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| PedidoEnvioRPS.xsd*   | PedidoEnvioRPS.xsd*   | PedidoEnvioRPS.xsd*                                       | PedidoEnvioRPS.xsd*   | PedidoEnvioRPS.xsd*   | PedidoEnvioRPS.xsd*   | PedidoEnvioRPS.xsd*   | PedidoEnvioRPS.xsd*                                                                                                  |
|-----------------------|-----------------------|-----------------------------------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------|
| #                     | Campo                 | Descrição                                                 | Ele                   | Pai                   | Tipo                  | Ocorr.                | Observação                                                                                                           |
| P1                    | Cabecalho             | TAG de grupo das informações do cabeçalho.                | G                     | -                     | -                     | 1-1                   |                                                                                                                      |
|                       | Versao                | Versão do XML Schema Utilizado.                           | A                     | P1                    | tpVersao              | 1-1                   |                                                                                                                      |
|                       | CNPJRemetente         | CNPJ do Remetente autorizado a transmitir a mensagem XML. | E                     | P1                    | tpCPFCNPJ             | 1-1                   |                                                                                                                      |
| P2                    | RPS                   | Recibo Provisório de Serviço.                             | G                     | -                     | tpRPS                 | 1-1                   |                                                                                                                      |
| P3                    | Signature             | Assinatura digital da mensagem XML.                       | G                     | -                     | SignatureType         | 1-1                   | "Signature" é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig-core-schema_v01.xsd |

* Representação da estrutura definida no schema XML PedidoEnvioRPS.xsd.

## Observação: Assinatura Adicional

O RPS deverá ter uma assinatura digital. Esta assinatura utilizará o mesmo certificado digital usado na assinatura da mensagem XML (item 3.2.2A), com os mesmos padrões de criptografia assimétrica RSA e algoritmo message digest SHA-1.

Para criar a assinatura deverá ser gerado um Hash (utilizando SHA1) de uma cadeia de caracteres (ASCII) com informações do RPS emitido. Este Hash deverá ser assinado utilizando RSA. A assinatura do Hash será informada na TAG Assinatura (tipo RPS apresentado no item 4.2.1).

A cadeia de caracteres a ser assinada deverá conter 86 posições com as informações apresentadas na tabela a seguir:

|   # | Informação                       | Conteúdo                                                                                                                                                                                                                                                                |
|-----|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   1 | Inscrição Municipal do Prestador | Inscrição Municipal do Prestador com 8 posições (dígitos). Completar com zeros à esquerda caso seja necessário.                                                                                                                                                         |
|   2 | Série do RPS                     | Série do RPS com 5 posições (caracteres). Completar com espaços em branco à direita caso seja necessário. Atenção: Não utilize espaços à esquerda. O conteúdo deverá estar alinhado à esquerda.                                                                         |
|   3 | Número do RPS                    | Número do RPS com 12 posições (dígitos). Completar com zeros à esquerda caso seja necessário.                                                                                                                                                                           |
|   4 | Data de Emissão do RPS           | Data de emissão do RPS no formato AAAAMMDD (caracteres).                                                                                                                                                                                                                |
|   5 | Tipo de Tributação do RPS        | Tipo de Tributação do RPS com 1 posição (caractere): a) NFS-e emitidas até 22/02/2015 T - Tributação no municipio de São Paulo; F - Tributação fora do municipio de São Paulo; I - Isento; J - ISS Suspenso por Decisão Judicial. a) NFS-e emitidas a partir 23/02/2015 |

|    |                                        | T - Tributado em São Paulo F - Tributado Fora de São Paulo A - Tributado em São Paulo, porém Isento B - Tributado Fora de São Paulo, porém Isento D - Tributado em São Paulo com isenção parcial M - Tributado em São Paulo, porém com indicação de imunidade subjetiva N - Tributado fora de São Paulo, porém com indicação de imunidade subjetiva R - Tributado em São Paulo, porém com indicação de imunidade objetiva S - Tributado fora de São Paulo, porém com indicação de imunidade objetiva X - Tributado em São Paulo, porém Exigibilidade Suspensa V - Tributado Fora de São Paulo, porém Exigibilidade Suspensa P - Exportação de Serviços   |
|----|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  6 | Status do RPS                          | Status do RPS com 1 posição (caractere): N - Normal; C - Cancelado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|  7 | ISS Retido                             | Valor 'S' (SIM) para ISS Retido (caractere). Valor 'N' (NÃO) para Nota Fiscal sem ISS Retido.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|  8 | Valor dos Serviços                     | Valor dos Serviços do RPS, incluindo os centavos (sem ponto decimal e sem R$), com 15 posições (dígitos). Exemplo: R$ 500,85 - 000000000050085 R$ 500,00 - 000000000050000                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|  9 | Valor das Deduções                     | Valor das Deduções do RPS, incluindo os centavos (sem ponto decimal e sem R$), com 15 posições (dígitos). Exemplo: R$ 500,85 - 000000000050085 R$ 500,00 - 000000000050000                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 10 | Código do Serviço Prestado             | Código do Serviço do RPS com 5 posições (dígitos). Completar com zeros à esquerda caso seja necessário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 11 | Indicador de CPF/CNPJ do Tomador       | Indicador de CPF/CNPJ com 1 posição (dígito). Valor 1 para CPF. Valor 2 para CNPJ. Valor 3 para Não informado                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 12 | CPF/CNPJ do Tomador                    | CPF/CNPJ do tomador com 14 posições (dígitos). Sem formatação (ponto, traço, barra, ....). Completar com zeros à esquerda caso seja necessário. Se o Indicador do CPF/CNPJ for 3 (não informado), preencher com 14 zeros.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 13 | Indicador de CPF/CNPJ do Intermediário | Indicador de CPF/CNPJ com 1 posição (dígito). Valor 1 para CPF. Valor 2 para CNPJ. Valor 3 para Não informado o CPF/CNPJ do Intermediário                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 14 | CPF/CNPJ do Intermediário              | CPF/CNPJ do intermediário com 14 posições (dígitos). Sem formatação (ponto, traço, barra,....). Completar com zeros à esquerda caso seja necessário. Se o Indicador do CPF/CNPJ for 3 (não informado), preencher com 14 zeros.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 15 | ISS Retido Intermediário               | Valor 'S' (SIM) para ISS Retido pelo Intermediário Valor 'N' (NÃO) para ISS não retido pelo Intermediário                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Passos básicos para assinatura de um RPS:

1º - Monte a string de caracteres conforme a tabela a apresentada anteriormente.

A seguir apresentamos o exemplo de parte de uma mensagem XML de pedido de envio de RPS (os campos utilizados na montagem da cadeia de caracteres estão em negrito).

```
... <ChaveRPS> <InscricaoPrestador>31000000</InscricaoPrestador> <SerieRPS>OL03</SerieRPS> <NumeroRPS>1</NumeroRPS> </ChaveRPS> <TipoRPS>RPS-M</TipoRPS> <DataEmissao>2007-01-03</DataEmissao> <StatusRPS>N</StatusRPS> <TributacaoRPS>T</TributacaoRPS> <ValorServicos>20500</ValorServicos> <ValorDeducoes>5000</ValorDeducoes> <CodigoServico>2658</CodigoServico> <AliquotaServicos>0.05</AliquotaServicos> <ISSRetido>false</ISSRetido> <CPFCNPJTomador> <CPF>13167474254</CPF> </CPFCNPJTomador> ... <CPFCNPJIntermediario> <CNPJ> 09999999000106 </CNPJ> </CPFCNPJIntermediario> <InscricaoMunicipalIntermediario>99999999</InscricaoMunicipalIntermediario> <ISSRetidoIntermediario>true</ISSRetidoIntermediario>
```

...

Com base no trecho da mensagem XML apresentada, montamos a seguinte string de caracteres:

```
"31000000OL03 00000000000120070103TNN00000000205000000000000050000002658100013167474254209999999000106S"
```

Note que o valor dos serviços (R$ 20.500,00) foi transformado em 2050000, o valor de deduções (R$ 5.000,00) foi transformado em 500000. Também foi acrescentado à série do RPS um espaço em branco à direita para preencher as 5 posições.

Observação:  não  é  necessário  informar  os  dados  de  intermediário  na  assinatura  se  não  houver intermediário. Como exemplo, sem intermediário a string montada seria dessa forma:

```
"31000000OL03 00000000000120070103TNN00000000205000000000000050000002658100013167474254 ' 2º - Converta a cadeia de caracteres ASCII para bytes. 3º - Gere o HASH (array de bytes) utilizando SHA1. 4º - Assine o HASH (array de bytes) utilizando RSA-SHA1.
```

ATENÇÃO! Na maioria das linguagens de programação, os passos 3 e 4 são feitos através de uma única função. Verifique a documentação de sua linguagem para evitar assinar um hash de um hash.

IV. Schema da Mensagem XML do Retorno: RetornoEnvioRPS.xsd

| RetornoEnvioRPS.xsd*   | RetornoEnvioRPS.xsd*   | RetornoEnvioRPS.xsd*                                                                                    | RetornoEnvioRPS.xsd*   | RetornoEnvioRPS.xsd*   | RetornoEnvioRPS.xsd*   | RetornoEnvioRPS.xsd*   | RetornoEnvioRPS.xsd*   |
|------------------------|------------------------|---------------------------------------------------------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| #                      | Campo                  | Descrição                                                                                               | Ele                    | Pai                    | Tipo                   | Ocorr.                 | Observação             |
| P1                     | Cabecalho              | TAG de grupo das informações do cabeçalho.                                                              | G                      | -                      | -                      | 1-1                    |                        |
|                        | Versao                 | Versão do XML Schema Utilizado.                                                                         | A                      | P1                     | tpVersao               | 1-1                    |                        |
|                        | Sucesso                | Status do Pedido de Envio de RPS.                                                                       | E                      | P1                     | tpSucesso              | 1-1                    |                        |
| P2                     | Alerta                 | Informações sobre a ocorrência de eventos geradores de alertas durante o processamento da mensagem XML. | G                      | -                      | tpEvento               | 0-N                    |                        |
| P3                     | Erro                   | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML.   | G                      | -                      | tpEvento               | 0-N                    |                        |
| P4                     | ChaveNFeRPS            | Chave do RPS e Chave da NF-e gerada.                                                                    | G                      | -                      | tpChaveNFeRPS          | 0-1                    |                        |

* Representação da estrutura definida no schema XML RetornoEnvioRPS.xsd.

## V. Formato das Mensagens SOAP:

## Pedido:

```
< ?xnl version=" 1.0" encoding= utf-8" ?> <soap: Envelope w3 org/ 2001 / XMLSchema-instance xmlns:xsd=" w3 .org/ 2001/XMLSchema xmlns:soap="http://schenas.xnlsoap.org/ soaplenvelope/ <soap: Body> <EnvioRPSRequest xmlns= br/ nfe" > <Versaoschema> 1</VersaoSchena> <MensagemXHL > INCLUIR AQUI MENSAGEM XML CONFORME ITEM III</MensagemXML> EnvioRPSRequest> </soap: </soap: Envelope> Body>
```

## Retorno:

```
<?xnl version=" 1.0" encoding= utf-8" ?> <soap: Envelope w3 .org/ 2001/ XMLSchema-instance xmlns:xsd="http://wwv w3 .org/2001/XMLSchema xmlns:soap= 'http://schemas xmlsoap org/ soaplenvelope/ " > <soap: Body> <EnvioRPSResponse xmlns= "http://www.prefeitura.sP.gov br/ nfe" > <RetornoxML>MENSAGEM XML DE RETORNO CONFORME ITEM IV< RetornoXML> <1 EnvioRPSResponse> </soap: Body>
```

## 4.3.3. Envio de Lote de RPS (EnvioLoteRPS)

<!-- image -->

- I.  Descrição:  Este  método  é  responsável  por  atender  aos  pedidos  de  Envio  de  Lote  de  RPS  para substituição por NF-e.
- II. Método: EnvioLoteRPS.
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| PedidoEnvioLoteRPS.xsd*   | PedidoEnvioLoteRPS.xsd*   | PedidoEnvioLoteRPS.xsd*                                                             | PedidoEnvioLoteRPS.xsd*   | PedidoEnvioLoteRPS.xsd*   | PedidoEnvioLoteRPS.xsd*   | PedidoEnvioLoteRPS.xsd*   | PedidoEnvioLoteRPS.xsd*                                                                                                                                                                                                                                         |
|---------------------------|---------------------------|-------------------------------------------------------------------------------------|---------------------------|---------------------------|---------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #                         | Campo                     | Descrição                                                                           | Ele                       | Pai                       | Tipo                      | Ocorr.                    | Observação                                                                                                                                                                                                                                                      |
| P1                        | Cabecalho                 | TAG de grupo das informações do cabeçalho.                                          | G                         | -                         | -                         | 1-1                       |                                                                                                                                                                                                                                                                 |
|                           | Versao                    | Versão do XML Schema Utilizado.                                                     | A                         | P1                        | tpVersao                  | 1-1                       |                                                                                                                                                                                                                                                                 |
|                           | CNPJRemetente             | CNPJ do Remetente autorizado a transmitir a mensagem XML.                           | E                         | P1                        | tpCPFCNPJ                 | 1-1                       |                                                                                                                                                                                                                                                                 |
|                           | Transacao                 | Informe se os RPS a serem substituídos por NF-e farão parte de uma mesma transação. | E                         | P1                        | boolean                   | 0-1                       | True - Os RPS só serão substituidos por NF-e se não ocorrer nenhum evento de erro durante o processamento de todo o lote. False - Os RPS válidos serão substituídos por NF-e, mesmo que ocorram eventos de erro durante processamento de outros RPS deste lote. |
|                           | dtInicio                  | Data de início do período transmitido.                                              | E                         | P1                        | D                         | 1-1                       | (AAAA-MM-DD)                                                                                                                                                                                                                                                    |
|                           | dtFim                     | Data final do período transmitido.                                                  | E                         | P1                        | D                         | 1-1                       | (AAAA-MM-DD)                                                                                                                                                                                                                                                    |
|                           | QtdeRPS                   | Quantidade de RPS contidos no lote.                                                 | E                         | P1                        | tpQuantidade              | 1-1                       |                                                                                                                                                                                                                                                                 |
|                           | ValorTotalServicos        | Valor total dos serviços dos RPS contidos no lote.                                  | E                         | P1                        | tpValor                   | 1-1                       |                                                                                                                                                                                                                                                                 |
|                           | ValorTotalDeducoes        | Valor total das deduções dos RPS/Cupom contidos no lote.                            | E                         | P1                        | tpValor                   | 1-1                       |                                                                                                                                                                                                                                                                 |
| P2                        | RPS                       | Recibo Provisório de Serviço.                                                       | G                         | -                         | tpRPS                     | 1-50                      |                                                                                                                                                                                                                                                                 |
| P3                        | Signature                 | Assinatura digital da mensagem XML.                                                 | G                         | -                         | SignatureType             | 1-1                       | "Signature" é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig-core-schema_v01.xsd                                                                                                                                            |

* Representação da estrutura definida no schema XML PedidoEnvioLoteRPS.xsd.

## Observação 1: Assinatura Adicional

Cada RPS enviado no lote deverá ser assinado digitalmente conforme especificado no item 4.3.2. (Envio de RPS).

## Observação 2: Transação

Se ocorrerem eventos de erro de validação dos dados do cabeçalho do pedido de envio de lote de RPS, independente da opção informada no campo 'Transação', nenhum RPS será substituído por NF-e.

## IV. Schema da Mensagem XML do Retorno: RetornoEnvioLoteRPS.xsd

| RetornoEnvioLoteRPS.xsd*   | RetornoEnvioLoteRPS.xsd*   | RetornoEnvioLoteRPS.xsd*                                                                                | RetornoEnvioLoteRPS.xsd*   | RetornoEnvioLoteRPS.xsd*   | RetornoEnvioLoteRPS.xsd*   | RetornoEnvioLoteRPS.xsd*   | RetornoEnvioLoteRPS.xsd*   |
|----------------------------|----------------------------|---------------------------------------------------------------------------------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| #                          | Campo                      | Descrição                                                                                               | Ele                        | Pai                        | Tipo                       | Ocorr.                     | Observação                 |
| P1                         | Cabecalho                  | TAG de grupo das informações do cabeçalho.                                                              | G                          | -                          | -                          | 1-1                        |                            |
|                            | Versao                     | Versão do XML Schema Utilizado.                                                                         | A                          | P1                         | tpVersao                   | 1-1                        |                            |
|                            | Sucesso                    | Status do Pedido de Envio de Lote de RPS.                                                               | E                          | P1                         | tpSucesso                  | 1-1                        |                            |
|                            | InformacoesLote            | Informações sobre o Lote                                                                                | G                          | P1                         | tpInformacoesLote          | 0-1                        |                            |
| P2                         | Alerta                     | Informações sobre a ocorrência de eventos geradores de alertas durante o processamento da mensagem XML. | G                          | -                          | tpEvento                   | 0-N                        |                            |
| P3                         | Erro                       | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML.   | G                          | -                          | tpEvento                   | 0-N                        |                            |
| P4                         | ChaveNFeRPS                | Chave do RPS e Chave da NF- e gerada.                                                                   | G                          | -                          | tpChaveNFeRPS              | 0-50                       |                            |

* Representação da estrutura definida no schema XML RetornoEnvioLoteRPS.xsd.

## Observação: Transação

Para pedidos de envio de lote de RPS com transação (Transacao = True), o campo InformacoesLote retornará (dentre outras informações) o total dos serviços, o total das deduções e a quantidade de RPS enviados na mensagem XML de pedido do serviço.

Para pedidos de envio de lote de RPS sem transação (Transacao = False), o campo InformacoesLote retornará (dentre outras informações) o total dos serviços, o total das deduções e a quantidade de RPS que efetivamente foram substituídos por NF-e.

## V. Formato das Mensagens SOAP:

## Pedido:

<!-- image -->

## Retorno:

```
< ?xnl version= 1 .0" encoding= utf-8" ?> <soap: Enve lope org/ 2001/ XMLSchema-instance xmlns:xsd="http://www org/ 2001/ XMLSchema xmlns:soap="http://schemas xmlsoap org/ soap/envelope/"> <soap: Body> <EnvioLoteRPSResponse xnlns="http: /nw.prefeitura.sp.gov br /nfe" > <RetornoXML>MENSAGEM XML DE RETORNO CONFORME ITEM IV< RetornoXML> EnvioloteRPSResponse> soap: Body> <soap: Enve lope>
```

## 4.3.4. Teste de Envio de Lote de RPS (TesteEnvioLoteRPS)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de Teste de Envio de Lote de RPS para substituição por NF-e. Este método não substitui os RPS por NF-e.

## Observação:

Conforme informado no item 2.1.3, este método deverá ser usado apenas na fase de adaptação dos  sistemas  dos  contribuintes.  Nos  casos  de  sistemas  já  adaptados,  seu  uso  resulta  em duplicidade de esforços desnecessários, pois as verificações feitas no método TesteEnvioLoteRPS são as mesmas realizadas pelo método EnvioLoteRPS.

- II. Método: TesteEnvioLoteRPS
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela apresentada no item V
- IV. Schema  da  Mensagem  XML  do  Retorno:  RetornoEnvioLoteRPS.xsd  (Idêntico  ao  Schema  da Mensagem XML do Retorno do item V)

## 4.3.5. Pedido de Consulta de NF-e (ConsultaNFe)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de consulta de NF-e / RPS. Seu acesso é permitido apenas pela chave de identificação da NF-e ou pela chave de identificação do RPS.
- II. Método: ConsultaNFe
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:
- IV. Schema da Mensagem XML do Retorno: RetornoConsulta.xsd
- V. Formato das Mensagens SOAP:

| PedidoConsultaNFe.xsd*   | PedidoConsultaNFe.xsd*   | PedidoConsultaNFe.xsd*                                    | PedidoConsultaNFe.xsd*   | PedidoConsultaNFe.xsd*   | PedidoConsultaNFe.xsd*   | PedidoConsultaNFe.xsd*   | PedidoConsultaNFe.xsd*                                                                                               |
|--------------------------|--------------------------|-----------------------------------------------------------|--------------------------|--------------------------|--------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------|
| #                        | Campo                    | Descrição                                                 | Ele                      | Pai                      | Tipo                     | Ocorr.                   | Observação                                                                                                           |
| P1                       | Cabecalho                | TAG de grupo das informações do cabeçalho.                | G                        | -                        | -                        | 1-1                      |                                                                                                                      |
|                          | Versao                   | Versão do XML Schema Utilizado.                           | A                        | P1                       | tpVersao                 | 1-1                      |                                                                                                                      |
|                          | CNPJRemetente            | CNPJ do Remetente autorizado a transmitir a mensagem XML. | E                        | P1                       | tpCPFCNPJ                | 1-1                      |                                                                                                                      |
| P2                       | Detalhe                  | TAG de grupo das informações do detalhe.                  | G                        | -                        |                          | 1-50                     |                                                                                                                      |
|                          | ChaveRPS                 | Chave do RPS.                                             | CE                       | P2                       | tpChaveRPS               | 1-1                      |                                                                                                                      |
|                          | ChaveNFe                 | Chave da NF-e.                                            | CE                       | P2                       | tpChaveNFe               | 1-1                      |                                                                                                                      |
| P3                       | Signature                | Assinatura digital da mensagem XML.                       | G                        | -                        | SignatureType            | 1-1                      | "Signature" é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig-core-schema_v01.xsd |

*Representação da estrutura definida no schema XML PedidoConsultaNFe.xsd.

| RetornoConsulta.xsd*   | RetornoConsulta.xsd*   | RetornoConsulta.xsd*                                                                                                                | RetornoConsulta.xsd*   | RetornoConsulta.xsd*   | RetornoConsulta.xsd*   | RetornoConsulta.xsd*   | RetornoConsulta.xsd*   |
|------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| #                      | Campo                  | Descrição                                                                                                                           | Ele                    | Pai                    | Tipo                   | Ocorr.                 | Observação             |
| P1                     | Cabecalho              | TAG de grupo das informações do cabeçalho.                                                                                          | G                      | -                      | -                      | 1-1                    |                        |
|                        | Versao                 | Versão do XML Schema Utilizado.                                                                                                     | A                      | P1                     | tpVersao               | 1-1                    |                        |
|                        | Sucesso                | Status do envio do pedido de consulta.                                                                                              | E                      | P1                     | tpSucesso              | 1-1                    |                        |
| P2                     | Alerta                 | Informações sobre a ocorrência de eventos geradores de alertas durante o processamento da mensagem XML.                             | G                      | -                      | tpEvento               | 0-N                    |                        |
| P3                     | Erro                   | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML.                               | G                      | -                      | tpEvento               | 0-N                    |                        |
| P4                     | NFe                    | Elemento NFe - pode se repetir quantas vezes for necessário (respeitando o limite de máximo estabelecido). Cada item será uma NF-e. | G                      | -                      | tpNFe                  | 0-50                   |                        |

* Representação da estrutura definida no schema XML RetornoConsulta.xsd.

Pedido:

```
<?xml version=" 1.0" encoding="utf-8" ?> <soap Envelope xmlns:xsi="http: w3 org/2001/XMLSchema-instance xmlns xsd="http://www w3 org/ 2001/XMLSchema xmlns soap="http:// schemas xmlsoap.org/ soap/envelope <soap Body> <ConsultaNFeRequest xmlns="http: Www prefeitura sp. gov br / nfe" > <VersaoSchema> 1</VersaoSchema> <MensagemXML > INCLUIR AQUI MENSAGEM XML CONFORME ITEM III< MensagemXML > < /ConsultaNFeRequest> soap: Body> soap Envelope>
```

## Retorno:

```
<?xml Version=" 1.0" encoding="utf-8" ?> <soap: Enve lope xmlns:xsi="http:// www org/2001/XMLSchema-instance xmlns xsd="http://www w3 org/ 2001 / XMLSchema xmlns:soap= xmlsoap.org/ soap/envelope/ <soap: Body> <ConsultaNFeResponse xmlns= "http: prefeitura sp. gov br nfe <RetornoXML MENSAGEM XML DE RETORNO CONF ORME ITEM IV< RetornoXML> </ConsultaNFeResponse> < soap: Body> Envelope> http: "7
```

## 4.3.6. Pedido de Consulta de NF-e Recebidas (ConsultaNFeRecebidas)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de consulta de NF-e Recebidas.
- II. Método: ConsultaNFeRecebidas
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| PedidoConsultaNFePeriodo.xsd*   | PedidoConsultaNFePeriodo.xsd*   | PedidoConsultaNFePeriodo.xsd*                                                                                                                                                                                                   | PedidoConsultaNFePeriodo.xsd*   | PedidoConsultaNFePeriodo.xsd*   | PedidoConsultaNFePeriodo.xsd*   | PedidoConsultaNFePeriodo.xsd*   | PedidoConsultaNFePeriodo.xsd*                                                                                                  |
|---------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| #                               | Campo                           | Descrição                                                                                                                                                                                                                       | Ele                             | Pai                             | Tipo                            | Ocorr.                          | Observação                                                                                                                     |
| P1                              | Cabecalho                       | TAG de grupo das informações do cabeçalho.                                                                                                                                                                                      | G                               | -                               | -                               | 1-1                             |                                                                                                                                |
|                                 | Versao                          | Versão do XML Schema Utilizado.                                                                                                                                                                                                 | A                               | P1                              | tpVersao                        | 1-1                             |                                                                                                                                |
|                                 | CPFCNPJRemet ente               | CPF/CNPJ do Remetente autorizado a enviar a mensagem XML.                                                                                                                                                                       | E                               | P1                              | tpCPFCNPJ                       | 1-1                             |                                                                                                                                |
|                                 | CPFCNPJ                         | Para consulta de NF-e Recebidas: Informe o CPF/CNPJ do tomador da NF-e. Para consulta de NF-e Emitidas: Informe o CNPJ do                                                                                                       | E                               | P1                              | tpCPFCNPJ                       | 1-1                             |                                                                                                                                |
|                                 | Inscricao                       | Para consulta de NF-e Recebidas: Informe a Inscrição Municipal do Tomador. Para consulta de NF-e Emitidas: Informe a Inscrição Municipal do Prestador. Neste tipo de consulta o preenchimento deste campo se torna obrigatório. | E                               | P1                              | tpInscricaoMunicipal            | 0-1                             | ATENÇÃO 1: Este campo só deverá ser preenchido com a inscrição de contribuintes estabelecidos no município de São Paulo (CCM). |
|                                 | dtInicio                        | Data início da consulta.                                                                                                                                                                                                        | E                               | P1                              | D                               | 1-1                             |                                                                                                                                |
|                                 | dtFim                           | Data fim da consulta.                                                                                                                                                                                                           | E                               | P1                              | D                               | 1-1                             |                                                                                                                                |
|                                 | NumeroPagina **                 | Número da página consultada                                                                                                                                                                                                     | E                               | P1                              | tpNumero                        | 1-1                             | Default = 1                                                                                                                    |
| P2                              | Signature                       | Assinatura digital da mensagem XML.                                                                                                                                                                                             | G                               | -                               | SignatureType                   | 1-1                             | 'Signature' é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig- coreschema_v01.xsd           |

*  Representação  da  estrutura  definida  no  schema  XML  PedidoConsultaNFePeriodo.xsd.  Os  métodos ConsultaNFeRecebidas e ConsultaNFeEmitidasidas utilizam o mesmo schema XML para o pedido do serviço

**  Conforme  especificado  no  Schema  XML  RetornoConsulta.xsd  (utilizado  no  retorno  dos  pedidos  de Consulta de NF-e, Consulta de NF-e Recebidas, Consulta de NF-e Emitidas e Consulta de Lote) só serão retornadas até 50 NF-e por consulta. Porém a Consulta de NF-e Recebidas (assim como a Consulta de NF-e Emitidas) pode encontrar uma quantidade maior de NF-e do que o limite especificado.

Sendo assim, as NF-e encontradas serão agrupadas em páginas com até 50 NF-e. Para consultar as NFe de cada uma das páginas o contribuinte deverá transmitir uma mensagem XML de pedido de Consulta de NF-e Recebidas indicando qual página deseja consultar. Desta forma, caso um pedido de consulta de

NF-e Recebidas, para página X, retorne 50 NF-e o sistema de informação do Contribuinte deve efetuar novo  pedido  de  Consulta  de  NF-e  Recebidas,  para  página  X+1,  para  verificar  se  existem  mais  NF-e Recebidas no período consultado.

Quando o sistema de informação do Contribuinte efetuar um pedido de Consulta de NF-e Recebidas para uma  determinada  página  e  esta  consulta  retornar  menos  que  50  NF-e  o  sistema  de  informação  do contribuinte 'saberá' que estas são as últimas NF -e recebidas para o período consultado e que portanto está é a última página. Se o Web Service retornar uma mensagem XML informando sucesso (tag 'sucesso' = true) e sem nenhuma NF-e é por que a página consultada não existe.

## Exemplo:

O sistema de informação de um Contribuinte envia uma mensagem XML de Pedido Consulta de NF-e Recebidas para o período de 01/09/2006 a 30/09/2006 e requerendo a página 1. Para este pedido são encontradas 137 NF-e recebidas. As 137 NF-e são agrupadas em três páginas: Página 1 com as primeiras 50 NF-e (1ª à 50ª); página 2 com as próximas 50 NF-e (51ª à 100ª) e página 3 com as 37 NFe restantes (101ª à 137ª). O Web Service retorna uma mensagem XML com a página requerida (página 1).

Ao receber a mensagem XML de retorno o sistema de informação do Contribuinte verifica que foram retornadas 50 NF-e para a página 1. O sistema de informação do Contribuinte envia outra mensagem XML de Pedido Consulta de NF-e Recebidas para o mesmo período, mas desta vez requerendo a próxima página (página 2). O Web Service retorna uma mensagem XML com a página requerida (página 2). Ao receber  a  mensagem  XML  de  retorno  o  sistema  de  informação  do  Contribuinte  verifica  que  foram retornadas 50 NF-e para a página 2. O sistema de informação do Contribuinte envia outra mensagem XML de Pedido Consulta de NF-e Recebidas para o mesmo período, mas desta vez requerendo a próxima página (página 3). O Web Service retorna uma mensagem XML com a página requerida (página 3). Ao receber  a  mensagem  XML  de  retorno  o  sistema  de  informação  do  Contribuinte  verifica  que  foram retornadas  37  NF-e  para  a  página  3  e  portanto  não  existem  mais  NF-e  recebidas  para  o  período consultado.

Obs.: As NF-e encontradas são ordenadas por data de emissão da nota (ou data do cancelamento, caso a NF-e tenha sido cancelada) e pela inscrição municipal (CCM) do prestador que emitiu a nota.

Abaixo, fluxo de funcionamento baseado no exemplo descrito:

<!-- image -->

- IV. Schema da Mensagem XML do Retorno: RetornoConsulta.xsd (Idêntico ao do item 4.3.5)

## V. Formato das Mensagens SOAP:

## Pedido:

```
< ?xnl version=" 1.0" encoding= utf-8" ?> <soap: Envelope xmlns:xsi=" w3 .org/ 2001/ XMLSchema-instance xmlns:xsd="http://www org/ 2001 /XMLSchema xmlns:soap-"http://schenas xmlsoap.org/ soaplenvelope/ <soap: Body> {ConsultaNFeRecebidasRequest xmlns=" 'http: gov <Me nsagemXHL> INCLUIR AQUI A MENSAGEN XML CONFORME ITEM III</ </ConsultaNFeRecebidasRequest> Fsoap: Body> </soap: Envelope>
```

## Retorno:

```
< ?xnl version=" 1.0" encoding= utf-8" ?> <soap:Envelope xmlns:xsi=" w3 .org/ 2001/ XMLSchema-instance xmlns:xsd="http://www w3 .org/ 2001/XMLSchema xmlns:soap= 'http:// schemas xmlsoap org/ soaplenvelope/ <soap: Body> {ConsultaNFeRecebidasResponse xmlns="http: prefeitura. sP.gov br/ nfe" > <RetornoXML>MENSAGEM XML DE RETORNO CONFORME ITEM IV< RetornoXML> </ConsultaNFeRecebidasResponse> </soap: Body> soap:Envelope>
```

## 4.3.7. Pedido de Consulta de NF-e Emitidas (ConsultaNFeEmitidas)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de consulta de NF-e Emitidas.
- II. Método: ConsultaNFeEmitidas
- III. O parâmetro MensagemXML (idêntico ao Schema da Mensagem XML de pedido apresentado no item 4.3.6 III).
- IV. Schema da Mensagem XML do Retorno: RetornoConsulta.xsd (Idêntico ao do item 4.3.5)

## V. Formato das Mensagens SOAP:

## Pedido:

```
<?xml 0" encoding= utf-8" ?> <soap Envelope xmlns xsi="http://www w3 org/2001/XMLSchema-instance xmlns xsd=" 'http://www w3 org/ 2001 XMLSchema xmlns: soap=" 'http:// schemas xmlsoap.org/ soap/envelope " > <soap: Body> <ConsultaNFeEmitidasRequest xmlns=" prefeitura.sp.gov.br/nfe"> <VersaoSchema 1</ VersaoSchema> AQUI A MENSAGEM XM CONFORME ITEM III< Mens agemXML> </ConsultaNFeEmitidasRequest> </soap Body> < 'soap: Envelope> http:
```

## Retorno:

```
<?xml Version=" 1.0" encoding="utf-8" ?> <soap Envelope xmlns:xsi="http: Www w3 .org/2001/XMLSchema-instance Ins xsd=" w3.org/ 2001/XMLSchema xmlns soap=" 'http:// schemas.xmlsoap.org/soap/envelope / "> <soap: Body> <ConsultaNFeEmitidasResponse xmlns= feitura.sp.gov br / nfe" > <RetornoXML> MENSAGEM XM DE RETORNO CONF ORME ITEM IV< RetornoXML> </ConsultaNFeEmitidasResponse> </ soap: Body> < soap: Envelope> http: http: pre
```

## 4.3.8. Pedido de Consulta de Lote (ConsultaLote)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de Consulta de Lote de NF-e geradas a partir do método EnvioLoteRPS.
- II. Método: ConsultaLote
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| PedidoConsultaLote.xsd*   | PedidoConsultaLote.xsd*   | PedidoConsultaLote.xsd*                               | PedidoConsultaLote.xsd*   | PedidoConsultaLote.xsd*   | PedidoConsultaLote.xsd*   | PedidoConsultaLote.xsd*   | PedidoConsultaLote.xsd*                                                                                              |
|---------------------------|---------------------------|-------------------------------------------------------|---------------------------|---------------------------|---------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| #                         | Campo                     | Descrição                                             | Ele                       | Pai                       | Tipo                      | Ocorr.                    | Observação                                                                                                           |
| P1                        | Cabecalho                 | TAG de grupo das informações do cabeçalho.            | G                         | -                         | -                         | 1-1                       |                                                                                                                      |
|                           | Versao                    | Versão do XML Schema Utilizado.                       | A                         | P1                        | tpVersao                  | 1-1                       |                                                                                                                      |
|                           | CNPJRemetente             | CNPJ do Remetente autorizado a enviar a mensagem XML. | E                         | P1                        | tpCPFCNPJ                 | 1-1                       |                                                                                                                      |
|                           | NumeroLote                | Número do Lote a ser consultado.                      | E                         | P1                        | tpNumero                  | 1-1                       |                                                                                                                      |
| P2                        | Signature                 | Assinatura digital da mensagem XML.                   | G                         | -                         | SignatureType             | 1-1                       | 'Signature' é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig- coreschema_v01.xsd |

* Representação da estrutura definida no schema XML PedidoConsultaLote.xsd.

- IV. Schema da Mensagem XML do Retorno: RetornoConsulta.xsd (Idêntico ao do item 4.3.5)
- V. Formato das Mensagens SOAP:

## Pedido:

```
<?xml version=" 1 0" encoding= utf-8" ?> <soap Envelope xmlns xsi= "http: Www w3 .org/2001/XMLSchema-instance xmlns xsd="http:// www w3 .org/ 2001/XMLSchema xmlns soap=" 'http:// schemas xmlsoap.org/ soap/envelope / <soap Body> <ConsultaloteRequest xmlns=" 'http: Www prefeitura sp. gov br / nfe <MensagemXML > INCLUIR AQUI MENSAGEM XML CONFORME ITEM III< MensagemXML > < /ConsultaloteRequest> </ soap: Body> soap Envelope> "7 "7
```

## Retorno:

```
<?xml version=" 1 0 " encoding= utf-8" ?> <soap Envelope xmlns:xsi="http:/ Www w3 .org/2001/XMLSchema-instance xmlns xsd="http://www w3 .org/ 2001 XMLSchema xmlns soap= 'http:// schemas xmlsoap.org/ soap/envelope <soap Body> <ConsultaloteResponse xmlns="http: prefeitura sp.gov br/ nfe" > <RetornoXML> MENSAGEM XML DE RETORNO CONF ORME ITEM IV< RetornoXML> < /ConsultaLoteResponse> </ soap Body> </soap Envelope>
```

## 4.3.9. Pedido de Informações do Lote (ConsultaInformacoesLote)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de Consulta de Informações de Lote de NF-e geradas a partir do método EnvioLoteRPS.
- II. Método: ConsultaInformacoesLote
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:
- IV. Schema da Mensagem XML do Retorno: RetornoInformacoesLote.xsd

| PedidoInformaçõesLote.xsd*   | PedidoInformaçõesLote.xsd*   | PedidoInformaçõesLote.xsd*                                                      | PedidoInformaçõesLote.xsd*   | PedidoInformaçõesLote.xsd*   | PedidoInformaçõesLote.xsd*   | PedidoInformaçõesLote.xsd*   | PedidoInformaçõesLote.xsd*                                                                                           |
|------------------------------|------------------------------|---------------------------------------------------------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------|
| #                            | Campo                        | Descrição                                                                       | Ele                          | Pai                          | Tipo                         | Ocorr.                       | Observação                                                                                                           |
| P1                           | Cabecalho                    | TAG de grupo das informações do cabeçalho.                                      | G                            | -                            | -                            | 1-1                          |                                                                                                                      |
|                              | Versao                       | Versão do XML Schema Utilizado.                                                 | A                            | P1                           | tpVersao                     | 1-1                          |                                                                                                                      |
|                              | CNPJRemetente                | CNPJ do Remetente autorizado a enviar a mensagem XML.                           | E                            | P1                           | tpCPFCNPJ                    | 1-1                          |                                                                                                                      |
|                              | NumeroLote                   | Número do Lote a ser consultado.                                                | E                            | P1                           | tpNumero                     | 0-1                          | Caso não seja informado o número do lote, serão retornadas informações do último lote gerador de NF-e.               |
|                              | InscricaoPrestador           | Inscrição municipal do prestador de serviços que gerou o lote a ser consultado. | E                            | P1                           | tpInscricaoMunicipal         | 1-1                          |                                                                                                                      |
| P2                           | Signature                    | Assinatura digital da mensagem XML.                                             | G                            | -                            | SignatureType                | 1-1                          | 'Signature' é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig- coreschema_v01.xsd |

* Representação da estrutura definida no schema XML PedidoInformacoesLote.xsd.

| RetornoInformaçõesLote.xsd*   | RetornoInformaçõesLote.xsd*   | RetornoInformaçõesLote.xsd*                                                                             | RetornoInformaçõesLote.xsd*   | RetornoInformaçõesLote.xsd*   | RetornoInformaçõesLote.xsd*   | RetornoInformaçõesLote.xsd*   | RetornoInformaçõesLote.xsd*   |
|-------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
| #                             | Campo                         | Descrição                                                                                               | Ele                           | Pai                           | Tipo                          | Ocorr.                        | Observação                    |
| P1                            | Cabecalho                     | TAG de grupo das informações do cabeçalho.                                                              | G                             | -                             | -                             | 1-1                           |                               |
|                               | Versao                        | Versão do XML Schema Utilizado.                                                                         | A                             | P1                            | tpVersao                      | 1-1                           |                               |
|                               | Sucesso                       | Status do Envio de Lote                                                                                 | E                             | P1                            | tpSucesso                     | 1-1                           |                               |
|                               | InformacoesLote               | Informações sobre o Lote                                                                                | G                             | P1                            | tpInformacoesLote             | 0-1                           |                               |
| P2                            | Alerta                        | Informações sobre a ocorrência de eventos geradores de alertas durante o processamento da mensagem XML. | G                             | -                             | tpEvento                      | 0-N                           |                               |
| P3                            | Erro                          | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML.   | G                             | -                             | tpEvento                      | 0-N                           |                               |

* Representação da estrutura definida no schema XML RetornoInformacoesLote.xsd.

- V. Formato das Mensagens SOAP:

## Pedido:

```
<?xml version=" 1 0 " encoding= utf-8" ?> <soap Envelope xmlns:xsi="http: Www w3 .org/2001/XMLSchema-instance xmlns:xsd= 'http://www w3 org/ 2001/ XMLSchema xmlns soap="http:// schemas <soap <ConsultaInformacoesLoteRequest xmlns= http: <VersaoSchema> 1</ VersaoSchema> <MensagemXML > INCLUIR AQUI A MENSAGEM XML CONFORME ITEM III< MensagemXML > < /ConsultaInformacoesLoteRequest> soap: soap: Envelope> Body> Body>
```

## Retorno:

```
<?xml Version= 1 0 " encoding= utf-8" ?> <soap Envelope xmlns:xsi= "http: Www w3 .org/2001/XMLSchema-instance" xmlns:xsd= / / www w3 .org/ 2001/XMLSchema xmlns soap=" 'http:// schemas <soap Body> <ConsultaInformacoesloteResponse xmlns= 'http:/ / www.prefeitura sp br/ nfe" > <RetornoXML> MENSAGEM XML DE RETORNO CONF ORME ITEM IV< RetornoXML> </ConsultaInformacoesLoteResponse> </ soap Body> soap: Envelope> "http: gov
```

## 4.3.10. Pedido de Cancelamento de NF-e (CancelamentoNFe)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos referentes ao cancelamento de NF-e geradas a partir do método EnvioLoteRPS.
- II. Método: CancelamentoNFe
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| PedidoCancelamentoNFe.xsd*   | PedidoCancelamentoNFe.xsd*   | PedidoCancelamentoNFe.xsd*                                                | PedidoCancelamentoNFe.xsd*   | PedidoCancelamentoNFe.xsd*   | PedidoCancelamentoNFe.xsd*   | PedidoCancelamentoNFe.xsd*   | PedidoCancelamentoNFe.xsd*                                                                                                                                                                                                                                                                   |
|------------------------------|------------------------------|---------------------------------------------------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #                            | Campo                        | Descrição                                                                 | Ele                          | Pai                          | Tipo                         | Ocorr.                       | Observação                                                                                                                                                                                                                                                                                   |
| P1                           | Cabecalho                    | TAG de grupo das informações do cabeçalho.                                | G                            | -                            | -                            | 1-1                          |                                                                                                                                                                                                                                                                                              |
|                              | Versao                       | Versão do XML Schema Utilizado.                                           | A                            | P1                           | tpVersao                     | 1-1                          |                                                                                                                                                                                                                                                                                              |
|                              | CNPJRemetent e               | CNPJ do Remetente autorizado a enviar a mensagem XML                      | E                            | P1                           | tpCPFCNPJ                    | 1-1                          |                                                                                                                                                                                                                                                                                              |
|                              | Transacao                    | Informe se as NF-e a serem canceladas farão parte de uma mesma transação. | E                            | P1                           | Boolean                      | 0-1                          | True - As NF-e só serão canceladas se não ocorrer nenhum evento de erro durante o processamento de todo o lote. False - As NF-e aptas a serem canceladas serão canceladas, mesmo que ocorram eventos de erro durante processamento do cancelamento de outras NF-e deste lote. Default: true. |
| P2                           | Detalhe                      | Tag de grupo das informações de detalhe.                                  | G                            | -                            |                              | 1-50                         |                                                                                                                                                                                                                                                                                              |
|                              | ChaveNFe                     | Chave da NF-e.                                                            | E                            | P2                           | tpChaveNFe                   | 1-1                          |                                                                                                                                                                                                                                                                                              |
|                              | AssinaturaCanc elamento      | Assinatura de Cancelamento da NF-e.                                       | E                            | P2                           | tpAssinaturaCa ncelamento    | 1-1                          |                                                                                                                                                                                                                                                                                              |
| P3                           | Signature                    | Assinatura digital da mensagem XML.                                       | G                            | -                            | SignatureType                | 1-1                          | 'Signature' é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsigcore- schema_v01.xsd                                                                                                                                                                         |

* Representação da estrutura definida no schema XML PedidoCancelamentoNFe.xsd.

## Observação 1: Transação

Se ocorrerem eventos de erro de validação dos dados do cabeçalho do pedido de cancelamento de NF-e, independente da opção informada no campo 'Transação', nenhuma NF -e será cancelada.

## Observação 2: Assinatura Adicional

Cada NF-e a ser cancelada (representada pela TAG ChaveNFe) deverá ter sua respectiva assinatura de cancelamento. Esta assinatura utilizará o mesmo certificado digital usado na assinatura da mensagem XML (item 3.2.2A), com os mesmos padrões de criptografia assimétrica RSA e algoritmo message digest SHA-1.

Para criar a assinatura deverá ser gerado um Hash (utilizando SHA1) de uma cadeia de caracteres (ASCII) com informações da NF-e a ser cancelada. Este Hash deverá ser assinado utilizando RSA. A assinatura do Hash será informada na TAG AssinaturaCancelamento.

A cadeia de caracteres a ser assinada deverá conter 20 posições com as informações apresentadas na tabela a seguir:

|   # | Informação                       | Conteúdo                                                                                                        |
|-----|----------------------------------|-----------------------------------------------------------------------------------------------------------------|
|   1 | Inscrição Municipal do Prestador | Inscrição Municipal do Prestador com 8 posições (dígitos). Completar com zeros à esquerda caso seja necessário. |
|   2 | Número da NF-e                   | Nœmero da NF-e com 12 posiçıes (dígitos). Completar com zeros à esquerda caso seja necessÆrio.                  |

Passos básicos para assinatura de cancelamento de uma NF-e:

- 1º - Monte a string de caracteres conforme a tabela a apresentada anteriormente.

A seguir apresentamos o exemplo de um trecho de uma mensagem XML de pedido de cancelamento de NF-e (os campos utilizados na montagem da cadeia de caracteres estão em negrito).

```
<ChaveNFe> <NumeroNFe> 9 < / NumeroNFe> </ ChaveNFe>
```

Com  base  no  trecho  da  mensagem  XML  apresentada,  montamos  a  seguinte  String  de  caracteres: "31000000000000000009"

- 2º - Converta a cadeia de caracteres ASCII para bytes.
- 3º - Gere o HASH (array de bytes) utilizando SHA1.
- 4º - Assine o HASH (array de bytes) utilizando RSA-SHA1.

ATENÇÃO! Na maioria das linguagens de programação, os passos 3 e 4 são feitos através de uma única função. Verifique a documentação de sua linguagem para evitar assinar um hash de um hash.

- IV. Schema da Mensagem XML do Retorno: RetornoCancelamentoNFe.xsd

| RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*                | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   |
|-------------------------------|-------------------------------|--------------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
| #                             | Campo                         | Descrição                                  | Ele                           | Pai                           | Tipo                          | Ocorr.                        | Observação                    |
| P1                            | Cabecalho                     | TAG de grupo das informações do cabeçalho. | G                             | -                             | -                             | 1-1                           |                               |
|                               | Versao                        | Versão do XML Schema Utilizado.            | A                             | P1                            | tpVersao                      | 1-1                           |                               |

| RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*                                                                             | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   | RetornoCancelamentoNFe.xsd*   |
|-------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
| #                             | Campo                         | Descrição                                                                                               | Ele                           | Pai                           | Tipo                          | Ocorr.                        | Observação                    |
|                               | Sucesso                       | Status do cancelamento.                                                                                 | E                             | P1                            | tpSucesso                     | 1-1                           |                               |
| P2                            | Alerta                        | Informações sobre a ocorrência de eventos geradores de alertas durante o processamento da mensagem XML. | G                             | -                             | tpEvento                      | 0-N                           |                               |
| P3                            | Erro                          | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML.   | G                             | -                             | tpEvento                      | 0-N                           |                               |

* Representação da estrutura definida no schema XML RetornoCancelamentoNFe.xsd.

O Sistema da NF-e verificará se a NF-e existe e se não há nenhum impedimento para o cancelamento.

O cancelamento poderá ser realizado para várias notas numa mesma mensagem XML (Obedecendo ao limite de 50).

## V. Formato das Mensagens SOAP:

## Pedido:

```
<?xml version= 1.0" encoding="utf-8" ?> <soap: Enve lope xmlns:xsi="http: Www org/2001/XMLSchema-instance xmlns xsd= http:/ / www org/ 2001/XMLSchema xmlns 'http:// schemas xmlsoap.org/ soap/envelope / "> <soap Body> <CancelamentoNFeRequest xmlns="http: Www prefeitura.sp.gov br nfe" > <VersaoSchema> 1</VersaoSchema> <MensagemXML > INCLUIR AQUI MENSAGEM XML CONFORME ITEM III< MensagemXML > </CancelamentoNFeRequest> soap Body> soap: Envelope> w3 _ w3
```

## Retorno:

```
<?xml version= 1.0" encoding= utf-8" ?> <soap Envelope xmlns xsi="http://www w3 org/2001/XMLSchema-instance xmlns xsd="http://www w3 . org/ 2001/XMLSchema xmlns soap=" 'http:// schemas xmlsoap.org/ soap/envelope / "> <soap Body> <CancelamentoNFeResponse xmlns= 'http: Www prefeitura sp. gov br /nfe" > <RetornoXML> MENSAGEM XML DE RETORNO CONF ORME ITEM IV< RetornoXML> ICancelamentoNFeResponse> Body> soap Envelope >
```

## 4.3.11. Pedido de Consulta de CNPJ (ConsultaCNPJ)

Secretaria Municipal d Finanças

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de consulta de CNPJ. Este método possibilita aos tomadores e/ou prestadores de serviços consultarem quais Inscrições Municipais (CCM) estão vinculadas a um determinado CNPJ e se estes CCM emitem NF-e ou não.
- II. Método: ConsultaCNPJ
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:
- IV. Schema da Mensagem XML do Retorno: RetornoConsultaCNPJ.xsd

| PedidoConsultaCNPJ.xsd*   | PedidoConsultaCNPJ.xsd*   | PedidoConsultaCNPJ.xsd*                              | PedidoConsultaCNPJ.xsd*   | PedidoConsultaCNPJ.xsd*   | PedidoConsultaCNPJ.xsd*   | PedidoConsultaCNPJ.xsd*   | PedidoConsultaCNPJ.xsd*                                                                                              |
|---------------------------|---------------------------|------------------------------------------------------|---------------------------|---------------------------|---------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| #                         | Campo                     | Descrição                                            | Ele                       | Pai                       | Tipo                      | Ocorr.                    | Observação                                                                                                           |
| P1                        | Cabecalho                 | TAG de grupo das informações do cabeçalho.           | G                         | -                         | -                         | 1-1                       |                                                                                                                      |
|                           | Versao                    | Versão do XML Schema Utilizado.                      | A                         | P1                        | tpVersao                  | 1-1                       |                                                                                                                      |
|                           | CNPJRemetente             | CNPJ do Remetente autorizado a enviar a mensagem XML | E                         | P1                        | tpCPFCNPJ                 | 1-1                       |                                                                                                                      |
| P2                        | CNPJContribuinte          | CNPJ do contribuinte que se deseja consultar.        | E                         | -                         | tpCPFCNPJ                 | 1-1                       |                                                                                                                      |
| P3                        | Signature                 | Assinatura digital da mensagem XML.                  | G                         | -                         | SignatureType             | 1-1                       | 'Signature' é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsigcore- schema_v01.xsd |

*Representação da estrutura definida no schema XML PedidoConsultaCNPJ.xsd.

| RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*                   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   |
|----------------------------|----------------------------|--------------------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| #                          | Campo                      | Descrição                                  | Ele                        | Pai                        | Tipo                       | Ocorr.                     | Observação                 |
| P1                         | Cabecalho                  | TAG de grupo das informações do cabeçalho. | G                          | -                          | -                          | 1-1                        |                            |
|                            | Versao                     | Versão do XML Schema Utilizado.            | A                          | P1                         | tpVersao                   | 1-1                        |                            |

| RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*                                                                                | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   | RetornoConsultaCNPJ.xsd*   |
|----------------------------|----------------------------|---------------------------------------------------------------------------------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| #                          | Campo                      | Descrição                                                                                               | Ele                        | Pai                        | Tipo                       | Ocorr.                     | Observação                 |
|                            | Sucesso                    | Status do cancelamento.                                                                                 | E                          | P1                         | tpSucesso                  | 1-1                        |                            |
| P2                         | Alerta                     | Informações sobre a ocorrência de eventos geradores de alertas durante o processamento da mensagem XML. | G                          | -                          | tpEvento                   | 0-N                        |                            |
| P3                         | Erro                       | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML.   | G                          | -                          | tpEvento                   | 0-N                        |                            |
| P4                         | Detalhe                    | TAG de grupo das informações do detalhe.                                                                | G                          | -                          |                            | 0-N                        |                            |
|                            | InscricaoMunici pal        | Inscrição Municipal vinculada ao CNPJ consultado.                                                       | E                          | P4                         | tpInscricaoMuni cipal      | 1-1                        |                            |
|                            | EmiteNFe                   | Campo que indica se o contribuinte emite NF-e.                                                          | E                          | P4                         | Boolean                    | 1-1                        |                            |

* Representação da estrutura definida no schema XML RetornoConsultaCNPJ.xsd.

## V. Formato das Mensagens SOAP:

## Pedido:

```
<?xml version= 1 .0" encoding= utf-8" ?> <soap Envelope xmlns:xsi="http: w3 .org/2001/XMLSchema-instance xmlns:xsd= "http://www w3.org/ 2001/XMLSchema xmlns : soap= "http:// schemas xmlsoap.org/ soap/envelope / " > <soap Body> <ConsultaCNPJRequest xmlns="http: WWW .prefeitura sp gov br / nfe <VersaoSchema 1</VersaoSchema> <MensagemXML> INCLUIR AQUI A MENSAGEM XML CONFORME ITEM III< MensagemXML > IConsultaCNPJRequest> Body> </soap Envelope>
```

## Retorno:

```
<?xml version=" 1.0" encoding-"utf-8" ?> <soap Enve lope xmlns xsi="http:/ /www w3 .org/2001/XMLSchema-instance xmlns xsd="http://www w3 org/ 2001/ XMLSchema xmlns soap="http:// schemas xmlsoap.org/soaplenvelope <soap Body> <ConsultaCNPJResponse xmlns=" 'http: WWW .prefeitura sp.gov br/nfe" > <RetornoXML> MENSAGEM XML DE RETORNO CONFORME ITEM IV< RetornoXML> < /ConsultaCNPJResponse> </ soap Body> </ soap: Envelope>
```

## 4.4. SERVIÇOS E MÉTODOS ASSÍNCRONOS

## 4.4.1. Regras Gerais

Mesmas regras gerais utilizadas nos serviços e métodos síncronos (item 4.3.1).

## 4.4.2. Envio de Lote de RPS (EnvioLoteRpsAsync)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos assíncronos de Envio de Lote de RPS para substituição por NF-e.
- II. Método EnvioLoteRpsAsync.
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| PedidoEnvioLoteRPSAsync.xsd*   | PedidoEnvioLoteRPSAsync.xsd*   | PedidoEnvioLoteRPSAsync.xsd*                                                        | PedidoEnvioLoteRPSAsync.xsd*   | PedidoEnvioLoteRPSAsync.xsd*   | PedidoEnvioLoteRPSAsync.xsd*   | PedidoEnvioLoteRPSAsync.xsd*   | PedidoEnvioLoteRPSAsync.xsd*                                                                                                                                                                                                                                    |
|--------------------------------|--------------------------------|-------------------------------------------------------------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #                              | Campo                          | Descrição                                                                           | Ele                            | Pai                            | Tipo                           | Ocorr.                         | Observação                                                                                                                                                                                                                                                      |
| P1                             | Cabecalho                      | TAG de grupo das informações do cabeçalho.                                          | G                              | -                              | -                              | 1-1                            |                                                                                                                                                                                                                                                                 |
|                                | Versao                         | Versão do XML Schema Utilizado.                                                     | A                              | P1                             | tpVersao                       | 1-1                            |                                                                                                                                                                                                                                                                 |
|                                | CNPJRemetente                  | CNPJ do Remetente autorizado a transmitir a mensagem XML.                           | E                              | P1                             | tpCPFCNPJ                      | 1-1                            |                                                                                                                                                                                                                                                                 |
|                                | Transacao                      | Informe se os RPS a serem substituídos por NF-e farão parte de uma mesma transação. | E                              | P1                             | boolean                        | 0-1                            | True - Os RPS só serão substituidos por NF-e se não ocorrer nenhum evento de erro durante o processamento de todo o lote. False - Os RPS válidos serão substituídos por NF-e, mesmo que ocorram eventos de erro durante processamento de outros RPS deste lote. |
|                                | dtInicio                       | Data de início do período transmitido.                                              | E                              | P1                             | D                              | 1-1                            | (AAAA-MM-DD)                                                                                                                                                                                                                                                    |
|                                | dtFim                          | Data final do período transmitido.                                                  | E                              | P1                             | D                              | 1-1                            | (AAAA-MM-DD)                                                                                                                                                                                                                                                    |
|                                | QtdeRPS                        | Quantidade de RPS contidos no lote.                                                 | E                              | P1                             | tpQuantidade                   | 1-1                            |                                                                                                                                                                                                                                                                 |
|                                | ValorTotalServicos             | Valor total dos serviços dos RPS contidos no lote.                                  | E                              | P1                             | tpValor                        | 1-1                            |                                                                                                                                                                                                                                                                 |
|                                | ValorTotalDeducoes             | Valor total das deduções dos RPS/Cupom contidos no lote.                            | E                              | P1                             | tpValor                        | 1-1                            |                                                                                                                                                                                                                                                                 |
| P2                             | RPS                            | Recibo Provisório de Serviço.                                                       | G                              | -                              | tpRPS                          | 1-N                            | O limite de RPS dependerá do tamanho máximo do XML.**                                                                                                                                                                                                           |
| P3                             | Signature                      | Assinatura digital da mensagem XML.                                                 | G                              | -                              | SignatureType                  | 1-1                            | "Signature" é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig-core-schema_v01.xsd                                                                                                                                            |

* Representação da estrutura definida no schema XML PedidoEnvioLoteRPSAsync.xsd

**O XSD utilizado é praticamente igual ao do método síncrono, a diferença está na quantidade máxima de RPS que pode ser enviado; pode haver de 1 a N RPS em um mesmo lote, contudo, deve-se respeitar o tamanho máximo por mensagem XML (500 KB).

## Observação 1: Assinatura Adicional

Cada RPS enviado no lote deverá ser assinado digitalmente conforme especificado no item 4.3.2. (Envio de RPS).

## Observação 2: Transação

Se ocorrerem eventos de erro de validação dos dados do cabeçalho do pedido de envio de lote de RPS, independente da opção informada no campo 'Transação', nenhum RPS será substituído por NF-e.

- IV. Schema da Mensagem XML do Retorno: RetornoEnvioLoteRPSAsync.xsd
- V. Formato das Mensagens SOAP:

| RetornoEnvioLoteAsync.xsd*   | RetornoEnvioLoteAsync.xsd*   | RetornoEnvioLoteAsync.xsd*                                                                            | RetornoEnvioLoteAsync.xsd*   | RetornoEnvioLoteAsync.xsd*   | RetornoEnvioLoteAsync.xsd*   | RetornoEnvioLoteAsync.xsd*   | RetornoEnvioLoteAsync.xsd*   |
|------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| #                            | Campo                        | Descrição                                                                                             | Ele                          | Pai                          | Tipo                         | Ocorr.                       | Observação                   |
| P1                           | Cabecalho                    | TAG de grupo das informações do cabeçalho.                                                            | G                            | -                            | -                            | 1-1                          |                              |
|                              | Versao                       | Versão do XML Schema Utilizado.                                                                       | A                            | P1                           | tpVersao                     | 1-1                          |                              |
|                              | Sucesso                      | Status do Envio do Lote                                                                               | E                            | P1                           | tpSucesso                    | 1-1                          |                              |
|                              | InformacoesLote              | Informações sobre o Lote Assíncrono                                                                   | E                            | P1                           | tpInformacoesLoteAsync       | 0-1                          |                              |
| P2                           | Erro                         | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML. | G                            | -                            | tpEventoAsync                | 0-N                          |                              |

* Representação da estrutura definida no schema XML RetornoEnvioLoteAsync.xsd

## Pedido:

<!-- image -->

## Retorno:

<!-- image -->

## 4.4.3. Teste de Envio de Lote de RPS Assíncrono (TesteEnvioLoteRpsAsync)

<!-- image -->

- I. Descrição: Este método é responsável por atender aos pedidos de Teste de Envio de Lote de RPS para substituição por NF-e. Este método não substitui os RPS por NF-e.

## Observação:

Conforme informado no item 2.2.3, este método deverá ser usado apenas na fase de adaptação dos  sistemas  dos  contribuintes.  Nos  casos  de  sistemas  já  adaptados,  seu  uso  resulta  em duplicidade de esforços desnecessários, pois as verificações feitas no método TesteEnvioLoteRPSAsync são as mesmas realizadas pelo método EnvioLoteRPSAsync.

- II. Método: TesteEnvioLoteRPSAsync
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela apresentada no item III do método EnvioLoteRPSAsync.
- IV. Schema da Mensagem XML do Retorno: RetornoEnvioLoteRPSAsync.xsd (Idêntico ao Schema da Mensagem XML do Retorno do método EnvioLoteRPSAsync).

## 4.4.4. Pedido de Consulta da Situação do Lote RPS Assíncrono (ConsultaSituacaoLote)

<!-- image -->

- I. Descrição: Este método é responsável por atender os pedidos de consulta da situação do lote de RPS assíncrono.
- II. Método: ConsultaSituacaoLote
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote                                 | ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: PedidoConsultaSituacaoLote   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| #                                                                       | Campo                                                                   | Descrição                                                                                             | Ele                                                                     | Pai                                                                     | Tipo                                                                    | Ocorr.                                                                  | Observação                                                              |
| P1                                                                      | CPFCNPJRemet ente                                                       | CPF/CNPJ do Remetente autorizado a enviar a mensagem XML.                                             | E                                                                       | -                                                                       | tpCPFCNPJ                                                               | 1-1                                                                     |                                                                         |
| P2                                                                      | NumeroProtocolo                                                         | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML. | E                                                                       | -                                                                       | tpNumeroProtocoloA sync                                                 | 1-1                                                                     |                                                                         |

* Representação da estrutura definida no schema XML ConsultaSituacaoLoteAsync.xsd

## IV. Schema da Mensagem XML do Retorno: ConsultaSituacaoLoteAsync.xsd:

| ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote                                | ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote   | ConsultaSituacaoLoteAsync.xsd* - Elemento: RetornoConsultaSituacaoLote                                    |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| #                                                                        | Campo                                                                    | Descrição                                                                                             | Ele                                                                      | Pai                                                                      | Tipo                                                                     | Ocorr.                                                                   | Observação                                                                                                |
| P1                                                                       | Sucesso                                                                  | Status do Envio do Lote                                                                               | E                                                                        | -                                                                        | tpSucesso                                                                | 1-1                                                                      |                                                                                                           |
| P2                                                                       | Situacao                                                                 | Código do Status do Lote                                                                              | E                                                                        | -                                                                        | tpNumero                                                                 | 1-1                                                                      |                                                                                                           |
|                                                                          | Nome                                                                     | Descrição do Status do Lote                                                                           | A                                                                        | P2                                                                       | tpSituacaoLote                                                           | 1-1                                                                      |                                                                                                           |
| P3                                                                       | NumeroLote                                                               | Número do Lote após o processamento                                                                   | E                                                                        | -                                                                        | tpNumero                                                                 | 0-1                                                                      |                                                                                                           |
| P4                                                                       | DataRecebiment o                                                         | Data do recebimento do Lote                                                                           | E                                                                        | -                                                                        | D                                                                        | 0-1                                                                      |                                                                                                           |
| P5                                                                       | DataProcessame nto                                                       | Data que o Lote foi processado                                                                        | E                                                                        | -                                                                        | D                                                                        | 0-1                                                                      |                                                                                                           |
| P6                                                                       | ResultadoOperac ao                                                       | Informações sobre o Lote Assíncrono processado                                                        | E                                                                        | -                                                                        | C                                                                        | 0-1                                                                      | Retorna a mensagem XML conforme o Schema de retorno RetornoEnvioLoteRPS. xsd quando o Lote foi processado |
| P7                                                                       | Erro                                                                     | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML. | G                                                                        | -                                                                        | tpEventoAsync                                                            | 0-N                                                                      |                                                                                                           |

* Representação da estrutura definida no schema XML ConsultaSituacaoLoteAsync.xsd

- V. Formato das Mensagens SOAP:

## Pedido:

```
versions"1 0" encoding="utf-8"?> <soap:Envelope xmlns: xsis"http://wwn w3.org/2001/XMLSchema-instance xmlns xsd="http:/ /wwn w3 .org/ 2001 /XMLSchema xmlns:soap= "http:// schemas xmlsoap.org/soap/envelope/ <soap Body> <ConsultasituacaoloteRequest xmlns="http: gov .br/nfe"> <MensagemXML> INCLUIR AQUI 4 MENSAGEM XMI CONFORME ITEM III/ MensagenXML> </consultasituacaoloteRequest> soap Body> soap: Envelope) sp.
```

## Retorno:

```
<?xml versionz"1 0" encoding="utf-8"?> <soap:Envelope xmlns:xsi="http://wwn w3.org/2001/XMLSchema-instance xmlns: xsd="http:/ /wwn w3 .org/ 2001/XMLSchema xmlns:soap= http:/ / schemas xmlsoap org/ soap/envelope/ "> <soap: Body> <ConsultasituacaoloteResponse xmlns="http /wnw .prefeitura sp gov.br/nfe"> <RetornoXML>MPNSAGEM XM DE RETORNO CONFORMS IIEM IV< /RetornoxML> </ soap: Body> soap: Envelope>
```

## 4.4.5. Emissão de Guia de forma Assíncrona (EmissaoGuiaAsync)

<!-- image -->

- I. Descrição:  Este  método  é  responsável  por  atender  os  pedidos  de  emissão  de  guia  de  forma assíncrona.
- II. Método: EmissaoGuiaAsync
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:

| EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync    | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   |
|----------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| #                                                        | Campo                                                    | Descrição                                                 | Ele                                                      | Pai                                                      | Tipo                                                     | Ocorr.                                                   | Observação                                               |
| P1                                                       | CPFCNPJRemet ente                                        | CPF/CNPJ do Remetente autorizado a enviar a mensagem XML. | E                                                        | -                                                        | tpCPFCNPJ                                                | 1-1                                                      |                                                          |
| P2                                                       | InscricaoPrestador                                       | Inscrição Municipal do Prestador.                         | E                                                        | -                                                        | tpInscricaoMunicipal                                     | 1-1                                                      |                                                          |
| P3                                                       | TipoEmissaoGuia                                          | Tipo da emissão da guia.                                  | E                                                        | -                                                        | tpEmissaoGuia                                            | 1-1                                                      |                                                          |
| P4                                                       | Incidencia                                               | Incidência da Guia que deseja gerar                       | E                                                        | -                                                        | tpIncidencia                                             | 1-1                                                      |                                                          |

| EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: PedidoEmissaoGuiaAsync                                                                |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| #                                                        | Campo                                                    | Descrição                                                | Ele                                                      | Pai                                                      | Tipo                                                     | Ocorr.                                                   | Observação                                                                                                            |
| P5                                                       | DataPagamento                                            | Data que será o pagamento da Guia                        | E                                                        | -                                                        | D                                                        | 1-1                                                      |                                                                                                                       |
| P6                                                       | Signature                                                | Assinatura digital da mensagem XML                       | G                                                        | -                                                        | SignatureType                                            | 1-1                                                      | 'Signature' é o elemento raiz de uma assinatura XML. Este elemento é descrito no arquivo xmldsig-core- schema_v01.xsd |

* Representação da estrutura definida no schema XML EmissaoGuiaAsync.xsd

- IV. Schema da Mensagem XML do Retorno: EmissaoGuiaAsync.xsd:

| EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync                                               | EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync   | EmissaoGuiaAsync.xsd - element: RetornoEmissaoGuiaAsync   |
|-----------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| #                                                         | Campo                                                     | Descrição                                                                                             | Ele                                                       | Pai                                                       | Tipo                                                      | Ocorr.                                                    | Observação                                                |
| P1                                                        | Cabecalho                                                 | TAG de grupo das informações do cabeçalho.                                                            | G                                                         | -                                                         | -                                                         | 1-1                                                       |                                                           |
|                                                           | Versao                                                    | Versão do XML Schema Utilizado.                                                                       | A                                                         | P1                                                        | tpVersao                                                  | 1-1                                                       |                                                           |
|                                                           | Sucesso                                                   | Status do Envio do Lote                                                                               | E                                                         | P1                                                        | tpSucesso                                                 | 1-1                                                       |                                                           |
|                                                           | InformacoesLote                                           | Informações sobre a Guia Assíncrona                                                                   | G                                                         | P1                                                        | tpInformacoesGuiaAs ync                                   | 0-1                                                       |                                                           |
| P2                                                        | Erro                                                      | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML. | G                                                         | -                                                         | tpEventoAsync                                             | 0-N                                                       |                                                           |

* Representação da estrutura definida no schema XML EmissaoGuiaAsync.xsd

## V. Formato das Mensagens SOAP:

## Pedido:

<!-- image -->

## Retorno:

```
<?xml version="1.0" encoding="utf-8"?> <soap:Envelope xmlns: w3.org/2001/XMLSchema-instance xmlns:xsd="http: w3 org/ 2001 /XMLSchema xmlns soap= http:/ / schemas xmlsoap.org/soap/envelope/ <soap Body> <EmissaoGuiaResponse xmlns="http: Jwww prefeitura sp.gov .br/nfe <EmissaoGuiaResult)MENSAGEM XM DE RETORNO CONFORME IIEM IV EmissaoGuiaResult> </EmissaoGuiaResponse> <l soap Body> soap: Envelope) "7
```

## 4.4.6. Pedido de Consulta da Situação da Emissão de Guia Assíncrona (ConsultaSituacaoGuia)

<!-- image -->

- I. Descrição: Este método é responsável por atender os pedidos de consulta da situação da emissão de Guia Assíncrona.
- II. Método: ConsultaSituacaoGuia
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:
- IV. Schema da Mensagem XML do Retorno: ConsultaSituacaoGuiaAsync.xsd:

| ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia                                 | ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: PedidoConsultaSituacaoGuia   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| #                                                                       | Campo                                                                   | Descrição                                                                                             | Ele                                                                     | Pai                                                                     | Tipo                                                                    | Ocorr.                                                                  | Observação                                                              |
| P1                                                                      | CPFCNPJRemet ente                                                       | CPF/CNPJ do Remetente autorizado a enviar a mensagem XML.                                             | E                                                                       | -                                                                       | tpCPFCNPJ                                                               | 1-1                                                                     |                                                                         |
| P2                                                                      | NumeroProtocolo                                                         | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML. | E                                                                       | -                                                                       | tpNumeroProtocoloA sync                                                 | 1-1                                                                     |                                                                         |

* Representação da estrutura definida no schema XML ConsultaSituacaoGuiaAsync.xsd

| ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| #                                                                        | Campo                                                                    | Descrição                                                                | Ele                                                                      | Pai                                                                      | Tipo                                                                     | Ocorr.                                                                   | Observação                                                               |
| P1                                                                       | Sucesso                                                                  | Status da consulta da situação da Guia                                   | E                                                                        | -                                                                        | tpSucesso                                                                | 1-1                                                                      |                                                                          |

| ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia                                | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia   | ConsultaSituacaoGuiaAsync.xsd* - Elemento: RetornoConsultaSituacaoGuia                            |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| #                                                                        | Campo                                                                    | Descrição                                                                                             | Ele                                                                      | Pai                                                                      | Tipo                                                                     | Ocorr.                                                                   | Observação                                                                                        |
| P2                                                                       | Situacao                                                                 | Código do Status do processamento da Guia                                                             | E                                                                        | -                                                                        | tpNumero                                                                 | 1-1                                                                      |                                                                                                   |
|                                                                          | Nome                                                                     | Descrição do Status do processamento da Guia                                                          | A                                                                        | P2                                                                       | tpSituacaoGuia                                                           | 1-1                                                                      |                                                                                                   |
| P3                                                                       | NumeroGuia                                                               | Número da Guia após o processamento                                                                   | E                                                                        | -                                                                        | tpNumero                                                                 | 0-1                                                                      |                                                                                                   |
| P4                                                                       | DataRecebiment o                                                         | Data do recebimento do pedido de processamento da Guia                                                | E                                                                        | -                                                                        | D                                                                        | 0-1                                                                      |                                                                                                   |
| P5                                                                       | DataProcessame nto                                                       | Data que a Guia foi processada                                                                        | E                                                                        | -                                                                        | D                                                                        | 0-1                                                                      |                                                                                                   |
| P6                                                                       | ResultadoOperac ao                                                       | Informações sobre a Guia Assíncrono processado                                                        | E                                                                        | -                                                                        | C                                                                        | 0-1                                                                      | Retorna a mensagem XML conforme o Schema de retorno ConsultaGuia.xsd quando a Guia foi processado |
| P7                                                                       | Erro                                                                     | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML. | G                                                                        | -                                                                        | tpEventoAsync                                                            | 0-N                                                                      |                                                                                                   |

* Representação da estrutura definida no schema XML ConsultaSituacaoGuiaAsync.xsd

## V. Formato das Mensagens SOAP:

## Pedido:

```
0" encoding="utf-8"?> <soap:Envelope xmlns:xsis"http://wwn w3.org/2001/XMLSchema-instance w3 org/ 2001/XMLSchema xmlns soap="http://schemas xmlsoap org /soap/envelope/ <soap: Body> {ConsultasituacaoGuiaRequest xmlns="http: Iww . prefeitura sp.gov br/nfe"> <VersaoSchema>l</VersaoSchema) AQUI 4 MENSAGEM CONFORMS ITEM III</ MensagenXML> <l soap: Body> </soap: Envelope)
```

## Retorno:

```
<?xml version="1 0" encoding="utf-8" ?> <soap:Envelope xmlns:xsd="http: w3 .org/ 2001 /XMLSchema xmlns soap="http:// schemas xmlsoap org / soap/envelope/ "> <soap Body> <ConsultasituacaoGuiaResponse 'http://wnw.prefeitura sp.gov.br/nfe"> <RetornoXML>MENSAGEM XM DE RETORNO CONFORME IIEM IV</RetornoXM> </consultasituacaoGuiaResponse> soap: Body>
```

## 4.4.7. Pedido de Consulta de Guia (ConsultaGuia)

<!-- image -->

- I. Descrição: Este método é responsável por atender os pedidos de consulta de guia (tanto guias geradas de forma assíncrona, quanto as gerada diretamente no sistema).
- II. Método: ConsultaGuia
- III. O parâmetro MensagemXML (ver item 4.3.1) deverá ser preenchido conforme tabela a seguir:
- IV. Schema da Mensagem XML do Retorno: ConsultaGuia.xsd:

| ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia   | ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia   | ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia                         | ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia   | ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia   | ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia   | ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia   | ConsultaGuia.xsd* - Elemento: PedidoConsultaGuia   |
|----------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| #                                                  | Campo                                              | Descrição                                                                | Ele                                                | Pai                                                | Tipo                                               | Ocorr.                                             | Observação                                         |
| P1                                                 | CPFCNPJRemet ente                                  | CPF/CNPJ do Remetente autorizado a enviar a mensagem XML.                | E                                                  | -                                                  | tpCPFCNPJ                                          | 1-1                                                |                                                    |
| P2                                                 | InscricaoPrestad or                                | Inscrição Municipal vinculada ao CNPJ autorizado a enviar a mensagem XML | E                                                  | -                                                  | tpInscricaoMunicipal                               | 1-1                                                |                                                    |
| P3                                                 | Incidencia                                         | Incidência da emissão da guia                                            | E                                                  | -                                                  | tpIncidencia                                       | 1-1                                                |                                                    |
| P4                                                 | Situacao                                           | Tipo da situação da Guia                                                 | E                                                  | -                                                  | tpSituacaoGuia                                     | 1-1                                                |                                                    |
| P5                                                 | TipoEmissao                                        | Tipo da emissão da Guia                                                  | E                                                  | -                                                  | tpEmissaoGuia                                      | 0-1                                                |                                                    |

* Representação da estrutura definida no schema XML ConsultaGuia.xsd

| ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   |
|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| #                                                   | Campo                                               | Descrição                                           | Ele                                                 | Pai                                                 | Tipo                                                | Ocorr.                                              | Observação                                          |
| P1                                                  | Cabecalho                                           | TAG de grupo das informações do cabeçalho.          | G                                                   | -                                                   | -                                                   | 1-1                                                 |                                                     |
|                                                     | Versao                                              | Versão do XML Schema Utilizado.                     | A                                                   | P1                                                  | tpVersao                                            | 1-1                                                 |                                                     |
|                                                     | Sucesso                                             | Status do Envio do pedido de consulta               | E                                                   | P1                                                  | tpSucesso                                           | 1-1                                                 |                                                     |
| P2                                                  | Guia                                                | Informações sobre a Guia                            | G                                                   |                                                     | tpGuia                                              | 0-N                                                 |                                                     |

| ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia                                                     | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   | ConsultaGuia.xsd* - Elemento: RetornoConsultaGuia   |
|-----------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| #                                                   | Campo                                               | Descrição                                                                                             | Ele                                                 | Pai                                                 | Tipo                                                | Ocorr.                                              | Observação                                          |
| P3                                                  | Erro                                                | Informações sobre a ocorrência de eventos geradores de erros durante o processamento da mensagem XML. | G                                                   | -                                                   | tpEventoAsync                                       | 0-N                                                 |                                                     |

* Representação da estrutura definida no schema XML ConsultaGuia.xsd

## V. Formato das Mensagens SOAP:

## Pedido:

```
<?xml versions"1 0" encoding="utf-8"2> <soap:Envelope xmlns:xsi="http://wwn w3.org/2001/XMLSchema-instance xmlns:xsd="http: Iwwn w3 org/ 2001/XMLSchema xmlns:soap= "http://schemas.xmlsoap org / soap/envelope/ <soap: Body> {ConsultaGuiaRequest xmlns="http:/ /wWw.prefeitura sp.gov br/nfe"> <VersaoSchema>l</VersaoSchema> <MensagenXML> INCLUIR AQUI MENSAGEM XMI CONFORMES ITEM III< MensagenXML> </consultaGuiaRequest> soap: Body> soap: Envelope>
```

## Retorno:

```
<?xl version="1 0" encoding="utf-8"?> <soap:Envelope instance xmlns:xsd="http:/ /wnwn w3 .org/ 2001/XMLSchema xmlns:soap="http:// schemas .xmlsoap org/soap/envelope/ "> <soap:Body> <Consul gov.br/nfe"> {ConsultaGuiaResult)MENSAGEM XMI DE RETORNO CONFORME ITEM IV</ConsultaGuiaResult> </consultaGuiaResponse> soap Body> soap Envelope>
```

## 4.5. TABELA DE ERROS E ALERTAS

As tabelas a seguir, apresentam os erros e alertas relacionados ao Web Service do Sistema de Notas Fiscais Eletrônicas da Prefeitura de São Paulo.

Legenda da coluna 'Onde Ocorre':

- A.  VALIDAÇÃO DO SCHEMA;
- B.  VERIFICAÇÃO DO CERTIFICADO/ASSINATURA;
- C. Envio de RPS;
- D. Envio de Lote de RPS;
- E. Teste de Envio de Lote de RPS;
- F. Consulta de NF-e;
- G.  Consulta de NF-e Recebidas;
- H. Consulta de NF-e Emitidas;
- I. Consulta de Lote;
- J. Consulta de Informações de Lote;
- K. Cancelamento de NF-e;
- L. Consulta de CNPJ;
- M.  Consulta Situação de Lote de RPS (Assíncrono);
- N. Consulta Situação Emissão de Guia (Assíncrono).

## 4.5.1. Erros

## Tabela de erros HTTP

|   Código | Descriçªo                                                                                                                          |
|----------|------------------------------------------------------------------------------------------------------------------------------------|
|      426 | Versão do TLS não suportada. Desativação gradual das versões 1.0 e 1.1 até o dia 16/03/2025. Atualize para no mínimo a versão 1.2. |

## Tabela de Erros de Schema

|   Código | Descrição                                                                                                                                    | Onde Ocorre   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|     1000 | Protocolo TLS 1.0 ou 1.1 utilizado na comunicação será desativado gradualmente até o dia 16/03/2025. Atualize para a versão 1.2 ou superior. | A             |
|     1001 | XML não compatível com Schema.                                                                                                               | A             |
|     1002 | Versão do Schema XML Incorreto.                                                                                                              | A             |
|     1050 | Rejeição: Certificado Assinatura Inválido.                                                                                                   | B             |
|     1051 | Rejeição: Certificado Assinatura Data Validade.                                                                                              | B             |
|     1052 | Rejeição: Certificado Assinatura sem CNPJ.                                                                                                   | B             |
|     1053 | Rejeição: Certificado Assinatura - Erro Cadeia de Certificação.                                                                              | B             |
|     1054 | Rejeição: Certificado Assinatura revogado.                                                                                                   | B             |
|     1055 | Rejeição: Certificado Assinatura difere ICP-Brasil.                                                                                          | B             |
|     1056 | Rejeição: Assinatura - Digest difere do calculado.                                                                                           | B             |
|     1057 | Rejeição: Assinatura difere do calculado.                                                                                                    | B             |

## Tabela de Erros de Pedido de Serviço

|   Código | Descrição                                                                                                                                                               | Onde Ocorre   |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|      104 | A Data Inicial de emissªo das Notas Fiscais enviadas nªo pode ser inferior a 01/06/2006.                                                                                | D,E           |
|      106 | A Data Final de emissªo das Notas Fiscais enviadas nªo pode ser inferior a 01/06/2006.                                                                                  | D,E           |
|      107 | A Data Final de emissªo das Notas Fiscais enviadas nªo pode ser superior a <data atual>.                                                                                | D,E           |
|      108 | A Data Final de emissªo das Notas Fiscais enviadas deverÆ ser superior a Data Inicial.                                                                                  | D,E           |
|      206 | Tipo de tributaçªo invÆlido. Para mais informaçıes consulte o item 14.20 da seçªo de perguntas e respostas.                                                             | C,D,E         |
|      207 | Data de Emissªo do RPS nªo estÆ compreendida entre <data inicio de emissªo do lote> e <data fim de emissªo do lote> conforme especificado no cabeçalho da mensagem XML. | D,E           |
|      209 | O código de serviço prestado nªo permite retençªo de ISS.                                                                                                               | C,D,E         |
|      215 | RPS em duplicidade na mensagem XML enviada. RPS: <Nœmero do RPS> SØrie: <SØrie do RPS>.                                                                                 | D,E           |
|      218 | RPS nªo poderÆ ser enviado novamente, pois estÆ incluído em Guia de Recolhimento.                                                                                       | C,D,E         |
|      219 | O campo Inscriçªo Municipal do Tomador (<Inscriçªo Municipal Tomador>) só deverÆ ser preenchido para tomadores estabelecidos no município de Sªo Paulo.                 | C,D,E         |
|      220 | CPF/CNPJ do Tomador (<CPF/CNPJ do Tomador>) possui mais de uma inscriçªo municipal, sendo obrigatório o preenchimento do campo Inscriçªo Municipal do Tomador.          | C,D,E         |
|      222 | O código de serviço informado nªo corresponde à prestaçªo de serviço.                                                                                                   | C,D,E         |
|      225 | O Valor da Alíquota deverÆ estar entre 2% e 5%.                                                                                                                         | C,D,E         |
|      240 | Nota Fiscal indicada como compra governamental, mas nªo foi especificado o ente.                                                                                        | C,D,E         |
|      241 | Nota Fiscal referenciada, nœmero {0} - verificaçªo {1}, nªo encontrada.                                                                                                 | C,D,E         |

Versão do Manual: 3

|   Código | Descrição                                                                                                                                                                                                                                                 | Onde Ocorre   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|      242 | Nota Fiscal de Tomador referenciada, nœmero {0} - verificaçªo {1}, nªo encontrada.                                                                                                                                                                        | C,D,E         |
|      243 | Ao indicar o {0}, informar uma das opçıes, CPF ou CNPJ ou NIF ou o NaoNIF.                                                                                                                                                                                | C,D,E         |
|      244 | CPF/CNPJ do {0} de Serviços invÆlido.                                                                                                                                                                                                                     | C,D,E         |
|      245 | Valor de indicador de compra governamental deve ser 0 ou 1                                                                                                                                                                                                | C,D,E         |
|      246 | Código do município do endereço do {0} deve existir na tabela do IBGE.                                                                                                                                                                                    | C,D,E         |
|      247 | Informaçıes do endereço do {0} no Brasil e no exterior nªo devem ser preenchidas concomitantemente.                                                                                                                                                       | C,D,E         |
|      248 | Valor do campo indicador de exigibilidade suspensa por decisªo judicial ou administrativa deve ser 0 ou 1.                                                                                                                                                | C,D,E         |
|      249 | Valor do campo indicador de onerosidade de prestaçªo de serviço deve ser 0 ou 1.                                                                                                                                                                          | C,D,E         |
|      250 | Valor do campo indicador de modo de prestaçªo de serviço deve ser 1 ou 2.                                                                                                                                                                                 | C,D,E         |
|      251 | Bairro do {0} nªo informado.                                                                                                                                                                                                                              | C,D,E         |
|      252 | Logradouro do {0} nªo informado.                                                                                                                                                                                                                          | C,D,E         |
|      253 | Nœmero do endereço do {0} nªo informado.                                                                                                                                                                                                                  | C,D,E         |
|      254 | Código do país do endereço do {0} no exterior nªo informado.                                                                                                                                                                                              | C,D,E         |
|      255 | Código do país do endereço do {0} no exterior invÆlido.                                                                                                                                                                                                   | C,D,E         |
|      256 | Código do país do endereço do {0} no exterior nªo pode se referir ao Brasil. Para os casos em que o domicílio do {0} estiver no Brasil, deve ser preenchido o campo de código do município do endereço do {0}.                                            | C,D,E         |
|      257 | Estado, província ou regiªo da cidade do {0} devem ser informados.                                                                                                                                                                                        | C,D,E         |
|      258 | Cidade do {0} no exterior deve ser informado.                                                                                                                                                                                                             | C,D,E         |
|      259 | Endereçamento Postal no exterior do {0} deve ser informado.                                                                                                                                                                                               | C,D,E         |
|      260 | CEP do {0} informado invÆlido.                                                                                                                                                                                                                            | C,D,E         |
|      261 | E-mail informado do {0} invÆlido.                                                                                                                                                                                                                         | C,D,E         |
|      262 | Campo motivo para a nªo informaçªo do NIF do {0} deverÆ estar entre 0 e 2.                                                                                                                                                                                | C,D,E         |
|      263 | Local de prestaçªo do serviço determinado a partir dos dados informados Ø o local do domicílio do {fornecedor / destinatÆrio / adquirente} e diverge do local de prestaçªo do serviço informado.                                                          | C,D,E         |
|      264 | O código do município ou código do país do local da prestaçªo do serviço no exterior deve ser informado, nªo sendo permitido o preenchimento de ambos os campos concomitantemente.                                                                        | C,D,E         |
|      265 | Código do município do local da prestaçªo do serviço informado invÆlido.                                                                                                                                                                                  | C,D,E         |
|      266 | Código do país onde ocorreu a prestaçªo do serviço no exterior invÆlido.                                                                                                                                                                                  | C,D,E         |
|      267 | Código do país onde ocorreu a prestaçªo do serviço no exterior nªo pode se referir ao Brasil. Para os casos em que a prestaçªo de serviço ocorrer no Brasil, deve ser preenchido o campo de código do município do local da prestaçªo do serviço no país. | C,D,E         |
|      268 | Código NBS informado invÆlido                                                                                                                                                                                                                             | C,D,E         |
|      269 | Código NCM invÆlido.                                                                                                                                                                                                                                      | C,D,E         |
|      270 | Código CIB invÆlido.                                                                                                                                                                                                                                      | C,D,E         |
|      271 | Valor do campo indicador de nota fiscal de pagamento parcelado antecipado deve ser 0 ou 1.                                                                                                                                                                | C,D,E         |
|      272 | Valor Final Cobrado nªo informado.                                                                                                                                                                                                                        | C,D,E         |
|      273 | Classificaçªo tributÆria do IBS e da CBS invÆlida.                                                                                                                                                                                                        | C,D,E         |
|      274 | Classificaçªo tributÆria secundÆria do IBS e da CBS invÆlida.                                                                                                                                                                                             | C,D,E         |
|      277 | Nªo Ø permitida a utilizaçªo da classificaçªo tributÆria informada. Caso necessÆrio, orienta-se a utilizaçªo do emissor estadual.                                                                                                                         | C,D,E         |
|      280 | Nªo Ø permitida a utilizaçªo da classificaçªo tributÆria secundÆria informada. Caso necessÆrio, orienta-se a utilizaçªo do emissor estadual.                                                                                                              | C,D,E         |

|   Código | Descrição                                                                                                                                                             | Onde Ocorre   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|      281 | Classificaçªo tributÆria do IBS e da CBS secundÆria deve indicar a classificaçªo tributÆria adequada caso os requisitos de suspensªo nªo sejam futuramente cumpridos. | C,D,E         |
|      282 | Campo classificaçªo tributÆria secundÆria nªo pode ser preenchida.                                                                                                    | C,D,E         |
|      283 | Preenchimento do campo de tipo do ente da compra governamental nªo Ø permitido.                                                                                       | C,D,E         |
|      301 | O tomador de serviços informado Ø o próprio prestador.                                                                                                                | C,D,E         |
|      302 | CNPJ do Tomador de Serviços invÆlido (dígitos verificadores nªo conferem).                                                                                            | C,D,E         |
|      303 | O Valor dos serviços deverÆ ser superior a R$ 0,00 (zero).                                                                                                            | C,D,E         |
|      304 | O Valor das deduçıes deverÆ ser inferior ao valor dos serviços.                                                                                                       | C,D,E         |
|      305 | O Valor das deduçıes deverÆ ser superior ou igual a R$ 0,00 (zero).                                                                                                   | C,D,E         |
|      306 | Código do Serviço Prestado <código enviado> do RPS inexistente.                                                                                                       | C,D,E         |
|      308 | Código do Serviço Prestado <código enviado> do RPS nªo permite deduçªo na base de cÆlculo.                                                                            | C,D,E         |
|      309 | Código do Serviço Prestado <código enviado> do RPS nªo permite tributaçªo fora do município.                                                                          | C,D,E         |
|      310 | Código do Serviço Prestado <código enviado> nªo informado.                                                                                                            | C,D,E         |
|      311 | Apenas empresas tomadoras de serviços inscritas no município ou Órgªos pœblicos podem efetuar retençªo de ISS (CPF/CNPJ = <CPF/CNPJ do Tomador>).                     | C,D,E         |
|      312 | A data da emissªo do RPS nªo foi preenchida corretamente.                                                                                                             | C,D,E         |
|      313 | A data da emissªo do RPS nªo poderÆ ser superior a data de hoje.                                                                                                      | C,D,E         |
|      314 | A data da emissªo do RPS nªo poderÆ ser inferior a 01/06/2006.                                                                                                        | C,D,E         |
|      315 | Nœmero do RPS nªo informado.                                                                                                                                          | C,D,E         |
|      317 | Campo Endereço nªo preenchido (obrigatório para tomador com CNPJ).                                                                                                    | C,D,E         |
|      318 | Campo Cidade/UF nªo preenchido (obrigatório para tomador com CNPJ).                                                                                                   | C,D,E         |
|      320 | Inscriçªo Municipal do Tomador de Serviços consta como cancelada.                                                                                                     | C,D,E         |
|      321 | Apenas Notas com tributaçªo no município ou fora do município podem sofrer retençªo de ISS.                                                                           | C,D,E         |
|      322 | O campo discriminaçªo dos serviços nªo foi preenchido.                                                                                                                | C,D,E         |
|      323 | Nota nªo pode ser cancelada. Ver detalhes no Manual.                                                                                                                  | C,D,E         |
|      324 | Operaçªo nªo autorizada por meio eletrônico em razªo de ter sido ultrapassado o prazo permitido.                                                                      | C,D,E         |
|      335 | A data da prestaçªo do serviço deverÆ estar contida no Período de VigŒncia do Código de Serviço                                                                       | C,D,E         |
|      338 | RPS nªo poderÆ ser enviado novamente. A NFS-e (<NFS-e informada>) nªo pôde ser cancelada                                                                              | C,D,E         |
|      342 | Campo CEP invÆlido                                                                                                                                                    | C,D,E         |
|      343 | CNPJ do Tomador de Serviços invÆlido (dígitos verificadores nªo conferem);                                                                                            | C,D,E         |
|      359 | Emissão por prestadores MEI não permitida desde 03/04/2023. Utilizar a Nota Fiscal de Serviços Eletrônica - NFS-e de padrão nacional.                                 | C,D,E         |
|      361 | Código do Serviço Prestado <código de atividade> nªo permitido.                                                                                                       | C,D,E         |
|      367 | Código do Serviço <código de atividade> nªo pode ser utilizado pelo prestador de serviço.                                                                             | C,D,E         |
|      372 | RPS jÆ convertido em NFS-e aceita pelo tomador ou intermediÆrio.                                                                                                      | C,D,E         |
|      373 | RPS jÆ convertido em NFS-e rejeitada com emissªo de NFTS pelo tomador ou intermediÆrio.                                                                               | C,D,E         |

|   Código | Descrição                                                                                                                                                                                                      | Onde Ocorre   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|      374 | Para serviços de construçªo civil com deduçªo na base de cÆlculo do ISS Ø obrigatório informar o nœmero de inscriçªo no Cadastro TributÆrio de Obras de Construçªo Civil.                                      | C,D,E         |
|      375 | Para serviços de construçªo civil com deduçªo na base de cÆlculo do ISS Ø obrigatório informar o nœmero de controle do encapsulamento das notas dedutíveis.                                                    | C,D,E         |
|      376 | Nœmero de inscriçªo da obra declarado na NFS-e (<Nœmero da NFS-e>) nªo confere com o nœmero de inscriçªo de obra do encapsulamento de deduçıes (<nœmero do encapsulamento>).                                   | C,D,E         |
|      377 | Valor de deduçıes declarado na NFS-e Ø menor que o valor total de deduçıes contido no encapsulamento.                                                                                                          | C,D,E         |
|      378 | Nªo declare o nœmero de inscriçªo da obra para serviços tributados fora do município de Sªo Paulo ou para exportaçªo de serviços.                                                                              | C,D,E         |
|      379 | Nœmero de inscriçªo da obra invÆlido.                                                                                                                                                                          | C,D,E         |
|      380 | Nœmero de inscriçªo da obra inexistente.                                                                                                                                                                       | C,D,E         |
|      381 | Nœmero do encapsulamento invÆlido.                                                                                                                                                                             | C,D,E         |
|      382 | Encapsulamento de notas de subempreitadas e materiais jÆ foi vinculado à NFS-e n' <nœmero da NFS-e>.                                                                                                           | C,D,E         |
|      383 | Código de serviço nªo permite indicaçªo do nœmero da obra.                                                                                                                                                     | C,D,E         |
|      384 | Nœmero de encapsulamento de deduçıes foi cancelado e nªo poderÆ ser utilizado.                                                                                                                                 | C,D,E         |
|      385 | Valor de deduçıes declarado na NFS-e Ø maior que o valor total de deduçıes do encapsulamento.                                                                                                                  | C,D,E         |
|      386 | NFS-e a ser cancelada foi selecionada para deduçıes de subempreitadas.                                                                                                                                         | C,D,E         |
|      387 | Nªo informe nœmero de encapsulamento de deduçıes para emissªo de NFS-e de empreitadas isentas ou imunes.                                                                                                       | C,D,E         |
|      388 | Data do fato gerador de uma ou mais notas de subempreitadas ou registros de materiais Ø posterior à data do fato gerador da NFS-e a ser emitida pelo prestador de serviços.                                    | C,D,E         |
|      389 | Código de serviço nªo permite indicaçªo do nœmero do encapsulamento.                                                                                                                                           | C,D,E         |
|      390 | Nœmero do encapsulamento inexistente.                                                                                                                                                                          | C,D,E         |
|      391 | Código de atividade <código informado>, nªo permite Deduçıes para o Tipo de Registro=''3'' (Cupons).                                                                                                           | C,D,E         |
|      394 | Regime de tributaçªo cadastrado pelo contribuinte foi substituído pelo Simples Nacional e nªo pode ser utilizado na emissªo de NFS-e. Previamente à emissªo, deve-se escolher o regime de tributaçªo adequado. | C,D,E         |
|      505 | CNPJ do IntermediÆrio de Serviços invÆlido (dígitos verificadores nªo conferem).                                                                                                                               | C,D,E         |
|      506 | E-mail do intermediÆrio do serviço invÆlido.                                                                                                                                                                   | C,D,E         |
|      508 | O código de serviço ({0}) nªo permite que o ISS seja retido pelo IntermediÆrio.                                                                                                                                | C,D,E         |
|      509 | IntermediÆrio nªo possui inscriçªo municipal.                                                                                                                                                                  | C,D,E         |
|      511 | Inscriçªo Municipal do IntermediÆrio especificada no arquivo nªo confere com oCNPJ informado.                                                                                                                  | C,D,E         |
|      513 | Inscriçªo do IntermediÆrio de Serviços nªo encontrada na base de dados de CCM do município.                                                                                                                    | C,D,E         |
|      514 | CNPJ do IntermediÆrio ({0}) possui mais de uma inscriçªo municipal.                                                                                                                                            | C,D,E         |
|      516 | Código de Serviço Prestado ({0}) nªo permite a identificaçªo do intermediÆrio do serviço.                                                                                                                      | C,D,E         |

|   Código | Descrição                                                                                                                                                                                  | Onde Ocorre         |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
|      519 | Para NFS-e sem identificaçªo do intermediÆrio, a NFS-e deverÆ ser emitida sem retençªo ou com retençªo pelo tomador.                                                                       | C,D,E               |
|     1100 | O CNPJ do usuÆrio autorizado a enviar a mensagem XML nªo confere com o CNPJ usado na comunicaçªo.                                                                                          | C,D,E,F,G,H,I,J,K,L |
|     1101 | Tamanho da mensagem XML ultrapassou o limite mÆximo permitido de 500 Kbytes.                                                                                                               | C,D,E,F,G,H,I,J,K,L |
|     1102 | Mensagem XML de Pedido do serviço sem conteœdo.                                                                                                                                            | C,D,E,F,G,H,I,J,K,L |
|     1105 | Lote nªo encontrado.                                                                                                                                                                       | I,J                 |
|     1106 | NF-e nªo encontrada.                                                                                                                                                                       | F                   |
|     1107 | O CPF/CNPJ da assinatura da mensagem XML nªo corresponde ao CPF/CNPJ do Prestador de Serviços.                                                                                             | C,D,E,H,I,J         |
|     1108 | O CPF/CNPJ vinculado à Inscriçªo do Tomador nªo corresponde ao CPF/CNPJ informado no campo CPFCNPJTomador.                                                                                 | C,D,E               |
|     1109 | CPF/CNPJ invÆlido.                                                                                                                                                                         | C,D,E,G,H,L         |
|     1110 | Nªo foi possível processar a requisiçªo, por favor, envie novamente para uma nova tentativa.                                                                                               | M,N                 |
|     1111 | Lote nªo possui informaçıes para a emissªo de nota.                                                                                                                                        | M,N                 |
|     1112 | O lote causou muitos erros e foi descartado.                                                                                                                                               | M,N                 |
|     1113 | Guia assíncrona - <Mensagem específica de erro>.                                                                                                                                           | N                   |
|     1201 | Só Ø permitido o envio de RPS emitidos por um œnico Prestador de Serviços (mesma inscriçªo municipal).                                                                                     | D,E                 |
|     1202 | Prestador de Serviços nªo encontrado no Cadastro Municipal (CCM).                                                                                                                          | D,E                 |
|     1203 | Total de RPS nªo confere com o enviado (<total de RPS enviados no arquivo>).                                                                                                               | D,E                 |
|     1204 | Valor Total de Serviços nªo confere com o enviado (<somatório do valor dos serviços presentes no arquivo>).                                                                                | D,E                 |
|     1205 | Valor Total de Deduçªo nªo confere com o enviado (<somatório do valor das deduçıes presentes no arquivo>).                                                                                 | D,E                 |
|     1206 | Assinatura Digital do RPS incorreta.                                                                                                                                                       | C,D,E               |
|     1207 | Prestador de Serviços nªo autorizado a emitir NF-e.                                                                                                                                        | C,D,E               |
|     1208 | A Inscriçªo Municipal do Prestador de Serviços consta como cancelada. Emissªo de NFS-e nªo autorizada.                                                                                     | C,D,E               |
|     1212 | NFS-e não permite indicação de imunidade. CCM do prestador não cadastrado por meio do sistema de declaração de imunidades (SDI) para a data do fato gerador informada.                     | C,D,E               |
|     1213 | NFS-e não permite indicação de imunidade. Código de serviço informado na NFS-e não cadastrado por meio do sistema de declaração de imunidades (SDI) para a data do fato gerador informada. | C,D,E               |
|     1222 | Obrigatório informar o município onde o serviço foi prestado.                                                                                                                              | C,D,E               |
|     1223 | Para serviço tributado em São Paulo ou exportação de serviços não informe o município onde o serviço foi prestado.                                                                         | C,D,E               |
|     1225 | Município onde o serviço foi prestado inexistente.                                                                                                                                         | C,D,E               |
|     1227 | O prestador de serviços deverá registrar a solicitação de imunidade por meio do sistema de declaração de imunidades (Instrução Normativa no. XX/2014).                                     | C,D,E               |
|     1228 | Exportação de serviços não permite a indicação de retenção pelo tomador ou pelo intermediário.                                                                                             | C,D,E               |
|     1229 | Cadastro Específico do INSS (CEI) inválido.                                                                                                                                                | C,D,E               |
|     1232 | O município de São Paulo foi informado como Município da Prestação mas o serviço é tributado fora de São Paulo.                                                                            | C,D,E               |
|     1233 | NFS-e não permite indicação de imunidade ou isenção para profissional autônomo                                                                                                             | C,D,E               |
|     1236 | Código de serviço não permite a indicação de imunidade objetiva                                                                                                                            | C,D,E               |
|     1234 | Código do Serviço Prestado {0} não permite indicação do número do Cadastro Especifico do INSS (CEI)                                                                                        | C,D,E               |

|   Código | Descrição                                                                                                                                                                                                                                                     | Onde Ocorre   |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|     1254 | Prestador, tomador, código de serviço e/ou tipo de benefício fiscal não cadastrados por meio do Sistema de Gestão de Benefícios Fiscais (GBF) para a data de prestação informada. Para mais informações, clique aqui.                                         | C,D,E         |
|     1255 | Prestador, tomador, código de serviço e/ou tipo de benefício fiscal não cadastrados por meio do Sistema de Gestão de Benefícios Fiscais (GBF) para a data de prestação informada. Para mais informações, clique aqui.                                         | C,D,E         |
|     1256 | A isenção cadastrada no Sistema de Gestão de Benefícios Fiscais (GBF) para o prestador de serviços está vinculada a um CNPJ de tomador diferente do informado, para a data de prestação de serviço informada.                                                 | C,D,E         |
|     1259 | A NFS-e gerada com código de serviço específico para os serviços de diversões públicas é facultativa, sendo necessário que o recolhimento do ISS relativo a esta prestação de serviço seja realizado segundo as regras do Sistema de Diversões Públicas - SDP | C,D,E         |
|     1303 | Só Ø permitido o cancelamento de NF-e emitidas por um œnico Prestador de Serviços (mesma inscriçªo municipal).                                                                                                                                                | J             |
|     1304 | Erro ao cancelar NF-e.                                                                                                                                                                                                                                        | J             |
|     1305 | Assinatura de cancelamento da NF-e incorreta.                                                                                                                                                                                                                 | J             |
|     1306 | A NF-e que se deseja cancelar nªo foi gerada via Web Service.                                                                                                                                                                                                 | J             |
|     1401 | Só é permitido consultar NF-e emitidas por um único Prestador de Serviços (mesma inscrição municipal).                                                                                                                                                        | F             |
|     1402 | O CPF/CNPJ da assinatura da mensagem XML não tem acesso ao Tomador de Serviços informado.                                                                                                                                                                     | G,H           |
|     1403 | As datas informadas compreendem um período maior que o permitido. O período não pode abranger mais que 31 dias.                                                                                                                                               | G,H           |
|     1404 | A Inscrição Municipal do Prestador de Serviços não consta na base de dados.                                                                                                                                                                                   | J             |
|     1417 | O preenchimento do CNPJ ou do CCM do intermediário implica a obrigatoriedade do preenchimento do campo ISS Retido Intermediário.                                                                                                                              | C,D,E         |
|     1418 | O preenchimento do ISSRetidoIntermediário implica a obrigatoriedade do preenchimento do CNPJ ou do CCM do Intermediário.                                                                                                                                      | C,D,E         |
|     1419 | Se o intermediário for informado, o campo ISS Retido pelo tomador deve ser preenchido com 'false'.                                                                                                                                                            | C,D,E         |
|     1421 | Valor do parâmetro ISS intermediário não é um valor válido.                                                                                                                                                                                                   | C,D,E         |
|     1422 | ISS não pode ser retido pelo tomador e pelo intermediário.                                                                                                                                                                                                    | C,D,E         |
|     1613 | NFS-e não permite a indicação de isenção parcial para profissional autônomo                                                                                                                                                                                   | C,D,E         |
|     1614 | NFS-e não permite a indicação de isenção parcial para Sociedade de Profissionais                                                                                                                                                                              | C,D,E         |
|     1615 | A indicação de isenção parcial (D) somente é permitida para serviços com data de fato gerador a partir de {0}.                                                                                                                                                | C,D,E         |
|     1616 | Pessoa física não pode ser responsável tributário                                                                                                                                                                                                             | C,D,E         |
|     1630 | Código de serviço (<código de serviço informado no registro>) não permite indicação de Valor Total Recebido.                                                                                                                                                  | C,D,E         |
|     1631 | Quando informado, o valor do campo Valor Total Recebido deverá ser maior ou igual ao do campo Valor Total do Serviço.                                                                                                                                         | C,D,E         |
|     1633 | Os campos Valor Total Recebido e Valor Total das Deduções não podem ser preenchidos simultaneamente.                                                                                                                                                          | C,D,E         |

## 4.5.2. Alertas

## Tabela de Alertas

|   Código | Descrição                                                                                                                                                                                                                    | Onde Ocorre   |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|      208 | Alíquota informada (<valor da alíquota>) difere da alíquota vigente (<valor da alíquota vigente>) para o código de serviço informado (<código de atividade>). O sistema irá adotar a alíquota vigente.                       | C,D,E         |
|      211 | A inscrição municipal do tomador (<Inscrição Municipal do Tomador>) não foi encontrada na base de dados de CCM.                                                                                                              | C,D,E         |
|      214 | Cidade/UF informada (<cidade do Tomador>)/(<UF do Tomador>) não foi encontrada na base de dados.                                                                                                                             | C,D,E         |
|      216 | RPS já foi convertido individualmente em NF-e através do site e não será processado novamente.                                                                                                                               | C,D,E         |
|      217 | RPS reenviado. A NF-e (<número da NF-e>) referente ao RPS (Número: <número do RPS >, Série: <séria do RPS >) foi cancelada e uma nova NF-e foi emitida.                                                                      | C,D,E         |
|      221 | O CNPJ informado (<CNPJ>) possui inscrição municipal em São Paulo, porém foi informado endereço de fora do município (<cidade/UF>).                                                                                          | C,D,E         |
|      301 | O tomador de serviços informado é o próprio prestador.                                                                                                                                                                       | C,D,E         |
|      307 | <código de atividade> da NFS-e não está cadastrado para o prestador de serviço.                                                                                                                                              | C,D,E         |
|      337 | Dígitos verificadores do CPF do Tomador de Serviços não conferem. Não haverá geração de crédito.                                                                                                                             | C,D,E         |
|      515 | O intermediário de serviços informado é o próprio prestador.                                                                                                                                                                 | C,D,E         |
|     1251 | O código de serviço e o tipo de isenção do ISS deverão ser declarados pelo prestador ou tomador de serviços, conforme o caso, por meio do Sistema de Gestão de Benefícios Fiscais (GBF). Para mais informações, clique aqui. | C,D,E         |
|     1252 | O código de serviço e o tipo de isenção do ISS deverão ser declarados pelo prestador ou tomador de serviços, conforme o caso, por meio do Sistema de Gestão de Benefícios Fiscais (GBF). Para mais informações, clique aqui. | C,D,E         |
|     1253 | A isenção cadastrada no Sistema de Gestão de Benefícios Fiscais (GBF) para o prestador de serviços está vinculada a um CNPJ de tomador diferente do informado, para a data de prestação de serviço informada.                | C,D,E         |
|     1301 | NF-e já cancelada em <data de cancelamento>.                                                                                                                                                                                 | K             |
|     1302 | NF-e em duplicidade na mensagem XML enviada.                                                                                                                                                                                 | K             |
|     1405 | Não há nenhuma Inscrição Municipal vinculada ao CPF/CNPJ informado.                                                                                                                                                          | L             |
|     1612 | Isenção Parcial (D): Conforme legislação vigente, os benefícios fiscais não podem implicar em uma alíquota efetiva inferior a 2%                                                                                             | C,D,E         |

## 5. Arquivos de Exemplos

Para obter exemplos das mensagens XML para todos os pedidos e retornos, acesse:

- a) NFS-e emitidas até 22/02/2015 (Serviços síncronos)

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/exemplos-xml-v01-0.zip

- b) NFS-e emitidas a partir de 23/02/2015 (Serviços síncronos) https://nfpaulistana.prefeitura.sp.gov.br/arquivos/exemplos-xml-v01-1.zip
- c) Serviços Assíncronos

https://nfpaulistana.prefeitura.sp.gov.br/arquivos/exemplos-assincrono-v01-1.zip

## 6. Atualizações ( Changelog )

| Manual versão   | Atualizado                                                                                                                                                                                                                                                                                                          | Data        |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 2.7.8           | Inclusão do campo DataFatoGeradorNFe no tipo tpNFe                                                                                                                                                                                                                                                                  | Junho/2024  |
| 3.2             | Inclusão dos campos referente à Reforma Tributária 2026, para isso foi criada a versão 2.0 dos XSDs. São os mesmos campos da versão anterior, adicionados os campos da Reforma Tributária. Verificar o tpRPS (complemento para a versão 2.0 dos XSDs), que contém os campos adicionados para a versão 2.0 dos XSDs. | Agosto/2025 |