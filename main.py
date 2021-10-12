from aiohttp import web
routes = web.RouteTableDef()


@routes.post('/problem')
async def problem(request):
    text = request['post']['text']
    if text != '':
        pass

@routes.post('/duty')
async def duty(request):
    username = request['post']['username']
    date = request['post']['date']
    notify_token = request['post']['token']


@routes.post('/telegram')
async def telegram(request):
    pass




if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='0.0.0.0', port=8080)
