# Use a imagem base do Python
FROM python:3.8.10

# Defina a pasta de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o projeto para o container
COPY . /app/

# Execute as migrações do banco de dados e inicie o servidor
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
