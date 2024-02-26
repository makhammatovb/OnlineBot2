from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from config import DB_NAME
from keyboards.admin_inline_keyboards import make_categories_kb, make_confirm_kb
from states.admin_states import CategoryStates
from states.admin_states import ProductsStates
from utils.database import Database


category_router = Router()
product_router = Router()
db = Database(DB_NAME)


@category_router.message(Command('categories'))
async def category_list_handler(message: Message):
    await message.answer(
        text="All categories:",
        reply_markup=make_categories_kb()
    )


@category_router.message(Command('add_category'))
async def add_category_handler(message: Message, state: FSMContext):
    await state.set_state(CategoryStates.addCategoryState)
    await message.answer(text="Please, send name for new category...")


@category_router.message(CategoryStates.addCategoryState)
async def insert_category_handler(message: Message, state=FSMContext):
    if db.check_category_exists(message.text):
        if db.add_category(new_category=message.text):
            await state.clear()
            await message.answer(
                f"New category by name '{message.text}' successfully added!"
            )
        else:
            await message.answer(
                f"Something error, resend category"
                f"Send again or click /cancel for cancel process!"
            )
    else:
        await message.answer(
            f"Category \"{message.text}\" already exists\n"
            f"Send other name or click /cancel for cancel process!"
        )


@category_router.message(Command('edit_category'))
async def edit_category_handler(message: Message, state=FSMContext):
    await state.set_state(CategoryStates.startEditCategoryState)
    await message.answer(
        text="Select category which you want change:",
        reply_markup=make_categories_kb()
    )


@category_router.callback_query(CategoryStates.startEditCategoryState)
async def select_category_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CategoryStates.finishEditCategoryState)
    await state.update_data(cat_name=callback.data)
    await callback.message.edit_text(f"Please, send new name for category \"{callback.data}\":")


@category_router.message(CategoryStates.finishEditCategoryState)
async def update_category_handler(message: Message, state=FSMContext):
    if db.check_category_exists(message.text):
        all_data = await state.get_data()
        if db.rename_category(old_name=all_data.get('cat_name'), new_name=message.text):
            await state.clear()
            await message.answer(
                f"Category name successfully modified!"
            )
    else:
        await message.answer(
            f"Category \"{message.text}\" already exists\n"
            f"Send other name or click /cancel for cancel process!"
        )


@category_router.message(Command('del_category'))
async def del_category_handler(message: Message, state=FSMContext):
    await state.set_state(CategoryStates.startDeleteCategoryState)
    await message.answer(
        text="Select category which you want to delete:",
        reply_markup=make_categories_kb()
    )


@category_router.callback_query(CategoryStates.startDeleteCategoryState)
async def select_category_del_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CategoryStates.finishDeleteCategoryState)
    await state.update_data(cat_name=callback.data)
    await callback.message.edit_text(
        text=f"Do you want to delete category \"{callback.data}\":",
        reply_markup=make_confirm_kb()
    )


@category_router.callback_query(CategoryStates.finishDeleteCategoryState)
async def remove_category_handler(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'YES':
        all_data = await state.get_data()
        if db.delete_category(all_data.get('cat_name')):
            await callback.message.answer("Category successfully deleted!")
            await callback.message.delete()
            await state.clear()
        else:
            await callback.message.answer(
                f"Something went wrong!"
                f"Try again later or click /cancel for cancel process!"
            )
    else:
        await state.clear()
        await callback.message.answer('Process canceled!')
        await callback.message.delete()


