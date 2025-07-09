# frontierai Template
Esse é o template para estruturar sua API REST utilizando os princípios do Domain-Driven Design (DDD). Isso tornará sua aplicação mais robusta, escalável e alinhada com as regras de negócio.

Vou refatorar o projeto fornecido para seguir uma arquitetura em camadas, um padrão comum em DDD, separando as responsabilidades em:

# Domain (Domínio):
    O coração da aplicação. Contém as entidades, objetos de valor e a lógica de negócio principal, sem depender de detalhes de infraestrutura (como banco de dados ou frameworks web).
# Application (Aplicação):
    Orquestra as tarefas e casos de uso. Utiliza o domínio para executar as ações solicitadas pelas camadas externas (como a API).
# Infrastructure (Infraestrutura):
    Contém os detalhes técnicos, como o framework web (FastAPI), implementações de repositórios (SQLAlchemy), configuração de banco de dados, etc.

A nova estrutura de arquivos ficará assim:
.
├── app/
│   ├── __init__.py
│   ├── application/
│   │   ├── __init__.py
│   │   ├── dtos.py
│   │   └── use_cases.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities.py
│   │   └── repositories.py
│   └── infrastructure/
│       ├── __init__.py
│       ├── database/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── repositories.py
│       │   └── session.py
│       └── web/
│           ├── __init__.py
│           ├── dependencies.py
│           └── endpoints.py
├── .env
├── docker-compose.yml
├── Dockerfile
├── main.py
└── requirements.txt


## Documen
https://fastapi.tiangolo.com/tutorial/response-model/

# docker compose
docker-compose up --build
docker-compose down

 # criando container PostgreSQL para debug local
POSTGRES_USER=user
POSTGRES_PASSWORD=password

docker run --name some-postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres


Como Executar
Salve os arquivos acima na estrutura de pastas correta.
Instale o uvicorn, que é um servidor ASGI para rodar sua aplicação:
bash
pip install "uvicorn[standard]"
A partir do diretório raiz do seu projeto (frontierai), execute o servidor:
bash
uvicorn main:app --reload
Agora, a mágica acontece! Você pode acessar a documentação interativa do Swagger UI no seu navegador em:

http://127.0.0.1:8000/docs
E a documentação alternativa do ReDoc em:

http://127.0.0.1:8000/redoc
Lá você poderá ver e interagir com seus endpoints POST /items/ e GET /items/, com schemas, exemplos e a capacidade de testá-los diretamente pelo navegador.
