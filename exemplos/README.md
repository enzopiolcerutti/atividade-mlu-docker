# Exemplos de referência (para estudo)

Material de **estudo**. Para a ponderada, o professor pediu que os arquivos Docker sejam **seus**: rode, quebre, reescreva do zero com suas palavras e entenda cada linha antes de usar.

```
exemplos/
├── back/            Flask simples + Dockerfile multi-stage, usuário não-root
├── front/           Nginx servindo HTML estático e repassando /api/ para o back pelo nome do serviço
└── docker-compose.yml
```

## Rodar

```bash
cd exemplos
docker compose up --build
# abrir http://localhost:8080
docker compose down
```

## Experimentos para entender

1. `docker images`: veja o tamanho da imagem do back. Troque `python:3.12-slim` por `python:3.12` e compare.
2. `docker compose exec front wget -qO- http://back:5000/health`: DNS pelo nome do serviço.
3. `docker compose exec back whoami`: deve ser `app`, não root.
4. Mude `app.py` **sem rebuild** e observe que a imagem não muda. Faça rebuild e veja a nova versão.
5. Remova a rede explícita de um dos serviços e discuta o que acontece.
