# Atividade ponderada: Docker + ML + Modelagem

> **TEMPLATE para você preencher.** O professor disse que o README é o principal entregável e que quer ler **o que você escreveu**, sem passar por IA. Cada seção abaixo tem perguntas-guia; apague as perguntas e escreva com suas palavras.

**Nome:** _______________________
**Turma / Data:** _______________________

---

## 1. Visão geral do problema

_O que a aplicação faz? Quais são as partes (front, back, banco, modelo)?_

## 2. Como executar

_Passo a passo, com os comandos exatos (build, run ou compose). Alguém que nunca viu o projeto consegue rodar?_

```bash
# exemplo do formato (substitua pelos seus comandos)
docker build -t minha-app:1.0 .
docker run -p 8000:5000 minha-app:1.0
```

## 3. Decisões de Docker

_Para cada arquivo (Dockerfile, compose), explique **por que** foi feito assim, não só o que faz._

- Imagem base escolhida e por quê:
- Multi-stage? Qual ganho:
- Usuário não-root? Por quê:
- Tags / versionamento:
- Rede e comunicação entre serviços (DNS/nome do serviço):
- Volumes / persistência:

## 4. Diagrama de sequência

_Cole um diagrama (Mermaid ou imagem) do fluxo principal e explique em 2 a 3 frases como ele ajudaria a depurar._

## 5. Parte de ML

_Dados, features, modelo, métricas, partes do modelo. Por que esse tipo de rede/algoritmo para este problema?_

## 6. Problemas encontrados e como resolvi

_Erros reais que apareceram e o raciocínio usado. O professor valoriza ver você entendendo, mesmo com erro._

## 7. O que aprendi / o que faria diferente

---

### Uso de IA (transparência)

_Declare onde usou IA (ex.: código do Flask) e onde **não** usou (Docker, este README)._

---

📚 Material de apoio: [estudo/](estudo/00-regras-e-mapa.md) · Exemplos: [exemplos/](exemplos/README.md)
