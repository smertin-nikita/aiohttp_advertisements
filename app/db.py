from datetime import datetime

from sqlalchemy import MetaData, Table, Integer, Column, String, Text, DateTime

meta = MetaData()


# Объявление
advertisement = Table(
    'advertisement', meta,

    Column('id', Integer, primary_key=True),
    Column('title', String(64), index=True, unique=True, nullable=False),
    Column('description', Text, index=True, nullable=False, default=''),
    Column('creator_id', Integer, db.ForeignKey('user.id')),
    Column('created_on', DateTime, default=datetime.utcnow)
)
