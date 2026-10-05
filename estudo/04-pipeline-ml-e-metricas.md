# 04 · Pipeline de ML: os 5 pontos da Fabi

O professor: "Eu estudaria esses cinco para a prova." Aqui está o esqueleto; **complete com o material da Fabi** (slides/notebooks da aula dela), que não está na transcrição.

## 1. Exploração de dados (EDA)

Entender os dados antes de modelar.
- Formato, tipos, `df.info()`, `df.describe()`
- **Valores nulos**, duplicados, **outliers**
- Distribuição de cada variável (histograma, boxplot)
- **Correlação** entre variáveis e com o alvo
- **Balanceamento de classes** (se classificação)
- Para série temporal: tendência, sazonalidade, ordem cronológica

## 2. Feature engineering

Transformar/criar variáveis para ajudar o modelo.
- Tratar nulos (média/mediana/remoção)
- **Codificação** de categóricas (one-hot, label)
- **Escalonamento** (padronização, min-max): importante para redes neurais
- Criar variáveis novas (ex.: dia da semana, razões, lags em séries)
- Seleção de features / redução de dimensionalidade
- **Evitar vazamento (data leakage)**: ajustar scaler só no treino

## 3. Gerar (treinar) um modelo

- Separar **treino / validação / teste** (em série temporal, **respeitando o tempo**, sem embaralhar)
- Escolher algoritmo conforme o problema (classificação, regressão, sequência)
- Treinar = ajustar pesos minimizando uma **função de perda** (loss) via gradiente descendente
- Hiperparâmetros: learning rate, épocas, batch size, nº de camadas
- **Overfitting** (decora o treino) x **underfitting** (não aprende)

## 4. Métricas do modelo

**Classificação** (matriz de confusão: TP, TN, FP, FN)
| Métrica | Fórmula | Use quando |
|---|---|---|
| Acurácia | (TP+TN)/total | classes balanceadas |
| Precisão | TP/(TP+FP) | falso positivo é caro |
| Recall | TP/(TP+FN) | falso negativo é caro |
| F1 | 2·P·R/(P+R) | equilíbrio P e R, classes desbalanceadas |
| AUC-ROC | área sob a curva | qualidade geral do ranking |

**Regressão**
- MAE (erro absoluto médio), MSE/RMSE (penaliza erros grandes), R².

Sempre comparar **treino x teste**: gap grande = overfitting.

## 5. Partes do modelo

(Confirme com a Fabi o que ela chamou de "partes".) Interpretação provável:
- **Entrada (input)** e shape
- **Camadas** (input, ocultas, saída) e **neurônios** por camada
- **Pesos e vieses (bias)**
- **Função de ativação** (ReLU, sigmoid, softmax, tanh)
- **Função de perda** e **otimizador** (SGD, Adam)
- **Saída** (probabilidade, valor contínuo)
- Em Keras/PyTorch: onde cada parte aparece no código

## Como ligar tudo

`Dados -> EDA -> Features -> Treino -> Métricas -> (ajusta) -> Modelo salvo -> Container (Docker) servindo via API (Flask)`

Essa última seta é onde ML e Docker se encontram, e é onde a **dissertativa integrada** provavelmente mora.
