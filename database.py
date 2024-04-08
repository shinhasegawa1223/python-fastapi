from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://fastapiuser:fastapipass@0.0.0.0:5454/fleamarket"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit= False,autoflush=False,bind=engine)


# 規定クラス
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()