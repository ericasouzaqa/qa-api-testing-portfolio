# QA API Testing Portfolio

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-online-2ea44f?logo=github)](https://ericasouzaqa.github.io/qa-api-testing-portfolio/)
[![Windows Desktop](https://img.shields.io/badge/Windows-portable-0078D6?logo=windows)](https://github.com/ericasouzaqa/qa-api-testing-portfolio/releases/latest)
[![API Testing](https://img.shields.io/badge/QA-API%20Testing-6b7280)](https://github.com/ericasouzaqa/qa-api-testing-portfolio)
[![Postman](https://img.shields.io/badge/Postman-labs-ff6c37?logo=postman)](postman_pratica.html)
[![Cypress](https://img.shields.io/badge/Cypress-API%20testing-69d3a7?logo=cypress)](cypress_api_testing.html)
[![Release](https://img.shields.io/github/v/release/ericasouzaqa/qa-api-testing-portfolio)](https://github.com/ericasouzaqa/qa-api-testing-portfolio/releases/latest)
[![License](https://img.shields.io/github/license/ericasouzaqa/qa-api-testing-portfolio)](LICENSE)

Portfólio prático de QA para testes de API com Postman, JavaScript, Swagger/OpenAPI e Cypress. O projeto ensina uma pessoa iniciante a ler um contrato, criar uma request, adicionar validações, executar o teste e analisar o resultado.

O conteúdo é local e funciona como site estático. Não há backend, banco de dados, login, serviço pago, inteligência artificial ou chave privada obrigatória. A execução offline usa os mesmos arquivos HTML da versão Web.

## Acesso ao projeto

### Versão Web

Acesse o [GitHub Pages](https://ericasouzaqa.github.io/qa-api-testing-portfolio/). Não é necessário instalar nada: a aplicação abre diretamente em um navegador moderno e usa apenas HTML, CSS e JavaScript.

### Versão Desktop para Windows

Baixe [`qa-api-testing-portfolio-windows.zip`](https://github.com/ericasouzaqa/qa-api-testing-portfolio/releases/download/v2.0.0/qa-api-testing-portfolio-windows.zip) na [Release v2.0.0](https://github.com/ericasouzaqa/qa-api-testing-portfolio/releases/tag/v2.0.0). Extraia o ZIP e dê duplo clique em `QA-API-Testing-Portfolio.bat`. O launcher abre `app/index.html` localmente; não exige Node.js, servidor ou configuração adicional.

## Conteúdo disponível

| Parte | O que demonstra |
| --- | --- |
| Trilha de oito módulos | Fundamentos de API, HTTP/REST, Postman, JavaScript, Swagger/OpenAPI, Cypress, automação e boas práticas de QA. |
| Laboratório de Postman | Instalação, Collection, Environment, variáveis, organização, assertions, scripts, token, testes positivos/negativos e Collection Runner. |
| Laboratório de Cypress | Instalação opcional, configuração, estrutura, `cy.request()`, validações, CRUD, erros, autenticação e execução em lote. |
| APIs de treinamento | JSONPlaceholder, Reqres, REST Countries e Swagger Petstore. |
| Glossário | Termos de HTTP, REST, status codes, Postman, QA e automação. |

O fluxo de estudo usa a [documentação do Swagger Petstore](https://petstore3.swagger.io/) como exemplo real: localizar `GET /pet/{petId}`, entender método e parâmetros, criar a request, validar a resposta e analisar o resultado. Serviços públicos podem ficar indisponíveis; isso deve ser registrado como problema do ambiente, não confundido com falha funcional esperada.

## Tecnologias utilizadas

O projeto usa somente tecnologias que realmente fazem parte da solução: **HTML5, CSS3, JavaScript, Postman, Swagger/OpenAPI, Cypress, GitHub Pages e Windows Portable Launcher**. Postman e Cypress são ferramentas ensinadas nos laboratórios; não são dependências para abrir o site ou ler o material.

## CI/CD

O repositório possui dois workflows em `.github/workflows/`. O CI roda em Pull Requests para `main` e em pushes para `main`. Ele verifica os arquivos obrigatórios, a presença de `README.md` e `LICENSE`, a estrutura HTML, os links locais, os arquivos temporários/indevidos, a estrutura Web/Desktop e o formato do diff.

O CD roda somente após o CI terminar com sucesso para a branch `main`. Nesse momento, ele publica a raiz estática com as actions oficiais do GitHub Pages. Não existe etapa de build com dependências: o artefato publicado é formado pelos arquivos HTML, CSS e JavaScript versionados no repositório.

Se uma verificação crítica falhar, o CI interrompe o processo e o CD não publica aquela versão.

## Execução local

Para testar a versão Web com um servidor estático opcional:

```bash
python3 -m http.server 8000
```

Depois, acesse `http://localhost:8000/`. Para leitura offline no Windows, use o launcher do pacote Desktop.

## Contribuição

Para propor uma melhoria, faça um fork, crie uma branch, altere o conteúdo, valide os links e os arquivos HTML, registre um commit e abra um Pull Request:

```bash
git checkout -b melhoria-conteudo
# edite os arquivos
python3 -m http.server 8000
git add .
git commit -m "Melhora exemplos de testes de API"
git push origin melhoria-conteudo
```

O Pull Request deve explicar o objetivo da alteração, os arquivos envolvidos e como a validação foi feita. Não inclua tokens, senhas, chaves, credenciais ou dados pessoais reais.

## Licença

Este projeto é distribuído sob a [licença MIT](LICENSE).
