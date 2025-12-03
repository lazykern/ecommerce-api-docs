## **Autorização de loja**

Na Shopee, para que um App (criado no[ **Open Platform Console**](<https://open.shopee.com/myconsole/management/app>)) possa ter acesso aos dados de uma loja pela API, é preciso que ela dê autorização à esse App.

Para isso, **crie um link de autorização seguindo as regras abaixo** , forneça ele ao vendedor e oriente ele a autorizar. Este link deve ser colocado na interface do seu sistema para a conveniência do vendedor

 

## **1.1) Como criar a URL de autorização de loja?**

.A URL deve ser criada seguindo o padrão: **host + path + partner id + timestamp + redirect url + sign**.

  * **Host**
  *  _Ambiente Live: 'https://partner.shopeemobile.com'_
  * _Ambiente de Teste: 'https://partner.test-stable.shopeemobile.com'_
  * **Path:** '/api/v2/shop/auth_partner'
  * **Partner id:** id encontrado nos[ **detalhes**](<https://open.shopee.com/myconsole/management/app>) do seu App;
  * **Timestamp:** uint32, válido por 5 minutos;
  * **Redirect url:** essa será a página em que o vendedor será redirecionado depois de completar a autorização;
  * **Sign:** string criptografada gerada seguindo as regras do próximo item.



Confira o exemplo abaixo: 

  * **Ambiente Live** :[ **https://partner.shopeemobile.com/api/v2/shop/auth_partner?partner_id=844010 &timestamp=1615240504&redirect=https://shopee.com.br&sign=5f60ea34c2c395d3c9de03f8c3b23d4ddfce9ab237f3dd8ec1273492b0574056**](<https://partner.shopeemobile.com/api/v2/shop/auth_partner?partner_id=844010&timestamp=1615240504&sign=5f60ea34c2c395d3c9de03f8c3b23d4ddfce9ab237f3dd8ec1273492b0574056&redirect=https://shopee.com.br>)
  * **Ambiente de Teste:**[ **https://partner.test-stable.shopeemobile.com/api/v2/shop/auth_partner?partner_id=844010 &timestamp=1615240504&redirect=https://test-stable.shopee.com.br&sign=5f60ea34c2c395d3c9de03f8c3b23d4ddfce9ab237f3dd8ec1273492b0574056**](<https://partner.shopeemobile.com/api/v2/shop/auth_partner?partner_id=844010&timestamp=1615240504&sign=5f60ea34c2c395d3c9de03f8c3b23d4ddfce9ab237f3dd8ec1273492b0574056&redirect=https://shopee.com.br>)



## **1.2) Como gerar o sign de autorização de loja?**

Para calcular o Sign, crie uma string com 'partner_id+ path+timestamp' (nessa ordem e os mesmos usados na construção da url)  \- Ex: XXX/api/v2/shop/auth_partner1659992253

Criptografe essa string usando HMAC-SHA256 e o partner key encontrado nos detalhes do seu App como chave.

 

**Exemplo:** Ferramenta online que consegue encriptar a mensagem com algoritmo HMAC-SHA256:[ **https://codebeautify.org/hmac-generator**](<https://codebeautify.org/hmac-generator>)

Basta preencher os campos de forma correta.

**Exemplo de código em Python::** Código utilizado no "pre-request" do Postman, para gerar o sign:
    
    
    // Define partner_id
    
    pm.environment.set("partnerId",XXXX);
    
    
    
    
    //set timestamp
    
    vardate=newDate(); //generate timestamp
    
    vartime=parseInt(date.getTime()/1000); //decrease the size of timestamp
    
    pm.environment.set("currentTime", time); //set timestamp on environment variable
    
    
    
    
    //define path
    
    pm.environment.set("path",'/api/v2/shop/auth_partner');
    
    
    
    
    //define secret key to encrypt
    
    pm.environment.set("key",bc123339c962718c49dc8362c9eb73836bc881d5f0fbf1002b89947bf738dc55);
    
    
    
    
    // string_base = partnerId+path+timestamp - define string encrypt
    
    varstring_base=pm.environment.get("partnerId")+pm.environment.get("path")+pm.environment.get("currentTime");
    
    
    
    
    //call library
    
    varCryptoJS=require("crypto-js");
    
    
    
    
    //hmac encrypt partnerId+path+timestamp and set it as "sign" variable
    
    varsign=CryptoJS.HmacSHA256(encrypt,pm.environment.get("key")).toString(CryptoJS.enc.Hex);
    
    
    

 

 Apos isso, é possivel gerar o link de autorização utilizando os seguintes parâmetros: host + path + partner_id + redirect url + timestamp + sign:

[https://partner.shopeemobile.com/api/v2/shop/auth_partner](<https://partner.shopeemobile.com/api/v2/shop/auth_partner>)?partner_id=XXXX&&redirect=[https://www.shopee.com.br/](<https://www.google.com/>)[&timestamp=1659992253&sign=bc123339c962718c49dc8362c9eb73836bc881d5f0fbf1002b89947bf738dc55](<https://www.baidu.com/&timestamp=1594897040&sign=90c12d3932f3826f0c72242e1ec6492eec9a1298658f41f7a9469664801c4e5a>)

 

## **1.3) Fazendo a autorização de loja**

A URL de autorização expira em 5 minutos (devido à expiração do timestamp), após o qual você precisa gerar uma nova URL. 

Depois de clicar na URL de autorização, o vendedor terá 3 minutos para selecionar 'BR' e inserir o username e senha da loja na Shopee.

**⚠️ Atenção!**

  * Se ele não fizer login a tempo, será retornado um erro de "operation overtime" e o vendedor precisará abrir uma nova url (ao invés de atualizar a página).



Depois de fazer login, o vendedor será redirecionado para uma tela de confirmação de todos os acessos que o seu App terá na loja dele. O vendedor deverá clicar em 'Confirm Authorization'.

Em seguida, o vendedor será redirecionado para a url que você colocou no parâmetro 'redirect'. 

  * **Code:** usado para obter o access token, só pode ser usado uma vez e é válido por 10 minutos. Caso o access token não seja obtido em 10 minutos, é preciso que o vendedor faça esse processo de novo para gerar outro code;
  * **Shop id:** id da loja que autorizou o seu App.



Exemplo: 

  * **Ambiente Live** :[ **https://sua_url.com.br/?code=b5207f56565418145879f76398498 &shop_id=399772507**](<https://shopee.com.br/?code=b5207f56565418145879f76398498&shop_id=399772507>)
  * **Ambiente de Teste** :[**https://test-stable.sua_url.com.br/ code=b5207f56565418145879f7637d54684 &shop_id=1258**](<https://test-stable.shopee.com.br/?code=b5207f56565418145879f7637d54684&shop_id=1258>)



 

## **2)GetAccessToken**

Use essa chamada POST com o code e shop_id recebido na autorização de loja para obter o access_token e o refresh_token.

 O access_token é dinâmico e válido por 4 horas, para atualizar o access_token, basta utilizar a chamada ao RefreshAccessToken. A imagem abaixo demonstra como funciona fluxo de criação e uso do Access Token.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=3WhXEEybQEkbDHUyXoiPhvOjVc3MO8P%2FELaW9NhT2QXNZnFqfjWtZCREkirCwKDOZkDopxaJS%2B%2BBNkBGdqTdGg%3D%3D&image_type=jpg)

1 - Informação necessária para a chamada ao GetAccessToken:

**Parâmetro**| **Exemplo**| **Descrição/Detalhes**  
---|---|---  
Host| [https://partner.shopeemobile.com](<https://partner.shopeemobile.com/>)| Live environment  
[https://partner.test-stable.shopeemobile.com](<https://partner.test-stable.shopeemobile.com/>)| Test-stable/Sandbox environment  
Partner_id| XXXX| Informação disponível na Open Platform > Console > APP  
Shop_id| XXXX| Shop_id da loja que autorizou o APP.  
Path| /api/v2/auth/token/get|    
Secret Key  
 | Live Key| Live environment. Informação disponível na Open Platform > Console > APP - Live key  
Test Key| Test-Stable/Sandbox environment. Informação disponível na Open Platform > Console > APP - Test key  
Sign| bc123339c962718c49dc8362c9eb73836bc881d5f0fbf1002b89947bf738dc55| String criptografada: HMAC-SHA256  
Code| 6c4b4f544f7a416c6x4b6e6e734b7168| Gerado após a autorização da loja ao APP.  
  
2 - Criar a string base para gerar o sign com a seguinte sequência de valores: partner_id + path + timestamp

Ex: XXX/api/v2/auth/token/get1659992253

3 - Exemplo de cURL para chamada ao GetAccessToken (ambiente de teste/sandbox):
    
    
    curl --location --request POST
    
    'https://partner.test-stable.shopeemobile.com/api/v2/auth/token/get?partner_id=XXXX&timestamp=1659992253&sign=bc123339c962718c49dc8362c9eb73836bc881d5f0fbf1002b89947bf738dc55 \
    
    --header 'Content-Type: application/json' \
    
    --data-raw '{
    
    "code": "6c4b4f544f7a416c6x4b6e6e734b7168",
    
    "shop_id": XXXX,
    
    "partner_id": XXXX
    
    }'

  * **Code** : usado para obter o access token, só pode ser usado uma vez e é válido por 10 minutos. Caso o access token não seja obtido em 10 minutos, é preciso que o vendedor faça esse processo de novo para gerar outro code;
  * **Shop id** : id da loja que autorizou o seu App;
  * **Partner id** : id encontrado nos[ **detalhes**](<https://open.shopee.com/myconsole/management/app>) do seu App.



 

4 - Exemplo de resposta para a chamada ao GetAccessToken:
    
    
    {
    
    "refresh_token":"525745615465726cxxx1444d416c5859",
    
    "access_token":"6a555055544c7974xxxx0616e79664e73",
    
    "expire_in":14384,
    
    "request_id":"9930ba006b1153xxxxxx4b34aae0e52",
    
    "error":"",
    
    "message":""
    
    }

  * **access_token** : pode ser usado mais de uma vez, válido por 4 horas;
  * **expire_in** : depois de quantos segundos o access_token deixará de ser válido;
  * **refresh_token** : só pode ser usado uma vez e é válido por 30 dias. É usado na chamada RefreshAccessToken para atualizar o access_token.



## **3.1)RefreshAccessToken**

 

Depois que o access_token expirar, atualize utilizando a chamada ao RefreshAccessToken, a chamada irá gerar um novo set de access_token e refresh_token válidos. 

O novo refresh_token deve ser utilizado na próxima chamada para essa API para que um novo set de tokens seja gerado. 

Além disso, o refresh_token pode ser utilizado, apenas, uma única vez e tem v**alidade de 30 dias**. Caso o novo refresh_token seja perdido ou tenha passado de sua validade, deverá realizar a autorização da loja novamente.

 

1 - Informação necessária para a chamada ao RefreshAccessToken:

**Parâmetro**| **Exemplo**| **Descrição/Detalhes**  
---|---|---  
Host  
 | [https://partner.shopeemobile.com](<https://partner.shopeemobile.com/>)| Live environment  
[https://partner.test-stable.shopeemobile.com](<https://partner.test-stable.shopeemobile.com/>)| Test-stable/Sandbox environment  
Partner_id| XXXX| Informação disponível na Open Platform > Console > APP  
Shop_id| XXXX| Shop_id da loja que autorizou o APP.  
Path| /api/v2/auth/access_token/get|    
Secret Key  
 | Live Key| Live environment.Informação disponível na Open Platform > Console > APP - Live key  
Test Key| Test-Stable/Sandbox environment. Informação disponível na Open Platform > Console > APP - Test key  
refresh_token  
 | bc123339c962718c49dc8362c9eb73836bc881d5f0fbf1002b89947bf738dc55| String criptografada: HMAC-SHA256  
525745615465726cxxx1444d416c5859| Gerado na chamada do GetAccessToken, ou na última chamada ao RefreshAccessToken.  
  
2 - Criar a string base para gerar o sign com a seguinte sequência de valores: partner_id + path + timestamp

Ex: XXX/api/v2/auth/access_token/get1659992253

 

3 - Exemplo de URL para chamada ao RefreshAccessToken (ambiente de teste/sandbox):
    
    
    curl --location --request POST
    
    'https://partner.test-stable.shopeemobile.com/api/v2/auth/access_token/get?partner_id=XXXX&timestamp=1659992253&sign=bc123339c962718c49dc8362c9eb73836bc881d5f0fbf1002b89947bf738dc55 \
    
    --header 'Content-Type: application/json' \
    
    --data-raw '{
    
    "refresh_token": "525745615465726cxxx1444d416c5859",
    
    "shop_id": XXXX,
    
    "partner_id": XXXX
    
    }

  * **Refresh token** : só pode ser usado uma vez e é válido por 30 dias.
  * **Shop id** : id da loja que autorizou o seu App.
  * **Partner id** : id encontrado nos[ **detalhes**](<https://open.shopee.com/myconsole/management/app>) do seu App.



 

4 - Exemplo de resposta para a chamada ao RefreshAccessToken:
    
    
    {
    
    "partner_id":XXXX,
    
    "refresh_token":"724a5045557axxx42704d774d4e4b62",
    
    "access_token":"686b624c737xxx171774c6f75677046",
    
    "expire_in":14400,
    
    "request_id":"XXXX",
    
    "error":"",
    
    "message":"",
    
    "shop_id":XXXX
    
    }

  * **access_token** : pode ser usado mais de uma vez, válido por 4 horas;
  * **expire_in** : depois de quantos segundos o access_token deixará de ser válido;
  * **refresh_token** : só pode ser usado uma vez e é válido por 30 dias.



## **Entenda os erros mais comuns retornados na chamada ao GetAccessToken**

**1 - Error message: "Invalid code".**

a. Motivo: Ocorre, geralmente, quando o código enviado já foi utilizado antes. 

b. Parâmetro: code

c. Solução: Gerar um novo código através do processo de autorização, ou utilizar o código correto.

**2 - Error message: "Invalid partner id".**

a. Motivo: Ocorre quando o partner id utilizado não é válido. 

b. Parâmetro: partner_id

c. Solução: Verificar o partner id que está sendo utilizado na chamada.

**3 - Error message: "Invalid shop id".**

a. Motivo: Ocorre quando o shop id utilizado não corresponde com a loja que gerou o código. 

b. Parâmetro: shop_id

c. Solução: Verificar o shop id que está sendo utilizado na chamada.

**4 - Error message: "Invalid timestamp".**

a. Motivo: Timestamp já passou da validade de 5 minutos. 

b. Parâmetro: timestamp

c. Solução: Utilizar um timestamp dentro da sua validade (5 minutos).

**5 - Error message: "Wrong sign.".**

a. Motivo: O sign gerado está incorreto, geralmente o path na hora de gerar o sign está incorreto. 

b. Parâmetro: sign

c. Solução: Verificar se o path na montagem da string do sign está correto: "/api/v2/auth/token/get".

**6 - Error message: "No permission. Please inform seller to complete the Seller Registration on Shopee Seller Center first, then this shop can call for this API.".**

a. Motivo: O vendedor ainda não finalizou o cadastro na Central do Vendedor. 

b. Parâmetro: N/A

c. Solução: Solicitar ao vendedor que finalize o cadastro correspondente ao shop id na Central do Vendedor.

## **Erros mais comuns retornados na chamada ao RefreshAccessToken**

**1 - Error message: "Your refresh_token expired."**

a. Motivo: Ocorre, geralmente, quando o refresh_token já expirou, ele tem validade de 30 dias. 

b. Parâmetro: refresh_token

c. Solução: Caso não tenha um refresh_token novo, deverá realizar o procedimento de autorização novamente.

**2 - Error message: "Invalid refresh_token."**

a. Motivo: Ocorre quando o refresh_token utilizado não é válido, geralmente o refresh_token já foi utilizado anteriormente, ele é um token de uso único.

b. Parâmetro: refresh_token

c. Solução: Verificar se o refresh_token utilizado é o token gerado mais recente. Deve sempre utilizar o último gerado.

**3 - Error message: "Partner and shop has no linked."**

a. Motivo: Ocorre quando o shop_id utilizado na chamada não está conectado com o partner_id. 

b. Parâmetro: shop_id e partner_id

c. Solução: Verificar o shop id e o partner id que estão sendo utilizados na chamada.

**4 - Error message: "This shop account has been banned. Permissions for shop authorization and API calls have been suspended until the shop account is restored."**

a. Motivo: Loja está banida. 

b. Parâmetro: N/A

c. Solução: Verificar status da loja com o seller.

**5 - Error message: "Wrong sign."**

a. Motivo: O sign gerado está incorreto, geralmente o path na hora de gerar o sign está incorreto. 

b. Parâmetro: sign

c. Solução: Verificar se o path na montagem da string do sign está correto: "/api/v2/auth/access_token/get".

**6 - Error message: "No permission. Please inform seller to complete the Seller Registration on Shopee Seller Center first, then this shop can call for this API."**

a. Motivo: O vendedor ainda não finalizou o cadastro na Central do Vendedor. 

b. Parâmetro: N/A

c. Solução: Solicitar ao vendedor que finalize o cadastro correspondente ao shop id na Central do Vendedor.

**7 - Error message: "error params".**

a. Motivo: Request body/payload com nome de parâmetro incorreto. 

b. Parâmetro: refresh_token, shop_id, partner_id

c. Solução: Verificar qual dos parâmetros utilizado no request está incorreto e corrigir.