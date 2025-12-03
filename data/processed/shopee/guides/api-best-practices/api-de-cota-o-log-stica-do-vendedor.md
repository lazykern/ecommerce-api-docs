# O que é o canal Logística do vendedor 

 

Este canal permite que o vendedor utilize sua própria logística para cotação e envio de pedidos.

  * A cotação de frete é feita a partir da URL de cotação disponibilizada pelo vendedor.
  * O preço de envio e prazo de entrega são fornecidos pelo próprio vendedor.
  * O rastreamento dos pedidos é simplificado, ficando sob responsabilidade do vendedor enviar os eventos de “despachado”, “entrega” ou “falha na entrega” via OpenAPI.



 

_**Obs:** Este canal será disponibilizado a vendedores específicos, cujos produtos não são suportados pela logística própria da Shopee por conta de dimensões e peso, de acordo com as regras estabelecidas pelo time comercial da Shopee._

# URL Cotação de frete

 

É a ferramenta que permite ao vendedor enviar para a Shopee o custo do frete e prazo estimados que serão exibidos ao comprador no momento da compra. Para que o vendedor possa utilizar esse recurso, é preciso atender os requisitos de homologação pré-estabelecidos.

 

_*O vendedor tem a opção de integrar diretamente com a Shopee para conectar sua URL de cotação ou se conectar via um Integrador-HUB._

# Requisitos para homologação/Integração

 

Diferente dos outros tipos de integração, a integração da API de cotação e atualização de status de pedido (do canal seller logistics), exigem uma avaliação e aprovação do time Shopee antes de começar a operar. Para ser aprovado pelo time da Shopee é necessário:

  * Cumprimento do contrato da API de cotação de frete:
    * Configurar e disponibilizar a URL via método HTTP POST.
    * Cada solicitação (request) deve conter apenas um item de um vendedor.
    * A URL não tem uma estrutura específica, proporcionando flexibilidade na configuração.
  * Payload padrão da requisição e resposta de cotação (e validação com URL da Shopee)
  * Tempo de resposta limite de 400ms.
  * Tabela de contingência cadastrada diretamente pela Central do Vendedor.
  * Monitoramento de erros (e desenvolvimento das mensagens solicitadas)
  * Desenvolvimento API de atualização de status (“update_tracking_status);
    * _**Obs:** Os requisitos acima devem ser cumpridos pelo “próprio sistema” do vendedor ou pelo seu ERP/HUB/Integração. Vale ressaltar que sem eles os pedidos serão cancelados, pois o fluxo não pode ser realizado via Central do Vendedor de forma manual._
    * _**Obs2:** Todos que desenvolverem a API de cotação, também devem desenvolver a API de atualização de status;_
    * _**Obs3:** O APP Seller Logistics, só é usado para URL de cotação, para usar qualquer API é necessário a criação de um segundo APP;_
  * Passar e-mail de confirmação e aprovação do time da Shopee [via ticket](<https://open.shopee.com/myconsole/ticket-system/raise-ticket/>) (envolvendo todos critérios acima).



 

Para conseguir realizar a integração e os testes acima também é necessário:

a) Criar novo APP Seller Logistic na Open Platform e autorizar os sellers a esse APP

b) Ter um APP que seja capaz de chamar a OpenAPI para atualização de status (e também autorizar os sellers a esse APP)

 

_**Uma vez com todos esses passos realizados, será necessário a criação de pelo menos 2 pedidos testes, que precisarão ser conduzidos até os status de entregue e cancelado, para liberação do HUB como um canal aprovado.**_

# Criar APP Seller Logistics e autorizar sellers 

 

Uma vez que sua conta na Open Platform já esteja ativa, o próximo passo é criar um APP que será usado apenas para conectar sua URL de cotação a Shopee e respectivos sellers(shop_Id).

Segue passo a passo, abaixo:

 

1\. Fazer Login na Open Platform e entrar na aba “Console”:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=8dhYhblm%2FlT3sEGKh5synM1mGE7qxTcXnRgX2qr%2B1miAs7MhkfJsLepUtX9XcStrTyRmX8aOWC4yvGKBV5i8xw%3D%3D&image_type=png)

 

2\. Em “App List” clicar em “+ Add new APP”:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=BtBro5U%2BNrU9jHhAb9RpFjJ5GmTfZqPTiLaPOlBFOyv9S%2F0Zf7azJkPoAco%2FHbK%2FTQgZ6r1%2FKdLXgGAQeQ0e4g%3D%3D&image_type=png)

 

3\. Selecionar a “App Category” como “Seller Logistics”:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Sv5yW4Y%2F8xvWECI296njkyyMjHqfNJaml2ZchYPSi5ic5qHWFrc1mw82SkGGdApJMehI7pUOwUA8xZHDQ%2Bjg7A%3D%3D&image_type=png)

 

4\. Inserir no “App Description” as URLs que serão usadas em Live (produção) e em Test (ambiente de teste), e clicar em “Submit”.

*sem problemas se houver apenas uma URL;

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=SDzAxRWWV3Jw3M0LHU1vrMW%2Fgu%2BpMgu%2F5UN5AuvACe1nV1%2BsWSaUR4C5KdjUgBUn3jXkuceu8fFoAIr8jxLSPg%3D%3D&image_type=png)

 

5\. Assim o APP já estará criado, então, só seguir com a solicitação de “Go-Live”, que vai disponibilizar o APP no ambiente de produção em até 24 horas.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=i%2BNnpU4d3%2Fg81BlB643wC1WpAsWxeqG7xK11%2BryzeFpzTWPYYVq3yxEvYPJzZ7V%2FaaV4Lxfc%2Fgl13VC6UOPDGg%3D%3D&image_type=png)

 

6\. Só é necessário preencher mais algumas infos antes.

Caso não seja possível fornecer um “username” e “password”, podem preencher como no print abaixo:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=So38FJiibg0jTVT62sS8PvZkMtpb7PfayVf1b12SxUrLazGJdYSkQgPZZv9VLJ512Q22KMRKQzAyG8Pg3JgkKg%3D%3D&image_type=png)

 

7\. Para “App IP”, informar o IP principal da sua aplicação (vale ressaltar que não vamos limitar o acesso apenas a esse IP).

E para “Other IT Assets Declaration”, preencher como no print abaixo.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Jx8ukNF5yojqAm6sTTwJvtqVwqyHDDzmLg%2FpY7003hPkLDzXbxUrwBIZBStYDNxWmS0AITs8W9E2GlK3nWi2fQ%3D%3D&image_type=png)

 

24 horas após a solicitação do “Go-live” o partner_id de Live será liberado e você será notificado via e-mail. Assim que receber o e-mail, os próximos passos são:

 

1 - Abrir um ticket na [_Plataforma de Tickets da OP_](<https://open.shopee.com/myconsole/ticket-system/raise-ticket/>), com o assunto “Seller Logistics” informando o shop_id (ou quais Shop IDs) pretende conectar a sua URL, assim que recebermos a solicitação e o time da Shopee finalizando a conexão da URL, e permitindo avançar com a autorização do seller.

Obs: cada shop_id só pode estar conectado a uma URL aqui na Shopee;

 

2 - Realizar o fluxo de autorização para o seu seller, conforme passo a passo do [_link_](<https://open.shopee.com/developer-guide/20>) (até o tópico 4 do “Autorizando com uma conta de loja”).

 

3 - Assim que o time da Shopee responder seu ticket, confirmando que a configuração foi feita e seu seller realizar o fluxo de autorização, já será possível realizar os primeiros testes em LIVE.

##  

## Payload padrão da requisição e resposta de cotação

### Parâmetros da requisição (query)

 

URL Request Parameters:

-| Exemplo| HTTP Address  
---|---|---  
URL| https://api.frete/| URL fornecida pelo ERP ou seller  
Nome| Tipo| Exemplo| Descrição  
---|---|---|---  
partner_id| int| 1| O ID do parceiro é atribuído após o registro ser bem-sucedido. Obrigatório para todas as solicitações.  
timestamp| timestamp| 1610000000| Indica o carimbo de data/hora da solicitação. Obrigatório para todas as solicitações. Expira em 5 minutos.  
sign| string| e318d3e932719916a9f9ebb57e2011961  
bd47abfa54a36e040d050d8931596e2| Assinatura gerada pela base string "{}{}{}"%(parnter_id, api full path, timestamp) e partner_key via algoritmo HMAC-SHA256. Mais detalhes: [_https://open.shopee.com/documents?module=87 &type=2&id=58&version=2_](<https://open.shopee.com/documents?module=87&type=2&id=58&version=2>)   
  
 

Body Request Parameters:

Nome| Tipo| Obrigatório| Exemplo| Descrição  
---|---|---|---|---  
shop_id| int| True| 112345678| Identificador único de cada vendedor  
origin_zip_code| string| True| 12345000| CEP do vendedor com 8 dígitos, apenas números sem ponto e traço  
destination_zip_code| string| True| 12345000| CEP do comprador com 8 dígitos, apenas números sem ponto e traço  
items| array| True| -| Lista de produtos  
 | item_id| int| True| 12345678| Identificação do item na Shopee  
 | sku| string| False| item_sku| SKU cadastrado pelo seller na Shopee  
 | model_id| int| False| 12345678| Identificação do modelo cadastrado na Shopee._**Obs:** nas cotações da PDP, o model_id e category_id são enviados como zero, mas na página de checkout são enviamos normalmente_.  
 | category_id| int| True| 12345678| Categoria do item cadastrada na Shopee._**Obs:** nas cotações da PDP, o model_id e category_id são enviados como zero, mas na página de checkout são enviamos normalmente_  
 | quantity| int| True| 12345678| Quantidade de itens  
 | price| float| False| 150.4| Preço do produto  
 | dimensions| object| True| -| Dimensões do produto  
 |  | length| int| True| 10| Comprimento em centímetros  
 |  | width| int| True| 10| Largura em centímetros  
 |  | height| int| True| 10| Altura em centímetros   
 |  | weight| int| True| 100| Peso em gramas  
  
 

Response Parameters / Resposta da Cotação (erro):

Nome| Tipo| Obrigatório| Exemplo| Descrição  
---|---|---|---|---  
error| string| True| -| Identificador da cotação realizada pelo seller  
message| string| True| -| CEP do comprador   
request_id| string| True| -| Identificador da cahamada da API  
  
 

Response Parameters / Resposta da Cotação (sucesso):

Nome| Tipo| Obrigatório| Exemplo| Descrição  
---|---|---|---|---  
quotation_id| int| True| 091234000| Identificador da cotação realizada pelo seller  
destination_zip_code| string| True| 091234000| CEP do comprador   
packages| array| True| -| Lista de pacotes  
 | dimensions| object| True| -| Dimensões do produto  
 |  | length| int| True| 10| Comprimento em centímetros  
 |  | width| int| True| 10| Largura em centímetros  
 |  | height| int| True| 10| Altura em centímetros  
 |  | weight| int| True| 100| Peso em gramas  
 | items| array| True| -| lista de produtos  
 |  | item_id| int| True| 12345678| Identificação do item na Shopee  
 |  | sku| string| False| sku_item| SKU cadastrado pelo seller na Shopee  
 |  | model_id| int| False| 12345678| Identificação do modelo cadastrado na Shopee  
 |  | category_id| int| False| 12345678| Categoria do item cadastrada na Shopee  
 |  | quantity_id| int| True| 2| Quantidade de itens  
 |  | price| int| True| 150.4| Preço do produto  
 |  | dimensions| object| True| -| Dimensões do produto  
 |  |  | length| int| True| 10| Comprimento em centímetros  
 |  |  | width| int| True| 10| Largura em centímetros  
 |  |  | height| int| True| 10| Altura em centímetros  
 |  |  | weight| int| True| 100| Peso em gramas  
 | quotations| array| True| -| Lista de cotações de frete  
 |  | price| float| True| 150.4| Valor do frete exibido ao comprador  
 |  | handling_time| int| True| 20| Tempo de preparação do pedido em dias úteis. Sempre deve ser maior ou igual a 1.Esse tempo limita o tempo de emissão de NF e organização de envio do vendedor.  
 |  | shipping_time| int| True| 10| Tempo de transporte do pedido em dias úteis  
 |  | promise_time| int| True| 30| Somatório do tempo de preparação + tempo de transporte  
 |  | service_code| string| True| M1020| Código que identifica a transportadora no contexto do vendedor (código irá retornar no parâmetro “shipping_carrier” na API get_order_detail, ex: “Logística do Vendedor - M1020”.)  
  
### Exemplo de requisição
    
    
    curl --location 'https://api.frete/?partner_id=123456&sign=6b664c45535a544455524f6b565776706752784455784978574361444e795a4c&timestamp=1709843385' \
    --header 'Content-Type: application/json' \
    --data '{
        "shop_id": 601216389,
        "origin_zip_code": "87952525",
        "destination_zip_code": "17036785",
        "items": [
            {
                "item_id": 892569034,
                "model_id": 1,
                "sku": "",
                "category_id": 1,
                "quantity": 1,
                "price": 12.5,
                "dimensions": {
                    "length": 1,
                    "width": 1,
                    "height": 1,
                    "weight": 150
                }
            }
        ]
    }'

### Exemplo de retorno (sucesso)

 

  * Usar HTTP status code 200


    
    
    {
        "quotation_id": 1709843321,
        "destination_zip_code": "17036785",
        "packages": [
            {
                "dimensions": {
                    "length": 35,
                    "width": 90,
                    "height": 114,
                    "weight": 27300
                },
                "items": [
                    {
                        "item_id": 892569034,
                        "model_id": 1,
                        "sku": "",
                        "category_id": 1,
                        "quantity": 1,
                        "price": 12.5,
                        "dimensions": {
                            "length": 1,
                            "width": 1,
                            "height": 1,
                            "weight": 150
                        }
                    }
                ],
                "quotations": [
                    {
                        "price": 93.55,
                        "handling_time": 1,
                        "shipping_time": 7,
                        "promise_time": 8,
                        "service_code": "50"
                    }
                ]
            }
        ]
    }

### Exemplo de retorno (erro)

 

  * Usar HTTP status code 403


    
    
    {
        "request_id": "Id da requisição",
        "error": "coluna Error",
        "message": "coluna Message"
    }

### Retorno padrão para erros não mapeados na tabela de erros

 

  * Usar HTTP status code 500


    
    
    {
        "request_id": "65e9e26dd9d2565e9e26dd9d64",
        "error": "Internal system error",
        "message": "internal system error"
    }

### Códigos de retorno esperados

**HTTP status code**| **Error**| **Message**| **Ativa****Contingência**  
---|---|---|---  
200| success API call, error Empty| success API call, error Empty| False  
403| error_partner_id| there is no partner_id in query| False  
403| error_partner_id| partner_id is invalid| False  
403| error_ sign| there is no sign in query| False  
403| error_ sign| your sign is invalid| False  
403| error_timestamp| there is no timestamp in query| False  
403| error_timestamp| your timestamp is invalid| False  
403| error_ shop_id| there is no shop_id in body| False  
403| error_ shop_id| The shop_id is invalid| False  
403| Invalid origin_zip_code| The origin_zip_code is invalid| False  
403| invalid destination_zip_code| The destination_zip_code is invalid| False  
403| error_destination_zip_code| No shipping channel is available.| False  
403| Invalid item_id| The item_id is invalid| False  
403| Invalid model_id| The model_id is invalid| False  
403| Invalid sku| The sku is not valid| False  
403| invalid category_id| The category_id is invalid| False  
403| invalid quantity| The quantity is invalid| False  
403| invalid price| The price is invalid| False  
403| error_dimensions| The dimensions is invalid| False  
403| error_length| The length is invalid| False  
403| error_width| The width is invalid| False  
403| error_height| The height is invalid| False  
403| error_weight| The weight is invalid| False  
500| Internal system error| internal system error| True  
  
 

### Validação dos responses (com URL da Shopee)

  * Para garantir que o response está no formato esperado, temos uma URL que deve ser usada para validar e informar as correções necessárias.
  * URL: "https://seller-quotation-api.uat.shps-br-services.com/validate_quotation_endpoint"
  * Dentro do parâmetro "x-quotation-id" deve ser usado para inserir a URL que será cadastrada na Shopee.
  * Segue payload de exemplo de como utilizar a URL de validação do formato de response:


    
    
    curl --location 'https://seller-quotation-api.uat.shps-br-services.com/validate_quotation_endpoint' \
    --header 'api-key: 8a50d1d005d0649b5bdd9b13f0e871e0bd6439bd8e146577a6d51935a5ccea7c' \
    --header 'x-partner-id: 2007416' \
    --header 'x-quotation-api-url: https://api.cotação/shopee' \
    --header 'x-sign: 658ABD0FD8D8525C0A87B0E360A5C518C2987E5B4A3D20542A4B11594E11CE53' \
    --header 'Content-Type: application/json' \
    --data '{
        "shop_id": 549724933,
        "origin_zip_code": "16200850",
        "destination_zip_code": "16200850",
        "items": [
            {
                "item_id": 10010394,
                "sku": "10010394",
                "model_id": 1,
                "category_id": 1,
                "quantity": 1,
                "price": 277.67,
                "dimensions": {
                    "length": 1,
                    "width": 1,
                    "height": 1,
                    "weight": 10
                }
            }
        ]
    }'

 

  * Segue response sem erros (pode ser identificado quando o parâmetro "validation_errors" estiver vazio ("validation_errors:[]"):


    
    
    {
        "validation_errors": [],
        "details": {
            "called_api": "https://api.cotação/shopee",
            "with_params": {
                "sign": "658ABD0FD8D8525C0A87B0E360A5C518C2987E5B4A3D20542A4B11594E11CE53",
                "partner_id": 2007416,
                "timestamp": 1713445311
            },
            "with_body": {
                "shop_id": 549724933,
                "origin_zip_code": "16200850",
                "destination_zip_code": "16200850",
                "items": [
                    {
                        "item_id": 10010394,
                        "model_id": 1,
                        "sku": "10010394",
                        "category_id": 1,
                        "quantity": 1,
                        "price": 277.67,
                        "dimensions": {
                            "length": 1,
                            "width": 1,
                            "height": 1,
                            "weight": 10
                        }
                    }
                ]
            },
            "response_from_quotation_api": {
                "status_code": 200,
                "response_body": {
                    "quotation_id": 617788888,
                    "destination_zip_code": "16200850",
                    "packages": [
                        {
                            "dimensions": {
                                "length": 1,
                                "width": 1,
                                "height": 1,
                                "weight": 10
                            },
                            "items": [
                                {
                                    "item_id": 10010394,
                                    "sku": "10010394",
                                    "model_id": 1,
                                    "category_id": 1,
                                    "quantity": 1,
                                    "price": 277.67,
                                    "dimensions": {
                                        "length": 1,
                                        "width": 1,
                                        "height": 1,
                                        "weight": 10
                                    }
                                }
                            ],
                            "quotations": [
                                {
                                    "price": 34.9,
                                    "handling_time": 5,
                                    "shipping_time": 10,
                                    "promise_time": 20,
                                    "service_code": "2018605604"
                                }
                            ]
                        }
                    ]
                },
                "method_called": "POST"
            }
        }
    }

 

  * Segue response com exemplo de erros a serem corrigidos:


    
    
    {
        "validation_errors": "Input should be a valid string: ('error',)",
        "details": {
            "called_api": "https://api.cotação/shopee": {
                "sign": "658ABD0FD8D8525C0A87B0E360A5C518C2987E5B4A3D20542A4B11594E11CE53",
                "partner_id": 2007416,
                "timestamp": 1713472133
            },
            "with_body": {
                "shop_id": 549724933,
                "origin_zip_code": "16200850",
                "destination_zip_code": "16200850",
                "items": [
                    {
                        "item_id": 10010394,
                        "model_id": 0,
                        "sku": "10010394",
                        "category_id": 1,
                        "quantity": 1,
                        "price": 277.67,
                        "dimensions": {
                            "length": 1,
                            "width": 1,
                            "height": 1,
                            "weight": 10
                        }
                    }
                ]
            },
            "response_from_quotation_api": {
                "status_code": 403,
                "response_body": {
                    "request_id": "17134721330005",
                    "error": 403,
                    "message": "there is no partner_id in query",
                    "msger": "Nao foi possivel concluir sua solicitacao."
                },
                "method_called": "POST"
            }
        }
    }

##  

## Tempo de resposta limite (da cotação) 

 

  * Considerando que o checkout é o momento mais crítico da experiência do usuário durante a compra, é essencial garantir a melhor experiência possível ao comprador.
  * O tempo de resposta limite é de 1s. É necessário realizar um teste de carga para garantir que essa exigência seja atendida.
  * Tempos de resposta superiores a 1s não serão permitidos, inviabilizando a integração. Dessa forma, manter a otimização desse parâmetro é fator crucial para proporcionar a melhor experiência possível ao comprador.



# Tabela de contingência 

 

  * Este recurso tem como finalidade apoiar no cálculo do frete, caso ocorra algum problema na cotação de frete via API (timeout ou retorno 500 para as requisições).



## Configurações de valor de frete para contingência

 

  * Para que a contingência funcione, é necessário que o vendedor cadastre os valores de frete e habilite o canal **Logística do vendedor** , conforme passos descritos abaixo.
  * Na Central do Vendedor, acesse **Configurações de Envio** e clique no botão **Configuração do canal** :

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=axLhajSfgEBV5VxcLQac2I4DJ819EKiVG4BaFBpeX7tyXMFC2yOiY%2FZBjpzXXh3sXL0w14jP4jGdv%2FBXysWqdw%3D%3D&image_type=png)

## Preenchimento do valor de frete de contingência

 

Em seguida, será carregada a tela para preenchimento do valor de frete. O valor de frete pode ser preenchido por estado (valor único) ou por localidade.

## Valor de frete único por estado

 

  1. Selecione os estados
  2. Preencha o campo valor do frete
  3. Clique em Salvar

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=iqTvUj9g1dDUR6lK8Pwvg8k9uw%2Fq5EE7RaMwhoFeOlbziKeMF0U%2BO8VSx0R%2BeUrSgXDYT0TDrFeS%2F%2FBQIe%2BGgg%3D%3D&image_type=png)

## Valor de frete único por cidade

 

  1. Selecione os estados
  2. Desabilite o botão _Flat rate for this area_
  3. Desmarque a opção _Select All Cities_ e selecione as cidades que deseja informar o valor do frete
  4. Preencha o campo _Rate_ das respectivas cidades
  5. Clique em _Salvar_

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=sZze5JgkTw23vTywAHTztpHkGHSM9rxVpFct3lL9NiVPSh5rmsN27ykkw4C88%2BpqFmPwPBpyKfaEKPsnrJ9OYw%3D%3D&image_type=png)

## Habilitação do canal Logística do vendedor

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=GQqkuXNOHGSpwREwhv0g2lS9mxDBBwrUyEFQCb5OQVo05wb8tAC2k7w1Cs1Jd8b6XthNygVM2H4abUA0sYKzwg%3D%3D&image_type=png)

## Prazo de entrega para valor de frete de contingência

 

  * O prazo de entrega será fixo, quando acionada a tabela de contingência:
    * Prazo mínimo: 10 dias corridos
    * Prazo máximo: 20 dias úteis



# Status dos pedidos e rastreamento 

## Desenvolvimento API de atualização de status:

 

A atualização de status dos pedidos e rastreamento se dará por meio da API de atualização de tracking e será feita com base no número do pedido criado na Shopee (ID do Pedido, também conhecido por OrderSN). No qual também será obrigatório informar o número de rastreio.

Para atualização do número do rastreio e status do pedido deve ser utilizado o endpoint _**v2.logistics.update_tracking_status (OpenAPI)**_. Os status possíveis são:

  1. Pedido Enviado (logistics_pickup_done)
     * A URL e o tracking number podem ser enviados na atualização do status do pedido para Enviado.
  2. Pedido Entregue (logistics_delivery_done)
     * O status Entregue só será recebido, caso o pedido já possua status o status Enviado.
  3. Falha na Entrega (logistics_delivery_failed)
     * O status Falha na Entrega só será recebido, caso o pedido já possua status o status Enviado.



 

_**IMPORTANTE** : após envio dos status Pedido Entregue ou Falha na Entrega não será mais permitida atualização de status, pois ambos são status finalizadores;_

_*os parâmetros**tracking_number** e **tracking_url** devem ser enviados apenas na atualização do status para **logistics_pickup_done**._

 

_Segue link para documentação da API “_[ __/api/v2/logistics/update_tracking_status__](<https://open.shopee.com/documents/v2/v2.logistics.update_tracking_status?module=95&type=1>) _”._

# Fluxo e status de pedidos do canal 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=HlNk8Kk68dG3rPlRrgb8OWB34bmSuKnrsCJ853GXcbyVIwQuLCgjCC%2Bodz65bQANuqyn3AQ1Y53h6LPXIVE3dg%3D%3D&image_type=png)

#  

# Regras de comissão e frete para o canal

 

  * O desconto máximo do frete para o comprador é de R$ 20, caso o vendedor esteja no Programa de Frete Grátis
  * O vendedor terá uma coparticipação no desconto oferecido ao cliente.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=up740NiZdB4UHEVPAFbqCvpVwa056ylU1CFeHpzc6b3gvhCcXjSAUdGiVrz2ZZQzKEyODTGilTg%2FlmU7vWLR7Q%3D%3D&image_type=png)

# FAQ:

 

1 - Todos os vendedores tem acesso ao canal Logística do Vendedor?

R: Somente vendedores gerenciados tem acesso ao canal, para mais informações procure seu Gerente de contas.

 

2 - Como identificar uma cotação no pedido?

R: Uma vez um pedido criado com uma cotação de sucesso, o parâmetro “service_code”, será retornado no parâmetro “shipping_carrier” da API get_order_detail. 

Ex1: 

  * “service_code” enviado: “Canal X”
  * retorno do parâmetro “shipping_carrier”: “Logística do vendedor - Canal X”



Ex2: 

  * Tabela de contingência ativada.
  * retorno do parâmetro “shipping_carrier”: “Logística do vendedor”



 

3 - Posso usar o APP Seller Logistics para chamar a OpenAPI?

R: Não, esse tipo de APP só é usado para API de cotação (URL de cotação).

 

Para mais dúvidas técnicas, abrir um ticket na [_Plataforma de Tickets da OP_](<https://open.shopee.com/myconsole/ticket-system/raise-ticket/>).

Para dúvidas sobre acesso ao canal logístico, segue link.