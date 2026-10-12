# Getting started

## Pré-requisitos

- Docker
- Docker Compose

Nenhuma dependência Python precisa ser instalada localmente; tudo roda dentro do container.

## Subir o projeto

```bash
docker compose up -d --build
```

- API: http://localhost:5000
- Health check: http://localhost:5000/health
- Documentação interativa (Swagger): http://localhost:5000/docs

O diretório `app/` é montado no container, então alterações no código recarregam o servidor automaticamente.

## Comandos úteis

| Ação | Comando |
|---|---|
| Ver logs | `docker compose logs -f api` |
| Parar | `docker compose down` |
| Rebuild após mudar `requirements.txt` | `docker compose up -d --build` |
| Shell no container | `docker compose exec api bash` |
