# Portfólio de QA — testes de API e automação

Este repositório reúne estudos e ferramentas estáticas para aprender a testar APIs REST. O conteúdo começa pelos conceitos básicos e avança para Postman, scripts JavaScript, Swagger/OpenAPI, Cypress e práticas de automação.

A [página inicial publicada](https://ericasouzaqa.github.io/QA-API-Testing/) organiza o caminho de estudo para quem nunca trabalhou com testes de API. Ela apresenta o fluxo de uma requisição e uma resposta, os conceitos que precisam ser entendidos, as competências praticadas e os materiais disponíveis.

## Estrutura do portfólio

| Material | O que demonstra |
| --- | --- |
| [`index.html`](index.html) | Página inicial do portfólio, com fundamentos, exemplos e navegação para os materiais. |
| [`curso_api_testing.html`](curso_api_testing.html) | Curso local com 53 aulas em 7 módulos, progresso salvo no navegador, checklists e níveis de domínio. |
| [`qa_triagem.html`](qa_triagem.html) | Fluxo local em quatro etapas para organizar entrada, triagem, cenários e manual de um item de entrega. |
| [`postman.md`](postman.md) | Guia de Postman com requests, Collections, variáveis, autenticação, scripts e assertions. |
| [`terms.md`](terms.md) | Glossário rápido de API, HTTP, QA, automação e boas práticas. |
| [`curriculo_automacao_api.pdf`](curriculo_automacao_api.pdf) | Currículo completo da trilha de estudos em PDF. |

## O que é praticado

O curso explica como ler uma requisição e uma resposta, interpretar métodos HTTP e status codes, identificar cenários positivos e negativos e validar dados conforme o contrato da API. Também apresenta a leitura de documentação Swagger/OpenAPI e a transformação de uma regra em caso de teste.

Na parte prática, o material usa Postman para organizar Collections, configurar environments, reaproveitar variáveis, criar scripts JavaScript e executar assertions. Em seguida, mostra como levar as validações para Cypress com `cy.request()`, organizar arquivos e preparar a execução automatizada.

## Operação local

As páginas são HTML, CSS e JavaScript sem etapa de build. A triagem e o curso funcionam localmente; o progresso do curso é salvo no `localStorage` do navegador. A triagem não envia o texto nem os anexos para APIs externas e não depende de serviço de geração em tempo de execução.

Para abrir a cópia local com segurança, execute um servidor estático na raiz do repositório:

```bash
python3 -m http.server 8000
```

Depois, acesse `http://localhost:8000/` no navegador. Abrir pelo GitHub Pages também é possível usando a [publicação do projeto](https://ericasouzaqa.github.io/QA-API-Testing/).

## Publicação

O projeto é compatível com GitHub Pages por usar arquivos estáticos na raiz e links relativos entre as páginas. A publicação atual serve a branch `main`; não há dependências de Node.js, pacote de build ou backend neste repositório.

## Limites importantes

Os exemplos de API, Postman e Cypress são materiais de estudo. A triagem local organiza o conteúdo fornecido, sinaliza lacunas e monta estruturas de apoio; ela não substitui a leitura dos requisitos, a execução contra um ambiente real ou o julgamento de QA. Não versionar senhas, tokens, chaves, credenciais ou dados pessoais reais.
