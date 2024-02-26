from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import DB_NAME
from utils.database import Database


db = Database(DB_NAME)


def make_categories_kb():
    categories = db.get_categories()
    rows = []
    for cat in categories:
        rows.append([
            InlineKeyboardButton(
                text=cat[1], callback_data=str(cat[1])
            )]
        )
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )
    return inl_kb


def make_confirm_kb():
    rows = [
        InlineKeyboardButton(text='YES', callback_data='YES'),
        InlineKeyboardButton(text='NO', callback_data='NO')
    ]
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=[rows]
    )
    return inl_kb


def categories_kb_4_products():
    products = db.get_categories()
    rows = []
    for cat in products:
        rows.append([
            InlineKeyboardButton(
                text=cat[1], callback_data=str(cat[1])
            )]
        )
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )
    return inl_kb

def make_confirm_product_kb():
    a = [
        InlineKeyboardButton(text='YES', callback_data='YES'),
        InlineKeyboardButton(text='NO', callback_data='NO')
    ]
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=[a]
    )
    return inl_kb


def update_products_kb():
    products = db.get_categories()
    rows = []
    for cat in products:
        rows.append([
            InlineKeyboardButton(
                text=cat[1], callback_data=str(cat[1])
            )]
        )
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )
    return inl_kb


def delete_products_kb():
    products = db.get_categories()
    rows = []
    for cat in products:
        rows.append([
            InlineKeyboardButton(
                text=cat[1], callback_data=str(cat[1])
            )]
        )
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )
    return inl_kb

def make_product_kb():
    a = [
        InlineKeyboardButton(text='YES', callback_data='YES'),
        InlineKeyboardButton(text='NO', callback_data='NO')
    ]
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=[a]
    )
    return inl_kb


def get_products_kb():
    products = db.get_products()
    rows = []
    for cat in products:
        rows.append([
            InlineKeyboardButton(
                text=cat[1], callback_data=str(cat[1])
            )]
        )
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )
    return inl_kb