from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

db_url = f'sqlite:///{db_path}/db.sqlite3'

# Cria engine
engine = create_engine(db_url, echo=False)

# Cria classe base
Base = declarative_base()

# Cria sessão
Session = sessionmaker(bind=engine)

# Exportando Base e Session
__all__ = ['Base', 'Session']
