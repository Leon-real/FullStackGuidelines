from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# PostgreSQL 데이터베이스 URL
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL)

# SessionLocal 클래스 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성
Base = declarative_base()

# 데이터베이스 세션을 얻기 위한 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()