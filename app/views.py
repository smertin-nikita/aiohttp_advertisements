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
        advert = await Advert.get_or_404(uid)
        await advert.delete()
        return web.json_response(dict(id=uid))

