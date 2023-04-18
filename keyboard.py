from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_main = KeyboardButton('Главное меню')

btn_values = KeyboardButton('Все валюты')
btn_smpl = KeyboardButton('Шаблоны')
btn_help = KeyboardButton('Помощь')
main_menu = (ReplyKeyboardMarkup(resize_keyboard=True)
             .add(btn_values, btn_smpl, btn_help))
btn_sample1 = KeyboardButton('Евро Доллар 1')
btn_sample2 = KeyboardButton('Евро Рубль 1')
btn_sample3 = KeyboardButton('Доллар Евро 1')
btn_sample4 = KeyboardButton('Доллар Рубль 1')
btn_sample5 = KeyboardButton('Рубль Евро 1')
btn_sample6 = KeyboardButton('Рубль Доллар 1')
samples = (ReplyKeyboardMarkup(resize_keyboard=True)
           .add(btn_sample1, btn_sample2, btn_sample3,
           btn_sample4, btn_sample5, btn_sample6, btn_main))
