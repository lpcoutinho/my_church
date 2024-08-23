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

### 4. Configurar o Banco de Dados

Por padrão, o Django está configurado para usar SQLite. Se você deseja usar PostgreSQL, MySQL, ou outro banco de dados, altere as configurações em `settings.py`.

Para aplicar as migrações iniciais e configurar o banco de dados, execute:

```bash
python manage.py migrate
```

### 5. Rodar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Acesse a aplicação no navegador através do endereço: `http://localhost:8000`

### 6. Criar um Superusuário

Para acessar o admin do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

### 7. Contribuir

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir um pull request ou relatar problemas.

---

Este é um ponto de partida básico. Conforme o projeto evolui, você pode adicionar mais detalhes sobre como configurar o Docker, Celery, Redis, e outras ferramentas que serão usadas no projeto.

### 8. Estrutura do Projeto

Um breve resumo sobre a estrutura do projeto pode ser útil:

## Estrutura do Projeto

- `igreja/`: Contém a configuração principal do projeto Django.
- `core/`: Aplicativo principal do projeto (mais aplicativos serão adicionados conforme o desenvolvimento avança).
- `venv/`: Ambiente virtual para gerenciar as dependências (não incluído no repositório).
- `requirements.txt`: Lista de dependências do projeto.

### 9. Licença

Este projeto está licenciado sob os termos da Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 10. Contato


Para mais informações ou dúvidas, entre em contato pelo [Linkedin](https://www.linkedin.com/in/luizpaulocoutinho/).