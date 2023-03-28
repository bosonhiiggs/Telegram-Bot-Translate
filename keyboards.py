from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from config import LANG_DICT, LANG_DICT_1, LANG_DICT_2

'''Главное меню'''
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🟡 Изменить язык перевода 🟡'),
            KeyboardButton(text='🔴 Изменить список из Избранного(Недоделано) 🔴'),
        ],
    ],
    resize_keyboard=True,
)

menu_calling = InlineKeyboardMarkup()
menu_calling.add(InlineKeyboardButton(
    'Главное меню', callback_data='mainmenu'
))


'''Inline клавиатура всех языков'''
def create_inline_langall(lang: dict) -> InlineKeyboardMarkup:
    temp = 0
    keys_temp_list = []
    all_lang_keyboard = InlineKeyboardMarkup()
    for i_key, i_value in lang.items():
        button = InlineKeyboardButton(i_value.upper(), callback_data=i_key)
        keys_temp_list.append(button)
        temp += 1

        if temp == 4:
            temp = 0
            all_lang_keyboard.add(keys_temp_list[0], keys_temp_list[1], keys_temp_list[2])
            keys_temp_list = []

    return all_lang_keyboard


all_lang_keyboard_1 = create_inline_langall(LANG_DICT_1)
all_lang_keyboard_2 = create_inline_langall(LANG_DICT_2)


'''Inline Клавитаура избранных языков'''
async def create_inline_keyboard(lang_list: list) -> InlineKeyboardMarkup:
    famous_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=str(LANG_DICT[lang_list[0]]).capitalize(), callback_data=lang_list[0]),
            InlineKeyboardButton(text=str(LANG_DICT[lang_list[1]]).capitalize(), callback_data=lang_list[1]),
        ],
        [
            InlineKeyboardButton(text=str(LANG_DICT[lang_list[2]]).capitalize(), callback_data=lang_list[2]),
            InlineKeyboardButton(text=str(LANG_DICT[lang_list[3]]).capitalize(), callback_data=lang_list[3]),
        ],
    ])
    return famous_keyboard


'''Reply клавиатура для избранных языков'''
async def create_reply_keyboard(lang_list: list) -> ReplyKeyboardMarkup:
    famous_reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🍏 ' + str(LANG_DICT[lang_list[0]]).capitalize()),
                KeyboardButton(text='🍇 ' + str(LANG_DICT[lang_list[1]]).capitalize()),
            ],
            [
                KeyboardButton(text='🍍 ' + str(LANG_DICT[lang_list[2]]).capitalize()),
                KeyboardButton(text='🍅 ' + str(LANG_DICT[lang_list[3]]).capitalize()),
            ],
        ],
        resize_keyboard=True,
    )
    return famous_reply_keyboard


'''Назад (Cancel)'''
cancel_keyboard = InlineKeyboardMarkup()
cancel_keyboard.add(InlineKeyboardButton('Главное меню', callback_data='mainmenu'))
