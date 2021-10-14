import aiohttp
import config
import json
import requests


def set_webhook():
        headers = {
            'Content-Type': 'application/json'
        }
        url = {
            'url': config.URL
        }
        requests.post('https://api.telegram.org/bot'+config.TOKEN+'/setWebhook', data=json.dumps(url),
                                headers=headers)


async def get_bot_name():
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://api.telegram.org/bot'+config.TOKEN+'/getMe')
        data = await response.json()


async def send_message(text, chat_id):
    headers = {
        'Content-Type': 'application/json'
    }
    message = {
        'chat_id': chat_id,
        'text': text
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.telegram.org/bot'+config.TOKEN+'/sendMessage',
                                data=json.dumps(message),
                                headers=headers, ssl=False) as resp:
            response = await resp.text()
            print(response)

def is_command(text):
    if text == "/start":
        return True
    return False




