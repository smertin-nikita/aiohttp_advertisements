from sqlalchemy import create_engine, MetaData

from app.settings import config
from app.db import advertisement


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[advertisement])


def sample_data(engine):
    conn = engine.connect()
    # conn.execute(question.insert(), [
    #     {'question_text': 'What\'s new?',
    #      'pub_date': '2015-12-15 17:17:49.629+02'}
    # ])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)