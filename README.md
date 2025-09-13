# Docling com Interface de Upload - Guia Docker

Este guia explica como executar a aplicação Docling com interface de upload usando Docker.

## Arquivos Docker

A configuração Docker inclui três arquivos principais:

1. **docker-compose.yml** - Orquestra o contêiner e configura volumes e portas
2. **Dockerfile** - Define como a imagem Docker deve ser construída
3. **requirements.txt** - Lista as dependências Python necessárias

## Requisitos

- Docker instalado em seu sistema
- Docker Compose instalado em seu sistema

## Como Executar

1. **Preparação dos arquivos**:
   - Certifique-se de que os arquivos `docker-compose.yml`, `Dockerfile`, `requirements.txt` e `app.py` estejam no mesmo diretório

2. **Construir e iniciar o contêiner**:
   ```bash
   docker-compose up -d
   ```
   O parâmetro `-d` executa o contêiner em segundo plano.

3. **Acessar a aplicação**:
   - Abra seu navegador
   - Acesse: http://localhost:8080

4. **Parar a aplicação**:
   ```bash
   docker-compose down
   ```

## Estrutura de Volumes

- A pasta `uploads` é mapeada como um volume para persistência de dados
- Isso permite que os arquivos enviados sejam acessíveis tanto dentro quanto fora do contêiner

## Personalização

Para alterar a porta da aplicação, edite o arquivo `docker-compose.yml`:

```yaml
ports:
  - "NOVA_PORTA:8080"
```

Por exemplo, para usar a porta 9090:
```yaml
ports:
  - "9090:8080"
```

## Solução de Problemas

Se encontrar problemas ao executar a aplicação:

1. **Verificar logs do contêiner**:
   ```bash
   docker-compose logs
   ```

2. **Reiniciar o contêiner**:
   ```bash
   docker-compose restart
   ```

3. **Reconstruir a imagem**:
   ```bash
   docker-compose build --no-cache
   docker-compose up -d
   ```

## Notas Adicionais

- A aplicação dentro do contêiner executa em modo de depuração (debug)
- Para ambientes de produção, considere ajustar as configurações de segurança
- O contêiner reinicia automaticamente em caso de falha (configuração `restart: unless-stopped`)