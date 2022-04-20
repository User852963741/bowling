from sqlalchemy import Column, String, Integer, ForeignKey, Table, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import date

engine = create_engine("sqlite:///db.db")
Base = declarative_base()

game_players = Table('Game_players', Base.metadata,
    Column('game_id', Integer, ForeignKey('game.id')),
    Column('player_id', Integer, ForeignKey('player.id'))
)

# game_results = Table('Game_results', Base.metadata,
#     Column('game_id', Integer, ForeignKey('game.id')),
#     Column('result_id', Integer, ForeignKey('result.id'))
# )

class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column("First_name", String)
    lname = Column("Last_name", String, nullable=True)
    age = Column("Age", Integer, nullable=True)
    games = relationship('Game', secondary=game_players, back_populates='players')

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __repr__(self):
        return f"{self.id}.{self.fname}"

class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column("Date", Date, default=date.today)
    players = relationship('Player', secondary=game_players, back_populates='games')
    results = relationship('Result', back_populates='game')

    def __repr__(self):
        return f"{self.id}. {self.date}"

class Result(Base):
    __tablename__ = "result"
    id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column("Game_id", Integer, ForeignKey('game.id'))
    player_id = Column("Player_ID", Integer, ForeignKey('player.id'))
    score = Column("Score", Integer)
    game = relationship('Game', back_populates='results')

    def __repr__(self):
        return f"{self.id}. game {self.game_id}, player {self.player_id}, score {self.score}"

Base.metadata.create_all(engine)