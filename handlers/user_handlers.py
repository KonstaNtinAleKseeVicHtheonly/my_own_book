from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def other_updates(message:Message):
    await message.answer(text='Извините, я вас не понимаю, для подробной информации нажмите команду help')