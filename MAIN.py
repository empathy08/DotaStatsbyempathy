import aiogram.types
import requests
import json
import webbrowser
import time
import os

import redis
import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.markdown import hbold, hcode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from bs4 import BeautifulSoup

from main_stats import *
from benchmarks import *
from fantasypoints import *
from config import TOKEN

import sys
sys.path.append("venv\lib\site-packages\PIL")

BOT_TOKEN = TOKEN
DB_FILENAME = "DotaStats.db" # Настройки базы данных
logging.basicConfig(level=logging.INFO) # Настройки логирования

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

redis_db = redis.Redis(host='localhost', port=6379, db=0)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Добро пожаловать! Введи свой ID:")
    # Получаем id пользователя и сохраняем его в базе данных Redis
    user_id = message.from_user.id
    redis_db.set(f'id{user_id}', user_id)


id_reminder = types.Message() #запоминает сообщ юзера чтобы потом в def scheduler брать из него айдишник


@dp.message_handler()
async def getting_id(message: types.Message):
    global id_reminder

    id_reminder = message

    profile_id = message.text

    redis_db.set(f'profile{message.from_user.id}', str(profile_id))

    id_button_markup = InlineKeyboardMarkup(widht=1)
    id_button = InlineKeyboardButton("Начать", callback_data="Начать")
    id_button_markup.add(id_button)

    profid1 = str(redis_db.get(f'profile{message.from_user.id}'))[2:-1]
    profile_url1 = "https://api.opendota.com/api/players/" + profid1 + "/matches"
    r21 = requests.get(profile_url1)
    profile_data1 = json.loads(r21.text)
    last_match_id1 = (profile_data1[1])['match_id']

    redis_db.set(f'last{message.from_user.id}', str(last_match_id1))

    await message.reply("Ваш ID успешно сохранен! Нажмите на кнопку, чтобы начать.", reply_markup=id_button_markup)


@dp.callback_query_handler(text="Начать")
async def start_func(message: types.Message):
    await bot.send_message(message.from_user.id, "Загружаю информацию по вашему последнему матчу:\n(В первый раз это может занять чуть больше времени)\nP.S. КНОПКУ НУЖНО НАЖАТЬ ТОЛЬКО ПРИ ПЕРВОМ ЗАПУСКЕ, ДАЛЬШЕ БОТ САМ БУДЕТ ОТПРАВЛЯТЬ ВАМ СТАТИСТИКУ.")
    await scheduler()


async def send_stats(message: types.Message):

    profid = str(redis_db.get(f'profile{message.from_user.id}'))[2:-1]
    profile_url = "https://api.opendota.com/api/players/" + profid + "/matches"
    r2 = requests.get(profile_url)
    profile_data = json.loads(r2.text)
    last_match_id = (profile_data[0])['match_id']
    last_match_hero_id = (profile_data[0])['hero_id']  # получаю айди матча и айди героя на котором играл

    last_match_url = f"https://api.opendota.com/api/matches/{last_match_id}"
    r1 = requests.get(last_match_url)
    last_match_data = json.loads(r1.text)
    list_of_players = last_match_data['players']  # это массив из статы 10 игроков

    player_slot = 0  # тут цикл для получения индекса нужного игрока в массиве игроков
    for d in list_of_players:
        if d['hero_id'] == last_match_hero_id:
            break
        player_slot += 1

    last_match_player_stats = list_of_players[player_slot]  # стата интересующего игрока

    # Получаем текущий айди послледнего матча
    previous_state = str(redis_db.get(f'last{message.from_user.id}'))[2:-1]
    current_state = str(last_match_id)
    # Проверяем, изменился ли айди
    if str(current_state) != str(previous_state):

        # прасинг матча
        webbrowser.register('Chrome', None,
                            webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new(f"https://opendota.com/request#{last_match_id}")
        time.sleep(30)

        os.system("taskkill /im chrome.exe /f")

        redis_db.set(f'last{message.from_user.id}', str(last_match_id))

        overview(last_match_player_stats)
        benchmarks(last_match_player_stats["benchmarks"])
        fantasy(last_match_player_stats)

        # отправляем изображения пользователю
        photo1 = aiogram.types.InputMediaPhoto(open('images/mainstatsimg.jpg', 'rb'))
        photo2 = aiogram.types.InputMediaPhoto(open('images/Benchmarksimg.jpg', 'rb'))
        photo3 = aiogram.types.InputMediaPhoto(open('images/Fantasypointsimg.jpg', 'rb'))

        await bot.send_media_group(message.from_user.id, [photo1, photo2, photo3])
    else:
        pass


# Задаем периодическую проверку состояния сайта
async def scheduler():
    while True:
        await send_stats(id_reminder)
        await asyncio.sleep(300)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())

    executor.start_polling(dp)




