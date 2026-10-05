# 03 · Redes neurais: do neurônio à RNN/LSTM/GRU

A aula seguiu uma narrativa. Decore a **sequência de problema -> solução**.

## A linha do tempo

1. **Rede neural = aproximador universal de funções.** Inspirada no neurônio biológico.
2. **Um neurônio só (perceptron)** resolve só problemas **linearmente separáveis**: uma reta separa classe A de B. Representa AND e OR.
3. **XOR não é linearmente separável**: não dá com uma reta só. Isso travou as redes no começo.
4. **Solução: mais camadas de neurônios** (MLP) + função de **ativação** não linear. Passa de 1 neurônio para **vários**.
5. **Novo problema: como treinar?** Os pesos precisam ser ajustados. **Backpropagation**: propaga o **erro da saída para trás**, atualizando os pesos camada a camada.
6. O backprop usa **gradiente descendente** (cálculo): reduz o erro seguindo o gradiente para otimizar cada peso.
7. **Limite do MLP:** funciona bem para dados pequenos (ex.: reconhecer caracteres), mas **explode a dimensionalidade** com dados grandes. Uma foto inteira como entrada exige parâmetros demais.
8. **Solução: CNN (convolução).** Cada **filtro extrai uma característica** da imagem; as camadas convolucionais reduzem a dimensionalidade; no final liga-se a uma rede densa (MLP) para classificar.
9. **Limite de MLP e CNN: não lidam com tempo/sequência.** Cada previsão é independente da anterior.
10. **Solução: redes recorrentes (RNN).** Têm **memória**: a previsão atual depende da anterior (estado oculto reaproveitado a cada passo; pesos aplicados de forma recursiva). Boas para **séries temporais** e dados que se expandem no tempo.
11. **Limite da RNN simples: o gradiente "explode/desaparece"** em sequências longas (e, na analogia usada em aula, fica presa em ótimos locais ao considerar tudo). **LSTM e GRU** resolvem com **portões (gates)**, controlando o que lembrar e esquecer, o que dá o efeito de **"janela" de contexto**: considera o intervalo relevante.
12. "Estamos construindo os bloquinhos" -> próximo passo na história: **Transformer** (não é o foco da prova, mas é o destino).

> Nota de rigor: na aula o professor usou a analogia de **máximo local x máximo global** (heurísticas diferentes para achar o global) e de "janela deslizante" para explicar a vantagem de LSTM/GRU. Tecnicamente, o problema clássico é **vanishing/exploding gradient**. Cite as duas ideias, mas saiba o termo técnico.

## Tabela de arquitetura x problema

| Arquitetura | Resolve | Ideia-chave |
|---|---|---|
| Perceptron | AND, OR | 1 neurônio, só separável linearmente |
| MLP | XOR, problemas não lineares | camadas + ativação + backprop |
| CNN | imagens (dimensionalidade) | filtros extraem características |
| RNN | sequência / tempo | memória, estado anterior influencia o próximo |
| LSTM | sequências longas | portões (esquecer/entrada/saída) + célula de memória |
| GRU | idem, mais simples | 2 portões (update/reset), menos parâmetros |

## LSTM x GRU

- **LSTM**: 3 portões (forget, input, output) + estado de célula. Mais parâmetros.
- **GRU**: 2 portões (update, reset). Mais leve, geralmente desempenho parecido.
- Ambas existem para **mitigar o problema de dependências longas da RNN simples**.

## Pergunta-frase para a dissertativa

"Cada tipo de rede resolve um tipo de problema: MLP para dados tabulares/não lineares, CNN para imagem, RNN/LSTM/GRU para sequência temporal."
