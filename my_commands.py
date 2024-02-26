from aiogram.types import BotCommand
from aiogram.filters import Command

admin_commands = [
    BotCommand(command='start', description='Start/restart bot'),
    BotCommand(command='categories', description='All categories list'),
    BotCommand(command='add_category', description='Add a new category'),
    BotCommand(command='edit_category', description='Update any category'),
    BotCommand(command='add_product', description='Add a new product'),
    BotCommand(command='edit_product', description='Update any product'),
    BotCommand(command='del_product', description='Delete any product'),
    BotCommand(command='products', description='All products list'),

]

user_commands = [
    BotCommand(command='start', description='Start/restart bot'),
    BotCommand(command='help', description='Manual for using bot'),
]