from telebot import types


#Начало
Greet_keyboard = types.InlineKeyboardMarkup()
rows = [{'💵Матпомощь': 'CA', '🌏Сенат': 'Se'},
        {'🛠 Хозотдел': 'MD', '☎️Деканат': 'De'},
        {'🎒Абитуриентам': 'En'},
        {'👨🏻🎓Общие студ. дела': 'GS'},
        {'😳Жалобы и предложения': 'ClB'},
        {'6-ка: поломки/мыло/бумага': 'BrB'},
        {'Выручай-ФОПФ🤝': 'DGhB'}]
for row in rows:
    Greet_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Greet_keyboard    
Back_to_Greet_keyboard = types.InlineKeyboardMarkup()
Back_to_Greet_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="begin"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Матпомощь
Aid_keyboard = types.InlineKeyboardMarkup()
rows = [{'📲Контакты': 'Co','❌Правила': 'Ru'},
        {'📖Категории': 'CaB','📝Бланк': 'Fo'},
       #{'📫Удалённая подача':'Di'}, !!!Данная кнопка была актуальна на период пандемии, в данный момент заявления на МП онлайн не подаются!!!
        {'⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Aid_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Aid_keyboard
Back_to_Aid_keyboard = types.InlineKeyboardMarkup()
Back_to_Aid_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="CA"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Сенат
Senat_keyboard = types.InlineKeyboardMarkup()
rows = [{'📑Устав': 'Ch', '📬Контакты': 'Cse'},
        {'📊Инфографика': 'In'},
        {'⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Senat_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Senat_keyboard
Back_to_Senat_keyboard = types.InlineKeyboardMarkup()
Back_to_Senat_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="Se"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Хозотдел
MaintDep_keyboard = types.InlineKeyboardMarkup()
rows = [{'🛠Инструментарий': 'ToR'},
        {'🧻🧼Ответственные за этажи': 'FF'},
        {'🧑🏻💻КДС': 'RFK', '📽 Клуб': 'Cl'},
        {'🛁Душ': 'Sh', '🧑🎓Боталка': 'TR'},
        {'🏋️ Тренажёрка': 'SR', '🚴Велокомната': 'BR'},
        {'🧺Стиралка': 'WR', '⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    MaintDep_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню MaintDep_keyboard
Back_to_MaintDep_keyboard = types.InlineKeyboardMarkup()
Back_to_MaintDep_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="MD"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Деканат
Dekanat_keyboard = types.InlineKeyboardMarkup()
rows = [{'💁Дирекция это': 'Dir', '📲Контакты': 'DirC'},
        {'🏖 Академ. отпуск': 'Ac', '🧮Ведомость': 'VeB'},
        {'⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Dekanat_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Hosp_keyboard
Back_to_Dekanat_keyboard = types.InlineKeyboardMarkup()
Back_to_Dekanat_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="De"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Абитуриентам
Abit_keyboard = types.InlineKeyboardMarkup()
rows = [{'📚Конкурсные группы': 'Sy'},
        {'📊Статистика поступления': 'Stat'},
        {' Карта городка': 'Map'},
        {'🧭Ссылки': 'UL', '📜О ЛФИ': 'AS'},
        {'🏡Где я буду жить': 'Do', '⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Abit_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Abit_keyboard
Back_to_Abit_keyboard = types.InlineKeyboardMarkup()
Back_to_Abit_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="En"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Общие студ. дела
Stud_keyboard = types.InlineKeyboardMarkup()
rows = [{'📆Документы студента': 'StDoc'},
        {'💊Поликлиника': 'Pol', '💸Абрамовка': 'Abr'},
        {'📝Справки': 'Ce', '📚Библиотека': 'Lib'},
        {'🔍Воинский учёт': 'MilReg', '⬅️Назад': 'begin'}]#последняя кнопка возвращает в предыдущее Greet_keyboard меню
for row in rows:
    Stud_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Stud_keyboard
Back_to_Stud_keyboard = types.InlineKeyboardMarkup()
Back_to_Stud_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="GS"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Общие студ. дела --> Документы студента
Doc_keyboard = types.InlineKeyboardMarkup()
rows = [{'📘Студ. билет': 'StC', '🔐ЭКД': 'EC'},
        {'💳Соц. карта': 'SoC', '📫Phystech.edu': 'PhE'},
        {'🏡Регистрация': 'LiR', '⬅️Назад': 'GS'}]#последняя кнопка возвращает в предыдущее Stud_keyboard меню
for row in rows:
    Doc_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Doc_keyboard
Back_to_Doc_keyboard = types.InlineKeyboardMarkup()
Back_to_Doc_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="StDoc"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Общие студ. дела --> Поликлиника
Hosp_keyboard = types.InlineKeyboardMarkup()
rows = [{'📎Как прикрепляться': 'HTR'},
        {'📆Как записаться': 'HTV'},
        {'⬅️Назад': 'GS'}]#последняя кнопка возвращает в предыдущее Stud_keyboard меню
for row in rows:
    Hosp_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Hosp_keyboard
Back_to_Hosp_keyboard = types.InlineKeyboardMarkup()
Back_to_Hosp_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="Pol"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> Общие студ. дела --> Абрамовка
Abram_keyboard = types.InlineKeyboardMarkup()
rows = [{'🎁Что это и для кого': 'WTF'},
        {'Малообеспеченность': 'LAB'},
        {'Успеваемость': 'GMB'},
        {'Частозадаваемые вопросы': 'AQB'},
        {'⬅️Назад': 'GS'}]#последняя кнопка возвращает в предыдущее Stud_keyboard меню
for row in rows:
    Abram_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Abram_keyboard
Back_to_Abram_keyboard = types.InlineKeyboardMarkup()
Back_to_Abram_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="Abr"))
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


#Начало --> 6-ка: поломки/мыло/бумага --> 12345 этаж --> На кухне
Kitchen_keyboard = types.InlineKeyboardMarkup()
rows = [{'Кран подтекает/не закрывается': 'TaB'},
        {'Кран гудит': 'TaB2'},
        {'Труба под раковиной подтекает': 'PiB'},
        {'Закончилось мыло': 'SoB'},
        {'Что-то другое': 'AnB2'},
        {'⬅️Назад': 'Bb9'}] #последняя кнопка возвращает в предыдущее Rooms_keyboard меню
for row in rows:
    Kitchen_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Rooms_keyboard
Back_to_Kitchen_keyboard = types.InlineKeyboardMarkup()
Back_to_Kitchen_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="Ki"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> 6-ка: поломки/мыло/бумага --> 12345 этаж --> В умывалке
WashBasin_keyboard = types.InlineKeyboardMarkup()
rows = [{'Кран подтекает/не закрывается': 'TaB3'},
        {'Кран гудит': 'TaB4'},
        {'Труба под раковиной подтекает': 'PiB2'},
        {'Закончилось мыло': 'SoB2'},
        {'Что-то другое': 'AnB3'},
        {'⬅️Назад': 'Bb9'}] #последняя кнопка возвращает в предыдущее Rooms_keyboard меню
for row in rows:
    WashBasin_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню WashBasin_keyboard
Back_to_WashBasin_keyboard = types.InlineKeyboardMarkup()
Back_to_WashBasin_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="WaB"))
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
        {'⬅️Назад': 'WaB'}] #последняя кнопка возвращает в предыдущее WashBasin_keyboard меню
for row in rows:
    Sink_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Начало --> 6-ка: поломки/мыло/бумага --> 12345 этаж --> В туалете
Toilet_keyboard = types.InlineKeyboardMarkup()
rows = [{'Засорился писсуар': 'UrB'},
        {'Кончилась бумага': 'PaB'},
        {'Что-то другое': 'AnB4'},
        {'⬅️Назад': 'Bb9'}] #последняя кнопка возвращает в предыдущее Rooms_keyboard меню
for row in rows:
    Toilet_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#клавиатура из одной кнопки, возвращающая в меню Toilet_keyboard
Back_to_Toilet_keyboard = types.InlineKeyboardMarkup()
Back_to_Toilet_keyboard.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="ToB"))
#--------------------------------------------------------------------------------------------------------------------------------------------------


#Чат сената --> бот оповестил о поломке
Fix_keyboard = types.InlineKeyboardMarkup()
rows = [{'Починено': 'FiB'}]#Отправляет сообщение боту для удаление поломки из базы
for row in rows:
    Fix_keyboard.add(*[types.InlineKeyboardButton(text,callback_data=callback_data) for text,callback_data in row.items()])
#--------------------------------------------------------------------------------------------------------------------------------------------------

