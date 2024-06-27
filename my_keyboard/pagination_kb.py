"""МОдуль для создания кнопок перекючения между страницами <<,>> 
а так же текущая страницы/ все страницы: 33/180 например"""
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON


# функция для создания клавы страниц книги
def create_pagination_key_board(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons]
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()