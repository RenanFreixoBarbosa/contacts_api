from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from repository_layer.models.base import Base
from repository_layer.models.contact_model import Contact

db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

db_url = f"sqlite:///{db_path}/db.sqlite3"
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)

# Cria as tabelas
Base.metadata.create_all(engine)
