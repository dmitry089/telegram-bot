from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import config
Base = declarative_base()
class User(Base):
    tablename = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(100))
    first_name = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
# Пока оставляем простую структуру
engine = create_engine(config.DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)