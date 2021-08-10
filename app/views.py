import json
from aiohttp import web
from app.models.adverts import Advert

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.Response(text='Hello Aiohttp!')


@routes.view('/advertisements')
class AdvertList(web.View):
    async def get(self):
        adverts = await Advert.all()
        return web.json_response([advert.to_dict() for advert in adverts])

    async def post(self):
        data = await self.request.json()
        advert = await Advert.add(**data)
        return web.json_response(advert.to_dict())


@routes.view('/advertisements/{uid}')
class Advertisement(web.View):
    async def get(self):
        uid = int(self.request.match_info['uid'])
        advert = await Advert.get_or_404(uid)
        return web.json_response(advert.to_dict())

    async def delete(self):
        uid = int(self.request.match_info['uid'])
        return  await Advert.delete(uid)





# @routes.view('/advertisements/')
# class AdvertisementList(web.View):
#     async def get(self):
#         async with self.request.app['db'].acquire() as conn:
#             cursor = await conn.execute(db.advertisement.select())
#             records = await cursor.fetchall()
#             advertisements = [dict(_) for _ in records]
#         return web.Response(
#             body=json.dumps({"advertisements": advertisements}, default=lambda obj: obj.strftime('%d:%m:%Y')),
#             content_type='application/json'
#         )
#
#
# @routes.view('/advertisements/{id}')
# class Advertisement(web.View):
#     async def get(self):
#         async with self.request.app['db'].acquire() as conn:
#             advertisement_id = self.request.match_info['id']
#             try:
#                 advertisement = await db.get_advertisement(conn, advertisement_id)
#             except db.RecordNotFound as e:
#                 raise web.HTTPNotFound(text=str(e))
#             return web.Response(
#                 body=json.dumps({"advertisement": advertisement}),
#                 content_type='application/json'
#             )


    # async def post(self):
    #     return await post_resp(self.request)