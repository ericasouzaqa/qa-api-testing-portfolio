# Portfólio de QA — testes de API e automação

Este repositório contém uma trilha local e progressiva para aprender testes de API REST. O conteúdo parte dos conceitos básicos e chega à automação com Postman, JavaScript e Cypress, sempre usando uma documentação real como ponto de partida.

A [página inicial publicada](https://ericasouzaqa.github.io/QA-API-Testing/) apresenta o caminho de estudo. O conteúdo principal está nos próprios arquivos do projeto e não depende de inteligência artificial, API externa obrigatória, banco de dados, login, serviço pago, chave privada ou backend.

## Trilha de aprendizado

| Módulo | Conteúdo |
| --- | --- |
| 01 - Fundamentos de API | API, cliente, servidor, request, response e JSON. |
| 02 - HTTP e REST | Métodos HTTP, CRUD, status codes, headers e autenticação. |
| 03 - Postman | Requests, Collections, environments e variáveis. |
| 04 - JavaScript no Postman | Assertions, scripts, variáveis e request chaining. |
| 05 - Swagger/OpenAPI | Leitura de documentação, endpoints, parâmetros, modelos e respostas. |
| 06 - Cypress API Testing | `cy.request()`, assertions e cenários negativos em código. |
| 07 - Automação de Testes | Priorização, organização, execução e evidências. |
| 08 - Boas Práticas de QA | Contrato, risco, manutenção, regressão e proteção de dados. |

Cada aula apresenta uma explicação simples, um exemplo prático, código quando necessário, um exercício, o resultado esperado e um checklist de entendimento. O aluno pode avançar manualmente ou usar o botão de continuidade; o progresso fica salvo no `localStorage` deste navegador.

## Fluxo de teste ensinado

A trilha usa o mesmo fluxo do início ao fim: ler a documentação Swagger/OpenAPI, entender método, endpoint, parâmetros e respostas, criar a requisição, adicionar validações, executar o teste e analisar o resultado. O exemplo principal usa a documentação pública do [Swagger Petstore](https://petstore3.swagger.io/), com o endpoint `GET /pet/{petId}`.

O [guia de Postman](postman.md) amplia os exemplos de requests, Collections, variáveis, autenticação, scripts, assertions, cenários negativos e chaining. O [glossário de QA e API](terms.md) serve como consulta rápida para os termos usados nas aulas.

## Arquivos principais

| Arquivo | Finalidade |
| --- | --- |
| [`index.html`](index.html) | Página inicial do portfólio, com o mapa de conceitos e o fluxo de teste. |
| [`curso_api_testing.html`](curso_api_testing.html) | Aplicação local da trilha de oito módulos, com aulas, exercícios e progresso. |
| [`postman.md`](postman.md) | Material complementar de Postman e JavaScript. |
| [`terms.md`](terms.md) | Glossário de API, HTTP, QA e automação. |

## Execução local

As páginas usam somente HTML, CSS e JavaScript. Para abrir a cópia local com as mesmas condições de uma hospedagem estática, execute um servidor na raiz:

```bash
python3 -m http.server 8000
```

Depois, acesse `http://localhost:8000/`. Nenhum pacote ou etapa de build é necessário.

## Limites do projeto

Os exemplos são exercícios de estudo. Antes de executar uma request em outro ambiente, confirme a documentação, a autorização de acesso e os dados permitidos. Um teste automatizado não substitui a análise da regra de negócio nem a investigação da causa de uma falha. Nunca versionar senhas, tokens, chaves, credenciais ou dados pessoais reais.
