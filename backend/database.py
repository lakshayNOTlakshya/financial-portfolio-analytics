from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://portfolio:portfolio@localhost:5432/portfolio_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass