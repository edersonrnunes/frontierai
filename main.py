from fastapi import FastAPI

from app.infrastructure.database import ItemModels, PessoaModel
#from app.infrastructure.database import PessoaModel
from app.infrastructure.database.session import engine
from app.web.endpoints import router as api_router

# Cria as tabelas no banco de dados (se não existirem)
# Em um ambiente de produção, você provavelmente usaria Alembic para gerenciar migrações.
ItemModels.Base.metadata.create_all(bind=engine)
PessoaModel.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API com DDD",
    description="Uma API de exemplo com FastAPI e PostgreSQL seguindo princípios DDD.",
    version="1.0.0",
)

app.include_router(api_router)

