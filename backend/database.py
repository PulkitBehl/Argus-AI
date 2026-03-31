import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine,Column,Integer,String,Text,DateTime 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL=os.getenv("DATABASE_URL","sqlite:///./argus.db")

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

class Document(Base):
    __tablename__="documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String,index=True)
    content = Column(Text)
    summary = Column(Text)
    language = Column(String)
    tags = Column(String)
    created_at = Column(DateTime,default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)