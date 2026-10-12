---
name: doc-check
description: Valida e mantém atualizados o README.md e a documentação em docs/ (architecture, design-patterns, testing, getting-started) antes de um commit. Use antes de qualquer commit, quando o usuário pedir para commitar, revisar a documentação, ou quando alterações tocarem estrutura do projeto, dependências, Docker, rotas, padrões de código ou testes.
disable-model-invocation: false
allowed-tools: Read, Edit, Write, Glob, Grep, Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(ls:*)
---

# doc-check

Garante que o `README.md` e os arquivos em `docs/` reflitam o estado real do projeto antes de cada commit, alterando a documentação **somente quando as mudanças forem relevantes para ela**.

## Quando invocar

- Antes de criar um commit (sempre que o usuário pedir para commitar).
- Quando o usuário pedir para revisar ou atualizar a documentação.
- Depois de mudanças em: estrutura de pastas, dependências (`requirements.txt`), `Dockerfile`, `docker-compose.yml`, portas, variáveis de ambiente, rotas da API, camadas/módulos, padrões de projeto ou testes.

## Arquivos de documentação

| Arquivo | Conteúdo |
|---|---|
| `README.md` | Visão geral, stack, como rodar rapidamente e índice dos docs |
| `docs/architecture.md` | Estrutura de pastas, componentes, serviços Docker, fluxo de requisição |
| `docs/design-patterns.md` | Padrões e convenções de código adotados |
| `docs/testing.md` | Como os testes estão organizados e como executá-los |
| `docs/getting-started.md` | Pré-requisitos, setup, comandos do dia a dia |

## Passo a passo

### 1. Levantar as alterações

Rode `git status` e `git diff HEAD` (inclui staged e não staged). Se não houver commits ainda, use `git status` e leia os arquivos novos.

### 2. Validar a estrutura do README.md

O `README.md` deve existir e conter, nesta ordem, as seções:

1. `# <Nome do projeto>` com uma descrição curta
2. `## Stack`
3. `## Como rodar`
4. `## Documentação` com links para os quatro arquivos de `docs/`

Também verifique se todos os arquivos de `docs/` listados acima existem. Se faltar alguma seção ou arquivo, crie seguindo o modelo existente.

### 3. Decidir se a documentação precisa mudar

Mapeie cada alteração para o documento afetado:

| Alteração | Documento(s) |
|---|---|
| Nova pasta/módulo, novo serviço no compose, banco, fila, integração externa | `architecture.md`, README (Stack) |
| Novo padrão (repository, service layer, DI, schemas etc.) ou mudança de convenção | `design-patterns.md` |
| Novos testes, framework de testes, comando de teste, cobertura | `testing.md` |
| Mudança de porta, comando, variável de ambiente, pré-requisito, dependência | `getting-started.md`, README (Como rodar) |
| Nova rota ou recurso de API relevante para o usuário | README e/ou `architecture.md` |

**Não altere a documentação** quando as mudanças forem apenas:

- refatorações internas sem mudança de estrutura ou comportamento;
- correções de bug pontuais, ajustes de lógica, renomeação de variáveis locais;
- formatação, comentários, typos no código;
- mudanças em arquivos ignorados ou de configuração pessoal (`.claude/settings.local.json`).

Na dúvida, prefira não alterar.

### 4. Atualizar

- Edite apenas as seções afetadas; não reescreva documentos inteiros.
- Descreva o que existe de fato no código. Nunca documente algo planejado como se já existisse.
- Mantenha o idioma (português) e o estilo atual dos documentos.
- Confira se comandos, portas e caminhos citados batem com `Dockerfile`, `docker-compose.yml` e o código.

### 5. Reportar

Informe ao usuário em poucas linhas:

- se a estrutura do README estava válida (e o que foi corrigido, se algo);
- quais documentos foram atualizados e por quê, **ou** que nenhuma atualização foi necessária e o motivo.

Não faça o commit nesta skill; os arquivos de documentação alterados devem entrar no mesmo commit das mudanças de código.
