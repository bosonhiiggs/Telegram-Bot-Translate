from main import dp
from config import LANG_DICT
from sql import register, show_lang, show_choose, switch_choose, change_famous
from keyboards import all_lang_keyboard_1, all_lang_keyboard_2, main_menu, menu_calling, cancel_keyboard, \
    create_inline_keyboard, create_reply_keyboard

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from googletrans import Translator

translator = Translator()
country = ''


@dp.message_handler(Command('start'))
async def start_mes(message: Message):
    await message.answer('Привет, я твой карманный переводчик!')
    await message.answer(f'Начинаю регистрацию id({message.from_user.id})')
    flag = await register(message.from_user.id)
    if flag:
        await message.answer('Регистрация прошла успешно')
    else:
        await message.answer('Что-то пошло не так :(\nВы уже в системе')
    await message.answer('Menu:', reply_markup=menu_calling)


@dp.callback_query_handler(text_contains='mainmenu')
async def show_menu(call: CallbackQuery):
    data_handler = await show_lang(call.from_user.id)
    choose_user = (await show_choose(call.from_user.id))[0][0]
    data_normal_view = str(data_handler)[3:-4]
    lang_lst = data_normal_view.split(', ')

    await call.message.answer(f'Избранные языки:'
                              f'\n{(LANG_DICT[lang_lst[0]].capitalize())}\n{LANG_DICT[lang_lst[1]].capitalize()}\n'
                              f'{LANG_DICT[lang_lst[2]].capitalize()}\n{LANG_DICT[lang_lst[3]].capitalize()}'
                              )
    await call.message.answer(f'Выбранный язык: {LANG_DICT[choose_user].capitalize()}', reply_markup=main_menu)
    await call.message.answer('Введите текст для перевода')


@dp.message_handler()
async def choose_source(message: Message):
    data_handler = await show_lang(message.from_user.id)
    data_normal_view = str(data_handler)[3:-4]
    lang_lst = data_normal_view.split(', ')

    '''Вывод списка языков'''
    if message.text == '🔴 Изменить список из Избранного 🔴':
        await message.answer('🔍', reply_markup=ReplyKeyboardRemove())
        # await message.answer('Клавиатура 1:', reply_markup=all_lang_keyboard_1)
        # await message.answer('Клавиатура 2:', reply_markup=all_lang_keyboard_2)
        reply_keyboard = await create_reply_keyboard(lang_lst)
        await message.answer('Избранные языки', reply_markup=reply_keyboard)
        await message.answer('Главное меню', reply_markup=cancel_keyboard)

    elif message.text == '🟡 Изменить язык перевода 🟡':
        await message.answer('🔍', reply_markup=ReplyKeyboardRemove())
        famous_keyboard = await create_inline_keyboard(lang_lst)
        await message.answer(f'Избранные языки:', reply_markup=famous_keyboard)
        await message.answer('Главное меню', reply_markup=cancel_keyboard)

    elif message.text[0] in '🍏🍇🍍🍅':
        await message.answer('OK', reply_markup=ReplyKeyboardRemove())
        global country
        country = message.text[2:]
        await message.answer('Клавиатура 1:', reply_markup=all_lang_keyboard_1)
        await message.answer('Клавиатура 2:', reply_markup=all_lang_keyboard_2)
        await message.answer(f'Меняем язык: {country}')
        await message.answer('Главное меню', reply_markup=cancel_keyboard)

    else:
        await message.answer('🔍', reply_markup=ReplyKeyboardRemove())
        translate_lang = (await show_choose(message.from_user.id))[0][0]
        translate_phrase = translator.translate(message.text, dest=translate_lang).text
        await message.answer(f'Текст перевкен на {LANG_DICT[translate_lang].capitalize()}:\n{translate_phrase}', reply_markup=cancel_keyboard)


@dp.callback_query_handler(lambda c: c.data)
async def switch_lang(call: CallbackQuery):
    data_handler = await show_lang(call.from_user.id)
    data_normal_view = str(data_handler)[3:-4]
    lang_lst = data_normal_view.split(', ')
    if call.data in lang_lst:
        wish_lang = call.data
        await switch_choose(call.from_user.id, wish_lang)
        await call.answer(f'Язык успешно изменен на {(str(LANG_DICT[wish_lang]).capitalize())}')

    elif call.data in LANG_DICT:
        reverse_dict = {v: k for k, v in LANG_DICT.items()}
        await change_famous(call.from_user.id, call.data, reverse_dict[country.lower()])
        await call.message.answer(f'Перейдите в главное меню', reply_markup=menu_calling)


