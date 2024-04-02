from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
# from app.database.requests import set_user
import app.keyboards as kb
router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    # await set_user(message.from_user.id)
    await message.answer(f'Добро пожаловать в SHOP,'
                         f' {message.from_user.full_name}',
                         reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer(f'Выберите игру, из данного списка,'
                         f' {message.from_user.full_name}',
                         reply_markup=await kb.categories())