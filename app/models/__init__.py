import aiopg
from aiohttp import web
from asyncpg import UniqueViolationError
from gino import Gino

db = Gino()


async def pool_pg(app):
    conf = app['config']['postgres']
    dsn = f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['database']}"
    async with aiopg.create_pool(dsn) as pool:
        app['pool_pg'] = pool
        yield
        pool.close()


async def init_pg(app):
    conf = app['config']['postgres']
    dsn = f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['database']}"
    app['db'] = await db.set_bind(dsn)


async def close_pg(app):
    await app['db'].pop_bind().close()


class BaseModelMixin:

    @classmethod
    async def all(cls):
        return await cls.query.gino.all()

    @classmethod
    async def get_or_404(cls, uid):
        instance = await cls.get(uid)
        if instance:
            return instance
        raise web.HTTPNotFound()

    @classmethod
    async def add(cls, **kwargs):
        try:
            instance = await cls.create(**kwargs)
        except UniqueViolationError:
            raise web.HTTPBadRequest()
        return instance

    def put(self, kwargs):
        pass

    @classmethod
    async def delete(cls, uid):
        instance = await cls.query.gino.delete(uid)
        if instance:
            return instance
        raise web.HTTPNotFound()

    @classmethod
    def find_by_attr(cls, kwargs):
        pass