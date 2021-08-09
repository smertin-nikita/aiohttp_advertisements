from datetime import datetime

import aiopg.sa
from sqlalchemy import MetaData, Table, Integer, Column, String, Text, DateTime

meta = MetaData()


# Объявление
advertisement = Table(
    'advertisement', meta,

    Column('id', Integer, primary_key=True),
    Column('title', String(64), index=True, unique=True, nullable=False),
    Column('description', Text, index=True, nullable=False, default=''),
    # Column('creator_id', Integer, ForeignKey('user.id')),
    Column('created_on', DateTime, default=datetime.utcnow)
)


async def init_pg(app):
    conf = app['config']['postgres']
    dsn = f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['database']}"
    engine = await aiopg.sa.create_engine(
        dsn=dsn,
        minsize=1,
        maxsize=2
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
