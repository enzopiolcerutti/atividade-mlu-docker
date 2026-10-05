# 06 · Namespaces e cgroups

O professor não confirmou que cai ("dê uma passadinha no capítulo"). Conceito curto para ter na ponta da língua. **Confira com o capítulo do livro de Docker.**

Container não é uma "mini-VM": é um **processo Linux comum** com dois mecanismos do kernel:

| Mecanismo | Faz o quê | Resumo |
|---|---|---|
| **Namespaces** | **Isolamento**: o que o processo *enxerga* | PID, NET, MNT (filesystem), UTS (hostname), IPC, USER |
| **cgroups** (control groups) | **Limite de recursos**: o que o processo *pode usar* | CPU, memória, I/O |

- Exemplo namespace PID: dentro do container o processo principal é o PID 1; no host ele tem outro PID.
- Exemplo namespace NET: cada container tem sua interface/IP.
- Exemplo cgroup: `docker run --memory=256m --cpus=0.5 ...`.
- Containers **compartilham o kernel do host** (por isso um container Linux não roda nativamente "como Linux" em macOS: Docker Desktop usa uma VM Linux por baixo).
- VM x container: VM tem kernel próprio (hypervisor); container usa o kernel do host (mais leve, isolamento mais fraco).
