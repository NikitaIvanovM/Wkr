from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

next1_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Чем мне это будет полезно?", callback_data="next_1")
        ],
    ]
)

next2_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Для себя любимого", callback_data="next_2")
        ],
[
            InlineKeyboardButton(text="Для ребёнка", callback_data="next_3")
        ],
    ]
)

next3_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Найти вдохновение в работе", callback_data="next_4")
        ],
        [
            InlineKeyboardButton(text="Сменить профессию", callback_data="next_4")
        ],
        [
            InlineKeyboardButton(text="Много увлечений – не знаю, что выбрать", callback_data="next_4")
        ],
        [
            InlineKeyboardButton(text="Во что инвестировать время и деньги", callback_data="next_4")
        ],
    ]
)

next4_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Узнать таланты ребенка", callback_data="next_5")
        ],
[
            InlineKeyboardButton(text="Выбрать профиль класса", callback_data="next_5")
        ],
[
            InlineKeyboardButton(text="Подбор развивающих кружков/секций", callback_data="next_5")
        ],
[
            InlineKeyboardButton(text="Выбор дальнейшего образования колледж/ВУЗ", callback_data="next_5")
        ],
[
            InlineKeyboardButton(text="Подбор подходящих профессий", callback_data="next_5")
        ],
[
            InlineKeyboardButton(text="Выбор специальностей и необходимых ЕГЭ", callback_data="next_5")
        ],
    ]
)

next5_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Почему необходимо пройти глубокую профориентацию?", callback_data="next_5")
        ],
    ]
)

#next6_keyboard = InlineKeyboardMarkup(
#    inline_keyboard=[
#       [
#           InlineKeyboardButton(text="Что такое skills-ориентирование?", callback_data="video")
#       ],
#   ]
#)

next6_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="Узнать больше", callback_data="inf_video")
       ],
       [
           InlineKeyboardButton(text="Записаться на консультацию", callback_data="video")
       ],
   ]
)


next7_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Отзывы о моей работе", callback_data="review_1")
        ],
        [
            InlineKeyboardButton(text="Записаться на консультацию", callback_data="video")
        ],
    ]
)


next8_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ещё отзывы", callback_data="review_2")
        ],
        [
            InlineKeyboardButton(text="Хочу консультацию", callback_data="video")
        ],
    ]
)


next9_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Узнать больше о моих услугах", callback_data="review_3")
        ],
        [
            InlineKeyboardButton(text="Хочу консультацию", callback_data="video")
        ],
    ]
)


next10_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='', callback_data='text')
        ],
    ]
)


final_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Возможно")
        ],
    ]
)

# go_menu_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Сайт"),
#             KeyboardButton(text="Телеграмм канал")
#         ],
#         [
#             KeyboardButton(text="Оставить заявку")
#         ]
#     ],
#     resize_keyboard=True
# )

go_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оставить заявку", callback_data="vizov")
        ],
        [
            InlineKeyboardButton(text="Узнать об услугах подробнее", callback_data="usl")
        ]
    ],
)

go_menu1_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оставить заявку", callback_data="vizov")
        ],
        [
            InlineKeyboardButton(text="Узнать об услугах подробнее", callback_data="usl1")
        ]
    ],
)

go_menu2_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оставить заявку", callback_data="vizov")
        ],
    ],
)

go_menu3_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оставить заявку", callback_data="vizov")
        ],
    ],
)

questions_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Где и как проходят занятия?"),
        ],
        [
            KeyboardButton(text="Для какого возраста подходит профориентация подросткам?"),
        ],
        [
            KeyboardButton(text="Кто проводит профориентацию?"),
        ],
        [
            KeyboardButton(text="Нужно ли присутствовать родителю на профориентации для подростков?"),
        ],
        [
            KeyboardButton(text="Что мы получим в результате консультации?"),
        ],
        # [
        #     KeyboardButton(text="В чем заключается ваша методика?(дополнить)"),
        # ],
        [
            KeyboardButton(text="Назад к меню 🔙"),
        ],
    ],
resize_keyboard=True
)