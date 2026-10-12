# Arquitetura

## Estrutura de pastas

```
primos-pobres/
├── .claude/skills/      # skills do Claude Code
├── app/
│   ├── __init__.py
│   └── main.py          # instância FastAPI e rotas
├── docs/                # documentação do projeto
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Componentes

- **API (`app/main.py`)**: aplicação FastAPI. Hoje expõe apenas `GET /health`.

## Serviços Docker

| Serviço | Imagem | Porta | Observações |
|---|---|---|---|
| `api` | build local (`python:3.13-slim`) | 5000 | Roda `fastapi dev` com `./app` montado como volume (hot reload) |

O `Dockerfile` usa `fastapi run` (modo produção); o `docker-compose.yml` sobrescreve o comando para `fastapi dev` no desenvolvimento.
