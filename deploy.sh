#!/bin/bash

# Navegar até o diretório do repositório

cd /root/stock-management-system

# Puxar as últimas alterações do repositório
git pull origin main

# Parar os contêineres em execução
docker-compose down

# Reconstruir os contêineres
docker-compose build

# Reiniciar os contêineres
docker-compose up -d

echo "Deploy completed!"
