**Fluxo de Chamadas na v2**

 

![](https://cf.shopee.sg/file/8dca5e13068fa92eace8a072b9146b91)

 

O fluxo de chamadas na v2 que relaciona aos canais de envio é conforme:

 

**1.** A Shopee habilita o canal de envio para o vendedor. (ex.: Correios, aberto a todos os vendedores, Total Express, Sequoia, Loggi, ShopeeXpress).

 

**2.** Para verificar o canal logístico habilitado em sua loja:

  1. Basta chamar o endpoint: v2.logistics.get_channel_list



 

**3.** O vendedor deve definir o canal logístico para cada item de acordo com o que foi liberado para ele pela Shopee:

  1. Para habilitar/desabilitar os canais de envio do produto: v2.product.add_item ou v2.product.update_item usando os params dentro de logistic_info.



 

**4.** O vendedor recebe o pedido já com o canal de envio selecionado pelo comprador.

 

**5.** Para saber se é preciso informar a NF-e para um pedido antes de fazer a organização de envio (ship_order), você pode usar a chamada v2.order.get_order_list com o param "order_status": "INVOICE_PENDING".

  1. Para informar a NF-e use a chamada v2.order.add_invoice_data.
  2. Para conferir os dados da NF-e que já foram enviados: v2.order.get_order_detail com o param "response_optional_fields": "invoice_data" e verificar o param "invoice_data".
  3. Nos casos em que for necessário, a NF-e deve ser informada antes da chamada v2.logistics.ship_order.



 

**6.** Dependendo do canal de envio selecionado pelo comprador, o vendedor irá postar o pacote ou esperar a coleta.

a) Para saber se é coleta (pickup) ou postagem (dropoff): v2.logistics.get_shipping_parameter

b) Para fazer a organização de envio do pedido: v2.logistics.ship_order

i. Se for dropoff (hoje só temos os Correios como dropoff): caso o info_needed for vazio ("dropoff": []), a request do ship_order deverá ser: 

 
    
    
    {
    
    "order_sn":"201212DCXXXXX"
    
    "dropoff":{
    
    }
    
    }

 

ii. Se for pickup (hoje todos os outros são pickup, incluindo Coleta Correios): caso o info_needed tenha "pickup": ["address_id","pickup_time_id"], a request do ship_order deverá ser:

 
    
    
    {
    
    "order_sn":"201212DCXXXXX"
    
    ,"pickup":{
    
    "address_id":pickup.address_list.address_id do get_shipping_parameter,
    
    ,"pickup_time_id": pickup.address_list.time_slot_list. pickup_time_id do get_shipping_parameter
    
    }
    
    }

 

iii. Depois disso, para obter o código de rastreio basta chamar o endpoint: v2.logistics.get_tracking_number;

 

**7.** Todas as etiquetas de envio de pedidos da Shopee devem ser geradas pela Shopee. Com o código de rastreio já gerado, para gerar a etiqueta de envio:

a) Para obter os possíveis params para gerar a etiqueta: v2.logistics.get_shipping_document_parameter

  1. A response "selectable_shipping_document_type": ["NORMAL_AIR_WAYBILL","THERMAL_AIR_WAYBILL"] informa que a etiqueta pode ser gerada respectivamente em formato .pdf ou .zip (contendo a etiqueta em um .txt em formato ZPL + PDF com a declaração de conteúdo).



 

b) Para pedir para a Shopee gerar a etiqueta de um ou mais pedidos:

  1. v2.logistics.create_shipping_document
  2. É preciso enviar o parâmetro "tracking_number".



 

c) Para saber se a etiqueta já foi gerada ou ainda está sendo processada: 

  1. v2.logistics.get_shipping_document_resultOrder com response "status": "READY" já podem ter a etiqueta obtida.



 

d) Para obter a etiqueta depois que tiver sido gerada pela Shopee:

  1. v2.logistics.download_shipping_document



 

Todos os status dos pedidos são alterados pela Shopee.

 

Mais detalhes sobre o fluxo de chamadas de pedidos pode ser encontrado em nossa documentação na seção:

"Arrange Shipment & Get TrackingNo & Print AirwayBill": <https://open.shopee.com/developer-guide/27>

 

## **FAQ**

 

  1. Todos os envios são feitos com os canais de envio (transportadoras) direto com a Shopee. 



 

  1. Na Shopee o frete é pago pelo comprador ou pela Shopee. 



 

  1. Todas as etiquetas de envio são geradas pela Shopee, um vendedor ou Integradora/ERP nunca deve gerar a etiqueta por conta própria ou alterar a etiqueta da Shopee para nenhum canal de envio. 



 

  1. Cada vendedor possui um único canal de envio, ou seja, diferentes vendedores podem ter acesso a diferentes canais de envio. 
  2. Por exemplo, o vendedor 1 tem acesso aos Correios, e o vendedor 2 possui acesso somente à Loggi. 



 

  1. A Shopee pode habilitar ou desabilitar o acesso de um vendedor a um canal de envio a qualquer momento. 



 

  1. Pedidos dos Correios não possuem a função para informar a NF-e. 



 

  1. O vendedor pode emitir a NF-e caso tenha configurado a Shopee como Invoice Issuer.



 

  1. Quando recebemos os dados da NF-e, avaliamos se: 
  2. A chave de acesso da NF-e já não foi usada em outro pedido, caso a mesma chave seja informada para mais de um pedido, ela não será aceita. 
  3. A chave de acesso da NF-e e os dados que o vendedor informou no cadastro de vendedor da Shopee (CNPJ e UF), ou nos outros campos da NF-e (série, número da NF-e, mês/ano, UF) são compatíveis. 
  4. Se a data da NF-e é posterior à data de pagamento do pedido pelo comprador. 



 

  1. A documentação e suas chamadas pode ser encontrada em: 
  2. V2: https://open.shopee.com/documents?version=2.



 

Para dúvidas ou abertura de chamados, [**clique aqui**](<https://open.shopee.com/myconsole/ticket-system/raise-ticket/>).