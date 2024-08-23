
# my_church

Este é o repositório do projeto **my_church**, uma aplicação Django para gerenciar atividades de igrejas, incluindo permissões, comunicação interna, gestão de finanças, e muito mais.

## Configuração do Ambiente de Desenvolvimento

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone git@github.com:lpcoutinho/my_church.git
cd my_church
```

### 2. Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

- No Linux/MacOS:
    ```bash
    source venv/bin/activate
    ```

- No Windows:
    ```bash
    venv\Scripts\activate
    ```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```plaintext
cp .env.example .env
```

Edite o arquivo `.env` para incluir suas configurações locais, como detalhes do banco de dados e chaves de API.

### 5. Configurar o Banco de Dados

Se estiver usando PostgreSQL ou outro banco de dados, configure as variáveis de ambiente no `.env`. Para aplicar as migrações iniciais e configurar o banco de dados, execute:

```bash
python manage.py migrate
```

### 6. Rodar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Acesse a aplicação no navegador através do endereço: `http://localhost:8000`

### 7. Criar um Superusuário

Para acessar o admin do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

### 8. Contribuir

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir um pull request ou relatar problemas.

---

Este é um ponto de partida básico. Conforme o projeto evolui, mais detalhes sobre a configuração de Docker, Celery, Redis e outras ferramentas serão adicionados.

## Estrutura do Projeto

- `igreja/`: Contém a configuração principal do projeto Django.
- `core/`: Aplicativo principal do projeto (mais aplicativos serão adicionados conforme o desenvolvimento avança).
- `core/payment_processor.py`: Módulo para processar pagamentos via Mercado Pago.
- `core/templates/`: Contém os templates HTML para as diferentes páginas da aplicação.
- `core/static/core/styles.css`: Arquivo de estilos CSS para a aplicação.
- `venv/`: Ambiente virtual para gerenciar as dependências (não incluído no repositório).
- `requirements.txt`: Lista de dependências do projeto.
- `.env.example`: Arquivo de exemplo para configuração de variáveis de ambiente.

### 9. Licença

Este projeto está licenciado sob os termos da Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 10. Contato

Para mais informações ou dúvidas, entre em contato pelo [LinkedIn](https://www.linkedin.com/in/luizpaulocoutinho/).
