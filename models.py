from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///db.db")
Base = declarative_base()

class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column("First_name", String)
    lname = Column("Last_name", String)
    age = Column("Age", Integer)

    def __repr__(self):
        return

class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column("Date", String)
    player_id = Column("Winner_ID", Integer, ForeignKey('player.id'), nullable=True)
    result_id = Column("Winner_score_ID", Integer, ForeignKey('result.id'), nullable=True)
    player = relationship('Player')
    result = relationship('Result')

    def __repr__(self):
        return

class Result(Base):
    __tablename__ = "result"
    id = Column(Integer, primary_key=True)
    game_id = Column("Game_ID", Integer, ForeignKey('game.id'))
    player_id = Column("Player_ID", Integer, ForeignKey('player.id'))
    score = Column("Score", Integer)
    game = relationship('Game')
    player = relationship('Player')

    def __repr__(self):
        return

Base.metadata.create_all(engine)