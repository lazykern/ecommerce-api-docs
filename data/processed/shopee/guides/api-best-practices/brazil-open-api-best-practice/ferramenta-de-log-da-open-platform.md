A Shopee Open Platform possui uma ferramenta de log, que disponibiliza para o desenvolvedor o acesso aos logs dos últimos 7 dias do seu **partner_id** que já está em produção (Live). Atualmente, é possível consultar os dados dos logs a partir de 20 de Setembro de 2022.

  
 

## **Acesso aos Logs da API**

 

Acesse a ferramenta [**clicando aqui**](<https://open.shopee.com/console/tools/api-access-log>).

 

  1. Podem ser consultados os logs da API correspondente ao seu Live Partner dos últimos sete dias, se as solicitações retornaram sucesso ou não;
  2. Poderá verificar no log os parâmetros da request/response, os códigos de status e outras informações da API que foi chamada;
  3. Suporta pesquisa rápida através do request_id da sua chamada, dessa forma poderá encontrar com precisão o log pelo request_id que foi retornado no parâmetro de resposta da API;
  4. Suporta pesquisa por palavra-chave, por exemplo, pode ser inserido na busca a string de order_sn, ou mensagem de erro para procurar nos logs;
  5. Abrir um chamado de forma rápida, basta clicar no botão **Raise a Ticket** do lado direito da lista do log, e todas as informações relevantes serão copiadas automaticamente para o formulário de abertura de ticket;
  6. Visualizar a documentação da API rapidamente, basta clicar no botão **View API Detail** do lado direito da lista do log, e a documentação da API será aberta em uma nova página.



 

## **Abertura de chamado através da ferramenta de log da API**

 

1) Selecione o partner_id que deseja verificar os logs;

2) Caso possua o request_id, basta copiar o request_id no campo **Request ID**. Caso não possua o request_id da chamada, basta utilizar a palavra-chave que deseja procurar no campo **Keywords** ;

3) O campo **API Path** pode ser utilizado para filtrar as chamadas no seu histórico de logs;

4) O campo **Request Time (UTC-03:00)** pode ser utilizado para filtrar as chamadas pelo intervalo de datas;

5) Clique em **Search** ;

6) Clique em **Raise a Ticket** ;

7) Você será redirecionado para o nosso formulário de abertura de chamado, já com as informações mais relevantes, como: 

 

  1. Developer Email;
  2. L1 Question Category;
  3. L2 Question Category;
  4. Partner ID
  5. API Version
  6. API Category
  7. API Name
  8. Request 
  9. Response
  10. Request ID



 

8) Basta preencher o campo **Question Description** com a sua dúvida; 

 

![](https://cf.shopee.sg/file/d96688f74afed4b5b63176b1da8a0ecb)

 

9) Caso necessário, você poderá anexar arquivos relevantes para a abertura desse ticket, basta adicionar na seção **File** ;

 

![](https://cf.shopee.sg/file/d56ba816031e5b837a66f4fd68f868df)

 

10) Após preencher, clique em **Submit** e complete o Captcha;

11) Seu chamado terá sido submetido com sucesso.

 

## **Acesso aos Logs de Push**

 

Acesse a ferramenta [**clicando aqui**](<https://open.shopee.com/console/tools/push-log>).

 

  1. Podem ser consultados os logs de Push correspondente ao seu Live Partner dos últimos sete dias, se o push retornou com sucesso ou não;
  2. Se as mensagens não foram enviadas com sucesso, será enviado o motivo na mensagem de erro.



 

**Existem três situações em que o push não é bem sucedido:**

 

**1) Sem resposta da url de callback, mensagem de erro: "** Shopee has sent the push to your callback url, but we didn't get any response with 2xx code within the requested timeout seconds, please check your service."

 

**2) Recebemos uma resposta com um código que não é 2xx, mensagem de erro:** "Shopee has sent the push to your callback url, but the response code we got from your callback url is not 2xx, please check your service."

 

**3) Outros motivos, mensagem de erro:** "System error."

 

É possível pesquisar por palavra-chave, por exemplo, pode ser inserido na busca a string de order_sn, ou mensagem de erro para procurar nos logs de Push.

 

Lembre-se de preencher todos os campos obrigatórios (campos marcados com *):

 

  1. Partner ID;
  2. Push Mechanism;
  3. Send Time (UTC-03:00) - alterar para a data desejada (disponível log dos últimos 7 dias);
  4. Send Result.



 

Caso opte por buscar por uma palavra-chave específica, basta utilizar o campo **Keywords** , por exemplo a order_sn, e depois basta clicar em **Search**. A lista de logs de push e suas informações aparecerão nos resultados.