from googletrans import LANGUAGES

TOKEN = ''


'''Создание словарей для отображения'''
LANG_DICT = LANGUAGES

LANG_DICT_1 = dict()
LANG_DICT_2 = dict()
count = 0

for key, value in LANG_DICT.items():
    if count <= 60:
        LANG_DICT_1[key] = value
    elif count > 60:
        LANG_DICT_2[key] = value
    count += 1

