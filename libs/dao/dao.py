from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

import config

engine = create_engine('sqlite:///' + config.DATABASE_FILE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
