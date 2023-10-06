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

#после подключения создаём объект курсора в нашей базе
cur = con.cursor()

#Реакция бота на команды /start и /help
@bot.message_handler(commands=['start', 'help'])
def any_msg(message):
    try:
        bot.send_message(message.chat.id, "Привет, о чём ты хочешь узнать? \nОб ошибках и неточностях можно сообщать "
        "<a href='https://t.me/aslan_monahov'>моему создателю</a>. Если не видно названия кнопок, "
        "увеличь окно приложения.", parse_mode="HTML", disable_web_page_preview=1, reply_markup=Greet_keyboard)
        #после введения команд бот удаляет пользователя из таблицы users в базе и начинает работу с пользователем с чистого листа.
        #таблица users в базе отслеживает, в каком месте находится пользователь, в начальном меню или где-то ниже
        cur.execute('''DELETE from users where chat_id=(%s)''', [message.chat.id])
        con.commit() #сохранение изменений в базу
    except:
        print('/command problem')



#Реакция бота на отправленный кем либо текст (команды не считаются как текст)
@bot.message_handler(content_types=['text'])
def send_text(message):
    #далее идёт проверка на то, что сообщение является ответом кому-то, что этот кто-то это наш бот и что сообщение начинается с команды !rep
    if (message.reply_to_message != None) and (message.reply_to_message.from_user.id == 1134290542) and (message.text.startswith("!rep")): 
        if (message.reply_to_message.content_type=='text'):
            try:
                #Член сената из чата сената таким образом отправляет сообщение пожаловшемуся
                bot.send_message(str(message.reply_to_message.text.split('\n')[0]), message.text[4:len(message.text)])
                bot.send_message(-1001759376814, "Сообщение отправлено")
            except:
                print('MessageNotModifed')
                #если что-то пошло не так, например пожаловавшийся заблокировал бота, в чат сената отправляется предупреждение об этом
                bot.send_message(-1001759376814, "Сообщение не отправлено. Отвечать надо на пост с цифровым айди в начале.")
        if (message.reply_to_message.content_type=='photo') or (message.reply_to_message.content_type=='video'):
            try:
                #если из сената захотели отправить фото или видео
                bot.send_message(str(message.reply_to_message.caption.split('\n')[0]), message.text[4:len(message.text)])
                bot.send_message(-1001759376814, "Сообщение отправлено")
            except:
                print('MessageNotModifed')
                bot.send_message(-1001759376814,"Сообщение не отправлено. Отвечать надо на пост с цифровым айди в начале.")
    #проверка на тот случай, если в чате сената запросили список поломок из базы
    if (message.chat.id == -1001759376814) and (message.text.startswith("!list")):
        cur.execute('''SELECT floor,room,typeofproblem,numberofproblem from problems''')
        rows = cur.fetchall()
        if len(rows)== False:
            bot.send_message(-1001759376814, "Поломок в базе нет", parse_mode="HTML")
        for row in rows:
            s = ""
            s = s + "этаж "+ str(row[0]) + "\n" + str(row[1]) + "\n" + str(row[2])
            if not (row[3] is None):
                s = s + "\nномер "+str(row[3])
            bot.send_message(-1001759376814,s, parse_mode="HTML",
                     disable_web_page_preview=1, reply_markup=Fix_keyboard)
    #Пробегаемся теперь по базе пользователей, если сообщение отправили в личку боту а не в чате сената
    cur.execute('''SELECT chat_id,message_id,button,floor,room,typeofproblem from users''')
    rows = cur.fetchall()
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
            if (row[2] == 'что-то другое'):
                try:
                    s="этаж "+str(row[3])+'\n'
                    if not (row[4] is None):
                        s+=row[4]+'\n'
                    if not (row[5] is None):
                        s+=row[5]+'\n'
                    mes = str(message.chat.id) + "\n" + message.text
                    bot.send_message(-1001759376814, s+"поломка + ⬇️")
                    bot.send_message(-1001759376814, mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed2')

#тоже самое, но если кто-то отправил боту фото
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
                    print('MessageNotModifed1')
                break
            if (row[2] == 'что-то другое'):
                try:
                    s="этаж "+str(row[3])+'\n'
                    if not (row[4] is None):
                        s+=row[4]+'\n'
                    if not (row[5] is None):
                        s+=row[5]+'\n'
                    mes = str(message.chat.id) + "\n" + s + str(message.caption)
                    bot.send_photo(-1001759376814, message.photo[0].file_id, caption=mes)
                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
                except:
                    print('MessageNotModifed2')


#@bot.message_handler(content_types=['video'])
#def send_text(message):
#    cur.execute('''SELECT chat_id,message_id,button,floor,room,typeofproblem from users''')
#    rows = cur.fetchall()
#    for row in rows:
#        if (row[0] == message.chat.id):
#            if (row[2] == 'text'):
#                try:
#                    mes = str(message.chat.id) + "\n" + str(message.caption)
#                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
#                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
#                except:
#                    print('MessageNotModifed011')
#                break
#            if (row[3] == 1):
#                try:
#                    mes = str(message.chat.id) + "\n" + str(message.caption)
#                    bot.send_message(-1001759376814, "первый этаж, поломка + ⬇️")
#                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
#                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
#                except:
#                    print('MessageNotModifed022')
#            if (row[4] == 'text'):
#                try:
#                    mes = str(message.chat.id) + "\n" + str(message.caption)
#                    bot.send_message(-1001759376814, str(row[3]) + " этаж⬇️")
#                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
#                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
#                except:
#                    print('MessageNotModifed033')
#            if (row[5] == 'text'):
#                try:
#                    mes = str(message.chat.id) + "\n" + str(message.caption)
#                    bot.send_message(-1001759376814, str(row[3]) + " этаж\n" + str(row[4]) + "⬇️")
#                    bot.send_video(-1001759376814, message.video.file_id, caption=mes)
#                    bot.send_message(message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
#                except:
#                    print('MessageNotModifed044')




#обработка нажатий кнопок
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
        keyhandlers.MaintDep(call, bot)#Подразделы Хоз. Отдела
        keyhandlers.Claims(call, bot, cur, con)#Жалобы и предложения
        keyhandlers.DgapHelp(call, bot)#ВыручайФОПФ

        #Отдельная система кнопок для сообщений о поломках
        keyhandlers.Issues(call, bot, cur, con)
bot.infinity_polling(timeout=123)
