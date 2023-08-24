from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
import psycopg2, time


SQLALCHEMY_DATABASE_URL = "postgresql://hasanalay:1973@localhost:5432/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# region Db Connection
# Connection to PostgreSQL DB
# while True:
#     try:
#         connection = psycopg2.connect(host='localhost', database='fastapi', user='hasanalay', password='1973', cursor_factory=RealDictCursor)
#         cursor = connection.cursor()
#         print("Connection to PostgreSQL DB successful")
#         break
#     except Exception as e:
#         print(f"The error '{e}' occurred")
#         time.sleep(2)
# endregion