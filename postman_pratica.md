# Laboratório prático de Postman

Este guia acompanha a trilha do curso e transforma os conceitos em uma pequena suíte de testes. O objetivo é aprender a preparar, executar e analisar requests sem depender de backend próprio, banco de dados ou serviço pago.

## 1. Instalação

Baixe o aplicativo desktop na [página oficial de download do Postman](https://www.postman.com/downloads/). Depois de instalar, é possível usar o aplicativo sem criar uma conta para os exercícios locais. A conta e a sincronização são opcionais; o laboratório não depende delas.

Abra o Postman e crie um workspace local chamado `QA API - Estudos`. Use nomes que expliquem a intenção do teste. Uma request chamada `GET - Usuário existente` é mais útil do que uma request chamada apenas `Request 1`.

## 2. Criar uma Collection

Na barra lateral, selecione **Collections**, crie `API Training - QA` e organize as requests por API ou por fluxo. Uma organização simples é:

```text
API Training - QA/
├── JSONPlaceholder/
│   ├── GET - Post existente
│   ├── POST - Criar post
│   ├── PUT - Alterar post
│   └── DELETE - Excluir post
├── REST Countries/
│   └── GET - Buscar país
├── Reqres/
│   ├── GET - Usuários
│   └── POST - Login (token)
└── Swagger Petstore/
    ├── GET - Pet existente
    ├── POST - Criar pet
    ├── PUT - Alterar pet
    ├── DELETE - Excluir pet
    └── GET - Pet inexistente
```

Cada request deve ter método, URL, parâmetros, headers, body e testes coerentes com a documentação ou com o comportamento conhecido da API de treinamento.

## 3. Criar um Environment

Abra **Environments**, crie `Treinamento - público` e adicione variáveis. Preencha o valor inicial com os endereços abaixo e deixe o valor atual sem credenciais reais quando a API não exigir autenticação.

| Variável | Valor inicial | Uso |
| --- | --- | --- |
| `jsonplaceholderUrl` | `https://jsonplaceholder.typicode.com` | Posts e usuários simulados. |
| `reqresUrl` | `https://reqres.in` | Usuários e login de treinamento. |
| `countriesUrl` | `https://restcountries.com/v3.1` | Consulta de países. |
| `petstoreUrl` | `https://petstore3.swagger.io/api/v3` | API documentada com Swagger/OpenAPI. |
| `petId` | `1` | Identificador de estudo. |
| `token` | vazio | Será preenchido somente durante um exercício de autenticação. |

Selecione o Environment no canto superior direito. Use `{{jsonplaceholderUrl}}/posts/1` na URL, em vez de repetir o endereço completo em todas as requests.

## 4. Variáveis e escopo

Uma variável de Environment é adequada para valores que mudam entre ambientes. Uma variável de Collection é útil para compartilhar um id criado entre requests da mesma suíte. Uma variável local serve apenas para a execução atual.

Não salve senhas, tokens reais ou chaves de API em uma Collection versionada. Se uma API exigir chave, crie uma variável local ou use o mecanismo de segredo do seu ambiente de trabalho.

## 5. Requests e cenários CRUD

### JSONPlaceholder: consulta

`GET {{jsonplaceholderUrl}}/posts/1`

O JSONPlaceholder é uma API de treinamento. A consulta deve retornar status `200` e um objeto com `userId`, `id`, `title` e `body`.

### JSONPlaceholder: criação

`POST {{jsonplaceholderUrl}}/posts`

Header: `Content-Type: application/json`

```json
{
  "title": "estudo de API",
  "body": "post criado no exercício",
  "userId": 1
}
```

Espere `201` e valide que a resposta contém um `id`. A API simula a criação; não trate o recurso como persistido para um exercício posterior sem confirmar a documentação.

### JSONPlaceholder: alteração

`PUT {{jsonplaceholderUrl}}/posts/1`

```json
{
  "id": 1,
  "title": "título alterado",
  "body": "conteúdo alterado",
  "userId": 1
}
```

Espere `200` e confirme que os campos enviados aparecem na resposta.

### JSONPlaceholder: exclusão

`DELETE {{jsonplaceholderUrl}}/posts/1`

Espere `200` ou o status descrito na documentação da API utilizada. Registre o status recebido; não invente uma expectativa só porque outra API usa `204`.

### REST Countries: consulta

`GET {{countriesUrl}}/name/brazil`

Valide status `200`, uma lista no body e a presença de `name.common` e `cca2`. Esse cenário é uma boa prática para validar estrutura de resposta, não apenas status.

### Swagger Petstore: consulta e erro

Abra a [documentação Swagger Petstore](https://petstore3.swagger.io/), localize `GET /pet/{petId}` e execute:

```text
GET {{petstoreUrl}}/pet/1
```

Depois execute um id inexistente. O objetivo é comparar a resposta de sucesso e a resposta de erro conforme o contrato, registrando status, headers e body. Se o serviço responder 5xx ou estiver indisponível, registre isso como problema do ambiente/serviço e não como o erro funcional esperado do endpoint.

### Swagger Petstore: criação, alteração e exclusão

As operações abaixo demonstram o ciclo completo documentado:

```text
POST   {{petstoreUrl}}/pet
PUT    {{petstoreUrl}}/pet
DELETE {{petstoreUrl}}/pet/1
```

Para POST e PUT, use o modelo de `Pet` exibido no Swagger. Para DELETE, confirme o id usado e valide o status documentado. Dados criados em um serviço público podem ser compartilhados com outros estudantes; use somente dados de treinamento. Como a instância pública pode ficar instável, confirme sua disponibilidade antes de transformar `200` em uma expectativa rígida.

## 6. Testes de status e campo

No painel **Tests** da request, cole exatamente uma assertion por regra. O status e o campo são verificações diferentes:

```javascript
pm.test("Status deve ser 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Resposta possui campo esperado", function () {
    const body = pm.response.json();
    pm.expect(body).to.have.property("name");
});
```

Para JSONPlaceholder, o campo pode ser `title` em vez de `name`:

```javascript
pm.test("Post possui title", function () {
    const body = pm.response.json();
    pm.expect(body).to.have.property("title");
    pm.expect(body.title).to.be.a("string");
});
```

Para REST Countries, a resposta é uma lista:

```javascript
pm.test("País retornado possui código", function () {
    const countries = pm.response.json();
    pm.expect(countries).to.be.an("array").that.is.not.empty;
    pm.expect(countries[0].cca2).to.be.a("string");
});
```

## 7. Testes positivos e negativos

Um teste positivo confirma o caminho esperado: um id válido retorna o recurso, um POST válido retorna criação e uma busca de país conhecido retorna uma lista. Um teste negativo envia uma condição inválida ou inexistente: id que não existe, body incompleto, método não permitido ou credencial ausente.

O status negativo precisa vir do contrato. Uma forma segura de testar respostas de erro sem fazer o Postman marcar a request como falha de transporte é desativar **Settings → General → Request → HTTP status codes** somente quando necessário ou usar a opção de execução que permite respostas de erro. O teste deve continuar verificando o status esperado:

```javascript
pm.test("Usuário inexistente retorna erro documentado", function () {
    pm.expect([404, 400]).to.include(pm.response.code);
});
```

Não transforme qualquer erro em sucesso. O teste só passa se o código recebido fizer parte da expectativa do cenário.

## 8. Captura de token

Quando uma API de treinamento oferecer login, use um endpoint documentado. O Reqres possui o fluxo `POST /api/login`; a política de acesso pode exigir uma chave de teste e pode mudar, então confira a documentação atual antes de executar. Nunca coloque uma chave ou senha real no arquivo.

Body de exemplo do exercício:

```json
{
  "email": "eve.holt@reqres.in",
  "password": "pistol"
}
```

No **Tests** do login, capture o token somente se a resposta tiver o campo:

```javascript
pm.test("Login retorna token", function () {
    pm.response.to.have.status(200);
    const body = pm.response.json();
    pm.expect(body).to.have.property("token");
    pm.environment.set("token", body.token);
});
```

Na request seguinte, use `Authorization: Bearer {{token}}` somente se a documentação do endpoint exigir Bearer token. O objetivo é entender o encadeamento, não contornar autenticação.

## 9. Collection Runner

Abra a Collection, selecione **Run**, escolha o Environment e marque as requests que formam um fluxo. Comece com uma execução pequena: consulta, criação, alteração, exclusão e cenário de erro. Defina iterações e, se houver dados variados, carregue um CSV ou JSON de treino sem segredos.

Acompanhe total de requests, testes aprovados, falhas, duração e console. Uma execução em lote útil responde: qual request falhou, qual assertion falhou, qual status foi recebido e qual evidência deve ser investigada.

Para um CSV simples:

```csv
petId,country
1,brazil
2,canada
```

Use `{{petId}}` e `{{country}}` nas requests. Antes de rodar várias iterações, confirme que o cenário não altera dados compartilhados de forma irreversível.

## 10. Exercício final

Monte uma Collection com seis requests: consulta de recurso, criação, alteração, exclusão, usuário inexistente e login quando disponível. Adicione pelo menos uma assertion de status e uma de body em cada request. Execute a Collection Runner com duas iterações e registre o resultado.

O resultado esperado é uma execução reproduzível, com variáveis separadas, requests nomeadas, testes que explicam a regra e relatório que diferencia falha de API, falha de dado e falha de configuração.

## Referências

- [Postman Learning Center](https://learning.postman.com/)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- [Reqres](https://reqres.in/)
- [REST Countries](https://restcountries.com/)
- [Swagger Petstore](https://petstore3.swagger.io/)
