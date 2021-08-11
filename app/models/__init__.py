from asyncpg import UniqueViolationError
from aiohttp import web
from gino import Gino

db = Gino()


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