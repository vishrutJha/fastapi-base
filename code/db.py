# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# DB Connection
user_name = "user"
password = "password"
host = "db"
database_name = "sample_db"

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

# DB Engine
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

# Session Manager
session = scoped_session(
    # ORM Binder
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# model Model
Base = declarative_base()
# DB Query Handler
Base.query = session.query_property()
