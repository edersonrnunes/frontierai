import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv(verbose=True)

## Código para utilizar Supabase como banco de dados PostgreSQL
# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")

## Descomentar se não utilizar Supabase ##
## Este código utiliza DB PostgreSQL utilizando containers Docker
## Conexão local para debug (Container local)
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/mydatabase"
## Conexão para utilizar dentro do Docker Compose
#SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/mydatabase")
#SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") 

#engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()