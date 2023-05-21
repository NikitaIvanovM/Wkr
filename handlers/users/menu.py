from aiogram import types
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data import config
from keyboards.inline.keyboards import questions_keyboard, go_menu_keyboard, next10_keyboard, final_keyboard
from handlers.users.start import video, Form
from loader import dp, bot


# @dp.message_handler(text_contains="Узнать об услугах подробнее")
# async def rate(message: types.Message):
#     await message.answer('Исчерпывающую информацию обо мне, можно найти на сайте: '
#                          'future-mission.ru')
#


#
# @dp.message_handler(text_contains="Телеграмм канал")
# async def check(message: types.Message):
#     print(config.chat_id)
#     for chat_id in config.chat_id:
#         print(chat_id)
#         sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
#         if sub.status != types.ChatMemberStatus.LEFT:
#             await dp.bot.send_message(chat_id=message.from_user.id,
#                                       text='Спасибо за подписку, получите ваш подарок https://drive.google.com/file/d/1IdVfz1Hf5j2H1uaMpLAT94tMh0rfzl1X/view?usp=sharing')
#             return True
#         else:
#             await dp.bot.send_message(chat_id=message.from_user.id,
#                                       text='После подписки на телеграмм канал вам сделают подарок https://t.me/+B70N30JaIj45ZTU6')
#             return False


# async def questions(message: types.Message):
#     await message.answer("После подписки на телеграмм канал вам сделают подарок"
#         'https://web.telegram.org/a/#-1774944385')


# @dp.message_handler(text_contains="Оставить заявку")
# async def video(call: types.CallbackQuery):
#     await Form.question.set()
#     user_id = call.from_user.id
#     # await bot.send_message(user_id, text="text")


# @dp.message_handler(text_contains="Отзывы")
# async def feedback(message: types.Message):
#     await message.answer(
#         "<a href='https://future-mission.ru/otzyvy-o-konsultaciah'>С отзывами можете озакомиться здесь</a>\n")
#
#
# @dp.message_handler(text_contains="Контакты")
# async def contacts(message: types.Message):
#     await message.answer("<a href='https://future-mission.ru/contacts'>Наши контакты здесь</a>")
#
#
# @dp.message_handler(text_contains="Частые вопросы")
# async def questions(message: types.Message):
#     await bot.send_message(message.from_user.id, "Часто задаваемые вопросы:", reply_markup=questions_keyboard)
#
#
@dp.message_handler(text_contains="Где и как проходят занятия?")
async def question1(message: types.Message):
    await message.answer("Профориентация для подростков в Future Mission проходит по предварительной записи - в формате онлайн, с любого компьютера с доступом в интернет.")


@dp.message_handler(text_contains="Для какого возраста подходит профориентация подросткам?")
async def question2(message: types.Message):
    await message.answer("У нас есть как отдельные программы для детей 10-14 лет, так и для подростов 15-18 лет")


@dp.message_handler(text_contains="Кто проводит профориентацию?")
async def question3(message: types.Message):
    await message.answer(
        "Занятия проводит Марина Илалова - карьерный консультант, профориентолог, ТАЛАНТориентолог, автор методики выявления природных талантов")


@dp.message_handler(text_contains="Нужно ли присутствовать родителю на профориентации для подростков?")
async def question4(message: types.Message):
    await message.answer(
        "Наша многолетняя практика показала, что в подавляющем большинстве случаев решение о выборе профессии принимается совместно — подростком и родителем, "
        "поэтому очень важно, чтобы и у самого родителя сформировалось четкое понимание направлений развития, всех «за и против». В этом случае родитель будет "
        "поддерживать своего ребенка в его выборе, а не сомневаться или даже препятствовать. Из нашей практики известны случаи, когда родители не хотели (или не могли) "
        "на профориентации для школьника, и по итогам работы у них возникало множество вопросов и сомнений. И это понятно — ведь они не прошли вместе с нами весь путь "
        "от непонимания к ясному осознанию. Поэтому мы рекомендуем присутствовать одному из родителей в течение всего времени на профориентации, чтобы у всех членов семьи "
        "сложилось четкое видение.")


@dp.message_handler(text_contains="Что мы получим в результате консультации?")
async def question5(message: types.Message):
    await message.answer(
        "Вы сможете разобраться со своими желаниями, определите склонности и способности; сформируется четкое понимание направлений развития, определите сферу (или сферы) "
        "профессионального развития, получите список из 2-3 наиболее подходящих для вас профессий.")


# @dp.message_handler(text_contains="В чем заключается ваша методика?")
# async def question6(message: types.Message):
#     await message.answer("Дополнить")


@dp.message_handler(text_contains="Назад к меню")
async def question7(message: types.Message):
    await message.answer("Возвращаемся в меню", reply_markup=go_menu_keyboard)
