# Sistema de Gerenciamento de Estoque

Um sistema abrangente de gerenciamento de estoque projetado para pequenas empresas, construído usando Python e Flask. Este projeto inclui uma configuração Docker para simplificar a instalação em ambientes de desenvolvimento e produção.

## Índice
- [Introdução](#introdução)
- [Recursos](#recursos)
- [Tecnologias](#tecnologias)
- [Arquitetura](#arquitetura)
- [Primeiros Passos](#primeiros-passos)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Executando a Aplicação](#executando-a-aplicação)
- [Uso](#uso)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Introdução
Este Sistema de Gerenciamento de Estoque é uma aplicação web que ajuda pequenas empresas a gerenciar seu estoque de forma eficiente. O sistema permite que os usuários acompanhem produtos, entradas de estoque e saídas de estoque. A aplicação é construída usando Python e Flask e é containerizada usando Docker para garantir um processo de instalação suave tanto para ambientes de desenvolvimento quanto de produção.

## Recursos
- Autenticação e gerenciamento de usuários
- Gerenciamento de produtos (adicionar, atualizar, excluir produtos)
- Rastreamento de entradas e saídas de estoque
- Interface web responsiva
- Dockerizado para fácil implantação

## Tecnologias
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Banco de Dados:** SQLite (pode ser configurado para usar PostgreSQL, MySQL, etc.)
- **Containerização:** Docker

## Arquitetura
O sistema segue uma arquitetura simples com os seguintes componentes:
- **Usuário:** Gerencia autenticação e autorização
- **Produto:** Gerencia detalhes do produto
- **Entrada de Estoque:** Rastreamento de entradas de estoque
- **Saída de Estoque:** Rastreamento de saídas de estoque

![Esquema do Banco de Dados](https://diagrams.helpful.dev/d/d:8wvhXu7n)

## Primeiros Passos

### Pré-requisitos
- Docker
- Docker Compose

### Instalação
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/sistema-de-gerenciamento-de-estoque.git
   cd sistema-de-gerenciamento-de-estoque
Executando a Aplicação
Ambiente de Desenvolvimento
Construa e execute os containers Docker:

bash
Copiar código
docker-compose -f docker-compose.dev.yml up --build
Acesse a aplicação:
Abra seu navegador e navegue até http://localhost:5000.

Ambiente de Produção
Construa e execute os containers Docker:

bash
Copiar código
docker-compose -f docker-compose.prod.yml up --build
Acesse a aplicação:
Abra seu navegador e navegue até o endereço IP ou domínio do seu servidor.

Uso
Uma vez que a aplicação esteja em execução, você pode:

Registrar e fazer login como usuário
Adicionar, atualizar e excluir produtos
Acompanhar entradas e saídas de estoque
Contribuindo
Contribuições são bem-vindas! Por favor, faça um fork do repositório e crie um pull request com suas alterações. Certifique-se de que seu código segue os padrões de codificação do projeto e inclui testes apropriados.
