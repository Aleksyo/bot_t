from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в бот Энергосбыта', reply_markup=kb_client)


# @dp.message_handler(commands=['work'])
async def command_work(message: types.Message):
    await bot.send_message(message.from_user.id, 'Режим работы с 8:00 до 17:15')


# @dp.message_handler(commands=['place'])
async def command_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бабушкина 38')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_work, commands=['Режим_работы'])
    dp.register_message_handler(command_place, commands=['Расположение'])
