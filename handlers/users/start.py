from aiogram import types
# from notifiers import get_notifier
import time
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data import config
from data.config import BOT_TOKEN
from keyboards.inline.keyboards import next1_keyboard, next2_keyboard, next3_keyboard, next4_keyboard, \
    next5_keyboard, next6_keyboard, next7_keyboard, next8_keyboard, next9_keyboard, go_menu_keyboard, final_keyboard, \
    go_menu1_keyboard, go_menu2_keyboard, go_menu3_keyboard
from loader import dp, bot
from handlers.users.sqlite import db_start, create_profile, edit_profile


async def on_startup(_):
    await db_start()


logging.basicConfig(level=logging.INFO)
bott = Bot(token=BOT_TOKEN)
dpp = Dispatcher(bot=bott)
MSG = 'Ghbdtn fylhtq'


class Form(StatesGroup):
    name = State()
    phone = State()
    mail = State()


# @dp.message_handler()
# async def test(message: types.Message):
#     print(message.chat.id)

async def do_something(message: types.Message):
    await asyncio.sleep(60*15)
    print('async_task_finished')
    for chat_id in config.chat_id:
        print(chat_id)
        sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
        # if sub.status != types.ChatMemberStatus.LEFT:
        #     await dp.bot.send_message(chat_id=message.from_user.id,
        #                               text='Спасибо за подписку, получите ваш подарок https://drive.google.com/file/d/1hwFmWTXBH9TC4wpj-56fyoT9WMpb90hN/view?usp=sharing')
        #     return True
        if sub.status == types.ChatMemberStatus.LEFT:
            await dp.bot.send_message(chat_id=message.from_user.id,
                                      text="Предлагаю подписаться на мой телеграмм канал, где я рассказываю примеры из практики и истории ребят и их родителей. За подписку вы получите полезный подарок https://t.me/marinailalova")
            return False


async def do_some(from_user_id):
    await asyncio.sleep(60*1)
    for chat_id in config.chat_id:
        print(chat_id)
        sub = await bot.get_chat_member(chat_id=chat_id, user_id=from_user_id)
        if sub.status != types.ChatMemberStatus.LEFT:
            await dp.bot.send_message(chat_id=from_user_id,
                                      text='Спасибо за подписку, получите ваш подарок https://drive.google.com/file/d/1IdVfz1Hf5j2H1uaMpLAT94tMh0rfzl1X/view?usp=sharing')
            return True


async def do_some1(from_user_id):
    await asyncio.sleep(60*1)
    for chat_id in config.chat_id:
        print(chat_id)
        sub = await bot.get_chat_member(chat_id=chat_id, user_id=from_user_id)
        if sub.status != types.ChatMemberStatus.LEFT:
            await dp.bot.send_message(chat_id=from_user_id,
                                      text='Спасибо за подписку, получите ваш подарок https://drive.google.com/file/d/1hwFmWTXBH9TC4wpj-56fyoT9WMpb90hN/view?usp=sharing')
            return True


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    asyncio.ensure_future(do_something(message))
    await create_profile(user_id=message.from_user.id)
    # print(123)
    # print(message.chat.id)

    # user_id = message.from_user.id
    # user_name = message.from_user.first_name
    # user_full_name = message.from_user.full_name
    # logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    #
    #
    # # await asyncio.sleep(60)
    # await bot.send_message(user_id, MSG.format(user_name))
    # await message.reply(f"Привет, {user_full_name}!")

    photo123 = open('data/logo.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo123, caption="Приветствую вас! Меня зовут Марина Илалова. Я - профориентолог, семейный консультант по талантам. Я разработала авторскую "
        "методику выявления природных способностей и превращения их в любимое дело!",
                   reply_markup=next1_keyboard)
    # await message.answer(
    #     "Приветствую вас! Меня зовут Марина Илалова. Я - профориентолог, семейный консультант по талантам. Я разработала авторскую "
    #     "методику выявления природных способностей и превращения их в любимое дело!",
    #     reply_markup=next1_keyboard)


# @dp.callback_query_handler(CommandStart())
# async def start(call: types.CallbackQuery):
#     # print(123)
#     # print(message.chat.id)
#     print(123)
#     await call.message.edit_reply_markup()
#     user_id = call.from_user.id
#     photo123 = open('data/logo.jpg', 'rb')
#     await bot.send_photo(user_id, caption="Приветствую вас! Меня зовут Марина Илалова."
#                                           " Я - профориентолог, семейный консультант по талантам."
#                                           " Я разработала авторскую "
#         "методику выявления природных способностей и превращения их в любимое дело!",
#                          photo=photo123,
#                          reply_markup=next1_keyboard)


@dp.callback_query_handler(text="next_1")
async def next1(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id, "Я смогу найти дело жизни для вас или вашего ребенка всего за 2-3 часа. "
                                    "Вам не придется заполнять никаких предварительных анкет или тестов. "
                                    "Вы просто записываетесь ко мне на интервью , а я диагностирую ваши природные способности  и показываю все возможности их применения на реальном рынке. "
                                    "В результате вы получаете план вашей реализации на ближайшие несколько лет, чтобы учиться, работать с удовольствием и получать за это достойное вознаграждение. "
                                    "Для кого необходимо выявить таланты?",
                           reply_markup=next2_keyboard)


@dp.callback_query_handler(text="next_2")
async def next2(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id, "Какую задачу вы бы хотели решить?",
                           reply_markup=next3_keyboard)


@dp.callback_query_handler(text="next_3")
async def next3(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "Какую задачу вы бы хотели решить?",
                           reply_markup=next4_keyboard)


@dp.callback_query_handler(text="next_4")
async def next4(call: types.CallbackQuery):
    asyncio.ensure_future(do_some(call.from_user.id))
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "С радостью помогу вам решить эту задачу. Для этого оставьте заявку. Я свяжусь с вами, и мы обсудим, как можно решить вашу задачу.",
                           reply_markup=go_menu_keyboard)


@dp.callback_query_handler(text="next_5")
async def next4(call: types.CallbackQuery):
    asyncio.ensure_future(do_some1(call.from_user.id))
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "С радостью помогу вам решить эту задачу. Для этого оставьте заявку. Я свяжусь с вами, и мы обсудим, как можно решить вашу задачу.",
                           reply_markup=go_menu1_keyboard)


# @dp.callback_query_handler(text="next_5")
# async def next5(call: types.CallbackQuery):
#     await call.message.edit_reply_markup()
#     user_id = call.from_user.id
#     await bot.send_message(user_id,
#                            "1) Меньше 27% россиян работают по своей специальности ВУЗа. Остальные потратили время и деньги зря"
#                            "\n2) Больше 70% школьников не знают своих талантов, не понимают в какой профессии они будут успешны"
#                            "\n3) 83% людей не получают удовольствие от своей работы и заставляют себя ходить на нее из-за денег"
#                            "\n4) Больше 54% людей сталкивались с проблемой выгорания и необходимостью искать новую сферу"
#                            "\n5) Больше 20% профессий становятся неактуальными каждые 5-7 лет, оставшиеся видоизменяются",
#                            reply_markup=next6_keyboard)


@dp.callback_query_handler(text_contains="inf_video")
async def inf_video(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "Посмотрите короткое видео о нас и узнайте подробнее зачем нужно глубокое skills-ориентирование в современном мире"
                           " \nhttps://www.youtube.com/watch?v=VbzqAek2p2A",
                           reply_markup=next7_keyboard)


@dp.callback_query_handler(text_contains="review_1")
async def review_1(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    photo3 = open('data/review1.jpg', 'rb')
    photo4 = open('data/review2.jpg', 'rb')
    photo5 = open('data/review3.jpg', 'rb')
    await bot.send_photo(user_id, photo=photo3)
    await bot.send_photo(user_id, photo=photo4)
    await bot.send_photo(user_id, photo=photo5, reply_markup=next8_keyboard)


@dp.callback_query_handler(text_contains="review_2")
async def review_2(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    photo6 = open('data/review4.jpg', 'rb')
    photo7 = open('data/review5.jpg', 'rb')
    photo8 = open('data/review6.jpg', 'rb')
    await bot.send_photo(user_id, photo=photo6)
    await bot.send_photo(user_id, photo=photo7)
    await bot.send_photo(user_id, photo=photo8, reply_markup=next9_keyboard)


@dp.callback_query_handler(text_contains="review_3")
async def review_3(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "Более подробную информацию можно получить на сайте <a href='https://future-mission.ru/otzyvy-o-konsultaciah'>С отзывами можете озакомиться здесь</a>\n")
    await bot.send_message(user_id, "Какую задачу вы хотите решить с помощью консультации?",
                           reply_markup=final_keyboard)


@dp.callback_query_handler(text_contains="video")
async def video(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id, reply_markup=final_keyboard)


@dp.callback_query_handler(text_contains="usl")
async def rate(call: types.CallbackQuery):
    user_id = call.from_user.id
    await bot.send_message(user_id, 'Исчерпывающую информацию обо мне, можно найти на сайте: '
                         'future-mission.ru',
                           reply_markup=go_menu2_keyboard)

@dp.callback_query_handler(text_contains="usl1")
async def rate(call: types.CallbackQuery):
    user_id = call.from_user.id
    await bot.send_message(user_id, 'Исчерпывающую информацию обо мне, можно найти на сайте: '
                                    'future-mission.ru',
                            reply_markup=go_menu3_keyboard)


@dp.callback_query_handler(text_contains="vizov")
async def form_question(call: types.CallbackQuery, state: FSMContext):
    print("form_question method")
    print(call)
    message = call.message
    user_id = call.from_user.id
    # await bot.send_message(user_id, "Назовите, пожалуйста, свое имя")
    await message.answer("Назовите, пожалуйста, свое имя")
    async with state.proxy() as data:
        data['question'] = message.text
    await Form.next()


@dp.message_handler(content_types=['text'], state=Form.name)
async def form_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        p = message.text
        if not set(p).isdisjoint(set("@/*#!$%^?\[]-_)+=;`~.,<>'|1234567890")):
            return
        else:
            data['name'] = p
    await message.answer("Напишите номер телефона")
    await Form.next()


@dp.message_handler(content_types=['text'], state=Form.phone)
async def form_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        p = message.text
        if not set(p).isdisjoint(set("@/*#!$%^?\[]-_)=;`~.,<>'|qazwsxedcrfvtgbyhnujmikQAZWSXEDCRFVTGBYHNUJMIKЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛЩДЗХЖйфяцычувскамепинртгоьшлбщдюзжхэъ")):
            return
        else:
            data['phone'] = p
    print(message.chat.id)
    await message.answer("Напишите, пожалуйста, вашу электронную почту")
    await Form.next()


@dp.message_handler(content_types=['text'], state=Form.mail)
async def form_mail(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        admin_id = config.ADMINS[0]
        data['mail'] = message.text
        msg = ("Получена новая заявка"
               + "\nИмя: " + data['name']
               + "\nНомер телефона: " + data['phone']
               + "\nПочта: " + data['mail']
               )
        await bot.send_message(admin_id, msg)
    await edit_profile(state, user_id=message.from_user.id)
    await message.answer("Спасибо, ваша заявка была отправлена, скоро я с вами свяжусь. А пока предлагаю подписаться на мой телеграмм канал, "
                         "где я рассказываю примеры из практики и истории ребят и их родителей. За подписку вы получите полезный подарок https://t.me/marinailalova")
    await state.finish()
