# ---- Estágio 1: build (instala dependências; pode ter ferramentas de compilação) ----
FROM python:3.12-slim AS build
WORKDIR /install
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install/deps -r requirements.txt

# ---- Estágio 2: runtime (só o necessário para rodar) ----
FROM python:3.12-slim
WORKDIR /app

# copia só as dependências já instaladas, sem cache/ferramentas de build
COPY --from=build /install/deps /usr/local
COPY app.py .

# usuário comum: o runtime não precisa de root
RUN useradd --create-home app
USER app

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
