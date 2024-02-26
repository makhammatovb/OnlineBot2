from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import admins
from utils.my_commands import user_commands, admin_commands


cmd_router = Router()


@cmd_router.message(CommandStart())
async def start_handler(message: Message):
    if message.from_user.id in admins:
        await message.bot.set_my_commands(commands=admin_commands)
        await message.answer("Dear admin, welcome!")
    else:
        await message.bot.set_my_commands(commands=user_commands)
        await message.answer("Welcome")


@cmd_router.message(Command('cancel'))
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("All actions cancelled!")