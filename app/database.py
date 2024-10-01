from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Retrieve environment variables
db_user = os.getenv('DB_USER', 'postgres')
db_pass = os.getenv('DB_PASS', '123456')
db_host = os.getenv('DB_HOST', 'localhost')
db_name = os.getenv('DB_NAME', 'postgres')

# Construct the database URL
SQLALCHEMY_DATABASE_URL = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models
Base = declarative_base()
