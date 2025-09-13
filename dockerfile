FROM python:3.11-slim

# Cria um usuário não root
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Instalar dependências do sistema necessárias
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# Copiar os arquivos de requisitos primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app.py .
RUN mkdir -p uploads

# Ajusta permissões
RUN chown -R appuser:appuser /app

# Adiciona a permissão de escrita para o diretório de uploads
RUN chmod 777 /app/uploads

# Definir o diretório HOME para o usuário appuser
ENV HOME /app

# Mudar para usuário não-root
USER appuser

# Expor a porta que a aplicação usa
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["python", "app.py"]