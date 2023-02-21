# - *- coding: utf- 8 - *-
import telebot 
import psycopg2 
from telebot import types 
import config 
from keyboards import *
import keyhandlers

bot = telebot.TeleBot(config.token, threaded=False) #создание объекта бота
try: #пытаемся подключиться к базе данных
    con = psycopg2.connect(
      database="postgres",
      user="postgres",
      password="infodept",
      host="localhost",
      port="5432"
    )
except:
    bot.send_message(446636263,"С базой проблема")

cur = con.cursor() #после подключения создаём объект курсора в нашей базе



@bot.message_handler(commands=['start', 'help']) #Реакция бота на команды /start и /help
def any_msg(message):
    try:
        bot.send_message(message.chat.id, "Привет, о чём ты хочешь узнать? \nОб ошибках и неточностях можно сообщать "
        "<a href='https://t.me/aslan_monahov'>моему создателю</a>. Если не видно названия кнопок, "
        "увеличь окно приложения.", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Greet_keyboard)
        #после введения команд бот удаляет пользователя из таблицы users в базе и начинает работу с пользователем с чистого листа.
        #таблица users в базе отслеживает, в каком месте находится пользователь, в начальном меню или где-то ниже
        cur.execute('''DELETE from users where chat_id=(%s) AND (button=(%s) OR floor=(%s) OR room=(%s) OR typeofproblem=(%s))''', [message.chat.id, 'text', 1, 'text', 'text'])
        con.commit() #сохранение изменений в базу
    except:
        print('Database problem')




@bot.message_handler(content_types=['text']) #Реакция бота на отправленный кем либо текст (команды не считаются как текст)
def send_text(message):
    #далее идёт проверка на то, что сообщение является ответом кому-то, что этот кто-то это наш бот и что сообщение начинается с команды !rep
    if (message.reply_to_message != None) and (message.reply_to_message.from_user.id == 1134290542) and (message.text.startswith("!rep")): 
        if (message.reply_to_message.content_type=='text'):
            try:
                bot.send_message(str(message.reply_to_message.text.split('\n')[0]), message.text[4:len(message.text)])
                bot.send_message(-1001759376814, "Сообщение отправлено")
            except:
                print('MessageNotModifed')
                bot.send_message(-1001759376814, "Сообщение не отправлено. Отвечать надо на пост с цифровым айди в начале.")
        if (message.reply_to_message.content_type=='photo') or (message.reply_to_message.content_type=='video'):
            try:
                bot.send_message(str(message.reply_to_message.caption.split('\n')[0]), message.text[4:len(message.text)])
                bot.send_message(-1001759376814, "Сообщение отправлено")
            except:
                print('MessageNotModifed')
                bot.send_message(-1001759376814,"Сообщение не отправлено. Отвечать надо на пост с цифровым айди в начале.")
    if (message.chat.id == -1001759376814) and (message.text.startswith("!list")):
        cur.execute('''SELECT floor,room,typeofproblem,numberofproblem from problems''')
        rows = cur.fetchall()
        if len(rows)== False:
            bot.send_message(-1001759376814, "Поломок в базе нет", parse_mode="HTML")
        for row in rows:
            s = ""
            s = s + "этаж "+ str(row[0]) + "\n" + str(row[1]) + "\n" + str(row[2])
            if (row[3]!=None):
                s = s + "\nномер "+str(row[3])
            bot.send_message(-1001759376814,s, parse_mode="HTML",
                     disable_web_page_preview=1, reply_markup=keyboard111)

    cur.execute('''SELECT chat_id,message_id,button,floor,room,typeofproblem from users''')
    try:
        rows = cur.fetchall()
    except:
        bot.send_message(446636263, str(rows))
        cur.execute('''SELECT floor,room,typeofproblem,numberofproblem from problems''')
        rows = cur.fetchall()
        bot.send_message(446636263, str(rows))
    for row in rows:
        if (row[0] == message.chat.id):
            if (row[2] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + message.text
                    bot.send_message(-1001759376814, mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed1')
                break
            if (row[3] == 1):
                try:
                    mes = str(message.chat.id) + "\n" + message.text
                    bot.send_message(-1001759376814, "первый этаж, поломка + ⬇️")
                    bot.send_message(-1001759376814, mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed2')
            if (row[4] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + message.text
                    bot.send_message(-1001759376814, str(row[3]) + " этаж⬇️")
                    bot.send_message(-1001759376814, mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed3')
            if (row[5] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + message.text
                    bot.send_message(-1001759376814, str(row[3])+ " этаж\n" + str(row[4])+"⬇️")
                    bot.send_message(-1001759376814, mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed4')
@bot.message_handler(content_types=['photo'])
def send_text(message):
    cur.execute('''SELECT chat_id,message_id,button,floor,room,typeofproblem from users''')
    rows = cur.fetchall()
    for row in rows:
        if (row[0] == message.chat.id):
            if (row[2] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_photo(-1001759376814, message.photo[0].file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed01')
                break
            if (row[3] == 1):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_message(-1001759376814, "первый этаж, поломка + ⬇️")
                    bot.send_photo(-1001759376814, message.photo[0].file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed02')
            if (row[4] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_message(-1001759376814, str(row[3]) + " этаж⬇️")
                    bot.send_photo(-1001759376814, message.photo[0].file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed03')
            if (row[5] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_message(-1001759376814, str(row[3]) + " этаж\n" + str(row[4]) + "⬇️")
                    bot.send_photo(-1001759376814, message.photo[0].file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed04')
@bot.message_handler(content_types=['video'])
def send_text(message):
    cur.execute('''SELECT chat_id,message_id,button,floor,room,typeofproblem from users''')
    rows = cur.fetchall()
    for row in rows:
        if (row[0] == message.chat.id):
            if (row[2] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed011')
                break
            if (row[3] == 1):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_message(-1001759376814, "первый этаж, поломка + ⬇️")
                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed022')
            if (row[4] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_message(-1001759376814, str(row[3]) + " этаж⬇️")
                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed033')
            if (row[5] == 'text'):
                try:
                    mes = str(message.chat.id) + "\n" + str(message.caption)
                    bot.send_message(-1001759376814, str(row[3]) + " этаж\n" + str(row[4]) + "⬇️")
                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed044')
@bot.message_handler(content_types=['video_note'])
def send_text(message):
    cur.execute('''SELECT chat_id,message_id,button,floor,room,typeofproblem from users''')
    rows = cur.fetchall()
    for row in rows:
        if (row[0] == message.chat.id):
            if (row[2] == 'text'):
                try:
                    bot.send_video_note(-1001759376814, message.video_note.file_id)
                    bot.send_message(-1001759376814, str(message.chat.id))
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed1')
                break
            if (row[3] == 1):
                try:
                    bot.send_message(-1001759376814, "первый этаж, поломка + ⬇️")
                    bot.send_video_note(-1001759376814, message.video_note.file_id)
                    bot.send_message(-1001759376814, str(message.chat.id))
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed2')
            if (row[4] == 'text'):
                try:
                    bot.send_message(-1001759376814, row[3] + "⬇️")
                    bot.send_video_note(-1001759376814, message.video_note.file_id)
                    bot.send_message(-1001759376814, str(message.chat.id))
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed3')
            if (row[5] == 'text'):
                try:
                    bot.send_message(-1001759376814, str(row[3]) + " этаж\n" + str(row[4]) + "⬇️")
                    bot.send_video_note(-1001759376814, message.video_note.file_id)
                    bot.send_message(-1001759376814, str(message.chat.id))
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed4')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        #В беседе сената починили поломку и сообщили боту
        keyhandlers.Fix(call,bot,cur,con)

        #В диалоге с ботом открылось начальное меню
        keyhandlers.Beginning(call,bot,cur,con)

        #Подразделы начального меню
        keyhandlers.CashAid(call, bot)#Подразделы Матпомощи
        keyhandlers.Senat(call, bot)#Подразделы Сената
        keyhandlers.Dekanat(call, bot)#Подразделы Деканата
        keyhandlers.MaintDep(call, bot)#Подразделы Хоз. Отдела
        keyhandlers.Abiturient(call, bot)#Подразделы Абитуриентов
        keyhandlers.GeneralStudentBuisness(call, bot)#Подразделы Общих Студ. Дел
        keyhandlers.Claims(call, bot, cur, con)#Жалобы и предложения

        #Отдельная система кнопок для сообщений о поломках
        if call.data == "BrB":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="На каком этаже произошла проблема?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Broken_keyboard)
                cur.execute('''DELETE from users where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                cur.execute('''INSERT INTO users (chat_id,message_id,button) VALUES (%s, %s, %s)''',[call.message.chat.id, call.message.message_id, 'Problem'])
                con.commit()
            except:
                print('MessageNotModifed59')
        if call.data == "Bb9":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Где произошла проблема?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Rooms_keyboard)
                cur.execute('''UPDATE users SET room=NULL where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed60')
        if call.data == "Bb10":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что случилось?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Kitchen_keyboard)
                cur.execute('''UPDATE users SET typeofproblem=NULL where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed61')
        if call.data == "Bb12":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что случилось?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=WashBasin_keyboard)
                cur.execute('''UPDATE users SET typeofproblem=NULL where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed61')
        if call.data == "Bb14":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что случилось?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Toilet_keyboard)
                cur.execute('''UPDATE users SET typeofproblem=NULL where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed61')
        if call.data == "1F":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Опишите проблему сообщением", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Back_to_Broken_keyboard)
                cur.execute('''UPDATE users SET floor=1 where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                cur.execute('''UPDATE users SET room=NULL where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed62')
        if call.data == "2F":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Где произошла проблема?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Rooms_keyboard)
                cur.execute('''UPDATE users SET floor=2 where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                cur.execute('''UPDATE users SET room=NULL where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed63')
        if call.data == "3F":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Где произошла проблема?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Rooms_keyboard)
                cur.execute('''UPDATE users SET floor=3 where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                cur.execute('''UPDATE users SET room=NULL where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed64')
        if call.data == "4F":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Где произошла проблема?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Rooms_keyboard)
                cur.execute('''UPDATE users SET floor=4 where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                cur.execute('''UPDATE users SET room=NULL where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed65')
        if call.data == "5F":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Где произошла проблема?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Rooms_keyboard)
                cur.execute('''UPDATE users SET floor=5 where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                cur.execute('''UPDATE users SET room=NULL where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed66')
        if call.data == "WaB":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что случилось?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=WashBasin_keyboard)
                cur.execute('''UPDATE users SET room='умывальник' where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                cur.execute('''UPDATE users SET typeofproblem=NULL where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed0676')
        if call.data == "TaB3":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Какой номер у этой раковины/крана?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Sink_keyboard)
                cur.execute('''UPDATE users SET typeofproblem='Кран подтекает/не закрывается' where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed685')
        if call.data == "TaB4":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Какой номер у этой раковины/крана?", parse_mode="HTML", disable_web_page_preview=1,reply_markup=Sink_keyboard)
                cur.execute('''UPDATE users SET typeofproblem='Кран гудит' where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed688')
        if call.data == "PiB2":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Какой номер у этой раковины/крана?", parse_mode="HTML", disable_web_page_preview=1,
                                      reply_markup=Sink_keyboard)
                cur.execute('''UPDATE users SET typeofproblem='Труба под раковиной подтекает' where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed688')
        if call.data == "SoB2":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room from problems WHERE typeofproblem=(%s)''',["Закончилось мыло"])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\nЗакончилось мыло", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem) VALUES (%s, %s, %s)''',[row[0], row[1], "Закончилось мыло"])
                        con.commit()
            except:
                print('MessageNotModifed6870')
        if call.data == "SiB1":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room,typeofproblem from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room,typeofproblem from problems WHERE numberofproblem=(%s)''',[1])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]) and (row[2]==row2[2]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\n"+row[2]+"\nРаковина номер 1", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) VALUES (%s, %s, %s, %s)''',[row[0], row[1], row[2], 1])
                        con.commit()
            except:
                print('MessageNotModifed608')
        if call.data == "SiB2":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room,typeofproblem from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room,typeofproblem from problems WHERE numberofproblem=(%s)''',['2'])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]) and (row[2]==row2[2]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\n"+row[2]+"\nРаковина номер 2", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) VALUES (%s, %s, %s, %s)''',[row[0], row[1], row[2], 2])
                        con.commit()
            except:
                print('MessageNotModifed68002')
        if call.data == "SiB3":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room,typeofproblem from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room,typeofproblem from problems WHERE numberofproblem=(%s)''',['3'])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]) and (row[2]==row2[2]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\n"+row[2]+"\nРаковина номер 3", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) VALUES (%s, %s, %s, %s)''',[row[0], row[1], row[2], 3])
                        con.commit()
            except:
                print('MessageNotModifed68003')
        if call.data == "SiB4":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room,typeofproblem from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room,typeofproblem from problems WHERE numberofproblem=(%s)''',['4'])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]) and (row[2]==row2[2]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\n"+row[2]+"\nРаковина номер 4", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) VALUES (%s, %s, %s, %s)''',[row[0], row[1], row[2], 4])
                        con.commit()
            except:
                print('MessageNotModifed68004')
        if call.data == "SiB5":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room,typeofproblem from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room,typeofproblem from problems WHERE numberofproblem=(%s)''',['5'])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]) and (row[2]==row2[2]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\n"+row[2]+"\nРаковина номер 5", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) VALUES (%s, %s, %s, %s)''',[row[0], row[1], row[2], 5])
                        con.commit()
            except:
                print('MessageNotModifed68005')
        if call.data == "SiB6":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room,typeofproblem from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room,typeofproblem from problems WHERE numberofproblem=(%s)''',['6'])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]) and (row[2]==row2[2]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\n"+row[2]+"\nРаковина номер 6", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) VALUES (%s, %s, %s, %s)''',[row[0], row[1], row[2], 6])
                        con.commit()
            except:
                print('MessageNotModifed68006')
        if call.data == "LaB":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room,typeofproblem from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room,typeofproblem from problems WHERE numberofproblem=(%s)''',['0'])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]) and (row[2]==row2[2]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\n"+row[2]+"\nНеизвестный номер раковины", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) VALUES (%s, %s, %s, %s)''',[row[0], row[1], row[2], 0])
                        con.commit()
            except:
                print('MessageNotModifed6800')
        if call.data == "ToB":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что случилось?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Toilet_keyboard)
                cur.execute('''UPDATE users SET room='туалет' where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed167')
        if call.data == "UrB":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room from problems WHERE typeofproblem=(%s)''',
                            ["Засорился писсуар"])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0] == row2[0]) and (row[1] == row2[1]):
                            N = True
                    if (N == False):
                        bot.send_message(-1001759376814,
                                         "Новая поломка в базе, этаж " + str(row[0]) + "\n" + row[
                                             1] + "\nЗасорился писсуар", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem) VALUES (%s, %s, %s)''',
                                    [row[0], row[1], "Засорился писсуар"])
                        con.commit()
            except:
                print('MessageNotModifed619')
        if call.data == "PaB":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room from problems WHERE typeofproblem=(%s)''',
                            ["Кончилась бумага"])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0] == row2[0]) and (row[1] == row2[1]):
                            N = True
                    if (N == False):
                        bot.send_message(-1001759376814,
                                         "Новая поломка в базе, этаж " + str(row[0]) + "\n" + row[
                                             1] + "\nКончилась бумага", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem) VALUES (%s, %s, %s)''',
                                    [row[0], row[1], "Кончилась бумага"])
                        con.commit()
            except:
                print('MessageNotModifed6191')
        if call.data == "Ki":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что случилось?", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Kitchen_keyboard)
                cur.execute('''UPDATE users SET room='кухня' where chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed67')
        if call.data == "TaB":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room from problems WHERE typeofproblem=(%s)''',["Кран подтекает/не закрывается"])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0]==row2[0]) and (row[1]==row2[1]):
                            N=True
                    if (N==False):
                        bot.send_message(-1001759376814, "Новая поломка в базе, этаж "+str(row[0])+"\n"+row[1]+"\nКран подтекает/не закрывается", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem) VALUES (%s, %s, %s)''',[row[0], row[1], "Кран подтекает/не закрывается"])
                        con.commit()
            except:
                print('MessageNotModifed68')
        if call.data == "TaB2":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room from problems WHERE typeofproblem=(%s)''',
                            ["Кран гудит"])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0] == row2[0]) and (row[1] == row2[1]):
                            N = True
                    if (N == False):
                        bot.send_message(-1001759376814,
                                         "Новая поломка в базе, этаж " + str(row[0]) + "\n" + row[
                                             1] + "\nКран гудит", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem) VALUES (%s, %s, %s)''',
                                    [row[0], row[1], "Кран гудит"])
                        con.commit()
            except:
                print('MessageNotModifed69')
        if call.data == "PiB":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room from problems WHERE typeofproblem=(%s)''',
                            ["Труба под раковиной подтекает"])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0] == row2[0]) and (row[1] == row2[1]):
                            N = True
                    if (N == False):
                        bot.send_message(-1001759376814,
                                         "Новая поломка в базе, этаж " + str(row[0]) + "\n" + row[
                                             1] + "\nТруба под раковиной подтекает", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem) VALUES (%s, %s, %s)''',
                                    [row[0], row[1], "Труба под раковиной подтекает"])
                        con.commit()
            except:
                print('MessageNotModifed70')
        if call.data == "SoB":
            try:
                bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                cur.execute('''SELECT floor,room from users WHERE chat_id=(%s) AND message_id=(%s)''',
                            [call.message.chat.id, call.message.message_id])
                rows = cur.fetchall()
                cur.execute('''SELECT floor,room from problems WHERE typeofproblem=(%s)''',
                            ["Закончилось мыло"])
                rows2 = cur.fetchall()
                for row in rows:
                    N = False
                    for row2 in rows2:
                        if (row[0] == row2[0]) and (row[1] == row2[1]):
                            N = True
                    if (N == False):
                        bot.send_message(-1001759376814,
                                         "Новая поломка в базе, этаж " + str(row[0]) + "\n" + row[
                                             1] + "\nЗакончилось мыло", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
                        cur.execute('''INSERT INTO problems (floor,room,typeofproblem) VALUES (%s, %s, %s)''',
                                    [row[0], row[1], "Закончилось мыло"])
                        con.commit()
            except:
                print('MessageNotModifed71')
        if call.data == "AnB":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Опишите проблему сообщением", parse_mode="HTML", reply_markup=Back_to_Rooms_keyboard)
                cur.execute('''UPDATE users SET room='text' where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed072')
        if call.data == "AnB2":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Опишите проблему сообщением", parse_mode="HTML", reply_markup=Back_to_Kitchen_keyboard)
                cur.execute('''UPDATE users SET typeofproblem='text' where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed72')
        if call.data == "AnB3":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Опишите проблему сообщением", parse_mode="HTML", reply_markup=Back_to_WashBasin_keyboard)
                cur.execute('''UPDATE users SET typeofproblem='text' where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed720')
        if call.data == "AnB4":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Опишите проблему сообщением", parse_mode="HTML", reply_markup=Back_to_Toilet_keyboard)
                cur.execute('''UPDATE users SET typeofproblem='text' where chat_id=(%s) AND message_id=(%s)''',[call.message.chat.id, call.message.message_id])
                con.commit()
            except:
                print('MessageNotModifed7201')
bot.infinity_polling()
