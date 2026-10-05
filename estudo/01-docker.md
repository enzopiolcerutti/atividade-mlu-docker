# 01 · Docker (conceitos que o professor cobrou)

## Por que Docker? Reprodutibilidade

Problema: "funciona na minha máquina" (macOS) mas não no servidor (Linux). Diferem SO, arquitetura, dependências, versões.

Soluções possíveis, em ordem:
1. Todo mundo ter a mesma máquina/SO/versões. **Inviável.**
2. **Máquinas virtuais**: resolvem, mas têm custo alto (sobem um SO inteiro, muitos recursos).
3. **Containers**: só um **processo isolado**, compartilha o kernel do host. Leve e rápido.

> Resposta para "qual problema o Docker resolve?": **reprodutibilidade** do ambiente.

## Imagem x Container

- **Imagem**: modelo imutável, "compilada" (build). Contém SO base, dependências, código.
- **Container**: **instância em execução de uma imagem**. (Frase do professor: "o container é a instanciação de uma imagem".)

Analogia: imagem = classe / receita; container = objeto / bolo pronto.

## Fluxo

```
Dockerfile --docker build--> Imagem (com tag) --docker run--> Container
```

| Quero... | Comando |
|---|---|
| Usar imagem já pronta | `docker pull python:3.7` / `docker run python:3.7` (baixa de um registry) |
| Criar minha imagem | escrever `Dockerfile` + `docker build -t nome:tag .` |
| Rodar | `docker run -p 8000:5000 nome:tag` |
| Listar | `docker ps` (rodando), `docker ps -a`, `docker images` |
| Parar/remover | `docker stop <id>`, `docker rm <id>`, `docker rmi <img>` |
| Logs / entrar | `docker logs <id>`, `docker exec -it <id> sh` |

## Dá para mudar uma imagem? (pegadinha explícita da aula)

"Depende do sentido":
- Com o container **em execução** você pode trocar **arquivos que ele acessa** (ex.: volume/bind mount), mas **não muda a imagem**.
- Para mudar a imagem: editar o Dockerfile e fazer **novo build** -> **outra imagem** (nova tag).

## Tags: vantagem ou desvantagem?

**Vantagem.** Tags versionam imagens (`python:3.7`, `app:1.2`). Permitem rodar algo que depende de versão antiga (ex.: precisa de Python 3.7 -> imagem `python:3.7`), rollback, e convivência de versões.

## Dockerfile (instruções principais)

| Instrução | Função |
|---|---|
| `FROM` | imagem base |
| `WORKDIR` | diretório de trabalho |
| `COPY` / `ADD` | copia arquivos para a imagem |
| `RUN` | executa comando **durante o build** (ex.: `pip install`) |
| `ENV` | variável de ambiente |
| `EXPOSE` | documenta a porta (não publica) |
| `USER` | usuário que roda o processo |
| `CMD` / `ENTRYPOINT` | comando **ao iniciar o container** |

Boas práticas: copiar `requirements.txt` antes do código (cache de camadas), usar imagens `-slim`, `.dockerignore`, não rodar como root.

## Multi-stage build

- Pergunta: "para que serve?" -> **separar o momento de build do momento de run (runtime)**.
- Linguagens compiladas (Go, Rust, C): estágio 1 compila e gera executável; estágio 2 só copia o executável.
- Front-end (React, Svelte, TS): estágio 1 faz o build/transpilação (TS/JS moderno -> JS padrão); estágio 2 serve só os arquivos estáticos (ex.: nginx).

**Vantagens**
- Exclui arquivos que só servem para build (compiladores, node_modules, código-fonte) -> **imagem menor/mais leve**.
- Menos recurso (disco, memória, rede); mais fácil derrubar e subir de novo.
- **Segurança**: menor superfície de ataque.
- **Usuário diferente**: o estágio de build pode rodar como **root** (precisa de mais permissões); o de run roda como **usuário comum** (`USER app`), sem privilégio. (Ponto levantado na aula, "a Isa lembrou".)

## Container grande x vários pequenos

Pergunta da aula: quando faz sentido ter **um container gigante** em vez de vários pequenos?

- Faz sentido quando a aplicação tem **muitas dependências pesadas e acopladas** que você quer isoladas juntas. Ex.: modelo de ML com **TensorFlow** -> imagem naturalmente grande, e não dá para "quebrar a base".
- Distinção importante: *container pequeno que libera o servidor* (tamanho) **≠** *quebrar uma imagem gigante em vários serviços* (arquitetura).
- Caso do **monolito**: back, front e banco tudo num único Dockerfile, subido por um compose que chamava uma só imagem.
  - **Regra de ouro**: se **está em produção e funciona**, primeiro **dar suporte / garantir que continue funcionando**; só depois, em paralelo, planejar a melhoria (quebrar em serviços).

## Namespaces e cgroups (base técnica de containers)

Ver [06-namespaces-cgroups.md](06-namespaces-cgroups.md).

## Frases-chave para a dissertativa

- "Container isola processo; VM isola máquina inteira."
- "Imagem é imutável; container é a execução; mudou imagem, rebuild e nova tag."
- "Multi-stage separa build de runtime: imagem menor, mais segura, roda sem root."
- "Tag permite escolher a versão exata de dependências."
