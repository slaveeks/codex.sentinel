from aiohttp import web

import config
import handlers
import telegram
from urllib.parse import urlparse


if __name__ == '__main__':
    app = web.Application()
    url = urlparse(config.URL)
    app.router.add_post('/', handlers.telegram_callbacks)
    app.router.add_post('/{token}/set_duty', handlers.duty)
    app.router.add_post('/problem', handlers.problem)
    telegram.set_webhook()
    web.run_app(app, host='127.0.0.1', port=1338)
