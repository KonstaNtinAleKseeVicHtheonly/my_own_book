from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON
from services.file_handling import book

def create_bookmarks_keyboard(*args:int) -> InlineKeyboardMarkup:
    """функция создает клавиаутру с callback кнопками для закладок"""
    bookmark_builder = InlineKeyboardBuilder()
    for elem in sorted(args):
        bookmark_builder.row(InlineKeyboardButton(text=f"{elem} - {book[elem][:50]}",callback_data=str(elem)))

    #Добавим кнопки редактировать и отменить в самом конце клавы bookmark
    bookmark_builder.row(InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'],callback_data='edit_bookmarks'),
                           InlineKeyboardButton(text=LEXICON['cancel'],callback_data='cancel'), width = 2)
    
    return bookmark_builder.as_markup()


def create_edit_keyboard(*args:int) -> InlineKeyboardMarkup:
    """Функция создает  клаву с закладками на удаление"""
    kb_builder = InlineKeyboardBuilder()
    for elem in sorted(args):
        kb_builder.row(InlineKeyboardButton(text=f"{book['del']} {book[elem]}",callback_data=f"{elem}del"))

    kb_builder.row(InlineKeyboardButton(text=LEXICON['cancel'],callback_data='cancel'))

    return kb_builder.as_markup()