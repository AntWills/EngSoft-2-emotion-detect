# Imagem base oficial do Python
FROM python:3.10-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia os arquivos para dentro do container
COPY ./src/ ./src/
COPY requirements.txt .

# Instala dependências do sistema (ex: para compilar pacotes como numpy, etc.)
RUN apt-get update && apt-get install -y gcc

# Instala dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta usada pelo Uvicorn
EXPOSE 8000

ENV PYTHONPATH=/app/src

# Comando para iniciar o servidor
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
