FROM python:3.12-slim
WORKDIR /app/training
COPY training/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY training/treino.ipynb .
CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--ExecutePreprocessor.kernel_name=python3", "treino.ipynb", "--output-dir", "/tmp"]
