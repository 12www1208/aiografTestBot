#sqlite3------------------------------------------
import sqlite3
connect = sqlite3.connect('src/db/async.db')
cursors = connect.cursor()

#aiogram----------------------------------------------
import aiogram
from  aiogram import Dispatcher, executor, types, Bot
from aiogram.dispatcher.filters.state import State, StatesGroup
#---------------------------------------------------------------

bot  = Bot(token='5146638518:AAExU7G5-hFexzI2bNdPJBAC1giRbCwbMx8')

dis = Dispatcher(bot)

class Order(StatesGroup):
    product = State()
    pay = State()

@dis.message_handler(commands='start')
async def start(message : types.Message):
    await message.answer('Привет')


@dis.message_handler(lambda message : message.text == "Menu")
async def prosmltor_Menu(message : types.Message):
    await
    cursors.execute(f'SELECT NamePiza FROM menu')


if __name__ == '__main__':
    executor.start_polling(dis, skip_updates=True)