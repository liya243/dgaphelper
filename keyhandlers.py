#Здесь происходит принятие сигнала от бота и проверка, какая кнопка была нажата и куда эта кнопка ведёт
#----------------------------------------------------------------------------------------
from keyboards import *

#Начальное меню
def Beginning(call, bot, cur, con):
    if call.data == "begin":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/Начало.txt','r').read(),
                reply_markup=Greet_keyboard)
            cur.execute('''DELETE from users 
                WHERE chat_id=(%s) AND 
                message_id=(%s)''', 
                [call.message.chat.id, call.message.message_id])
            con.commit()
        except:
            print('MessageNotModifed8')
#----------------------------------------------------------------------------------------


#Матпомощь
def CashAid(call, bot):
    #Начало --> Матпомощь
    if call.data == "CA":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Матпомощь/Матпомощь.txt','r').read(),         
                parse_mode="HTML", 
                reply_markup=Aid_keyboard)
        except:
            print('MessageNotModifed9')
    #Начало --> Матпомощь --> Контакты
    if call.data == "Co":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Матпомощь/Контакты.txt','r').read(), 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Back_to_Aid_keyboard)
        except:
            print('MessageNotModifed10')
    #Начало --> Матпомощь --> Правила
    if call.data == "Ru":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Матпомощь/Правила.txt','r').read(),                 
                parse_mode="HTML", 
                reply_markup=Back_to_Aid_keyboard)
        except:
            print('MessageNotModifed11')
    #Начало --> Матпомощь --> Категории
    if call.data == "CaB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Матпомощь/Категории.txt','r').read(), 
                parse_mode="HTML", 
                reply_markup=Back_to_Aid_keyboard)
        except:
            print('MessageNotModifed12')
    #Начало --> Матпомощь --> Бланк Матпомощи
    if call.data == "Fo":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Матпомощь/БланкМатпомощи.txt','r').read(),
                parse_mode="HTML", 
                reply_markup=Back_to_Aid_keyboard)
        except:
            print('MessageNotModifed13')
    #Начало --> Матпомощь --> Удалённая подача (Кнопка отключена за неактуальностью)
    if call.data == "Di":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Матпомощь/УдалённаяПодача.txt','r').read(), 
                disable_web_page_preview=1, 
                parse_mode="HTML", 
                reply_markup=Back_to_Aid_keyboard)
        except:
            print('MessageNotModifed14')
#------------------------------------------------------------------------------------------------------


#Сенат
def Senat(call, bot):
    #Начало --> Сенат
    if call.data == "Se":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Сенат/Сенат.txt','r').read(),   
                disable_web_page_preview=1, 
                parse_mode='HTML', 
                reply_markup=Senat_keyboard)
        except:
            print('MessageNotModifed15')
    #Начало --> Сенат --> Устав
    if call.data == "Ch":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Сенат/Устав.txt','r').read(),
                parse_mode='HTML', 
                reply_markup=Back_to_Senat_keyboard)
        except:
            print('MessageNotModifed16')
    #Начало --> Сенат --> Инфографика
    if call.data == "In":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Сенат/Инфографика.txt','r').read(), 
                parse_mode='HTML', 
                reply_markup=Back_to_Senat_keyboard)
        except:
            print('MessageNotModifed17')
    #Начало --> Сенат --> Контакты
    if call.data == "Cse":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Сенат/Контакты.txt','r').read(), 
                parse_mode='HTML', 
                disable_web_page_preview=1, 
                reply_markup=Back_to_Senat_keyboard)
        except:
            print('MessageNotModifed18')
#------------------------------------------------------------------------------------------------------


#Хозотдел
def MaintDep(call, bot):
    #Начало --> Хозотдел
    if call.data == "MD":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/Хозотдел.txt','r').read(),
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=MaintDep_keyboard)
        except:
            print('MessageNotModifed49')
    #Начало --> Хозотдел --> Инструментарий
    if call.data == "ToR":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Хозотдел/Инструментарий.txt','r').read(), 
                parse_mode="HTML", 
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed57')
    #Начало --> Хозотдел --> Ответственные за этажи
    if call.data == "FF":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/ОтветственныеЗаЭтажи.txt','r').read(), 
                parse_mode="HTML",
                reply_markup = Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed5767')
    #Начало --> Хозотдел --> КДС
    if call.data == "RFK":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/КДС.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed50')
    #Начало --> Хозотдел --> Клуб
    if call.data == "Cl":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/Клуб.txt','r').read(),
                parse_mode="HTML", 
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed51')
    #Начало --> Хозотдел --> Душ
    if call.data == "Sh":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/Душ.txt','r').read(),   
                parse_mode="HTML", 
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed52')
    #Начало --> Хозотдел --> Боталка
    if call.data == "TR":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/Боталка.txt','r').read(), 
                parse_mode="HTML", 
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed53')

    #Начало --> Хозотдел --> Тренажёрка
    if call.data == "SR":
        try: 
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/Качалка.txt','r').read(),
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed54')
    #Начало --> Хозотдел --> Велокомната
    if call.data == "BR":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/Велокомната.txt','r').read(),
                parse_mode="HTML", 
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed55')
    #Начало --> Хозотдел --> Стиралка
    if call.data == "WR":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('texts/Хозотдел/Стиралка.txt','r').read(),
                parse_mode="HTML", 
                reply_markup=Back_to_MaintDep_keyboard)
        except:
            print('MessageNotModifed56')
#------------------------------------------------------------------------------------------------------


#Деканат
def Dekanat(call, bot):
    #Начало --> Деканат
    if call.data == "De":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Деканат/Деканат.txt','r').read(),
                disable_web_page_preview=1, 
                reply_markup=Dekanat_keyboard)
        except:
            print('MessageNotModifed43')
    #Начало --> Деканат --> Дирекция это
    if call.data == "Dir":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Деканат/ДирекцияЭто.txt','r').read(),
                disable_web_page_preview=1, 
                parse_mode="HTML" , 
                reply_markup=Back_to_Dekanat_keyboard)
        except:
            print('MessageNotModifed44')
    #Начало --> Деканат --> Контакты
    if call.data == "DirC":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Деканат/Контакты.txt','r').read(),
                disable_web_page_preview=1, 
                parse_mode="HTML", 
                reply_markup=Back_to_Dekanat_keyboard)
        except:
            print('MessageNotModifed47')
    #Начало --> Деканат --> Ведомость
    if call.data == "VeB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Деканат/Ведомость.txt','r').read(),
                disable_web_page_preview=1, 
                parse_mode="HTML", 
                reply_markup=Back_to_Dekanat_keyboard)
        except:
            print('MessageNotModifed45')
    #Начало --> Деканат --> Академ. отпуск
    if call.data == "Ac":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('texts/Деканат/АкадемОтпуск.txt','r').read(),
                disable_web_page_preview=1, 
                parse_mode="HTML", 
                reply_markup=Back_to_Dekanat_keyboard)
        except:
            print('MessageNotModifed48')
#------------------------------------------------------------------------------------------------------


#Абитуриентам
def Abiturient(call, bot):
    #Начало --> Абитуриентам
    if call.data == "En":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Абитуриентам/Абитуриентам.txt','r').read(), 
                parse_mode="HTML", 
                reply_markup=Abit_keyboard)
        except:
            print('MessageNotModifed36')
    #Начало --> Абитуриентам --> Ссылки
    if call.data == "UL":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Абитуриентам/Ссылки.txt','r').read(), 
                parse_mode="HTML", 
                reply_markup=Back_to_Abit_keyboard)
        except:
            print('MessageNotModifed37')
    #Начало --> Абитуриентам --> КартаГородка
    if call.data == "Map":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Абитуриентам/КартаГородка.txt','r').read(),
                parse_mode="HTML", 
                reply_markup=Back_to_Abit_keyboard )
        except:
            print('MessageNotModifed38')
    #Начало --> Абитуриентам --> О ЛФИ
    if call.data == "AS":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id, 
                text=open('texts/Абитуриентам/ОЛФИ.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Abit_keyboard )
        except:
            print('MessageNotModifed21')
    #Начало --> Абитуриентам --> Конкурсные Группы
    if call.data == "Sy":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Абитуриентам/КонкурсныеГруппы.txt','r').read(),
                parse_mode="HTML", 
                reply_markup=Back_to_Abit_keyboard)
        except:
            print('MessageNotModifed40')
    #Начало --> Абитуриентам --> Где я буду жить
    if call.data == "Do":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Абитуриентам/ГдеЯБудуЖить.txt','r').read(), 
                parse_mode="HTML", 
                reply_markup=Back_to_Abit_keyboard)
        except:
            print('MessageNotModifed41')
    #Начало --> Абитуриентам --> Статистика Поступления
    if call.data == "Stat":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/Абитуриентам/СтатистикаПоступления.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Abit_keyboard)
        except:
            print('MessageNotModifed42')
#----------------------------------------------------------------------------------------


#Общие студенческие дела
def GeneralStudentBuisness(call, bot):
    #Общие студенческие дела
    if call.data == "GS":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('texts/ОбщиеСтуденческиеДела/ОбщиеСтуденческиеДела.txt','r').read(),
                reply_markup=Stud_keyboard)
        except:
            print('MessageNotModifed19')
    #Общие студенческие дела --> Документы студента
    if call.data == "StDoc":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/ДокументыСтудента/ДокументыСтудента.txt','r').read(),
                reply_markup=Doc_keyboard)
        except:
            print('MessageNotModifed21')
    #Общие студенческие дела --> Документы студента --> Студ. билет
    if call.data == "StC":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/ДокументыСтудента/СтудБилет.txt','r').read(),
                reply_markup=Back_to_Doc_keyboard)
        except:
            print('MessageNotModifed22')
    #Общие студенческие дела --> Документы студента --> ЭКД
    if call.data == "EC":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/ДокументыСтудента/ЭКД.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Doc_keyboard)
        except:
            print('MessageNotModifed23')
    #Общие студенческие дела --> Документы студента --> Соц. карта
    if call.data == "SoC":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/ДокументыСтудента/СоцКарта.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Doc_keyboard)
        except:
            print('MessageNotModifed29')
    #Общие студенческие дела --> Документы студента --> Phystech.edu
    if call.data == "PhE":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/ДокументыСтудента/PhystechEdu.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Doc_keyboard)
        except:
            print('MessageNotModifed28')
    #Общие студенческие дела --> Документы студента --> Регистрация
    if call.data == "LiR":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/ДокументыСтудента/Регистрация.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Doc_keyboard)
        except:
            print('MessageNotModifed30')
    #Общие студенческие дела --> Поликлиника
    if call.data == "Pol":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Поликлиника/Поликлиника.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Hosp_keyboard)
        except:
            print('MessageNotModifed24')
    #Общие студенческие дела --> Поликлиника --> Как прикрепляться
    if call.data == "HTR":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Поликлиника/КакПрикрепляться.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Hosp_keyboard)
        except:
            print('MessageNotModifed25')
    #Общие студенческие дела --> Поликлиника --> Как записаться
    if call.data == "HTV":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Поликлиника/КакЗаписаться.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Hosp_keyboard)
        except:
            print('MessageNotModifed26')
    #Общие студенческие дела --> Абрамовка
    if call.data == "Abr":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Абрамовка/Абрамовка.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Abram_keyboard)
        except:
            print('MessageNotModifed32')
    #Общие студенческие дела --> Абрамовка --> Что это и для кого?
    if call.data == "WTF":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Абрамовка/ЧтоЭто.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Abram_keyboard)
        except:
            print('MessageNotModifed32')
    #Общие студенческие дела --> Абрамовка --> Малообеспеченность
    if call.data == "LAB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Абрамовка/Малообеспеченность.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Abram_keyboard)
        except:
            print('MessageNotModifed33')
    #Общие студенческие дела --> Абрамовка --> Успеваемость
    if call.data == "GMB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Абрамовка/Успеваемость.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Abram_keyboard)
        except:
            print('MessageNotModifed34')
    #Общие студенческие дела --> Абрамовка --> Частозадаваемые вопросы
    if call.data == "AQB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Абрамовка/Вопросы.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Abram_keyboard)
        except:
            print('MessageNotModifed35')
    #Общие студенческие дела --> Справки
    if call.data == "Ce":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Справки.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Stud_keyboard)
        except:
            print('MessageNotModifed46')
    #Общие студенческие дела --> Библиотека
    if call.data == "Lib":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/Библиотека.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Stud_keyboard)
        except:
            print('MessageNotModifed27')
    #Общие студенческие дела --> Воинский учёт
    if call.data == "MilReg":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('texts/ОбщиеСтуденческиеДела/ВоинскийУчёт.txt','r').read(),
                parse_mode="HTML",
                reply_markup=Back_to_Stud_keyboard)
        except:
            print('MessageNotModifed20')
#----------------------------------------------------------------------------------------


#Жалобы и предложения
def Claims(call, bot, cur, con):
    if call.data == "ClB":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, 
                    message_id=call.message.message_id,
                    text=open('texts/ЖалобыИПредложения.txt','r').read(), 
                    parse_mode="HTML", 
                    disable_web_page_preview=1, 
                    reply_markup=Back_to_Greet_keyboard)
                cur.execute('''DELETE from users 
                    WHERE chat_id=(%s) AND 
                    message_id=(%s)''',
                    [call.message.chat.id, call.message.message_id])
                cur.execute('''INSERT INTO users (chat_id,message_id,button) 
                    VALUES (%s, %s, %s)''', 
                    [call.message.chat.id, call.message.message_id,'text'])
                con.commit()
            except:
                print('MessageNotModifed58')
#----------------------------------------------------------------------------------------


#Кнопка починки в чате сената
def Fix(call, bot, cur, con):
    if call.data == "FiB":
        Floor = call.message.text.split('\n')[0][len(call.message.text.split('\n')[0]) - 1]
        Room = call.message.text.split('\n')[1]
        TypeOfProblem = call.message.text.split('\n')[2]
        if len(call.message.text.split('\n')) == 3:
            cur.execute('''DELETE from problems 
                WHERE floor=(%s) AND 
                room=(%s) AND 
                typeofproblem=(%s)''',
                [int(Floor),Room,TypeOfProblem])
        else:
            NumberOfSink=call.message.text.split('\n')[3][len(call.message.text.split('\n')[3]) - 1]
            cur.execute('''DELETE from problems 
                WHERE floor=(%s) AND 
                room=(%s) AND 
                typeofproblem=(%s) AND 
                numberofproblem=(%s)''',
                [int(Floor),Room,TypeOfProblem, int(NumberOfSink)])
        bot.edit_message_text(chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="<b>Поломка:</b>\n"+call.message.text+"\n<b>удалена из базы</b>",
            parse_mode="HTML")
        con.commit() 
#----------------------------------------------------------------------------------------


#6-ка: поломки, мыло, бумага
def Issues(call, bot, cur, con):
    #6-ка: поломки, мыло, бумага
    if call.data == "BrB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text="На каком этаже произошла проблема?", 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Broken_keyboard)
            cur.execute('''DELETE from users 
                WHERE chat_id=(%s) AND 
                message_id=(%s)''',
                [call.message.chat.id, call.message.message_id])
            cur.execute('''INSERT INTO users (chat_id,message_id,button) 
                VALUES (%s, %s, %s)''',
                [call.message.chat.id, call.message.message_id, 'Problem'])
            con.commit()
        except:
            print('MessageNotModifed59')
    #6-ка: поломки, мыло, бумага --> Выбран 1ый этаж
    if call.data == "1F":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text="Опишите проблему сообщением", 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Back_to_Broken_keyboard)
            cur.execute('''UPDATE users SET floor=1 
                WHERE chat_id=(%s) AND 
                message_id=(%s)''',
                [call.message.chat.id, call.message.message_id])
            cur.execute('''UPDATE users SET room=NULL 
                WHERE chat_id=(%s) AND 
                message_id=(%s)''',
                [call.message.chat.id, call.message.message_id])
            con.commit()
        except:
            print('MessageNotModifed62')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж
    if call.data in ["2F","3F","4F","5F"]:
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text="Где произошла проблема?", 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Rooms_keyboard)
            cur.execute('''UPDATE users SET floor=(%s) 
                WHERE chat_id=(%s) AND 
                message_id=(%s)''',
                [int(call.data[0]), call.message.chat.id, call.message.message_id])
            cur.execute('''UPDATE users SET room=NULL 
                WHERE chat_id=(%s) AND 
                message_id=(%s)''',
                [call.message.chat.id, call.message.message_id])
                con.commit()
        except:
            print('MessageNotModifed63')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5 этаж <-- Назад
    if call.data == "Bb9":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text="Где произошла проблема?", 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Rooms_keyboard)
            cur.execute('''UPDATE users SET room=NULL 
                WHERE chat_id=(%s) AND message_id=(%s)''',
                [call.message.chat.id, call.message.message_id])
            con.commit()
        except:
            print('MessageNotModifed60')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж --> Кухня/Умывальник
    if call.data in ["Ki","WaB"]:
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text="Что случилось?", 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=KitchenWash_keyboard)
            match call.data:
                case "Ki":
                    cur.execute('''UPDATE users SET room='кухня' 
                        WHERE chat_id=(%s) AND 
                        message_id=(%s)''',
                        [call.message.chat.id, call.message.message_id])
                    con.commit()
                case "Wab":
                    cur.execute('''UPDATE users SET room='умывальник'
                        WHERE chat_id=(%s) AND
                        message_id=(%s)''',
                        [call.message.chat.id, call.message.message_id])
                    con.commit()
        except:
            print('MessageNotModifed67')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж --> Кухня/Умывальник --> Неполадки с краном
    if call.data in ["TaB","TaB2","PiB"]:
        cur.execute('''SELECT floor,room from users 
            WHERE chat_id=(%s) AND 
            message_id=(%s)''',
            [call.message.chat.id, call.message.message_id])
        rows = cur.fetchall()
        
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж --> Туалет
    if call.data == "ToB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text="Что случилось?", 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Toilet_keyboard)
            cur.execute('''UPDATE users SET room='туалет' 
                WHERE chat_id=(%s) AND message_id=(%s)''',
                [call.message.chat.id, call.message.message_id])
            con.commit()
        except:
            print('MessageNotModifed167')


