"""Это не совсем клава с кнопками, а просто стартовое меню, которое обычно создается через botFAther"""
from aiogram import Bot
from aiogram.types import BotCommand


from lexicon.lexicon_ru import LEXICON_COMMANDS

async def set_main_menu(bot:Bot):
    main_menu_commands = [BotCommand(command=command,description=description) for command,description in LEXICON_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)