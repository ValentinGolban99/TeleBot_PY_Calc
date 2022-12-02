from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = InlineKeyboardMarkup(row_width = 4)

button_1 = InlineKeyboardButton(text = '7', callback_data = 'but_7' )
button_2 = InlineKeyboardButton(text = '8', callback_data = 'but_8')
button_3 = InlineKeyboardButton(text = '9', callback_data = 'but_9')
button_4 = InlineKeyboardButton(text = '/', callback_data = 'but_del')
but_row_1 = [button_1, button_2, button_3, button_4]

button_5 = InlineKeyboardButton(text = '4', callback_data = 'but_4' )
button_6 = InlineKeyboardButton(text = '5', callback_data = 'but_5')
button_7 = InlineKeyboardButton(text = '6', callback_data = 'but_6')
button_8 = InlineKeyboardButton(text = '*', callback_data = 'but_mult')
but_row_2 = [button_5, button_6, button_7, button_8]

button_9 = InlineKeyboardButton(text = '1', callback_data = 'but_1' )
button_10 = InlineKeyboardButton(text = '2', callback_data = 'but_2')
button_11 = InlineKeyboardButton(text = '3', callback_data = 'but_3')
button_12 = InlineKeyboardButton(text = '-', callback_data = 'but_minus')
but_row_3 = [button_9, button_10, button_11, button_12]

button_13 = InlineKeyboardButton(text = '0', callback_data = 'but_0' )
button_14 = InlineKeyboardButton(text = 'ON', callback_data = 'but_ON')
button_15 = InlineKeyboardButton(text = '.', callback_data = 'but_tochka')
button_16 = InlineKeyboardButton(text = '+', callback_data = 'but_sum')
but_row_4 = [button_13, button_14, button_15, button_16]

# Обратите внимание на конструкцию *but_row_1. Звёздочка используется для распаковки списка.

kb.add(*but_row_1)
kb.add(*but_row_2)
kb.add(*but_row_3)
kb.add(*but_row_4)