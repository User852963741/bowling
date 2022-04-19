from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine("sqlite:///db.db")
session = sessionmaker(bind=engine)()

players = session.query(Result).all()
for i in players:
    print(i)