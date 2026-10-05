# 07 · Questões de treino

Responda no papel, sem olhar. Depois confira nos arquivos 01 a 06.

## Objetivas (V/F ou curtas)

1. Qual problema principal o Docker resolve?
2. Qual a diferença entre imagem e container?
3. Um container em execução permite alterar a imagem? Explique "depende".
4. Qual comando constrói uma imagem? E roda?
5. Para que serve a tag? É vantagem ou desvantagem?
6. Para que serve multi-stage build? Cite duas vantagens.
7. Por que o estágio final pode rodar sem root?
8. O que o Compose faz? Como o `front` encontra o `back`?
9. Por que declarar a rede explicitamente no Compose?
10. Diferença entre `RUN` e `CMD`.
11. Namespace x cgroup.
12. Por que um perceptron não resolve XOR? Como se resolveu?
13. O que o backpropagation faz? Qual técnica de cálculo usa?
14. Por que CNN em vez de MLP para imagens?
15. O que dá "memória" a uma rede recorrente? Quando usar?
16. Por que existem LSTM e GRU se já havia RNN?
17. Diferença entre precisão e recall. Quando priorizar cada uma?
18. O que é data leakage?
19. Para que serve um diagrama de sequência além de programar?
20. Em produção, algo funciona mas é um monolito. Qual a regra de ouro?

## Dissertativas integradas (estilo da prova)

**D1.** Você treinou um modelo de previsão de série temporal e precisa disponibilizá-lo via API para outras pessoas do time, que usam sistemas operacionais diferentes.
- (a) Qual rede você escolheria e por quê?
- (b) Como o Docker garante que todos rodem igual?
- (c) Descreva em texto o Dockerfile (base, dependências, usuário, comando) e justifique cada decisão.
- (d) Desenhe o diagrama de sequência de uma requisição de previsão.

**D2.** O sistema tem front, back (Flask) e banco.
- (a) Descreva o `docker-compose` e a rede entre os serviços.
- (b) O front chama o back por IP ou nome? Por quê?
- (c) A imagem do back ficou com 2 GB. Proponha como reduzi-la (multi-stage, slim, .dockerignore).
- (d) Quando faria sentido manter tudo em um container só?

**D3.** Um colega diz "na minha máquina funciona". Explique a causa e a solução, citando VM x container, e o que muda ao subir uma versão nova do código.

## Dica de redação

O professor corrige **conceito**, não sintaxe. Estruture: **problema -> solução -> por que funciona -> trade-off**.
