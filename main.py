from fastapi import FastAPI

from app.infrastructure.database.session import Base, engine
# Import all models to ensure they are registered with the Base metadata
from app.infrastructure.database import EnderecoModel, ItemModels, PessoaModel
from app.web.endpoints import router as api_router

# Cria as tabelas no banco de dados (se não existirem)
# Em um ambiente de produção, você provavelmente usaria Alembic para gerenciar migrações.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API com DDD",
    description="Uma API de exemplo com FastAPI e PostgreSQL seguindo princípios DDD.",
    version="1.0.0",
)

app.include_router(api_router)
