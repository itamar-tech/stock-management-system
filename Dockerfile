# Usar a imagem oficial do Python como base
FROM python:3.8-slim-buster

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de requisitos
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que a aplicação Flask roda
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
