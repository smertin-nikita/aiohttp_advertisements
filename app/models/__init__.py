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
    async def get(cls, uid):
        getter = db.bake(cls.query.where(cls.id == db.bindparam("uid")))
        return await getter.one_or_none(uid=uid)

    async def add(self):
        return await self.create()

    def put(self, kwargs):
        pass

    @classmethod
    def find_by_attr(cls, kwargs):
        pass