import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboard as navig
import extensions as ext
from config import values_dict, START, HELP
from TOKEN import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply((START.format(message.from_user))
                        + HELP,
                        reply_markup=navig.main_menu)


@dp.message_handler(commands=['samples'])
async def send_samples(message: types.Message):
    await message.answer('Выберите шаблон ⬇️ ',
                         reply_markup=navig.samples)


@dp.message_handler(commands=['values'])
async def values(message: types.Message):
    text = 'Доступные валюты:'
    for key, val in values_dict.items():
        text = '\n'.join((text, '💹 '
                          + key.capitalize()
                          + ' - ' + val))
    await message.answer(text)


@dp.message_handler()
async def send_change(message: types.Message):
    try:
        if message.text == 'Главное меню':
            await message.answer(f'{message.text} ⬇️ ',
                                 reply_markup=navig.main_menu)
        elif message.text == 'Шаблоны':
            await message.answer(f'{message.text} ⬇️ ',
                                 reply_markup=navig.samples)
        else:
            mess = ext.process_message(message.text, message)
            await message.answer(mess)
    except Exception as e:
        await message.answer(e)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
