from telebot import types


#Начало
Greet_keyboard = types.InlineKeyboardMarkup()
rows = [{'💵Матпомощь': 'CA', '🌏Сенат': 'Se'},
        {'🛠 Хозотдел': 'MD', 'Выручай-ФОПФ🤝': 'DGhB'},
        {'😳Жалобы и предложения': 'ClB'},
        {'6-ка: поломки/мыло/бумага': 'BrB'}]
for row in rows:
    Greet_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Greet_keyboard    
Back_to_Greet_keyboard = types.InlineKeyboardMarkup()
Back_to_Greet_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="begin"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Матпомощь
Aid_keyboard = types.InlineKeyboardMarkup()
rows = [{'⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Aid_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Aid_keyboard
Back_to_Aid_keyboard = types.InlineKeyboardMarkup()
Back_to_Aid_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="CA"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Сенат
Senat_keyboard = types.InlineKeyboardMarkup()
rows = [{'⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Senat_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Senat_keyboard
Back_to_Senat_keyboard = types.InlineKeyboardMarkup()
Back_to_Senat_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="Se"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Хозотдел
MaintDep_keyboard = types.InlineKeyboardMarkup()
rows = [{'⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    MaintDep_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню MaintDep_keyboard
Back_to_MaintDep_keyboard = types.InlineKeyboardMarkup()
Back_to_MaintDep_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="MD"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> 6-ка: поломки/мыло/бумага
Broken_keyboard = types.InlineKeyboardMarkup()
rows = [{'1 этаж': '1F'},
        {'2 этаж': '2F'},
        {'3 этаж': '3F'},
        {'4 этаж': '4F'},
        {'5 этаж': '5F'},
        {'⬅️Назад': 'begin'}] #последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Broken_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Broken_keyboard    
Back_to_Broken_keyboard = types.InlineKeyboardMarkup()
Back_to_Broken_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="BrB"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> 6-ка: поломки/мыло/бумага --> 12345 этаж
Rooms_keyboard = types.InlineKeyboardMarkup()
rows = [{'На кухне': 'Ki'},
        {'В умывалке': 'WaB'},
        {'В туалете': 'ToB'},
        {'В другом месте': 'AnB'},
        {'⬅️Назад': 'BrB'}] #последняя кнопка возвращает в предыдущее Broken_keyboard меню
for row in rows:
    Rooms_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Rooms_keyboard
Back_to_Rooms_keyboard = types.InlineKeyboardMarkup()
Back_to_Rooms_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="Bb9"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> 6-ка: поломки/мыло/бумага --> 12345 этаж --> Кухня/Умывальник
KitchenWash_keyboard = types.InlineKeyboardMarkup()
rows = [{'Кран подтекает/не закрывается': 'TaB'},
        {'Кран гудит': 'TaB2'},
        {'Труба под раковиной подтекает': 'PiB'},
        {'Закончилось мыло': 'SoB'},
        {'Что-то другое': 'AnB'},
        {'⬅️Назад': 'Bb9'}] #последняя кнопка возвращает в предыдущее Rooms_keyboard меню
for row in rows:
    KitchenWash_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Rooms_keyboard
Back_to_KitchenWash_keyboard = types.InlineKeyboardMarkup()
Back_to_KitchenWash_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="Ki"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> 6-ка: поломки/мыло/бумага --> 12345 этаж --> В умывалке --> Труба под раковиной подтекает
Sink_keyboard = types.InlineKeyboardMarkup()
rows = [{'Раковина номер 1': 'SiB1'},
        {'Раковина номер 2': 'SiB2'},
        {'Раковина номер 3': 'SiB3'},
        {'Раковина номер 4': 'SiB4'},
        {'Раковина номер 5': 'SiB5'},
        {'Раковина номер 6': 'SiB6'},
        {'Лень искать': 'LaB'},
        {'⬅️Назад': 'WaB'}] #последняя кнопка возвращает в предыдущее KitchenWash_keyboard меню
for row in rows:
    Sink_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> 6-ка: поломки/мыло/бумага --> 12345 этаж --> В туалете
Toilet_keyboard = types.InlineKeyboardMarkup()
rows = [{'Засорился писсуар': 'UrB'},
        {'Кончилась бумага': 'PaB'},
        {'Что-то другое': 'AnB'},
        {'⬅️Назад': 'Bb9'}] #последняя кнопка возвращает в предыдущее Rooms_keyboard меню
for row in rows:
    Toilet_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Toilet_keyboard
Back_to_Toilet_keyboard = types.InlineKeyboardMarkup()
Back_to_Toilet_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="ToB"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> ВыручайФОПФ
DgapHelp_keyboard = types.InlineKeyboardMarkup()
rows = [{'⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    DgapHelp_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню DgapHelp_keyboard
Back_to_DgapHelp_keyboard = types.InlineKeyboardMarkup()
Back_to_DgapHelp_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="DGhB"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Чат сената --> бот оповестил о поломке
Fix_keyboard = types.InlineKeyboardMarkup()
rows = [{'Починено': 'FiB'}]#Отправляет сообщение боту для удаление поломки из базы
for row in rows:
    Fix_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#--------------------------------------------------------------------------------------------------------------------------------------------------

