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

# Exponha a porta que o Django vai rodar
EXPOSE 8000

# Execute as migrações do banco de dados e inicie o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
