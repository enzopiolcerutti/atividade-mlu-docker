# 02 · Docker Compose e redes

## O que é o Compose

Ferramenta para **subir e gerenciar vários containers de uma vez**, descritos em um `docker-compose.yml` (ou `compose.yaml`).

```
docker compose up --build      # constrói e sobe tudo
docker compose up -d           # em segundo plano
docker compose down            # derruba (e remove a rede)
docker compose logs -f back
docker compose ps
```

## Rede (ponto que o professor admitiu ter esquecido e fez questão de corrigir)

- Containers do **mesmo compose ficam na mesma rede** e se enxergam.
- Há **DNS interno**: o **nome do serviço** vira hostname.
  - O container `front` **não precisa saber o IP** do `back`; chama `http://back:5000`.
- O Compose cria uma rede *default*, mas **é bom declarar a rede explicitamente** (boa prática dita em aula).
- Para dois serviços se falarem, **precisam estar na mesma rede**.

## Exemplo mínimo

```yaml
services:
  back:
    build: ./back
    networks: [app-net]

  front:
    build: ./front
    ports:
      - "8080:80"        # host:container (só o que o usuário acessa)
    depends_on: [back]
    networks: [app-net]

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - db-data:/var/lib/postgresql/data
    networks: [app-net]

networks:
  app-net:

volumes:
  db-data:
```

Pontos para explicar:
- `ports` publica porta para o **host**; comunicação entre containers **não precisa** de `ports`.
- `volumes` persistem dados (container é efêmero).
- `depends_on` controla ordem de início, **não** garante que o serviço esteja "pronto".
- `build:` cria imagem a partir de Dockerfile; `image:` usa uma pronta.

## Compose x Dockerfile (não confundir)

| Dockerfile | Compose |
|---|---|
| Descreve **uma imagem** | Descreve **vários serviços** (containers) |
| `docker build` | `docker compose up` |
