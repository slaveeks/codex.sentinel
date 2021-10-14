import json

from models import Duties
import datetime
import telegram



async def telegram_callbacks(request):
    print(123)
    data = await request.json()
    text = data["message"]["text"]
    chat_id = data["message"]["chat"]["id"]
    username = data["message"]["from"]["username"]
    if telegram.is_command(text):
        if not Duties.check_chat_id(chat_id):
            Duties.generate_token(username, chat_id)
        token = Duties.get_token(chat_id)
        await telegram.send_message(token, chat_id)





async def duty(request):
    token = request.match_info['token']
    if Duties.check_token(token):
        post = await request.post()
        username = post.get('username')
        date = post.get('date') #дд.мм.гггг
        duty = Duties(username, date)
        duty.new_duty()
        print(username, date)

async def problem(request):
    post = await request.post()
    text = post.get('text')
    if text == '':
        print("Message is empty")
    today = datetime.date.today()
    date = str(today.day)+'.'+str(today.month)+'.'+str(today.year)
    chat_id = Duties.find_duty(date=date)
    if chat_id != None:
        await telegram.send_message(text, chat_id)




