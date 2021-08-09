import json

from aiohttp import web

from app import db

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.Response(text='Hello Aiohttp!')


@routes.view('/advertisements/')
class AdvertisementList(web.View):
    async def get(self):
        async with self.request.app['db'].acquire() as conn:
            cursor = await conn.execute(db.advertisement.select())
            records = await cursor.fetchall()
            advertisements = [dict(_) for _ in records]
        return web.Response(body=json.dumps({"advertisements": advertisements}))


@routes.view('/advertisements/{id}')
class Advertisement(web.View):
    async def get(self):
        async with self.request.app['db'].acquire() as conn:
            advertisement_id = self.request.match_info['id']
            print(advertisement_id)
            try:
                advertisement = await db.get_advertisements(conn, advertisement_id)
            except db.RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            return web.Response(body=json.dumps({"advertisement": advertisement}))


    # async def post(self):
    #     return await post_resp(self.request)