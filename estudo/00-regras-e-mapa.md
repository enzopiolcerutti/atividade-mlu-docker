# 00 · Regras da ponderada e mapa de estudo

Fonte: transcrição automática da aula (aproximada, falas de alunos não são dicas do professor).

## O que o professor disse sobre a ponderada

| Tema | O que foi dito |
|---|---|
| **Quando** | Semana 10, segunda-feira. Quem aplica é o próprio professor (não a Fabi). |
| **Foco** | "Acima de tudo o Docker". ML também cai. |
| **Consulta** | Liberada **ao GitHub do aluno**: tudo que estiver no seu GitHub pode usar. |
| **Anotações fora do Git** | OneNote etc.: exporte para markdown e suba no repositório de estudo. Anotação em papel: pode trazer, não precisa digitalizar. |
| **Livro/curso de Docker** | Pode usar (o curso está no GitHub). |
| **Código** | Pode usar IA (ex.: "suba um back-end com Flask"). |
| **Docker** | Usar **os arquivos de vocês** (Dockerfile, compose etc.). A IA não deve fazer essa parte. |
| **Entregável principal** | **README**, escrito por você. Não passar por IA para "melhorar". O professor quer ler o que *você* escreveu, mesmo com erro. |
| **Template de README** | Foi pedido; o professor topou algo simples (nome etc.). Ver [README.md](../README.md). |
| **Sintaxe** | Não vai tirar ponto por sintaxe. Prova é no papel. Cobra **conceito**: "esse problema eu resolvo desse jeito, isso serve para isso". |
| **Dockerfiles de exemplo** | Vão aparecer na prova. "Olhem para eles." |
| **Dissertativa** | Autoria dele. Envolve as **três áreas** (ML, UML, Docker). Provavelmente um problema com sequência/relação entre as partes, e você escreve a resolução. |
| **Objetivas** | Vai ter. |
| **cgroups / namespaces** | Não confirmou nem negou. "Dê uma passadinha no capítulo do livro." Estude por segurança. |
| **Glossário** | Mencionado ao final por um aluno; não confirmado. |

## Os 5 pontos de ML ("estudaria esses cinco")

1. Exploração de dados
2. Feature engineering
3. Gerar (treinar) um modelo
4. Métricas do modelo
5. Partes do modelo

Mais: RNN, LSTM, GRU (aula do Jeff).

## Mapa geral

```
Prova ponderada
├── Docker (peso maior)         -> 01, 02, 06
├── ML                          -> 03, 04
└── Modelagem UML (sequência)   -> 05
Treino                          -> 07
Exemplos que rodam              -> ../exemplos/
```

## Checklist de preparação antes da segunda

- [ ] Rodar os exemplos de `exemplos/` na sua máquina e entender cada linha
- [ ] Escrever **com suas palavras** os resumos (os arquivos aqui são ponto de partida)
- [ ] Preencher o [README.md](../README.md) (template) à mão, sem IA
- [ ] Subir tudo no GitHub (consulta só vale o que estiver lá) e conferir que o repo abre no navegador
- [ ] Levar anotações de papel, se tiver
- [ ] Reler o capítulo de cgroups/namespaces do livro
- [ ] Fazer as questões de [07-questoes-treino.md](07-questoes-treino.md) sem olhar
