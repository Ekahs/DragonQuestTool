from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import create_engine

import config

Base = declarative_base()


class BossList(Base):
    __tablename__ = 'boss_list_m'

    boss_list_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    boss_type = Column(SmallInteger, nullable=False)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, name, boss_type=99):
        self.name = name
        self.boss_type = boss_type

class BossWeak(Base):
    __tablename__ = 'boss_weak_t'

    boss_weak_id = Column(Integer, primary_key=True)
    boss_list_id = Column(Integer, ForeignKey('boss_list_m.boss_list_id'))
    fire = Column(String(16), nullable=False)
    ice = Column(String(16), nullable=False)
    storm = Column(String(16), nullable=False)
    thunder = Column(String(16), nullable=False)
    soil = Column(String(16), nullable=False)
    dirk = Column(String(16), nullable=False)
    light = Column(String(16), nullable=False)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, boss_list_id, fire, ice, storm, thunder, soil, dirk, light):
        self.boss_list_id = boss_list_id
        self.fire = fire
        self.ice = ice
        self.storm = storm
        self.thunder = thunder
        self.soil = soil
        self.dirk = dirk
        self.light = light



def init():
    engine = create_engine('sqlite:///' + config.DATABASE_FILE, convert_unicode=True)
    Base.metadata.create_all(engine)
