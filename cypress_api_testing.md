# Laboratório prático de Cypress API Testing

Este guia mostra como transformar requests de API em testes versionados. O Cypress é opcional para quem está estudando; o portfólio continua funcionando como site estático e não precisa instalar Cypress para abrir o conteúdo.

## 1. Instalação

Em uma pasta separada para os exercícios, instale o Cypress como dependência de desenvolvimento:

```bash
mkdir qa-api-cypress
cd qa-api-cypress
npm init -y
npm install cypress --save-dev
npx cypress open
```

O comando `npx cypress open` cria a estrutura inicial quando necessário e abre a interface. Para executar sem interface, use:

```bash
npx cypress run
```

A instalação é feita somente no projeto de testes do aluno. Ela não é uma dependência obrigatória deste portfólio estático.

## 2. Configuração

Crie `cypress.config.js` na raiz. `baseUrl` evita repetir o domínio, mas não substitui a leitura da documentação da API:

```javascript
const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://jsonplaceholder.typicode.com',
    video: false,
  },
});
```

Para outro serviço de treinamento, altere `baseUrl` conscientemente:

```javascript
// Swagger Petstore
baseUrl: 'https://petstore3.swagger.io/api/v3'

// REST Countries não usa a mesma raiz de recursos
baseUrl: 'https://restcountries.com/v3.1'
```

Não coloque tokens, senhas ou chaves privadas no arquivo de configuração. Use variáveis de ambiente ou o mecanismo de segredo do pipeline quando a API realmente exigir autenticação.

## 3. Estrutura dos testes

Uma estrutura pequena e legível é suficiente para começar:

```text
qa-api-cypress/
├── cypress/
│   ├── e2e/
│   │   └── api/
│   │       ├── jsonplaceholder.cy.js
│   │       ├── petstore.cy.js
│   │       └── negative.cy.js
│   ├── fixtures/
│   │   └── pet.json
│   └── support/
├── cypress.config.js
└── package.json
```

Separe os testes por recurso ou comportamento. Nomeie o `describe` com a API e o `it` com o resultado esperado. O teste deve indicar método, endpoint, dados relevantes e assertions.

## 4. Primeira chamada com `cy.request()`

O exemplo abaixo consulta usuários simulados no JSONPlaceholder. A ideia é a mesma do fluxo solicitado: entender o contrato, criar a request, validar e analisar.

```javascript
describe('Teste de API', () => {
  it('Deve consultar usuários', () => {
    cy.request('GET', '/users')
      .then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.be.an('array');
        expect(response.body[0]).to.have.property('name');
      });
  });
});
```

Se a API não tiver sido configurada com `baseUrl`, use a URL completa. O status `200` sozinho não prova que a resposta está correta; valide também estrutura, tipos e campos relevantes.

## 5. Cenários de consulta

### JSONPlaceholder: post existente

```javascript
it('consulta um post existente', () => {
  cy.request('GET', '/posts/1').then((response) => {
    expect(response.status).to.eq(200);
    expect(response.body).to.include.keys('userId', 'id', 'title', 'body');
    expect(response.body.id).to.eq(1);
  });
});
```

### REST Countries: país

```javascript
describe('REST Countries', () => {
  it('consulta o Brasil', () => {
    cy.request('GET', 'https://restcountries.com/v3.1/name/brazil')
      .then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.be.an('array').and.not.be.empty;
        expect(response.body[0].name.common).to.be.a('string');
        expect(response.body[0].cca2).to.eq('BR');
      });
  });
});
```

## 6. Criação, alteração e exclusão

O JSONPlaceholder simula escrita e devolve respostas de treino. Os dados não devem ser tratados como persistidos sem confirmar a documentação.

```javascript
describe('JSONPlaceholder - ciclo de post', () => {
  it('cria um post', () => {
    cy.request('POST', '/posts', {
      title: 'estudo de API',
      body: 'conteúdo de teste',
      userId: 1,
    }).then((response) => {
      expect(response.status).to.eq(201);
      expect(response.body).to.have.property('id');
    });
  });

  it('altera um post', () => {
    cy.request('PUT', '/posts/1', {
      id: 1,
      title: 'título alterado',
      body: 'conteúdo alterado',
      userId: 1,
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.title).to.eq('título alterado');
    });
  });

  it('exclui um post', () => {
    cy.request('DELETE', '/posts/1').then((response) => {
      expect(response.status).to.eq(200);
    });
  });
});
```

Para o Swagger Petstore, consulte os modelos na documentação antes de enviar `POST /pet` e `PUT /pet`. Não copie um body de outra API: o contrato de cada serviço define campos e tipos.

## 7. Validação de erro e usuário inexistente

Para um erro esperado, use `failOnStatusCode: false` para receber a resposta e validar o status no teste:

```javascript
it('trata usuário inexistente', () => {
  cy.request({
    method: 'GET',
    url: 'https://reqres.in/api/users/9999',
    failOnStatusCode: false,
  }).then((response) => {
    expect([404, 400]).to.include(response.status);
  });
});
```

Escolha o status pela documentação ou pelo comportamento confirmado do serviço. Não transforme qualquer `4xx` em sucesso de forma genérica; o cenário deve dizer qual erro é esperado.

## 8. Autenticação quando disponível

O Reqres oferece um fluxo de login de treinamento, mas pode exigir uma chave de acesso conforme a política atual do serviço. Nunca versionar essa chave. O padrão de captura e uso do token é:

```javascript
it('captura token de login', () => {
  cy.request({
    method: 'POST',
    url: 'https://reqres.in/api/login',
    body: {
      email: 'eve.holt@reqres.in',
      password: 'pistol',
    },
    failOnStatusCode: false,
  }).then((response) => {
    expect([200, 401, 403]).to.include(response.status);
    if (response.status === 200) {
      expect(response.body).to.have.property('token');
    }
  });
});
```

Se a API documentar Bearer token, envie-o por header sem escrever o valor no código:

```javascript
cy.request({
  method: 'GET',
  url: '/users',
  headers: { Authorization: `Bearer ${Cypress.env('apiToken')}` },
});
```

## 9. Swagger Petstore no Cypress

Abra o [Swagger Petstore](https://petstore3.swagger.io/), leia `GET /pet/{petId}` e implemente o teste:

```javascript
describe('Swagger Petstore', () => {
  it('consulta um pet', () => {
    cy.request('GET', 'https://petstore3.swagger.io/api/v3/pet/1')
      .then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property('id');
        expect(response.body.name).to.be.a('string');
      });
  });
});
```

Depois, crie um cenário de pet inexistente e um cenário de criação. Primeiro registre o status e o modelo esperado na documentação; somente depois escreva as assertions.

## 10. Organização e execução

Mantenha cada `it` com uma intenção. Prefira comandos pequenos e independentes a um teste que faz consulta, criação, alteração e exclusão sem separar os resultados. Se houver dependência entre etapas, deixe os dados explícitos e limpe os recursos de teste quando a API permitir.

Execute um arquivo específico enquanto desenvolve:

```bash
npx cypress run --spec 'cypress/e2e/api/jsonplaceholder.cy.js'
```

Depois execute a suíte inteira:

```bash
npx cypress run --spec 'cypress/e2e/api/**/*.cy.js'
```

O resultado esperado é uma lista de testes com nome, status e mensagem de assertion. Ao investigar uma falha, confira contrato, endpoint, dados, ambiente e resposta antes de alterar o teste.

## Exercício final

Crie uma suíte com consulta, criação, alteração, exclusão, erro e usuário inexistente. Use JSONPlaceholder para CRUD, REST Countries para validação de lista, Swagger Petstore para contrato e Reqres para o cenário de login quando o serviço estiver disponível. Execute um arquivo específico e depois toda a pasta `api`.

Ao concluir, você deve conseguir explicar por que cada request existe, qual status e campo são esperados, como a resposta negativa é tratada e como outra pessoa executaria os testes.

## Referências

- [Cypress Documentation](https://docs.cypress.io/)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- [Reqres](https://reqres.in/)
- [REST Countries](https://restcountries.com/)
- [Swagger Petstore](https://petstore3.swagger.io/)
