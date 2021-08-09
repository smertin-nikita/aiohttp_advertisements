from datetime import datetime

import aiopg
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


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
