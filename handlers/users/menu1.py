from aiogram import types
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data import config
from keyboards.inline.keyboards import questions_keyboard, go_menu1_keyboard, next10_keyboard, final_keyboard
from handlers.users.start import video, Form
from loader import dp, bot


@dp.message_handler(text_contains="Узнать об услугах подробнее")
async def rate(message: types.Message):
    await message.answer('Исчерпывающую информацию обо мне, можно найти на сайте: '
                         'https://future-mission.ru/proforientaciya_vzroslym')


@dp.message_handler(text_contains="Телеграмм канал")
async def check(message: types.Message):
    print(config.chat_id)
    for chat_id in config.chat_id:
        print(chat_id)
        sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
        if sub.status != types.ChatMemberStatus.LEFT:
            await dp.bot.send_message(chat_id=message.from_user.id,
                                      text='Спасибо за подписку, получите ваш подарок https://drive.google.com/file/d/1hwFmWTXBH9TC4wpj-56fyoT9WMpb90hN/view?usp=sharing')
            return True
        else:
            await dp.bot.send_message(chat_id=message.from_user.id,
                                      text='После подписки на телеграмм канал вам сделают подарок https://t.me/+B70N30JaIj45ZTU6')
            return False


@dp.message_handler(text_contains="Назад к меню")
async def question7(message: types.Message):
    await message.answer("Возвращаемся в меню", reply_markup=go_menu1_keyboard)