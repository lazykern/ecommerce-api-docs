## **Fluxo de order**

 

![](https://cf.shopee.sg/file/f2bfc2e016b095f9bc0325e2b3979c10)

##  

## **Identificando uma nova order**

 

Atualmente existem duas formas de identificarmos uma nova order via API:

 

**1 - Push Mechanism (Webhooks):**

 

Com o Push Mechanism ativado sempre que uma nova order for criada ou mudar de status, um novo Push será enviado para o link informado (callback URL), a qual você precisa configurar para responder de acordo com esses requisitos de resposta HTTP:

  1. Incluir código de status 2xx;
  2. Incluir um corpo vazio (método POST);



 

Atualmente é possível ativar o Push Mechanism:

 

a) API "v2.push.set_push_config": informando quais Push devem ser ativados, o Push para criação e mudança de status das orders é o "order_status":

 

  1. Segue exemplo de request:



 
    
    
    {
    
    "push_config": {
    
    "order_status": 1,
    
    },
    
    "callback_url": "www.site.com.br"
    
    }

 

b) Open Platform: faça login na Open Platform > Console > App Management > Push Mechanism > Set Push e "ligar" nesse botões abaixo os Webhooks que deseja:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=1xwkte6qdiCTaaSGeVzOHtm7u9catV5AyyGLACwSS%2F4pRM2ZYtt50Zl2ASUi8Ot8vE12gkqbY0RCESEnsVbINQ%3D%3D&image_type=jpg)

**2 - Pela API**[**v2.get_order_list:**](<https://open.shopee.com/documents/v2/v2.order.get_order_list?module=94&type=1>)

 

Chamando a API get_order_list, seu response trará todas as order_sn do ShopId e período específico;

 

  1. Inserindo o parâmetro opcional "response_optional_fields=order_status", o response também apresentará os status das orders, como no exemplo abaixo:



 

**Request:**
    
    
    curl --location --request GET
    
    'https://partner.shopeemobile.com/api/v2/order/get_order_list?timestamp=timestamp&shop_id=shop_id&partner_id=partner_id&access_token=access_token&page_size=2&response_optional_fields=order_status&time_range_field=create_time&time_from=1607235072&time_to=1608271872&sign=sign&cursor=""'

 

**Response:**
    
    
    {
    
    "error": "",
    
    "message": "",
    
    "response": {
    
    "more": true,
    
    "next_cursor":"2",
    
    "order_list": [{
    
    "order_sn": "201218V2Y6E59M",
    
    "order_status": “READY_TO_SHIP”
    
    },
    
    {
    
    "order_sn": "201218V2W2SG1E",
    
    "order_status": “PENDING_INVOICE”
    
    },
    
    ]
    
    },
    
    "request_id": "XXXXXXXXXXXXXXXXXX"
    
    }

 

## **Status das orders na OpenAPI**

 

As orders podem ter 8 diferentes status na OpenAPI:

 

**1 - UNPAID:  **

Para orders que acabaram de ser criadas e ainda não foi possível validar o pagamento.

Normalmente orders de Boleto ou Pix apresentam esse status, pois as orders de Cartão de Crédito são validadas em minutos (às vezes até segundos).

 

**2 - INVOICE_PENDING:**

Esse status atualmente aparece apenas na API [**v2.get_order_list**](<https://open.shopee.com/documents/v2/v2.order.get_order_list?module=94&type=1>) e faz referência a orders que ainda não foi informado seus dados de invoice (usado apenas para orders não Correios).

 

**3 - READY_TO_SHIP:**

Para orders Correios que já tiveram sua confirmação de pagamento, ou para orders não correios onde os dados de invoice já foram enviados com sucesso.

 

Orders nesse status estão prontas para Organização de envio ([**v2.ship_order**](<https://open.shopee.com/documents/v2/v2.logistics.ship_order?module=95&type=1>)). Lembrando que é recomendado iniciar a organização de envio (ship_order) após 1 hora da confirmação de pagamento, pois dentro desse período o Buyer pode cancelar a pedido sem aprovação do Seller.

 

**4 - PROCESSED:  **

Orders que já tiveram organização de envio (v2.ship_order) e ainda não foi gerado o tracking Number.

 

**5 - SHIPEED:**

Após o pacote ser entregue ao parceiro logístico.

 

**6 - TO_CONFIRM_RECEIVE:**

Aguardando confirmação do buyer de recebimento.

 

**7 - COMPLETED:**

Quando a order chega a seu destino final, seja ele a casa do buyer, ou nos casos de devolução, retorna ao Seller.

 

**8 - TO_RETURN:**

Status quando buyer abre a solicitação de devolução do pedido.

 

**9 - CANCELLED:**

Quando a order é Cancelada, que pode ocorrer quando o buyer cancela o pedido, quando o Seller não organiza o pedido ou quando o pedido é perdido durante a entrega.

 

Segue comparação de status entre OpenAPI e Seller Center (que também pode ser encontrada na nossa [**Documentação**](<https://open.shopee.com/developer-guide/31>)):

 

**OpenAPI**| **SellerCenter**  
---|---  
UNPAID| Não Pago  
READY_TO_SHIP| A enviar (A enviar)  
IN_CANCEL| Cancelado (A responder)  
CANCELLED| Cancelado (Cancelado)  
SHIPPED| A enviar (Processado)  
TO_RETURN| Enviado  
TO_CONFIRM_RECEIVE| Devolução Reembolso  
COMPLETED| Shipping (Shipped)  
  
 

## **Cancelamento de pedidos**

 

Para cancelamento de pedidos do lado do Seller, utilize a API [**v2.cancel_order**](<https://open.shopee.com/documents/v2/v2.order.cancel_order?module=94&type=1>) , algumas regras:

 

1 - Não é possível cancelar uma order após a organização de envio e geração do tracking_number;

 

2 - Existem 4 motivos disponíveis para cancelamento:

  1. OUT_OF_STOCK: Para quando o estoque tiver acabado (sempre que esse for o motivo é necessário o envio do array “”item_list”:[“item_id”, “model_id”]” );
  2. CUSTOMER_REQUEST: Quando o Buyer solicita e não consegue mais cancelar sem sua autorização;
  3. UNDELIVERABLE_AREA: Quando o endereço solicitado não está dentro da sua área de entrega;
  4. COD_NOT_SUPPORTED: Cash in Delivery, não disponível para o Brasil.



 

Segue exemplo de request body para cancelamento de order:

 
    
    
    {
    
    "order_sn": "201020SQQ5K2EP",
    
    "cancel_reason": "OUT_OF_STOCK",
    
    "item_list": [{
    
    "item_id": 1680783,
    
    "model_id": 327890123
    
    }
    
    ]
    
    }

 

Caso receba a mensagem de erro: 

 

"Can not cancel this order.": é porque o pedido não pode ser cancelado por já ter sido gerado seu "tracking_number", ou porque a order já foi cancelada. Qualquer situação diferente dessas duas, por gentileza nos acionar via [**Plataforma de Tickets**](<https://open.shopee.com/myconsole/ticket-system/raise-ticket/>)).

 

Já para solicitação de cancelamento de pedido do lado do buyer, utilize a API [**v2.handle_buyer_cancellation**](<https://open.shopee.com/documents/v2/v2.order.handle_buyer_cancellation?module=94&type=1>) para aceitar ou rejeitar a solicitação de cancelamento.

 

## **Dúvidas frequentes (FAQ)**

 

1 - Seguem algumas APIs que **não são usadas** para integrações no Brasil:

 

_"v2.order.split_order";_

_"v2.order.unsplit_order";_

_"v2.order.get_buyer_invoice_info";_

_"v2.order.get_pending_buyer_invoice_order_list";_

_"v2.order.upload_invoice_doc";_

_"v2.order.download_invoice_doc";_

 

**2 - Por que foi possível criar uma order se o estoque foi zerado semana passada?**

 

Existem dois cenários possíveis, um deles é que o Seller tem um estoque separado e reservado para campanhas, a outra possibilidade é que uma order antiga foi cancelada e restaurou o estoque (toda order cancelada restaura o estoque automaticamente).