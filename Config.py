from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from main import *
from Settings import TOKEN
from Lang import LANGDICT
import sqlite3
Trans = GoogleTranslator()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    log_in = InlineKeyboardButton('Вход', callback_data='login')
    all_misses = InlineKeyboardButton('Языки', callback_data='lang')
    commands_mean = InlineKeyboardButton('Команды', callback_data='show_comm_mean')
    keyboard.add(log_in, all_misses, commands_mean )
    await bot.send_message(message.chat.id, "Привет, я бот-переводчик", reply_markup=keyboard)

# @dp.callback_query_handler(lambda a: a.data == 'login')
# if "en" in text:
# await  send_message(message.chat.id,"Вы выбрали Английский") тоже самое с elif (то же самое, что и if), else (в конце всегда одно).



@dp.callback_query_handler(lambda a: a.data == "lang")
async def choose (call: types.callback_query):
    await bot.send_message(call.message.chat.id, "Выберите язык")


@dp.message_handler()
async def add_miss(message: types.Message):
    text = message.text
    await bot.send_message(message.chat.id, f"Вы выбрали {LANGDICT[text]}")
# Нужно будет сделать глобальную переменную, которая будет хранить в себе язык. После нужно создать обработчик с командой Translate. Он будет храниться в Language.Она будет хранить язык. Старт будет начинаться со слов транслейт. Нужно будет возвращать язык, который будет получаться. Send text.




executor.start_polling(dp)