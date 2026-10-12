# Primos Pobres

API em FastAPI, executada inteiramente via Docker (nenhuma dependência precisa ser instalada na máquina local).

## Stack

- Python 3.13
- FastAPI
- Docker e Docker Compose

## Como rodar

```bash
docker compose up -d --build
```

A API fica disponível em http://localhost:5000 e a documentação interativa em http://localhost:5000/docs.

## Documentação

- [Arquitetura](docs/architecture.md)
- [Design patterns](docs/design-patterns.md)
- [Testes](docs/testing.md)
- [Getting started](docs/getting-started.md)
