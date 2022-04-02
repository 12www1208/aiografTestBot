import aiogram
from  aiogram import Dispatcher, executor, types, Bot

bot  = Bot(token='5146638518:AAExU7G5-hFexzI2bNdPJBAC1giRbCwbMx8')

dis = Dispatcher(bot)

@dis.message_handler(commands='start')
async def start(message : types.Message):
    await message.answer('Привет')

if __name__ == '__main__':
    executor.start_polling(skip_updates=True)