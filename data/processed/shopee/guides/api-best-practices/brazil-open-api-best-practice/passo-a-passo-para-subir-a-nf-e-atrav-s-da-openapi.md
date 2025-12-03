Na Shopee, para vendedores CNPJ é necessário que seja adicionado a Nota Fiscal no pedido, exceto para pedidos com o parceiro logístico que não tem suporte a Nota Fiscal, como por exemplo o Correios.

 

## **Dados Necessários do Comprador para Emissão de NF-e**

 

Os dados podem ser obtidos através do endpoint [**v2.order.get_order_detail**](<https://open.shopee.com/documents/v2/v2.order.get_order_detail?module=94&type=1>)**** com os valores indicados no parâmetro "response_optional_fields". No entanto, para aprimorar nossas políticas de proteção de dados, desde o dia 28 de Dezembro, os dados serão mascarados conforme:

 

**1\. Vendedor CPF:**

  1. Disponibilizado apenas o "Endereço" do comprador, para orders com status "READY_TO_SHIP", "PROCESSED" e "RETURN/REFUND" na API ("TO_SHIP" e ˜R/R˜ no Seller Center).
  2. "Nome", "Número" de "telefone" e "CPF" do Buyer não será disponibilizado em nenhum status da order, pois não é necessário;



 

 

![](https://down-br.img.susercontent.com/br-11134141-7r98o-lncwzappgq1b20)

 

**2\. Sellers CNPJ:**

  1. Disponibilizados “Nome”, “Endereço” e “CPF” do buyer para orders com status “INVOICE_PENDING”, “READY_TO_SHIP”, “PROCESSED” e “RETURN/REFUND˜ na API (“TO_SHIP” e “R/R” no Seller Center)
  2. O “telefone” do Buyer não será disponibilizado em nenhum status da order, pois não é necessário;



 

 

![](https://down-br.img.susercontent.com/br-11134141-7r98o-lncwzll7jtm18e)

 

Essa nova regra não deve afetar os atuais fluxos da order pois os dados não são obrigatórios para nenhuma etapa do processo.

 

## **Cálculo para Emissão de NF-e**

 

Os valores para emissão da NF podem ser obtidos através do endpoint [**v2.payment.get_scrow_detail**](<https://open.shopee.com/documents/v2/v2.payment.get_escrow_detail?module=97&type=1>) como no cálculo abaixo:

 

_**Valor total da NF = "original_price" - "seller_discount" - "discount_from_voucher_seller" + "buyer_paid_shipping_fee"**_

 

Lembrando que isso é apenas uma das formas de calcular o valor da NF, caso seu time Fiscal apresente outra forma, não necessariamente estará incorreta.

 

## Verificando pedidos que precisam da NF-e

 

1\. Chamar o endpoint [**v2.order.get_order_list**](<https://open.shopee.com/documents/v2/v2.order.get_order_list?module=94&type=1>) e passar o parâmetro opcional "order_status" com o valor "INVOICE_PENDING", dessa forma será retornado uma lista de pedidos que precisam ter a NF-e adicionada antes da organização de envio do pedido.

 

Ex de chamada em cURL:

 
    
    
    curl --location --request GET 'https://partner.shopeemobile.com/api/v2/order/get_order_list?partner_id=XXXX&timestamp=XXXX&access_token=XXXX&shop_id=XXXX&sign=XXXXXXXXXXXX&time_range_field=XXXX&time_from=XXXX&time_to=XXXX&page_size=100&order_status=INVOICE_PENDING' \
    
    --data-raw ''

 

Ex de response:

 
    
    
    {
    
    "error":"",
    
    "message":"",
    
    "response":{
    
    "more":false,
    
    "next_cursor":"",
    
    "order_list":[
    
    {
    
    "order_sn":"22002XXXXXXXX"
    
    },
    
    {
    
    "order_sn":"22003XXXXXXXX"
    
    },
    
    {
    
    "order_sn":"22001XXXXXXXX"
    
    }
    
    ]
    
    },
    
    "request_id":"XXXXXXXX"
    
    }

 

2\. Para verificar se a NF-e já está atrelada ao order_sn, basta utilizar o endpoint [v2.order.get_order_detail](<https://open.shopee.com/documents/v2/v2.order.get_order_detail?module=94&type=1>), com o parâmetro opcional: "response_optional_fields": "invoice_data" e a order_sn, dessa forma será retornado na response o objeto "invoice_data". 

 

Ex de chamada em cURL:

 
    
    
    curl --location --request GET 'https://partner.shopeemobile.com/api/v2/order/get_order_detail?partner_id=XXXXX&timestamp=XXXXX&access_token=XXXXX&shop_id=XXXXX&sign=XXXXX&order_sn_list=22002XXXXXXXX&response_optional_fields=invoice_data' \
    
    --header 'Content-Type: application/json' \
    
    --data-raw ''

 

a) Caso a order_sn já possua a invoice, então será retornado um objeto com os valores da NF-e.

 

Ex de response, order_sn com NF-e:

 
    
    
    {
    
    "error":"",
    
    "message":"",
    
    "response":{
    
    "order_list":[
    
    {
    
    "cod":false,
    
    "create_time":1662490093,
    
    "currency":"BRL",
    
    "days_to_ship":2,
    
    "invoice_data":{
    
    "number":"000000XXX",
    
    "series_number":"00X",
    
    "access_key":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    
    "issue_date":1662492013,
    
    "total_value":100,
    
    "products_total_value":100,
    
    "tax_code":"5101"
    
    },
    
    "message_to_seller":"",
    
    "order_sn":"22002XXXXXXXX",
    
    "order_status":"READY_TO_SHIP",
    
    "prescription_check_status":null,
    
    "region":"BR",
    
    "reverse_shipping_fee":0,
    
    "ship_by_date":1662606000,
    
    "update_time":1662492365
    
    }
    
    ]
    
    },
    
    "request_id":"e631c3f1b4fe93a54a696a3229xxxxxx"
    
    }

 

b) Caso a order_sn ainda não possua a invoice, então será retornado um objeto vazio, uma vez que ainda não consta os valores da NF-e em nosso sistema.

 

Ex de response, order_sn sem NF-e:

 
    
    
    {
    
    "error":"",
    
    "message":"",
    
    "response":{
    
    "order_list":[
    
    {
    
    "cod":false,
    
    "create_time":1663009716,
    
    "currency":"BRL",
    
    "days_to_ship":2,
    
    "invoice_data":{},
    
    "message_to_seller":"",
    
    "order_sn":"22002XXXXXXXX",
    
    "order_status":"READY_TO_SHIP",
    
    "prescription_check_status":null,
    
    "region":"BR",
    
    "reverse_shipping_fee":0,
    
    "ship_by_date":0,
    
    "update_time":1663009855
    
    }
    
    ]
    
    },
    
    "request_id":"c8691da53612d1bc8ee5bb97dxxxxxx"
    
    }

 

**⚠️ Nota**

  1. O status do pedido retornado no v2.order.get_order_detail, não é alterado depois de chamar a API add_invoice_data, tanto as orders que ainda não possuem a NF-e adicionada, quanto as orders que já possuem a NF-e adicionadas, vão apresentar o "order_status":"READY_TO_SHIP". O status apenas é modificado na API v2.order.get_order_list, para o parâmetro de filtro (INVOICE_PENDING)



 

## **Adicionando o Invoice**

 

Com a order_sn no status INVOICE_PENDING, ou após validar se a order tem Invoice_data, então pode-se usar a seguinte API para upload de invoice:

 

-[**v2.order.upload_invoice_doc**](<https://open.shopee.com/documents/v2/v2.order.upload_invoice_doc?module=94&type=1>) para subir um arquivo XML, onde os parâmetros são:

  1. **order_sn:** valor retornado na chamada anterior (v2.order.get_order_list)
  2. **file_type:** o tipo de arquivo, que para XML é “4”;
  3. **file:** que deve ser adicionado o caminho (ou “Path) do arquivo XML;



 

Ex de chamada em cURL:

 
    
    
    curl --location 'https://partner.shopeemobile.com/api/v2/order/upload_invoice_doc?partner_id=XXXXXX&timestamp=1682618933&access_token=XXXXXXXXXXXXXXXX&shop_id=XXXXXXX&sign=XXXXXXXXXXXXXX’ \
    
    --header 'Content-Type: application/json' \
    
    --form 'file=@"path/to/file"' \
    
    --form 'order_sn="2304278N5XXXXXXX"' \
    
    --form 'file_type="4"

 

Nota: Solicitamos que essa API seja chamada com um delay de 5 minutos após a criação da NF-e. Por conta da nova validação na SERPRO, é necessário que a NF-e esteja válida no sistema deles.

 

## **Entenda os erros que podem ser retornados pela api de upload de NF**

 

**1\. Error message: "**_**Wrong parameters, detail: Invalid CNPJ. The access key CNPJ must be the same as the registration.."**_

**a. Motivo:** Ocorre quando o CNPJ cadastrado em nosso sistema Shopee, não é o mesmo CNPJ emissor da nota fiscal que está sendo adicionada ao pedido. 

**b. Solução:** Emitir a NF-e com o mesmo CNPJ cadastrado na Shopee; ou verificar o CNPJ cadastrado na Shopee e fazer as devidas correções.

 

**2\. Error message: "**_**Wrong parameters, detail: Invalid UF. The access key UF must be the same as the registration.."**_

**a. Motivo:** Ocorre quando o estado do CNPJ emitente da nota fiscal não corresponde com o estado do seller cadastrado na Shopee.

**b. Solução:** Emitir a NF-e com o mesmo estado cadastrado na Shopee; ou verificar o estado cadastrado na Shopee e fazer as devidas correções.

 

**3\. Error message: "**_**Wrong parameters, detail: Invalid State Registration Number. The NF-e State Registration Number must be the same as the registration.."**_

**a. Motivo:** Ocorre quando a inscrição estadual do emitente da nota fiscal não corresponde com inscrição estadual do seller cadastrado na Shopee.

**b. Solução:** Emitir a NF-e com a mesma inscrição estadual cadastrada na Shopee; ou verificar a inscrição estadual cadastrada na Shopee e fazer as devidas correções.

 

**4\. Error message:**_**"Wrong parameters, detail: Don't support Invoice Issuer now, please switch Shop Default to upload invoice.."**_

**a. Motivo:** Ocorre quando o seller escolheu o emissor de NF Shopee. (Shopee Invoice Issuer) 

**b. Solução:** Entrar na Central do Vendedor em "Shop > Shop Profile > Invoice Setting > Edit > Other"

 

**5\. Error message: "**_**Wrong parameters, detail: Invalid NF-e."**_

**a. Motivo: NF-e não é válida.**

**b. Solução:** Adicionar uma nota fiscal válida. Caso a NF-e seja válida mas acabou de ser gerada, aguarde 5 minutos para que adicione a chave de acesso novamente.

 

**6\. Error message: "**_**Wrong parameters, detail: Canceled NF-e."**_

**a. Motivo:** NF-e cancelada.

**b. Solução:** Adicionar uma NF-e que não esteja cancelada.

 

**7\. Error message: "**_**Access Key duplicated, please do not use duplicated Access Key."**_

**a. Motivo:** NF-e já foi utilizada em outra order.

**b. Solução:** Adicionar uma NF-e que ainda não foi utilizada.

 

**8\. Error message: "**_**Wrong parameters, detail: access_key must be 44 characters in length."**_

**a. Motivo:** Chave de acesso adicionada contém menos ou mais dígitos do que o da NF-e válida.

**b. Solução:** Verificar a chave de acesso se está corretamente com os 44 dígitos.

 

**9\. Error message: "**_**Wrong parameters, detail: access_key is a required field."**_

**a. Motivo:** Request enviado sem a chave de acesso (access_key).

**b. Solução:** Adicionar a chave de acesso no request da chamada.

 

**10\. Error message: "**_**Wrong parameters, detail: Invalid issue date. The NF-e issue date cannot be greater than the current date.."**_

**a. Motivo:** A data de emissão da nota fiscal é maior que a data atual. Exemplo: data de emissão 20 de Agosto de 2022, data atual 18 de Agosto de 2022.

**b. Solução:** Adicionar uma NF-e com a data correta.

 

**11\. Error message: "**_**Wrong parameters, detail: The invoice status is invalid to upload invoice data."**_

**a. Motivo:** O pedido está atrelado a um parceiro logístico que não suporta NF-e (ex: Correios); ou o pedido já está cancelado.

**b. Solução:** Caso o pedido seja de um parceiro logístico que não suporta NF-e, basta organizar o envio da order através do endpoint v2.logistics.ship_order. Para pedidos cancelados, não tem correção.

 

**12\. Error message: "**_**Wrong parameters, detail: Invalid access key.."**_

**a. Motivo:** Chave de acesso é inválida.

**b. Solução:** Subir uma chave de acesso válida. 

 

**13\. Error message: "**_**Wrong parameters, detail: order_sn is a required field."**_

**a. Motivo:** Request sem o parâmetro order_sn.

**b. Solução:** Adicionar o parâmetro order_sn na request.

 

**14\. Error message:**_**"Invalid NF-e model. Only model 55 is accepted."**_

**a. Motivo:** "mod" do XML enviado diferente de 55

**b. Solução:** gerar uma NF apenas com o mod 55

 

**15\. Error message:**_**"CFOP invalid, please confirm it"  **_

**a. Motivo:** CFOP não aceito pela Shopee

**b. Solução:** os únicos CFOPs válidos são 6108, 6102, 5102, 6107, 6101, 5101, 5405, 6404, 6403, 6106, 5403, 5106, 6104, 6109, 6115, 6103, 6105, 6401, 5115, 6120, 5103, 5105, 5104, 5109, 6402, 5120, 6118, 5401, 5402, 5112, 5114, 6112, 5117, 6117, 5118, 6113, 6114, 6119, 5111, 6123, 6116, 5116, 5119, 5113, 6111;

 

**16\. Error message:**_**"Please upload a valid Invoice XML file"**_

**a** _**.**_**Motivo:  **Enviar um arquivo sem o formato correto do XML

**b. Solução:** Enviar arquivo formato correto (como gerado pelo seu emissor);

 

**17\. Error message:**_**"File Error"**_

**a** _**.**_**Motivo:  **Arquivo XML não contém a tag "<?xml version=“1.0” encoding=“UTF-8"?>"

**b. Solução:** Inserir a tag mencionada acima no seu arquivo XML, ou enviar NF via Seller Center (vale ressaltar que essa validação não será mais necessária a partir de 1º de Abril de 2024),