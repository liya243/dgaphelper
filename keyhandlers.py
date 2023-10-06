#Здесь происходит принятие сигнала от бота и проверка, какая кнопка была нажата и куда эта кнопка ведёт
#----------------------------------------------------------------------------------------
from keyboards import *
from dataload import *


#Начальное меню
def Beginning(call, bot, cur, con):
    if call.data == "begin":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=open('/home/user/infodept/texts/Начало.txt','r').read(),
                reply_markup=Greet_keyboard)
            cur.execute('''DELETE from users 
                WHERE chat_id=(%s) 
                AND   message_id=(%s)''', 
                [call.message.chat.id, call.message.message_id])
            con.commit()
        except:
            print('MessageNotModifed8')
#----------------------------------------------------------------------------------------


#Матпомощь
def CashAid(call, bot):
    #Начало --> Матпомощь
    if call.data == "CA":
        #try:
        bot.edit_message_text(chat_id=call.message.chat.id, 
            message_id=call.message.message_id, 
            text=open('/home/user/infodept/texts/Матпомощь/Матпомощь.txt','r').read(),         
            parse_mode="HTML", 
            reply_markup=Aid_keyboard)
        #except:
            #print('MessageNotModifed9')
#------------------------------------------------------------------------------------------------------


#Сенат
def Senat(call, bot):
    #Начало --> Сенат
    if call.data == "Se":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('/home/user/infodept/texts/Сенат/Сенат.txt','r').read(),   
                disable_web_page_preview=1, 
                parse_mode='HTML', 
                reply_markup=Senat_keyboard)
        except:
            print('MessageNotModifed15')
#------------------------------------------------------------------------------------------------------


#Хозотдел
def MaintDep(call, bot):
    #Начало --> Хозотдел
    if call.data == "MD":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text=open('/home/user/infodept/texts/Хозотдел/Хозотдел.txt','r').read(),
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=MaintDep_keyboard)
        except:
            print('MessageNotModifed49')
#------------------------------------------------------------------------------------------------------


#Жалобы и предложения
def Claims(call, bot, cur, con):
    if call.data == "ClB":
            try:
                bot.edit_message_text(chat_id=call.message.chat.id, 
                    message_id=call.message.message_id,
                    text=open('/home/user/infodept/texts/ЖалобыИПредложения.txt','r').read(), 
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


#ВыручайФОПФ
def DgapHelp(call, bot):
    #Начало --> ВыручайФОПФ
    if call.data == "DGhB":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                text=open('/home/user/infodept/texts/ВыручайФОПФ/ВыручайФОПФ.txt','r').read(),         
                parse_mode="HTML", 
                reply_markup=DgapHelp_keyboard)
        except:
            print('MessageNotModifed666')
#----------------------------------------------------------------------------------------


#Кнопка починки в чате сената
def Fix(call, bot, cur, con):
    if call.data == "FiB":
        Floor = call.message.text.split('\n')[0][-1]
        Room = call.message.text.split('\n')[1]
        TypeOfProblem = call.message.text.split('\n')[2]
        #проверка, 3 или 4 строки в жалобе (на случай если указан ещё и номер раковины)
        if len(call.message.text.split('\n')) == 3:
            cur.execute('''DELETE from problems 
                WHERE floor=(%s) AND 
                room=(%s) AND 
                typeofproblem=(%s)''',
                [int(Floor),Room,TypeOfProblem])
        else:
            NumberOfSink=call.message.text.split('\n')[3][len(call.message.text.split('\n')[3]) - 1]
            #Если было указано что лень искать раковин(у)
            if NumberOfSink=='у':
                #в таком случае в базе они указаны под номером 0
                NumberOfSink='0'
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
        #try:
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
        #except:
        #    print('MessageNotModifed59')
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
            con.commit()
        except:
            print('MessageNotModifed62')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж
    if call.data in ["2F","3F","4F","5F"]:
        #try:
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
        cur.execute('''UPDATE users SET room=(%s) 
            WHERE chat_id=(%s) AND 
            message_id=(%s)''',
            [None, call.message.chat.id, call.message.message_id])
        con.commit()
        #except:
        #    print('MessageNotModifed63')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5 этаж <-- Назад
    if call.data == "Bb9":
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, 
                message_id=call.message.message_id,
                text="Где произошла проблема?", 
                parse_mode="HTML", 
                disable_web_page_preview=1, 
                reply_markup=Rooms_keyboard)
            cur.execute('''UPDATE users SET room=(%s) 
                WHERE chat_id=(%s) 
                AND message_id=(%s)''',
                [None, call.message.chat.id, call.message.message_id])
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
                case "WaB":
                    cur.execute('''UPDATE users SET room='умывальник'
                        WHERE chat_id=(%s) AND
                        message_id=(%s)''',
                        [call.message.chat.id, call.message.message_id])
                    con.commit()
        except:
            print('MessageNotModifed67')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж --> Кухня/Умывальник --> Неполадки с краном
    if call.data in ["TaB","TaB2","PiB"]:
        #смотрим, какой этаж и комнату до этого выбрал пользователь (кран есть и на кухне и в умывалке)
        cur.execute('''SELECT floor,room from users 
            WHERE chat_id=(%s) AND 
            message_id=(%s)''',
            [call.message.chat.id, call.message.message_id])
        rows = cur.fetchall()
        match rows[0][1]:
            #если кран сломался на кухне, то сразу добавляем в базу поломку на кухне
            case "кухня":
                match call.data:
                    case "TaB":
                        problem(bot,cur,con,rows[0][0],'кухня','Кран подтекает/не закрывается',None)
                    case "TaB2":
                        problem(bot,cur,con,rows[0][0],'кухня','Кран гудит',None)
                    case "PiB":
                        problem(bot,cur,con,rows[0][0],'кухня','Труба под раковиной подтекает',None)
                deletequery(bot, call,cur,con)
            #если кран сломался в умывалке, то спрашиваем какой именно кран и записываем в базу какую конкретно поломку крана выбрал пользователь
            case "умывальник":
                try:
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id,
                        text="Какой номер у этой раковины/крана?", 
                        parse_mode="HTML", 
                        disable_web_page_preview=1,
                        reply_markup=Sink_keyboard)
                    match call.data:
                        case "TaB":
                            cur.execute('''UPDATE users SET typeofproblem='Кран подтекает/не закрывается' where chat_id=(%s) AND message_id=(%s)''',
                                [call.message.chat.id, call.message.message_id])
                        case "TaB2":
                            cur.execute('''UPDATE users SET typeofproblem='Кран гудит' where chat_id=(%s) AND message_id=(%s)''',
                                [call.message.chat.id, call.message.message_id])
                        case "PiB":
                            cur.execute('''UPDATE users SET typeofproblem='Труба под раковиной подтекает' where chat_id=(%s) AND message_id=(%s)''',
                                [call.message.chat.id, call.message.message_id])
                    con.commit()
                except:
                    print('MessageNotModifed688')
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж --> Умывальник --> Неполадки с краном --> Выбран 1,2,3,4,5,6ой/лень искать какой кран
    if call.data in ["SiB1","SiB2","SiB3","SiB4","SiB5","SiB6","LaB"]:
        #смотрим, какой этаж и вид поломки до этого выбрал пользователь
        cur.execute('''SELECT floor,typeofproblem from users
            WHERE chat_id=(%s) AND
            message_id=(%s)''',
            [call.message.chat.id, call.message.message_id])
        rows = cur.fetchall()
        #смотрим указано ли какая раковина или человеку лень
        if call.data!="LaB":
            problem(bot,cur,con,rows[0][0],'умывальник',rows[0][1],int(call.data[3]))
        else:
            problem(bot,cur,con,rows[0][0],'умывальник',rows[0][1],0)
        deletequery(bot, call,cur,con)
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж --> Кухня/Умывальник --> Закончилось мыло
    if call.data=="SoB":
        #смотрим, какой этаж и комнату до этого выбрал пользователь (мыло есть и на кухне и в умывалке)
        cur.execute('''SELECT floor,room from users 
            WHERE chat_id=(%s) AND 
            message_id=(%s)''',
            [call.message.chat.id, call.message.message_id])
        rows = cur.fetchall()
        problem(bot,cur,con,rows[0][0],rows[0][1],'Закончилось мыло',None)
        deletequery(bot, call,cur,con)    
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
    #6-ка: поломки, мыло, бумага --> Выбран 2,3,4,5ый этаж --> Туалет --> Засорился писсуар/Кончилась бумага
    if call.data in ["UrB","PaB"]:
        #try:
        #смотрим, какой этаж до этого выбрал пользователь
        cur.execute('''SELECT floor from users 
            WHERE chat_id=(%s) AND 
            message_id=(%s)''',
            [call.message.chat.id, call.message.message_id])
        rows = cur.fetchall()
        floor=rows[0][0]
        match call.data:
            case "UrB":
                problem(bot,cur,con,rows[0][0],'туалет','Засорился писсуар',None)
            case "PaB":
                problem(bot,cur,con,floor,'туалет','Кончилась бумага',None)
        deletequery(bot, call, cur, con) 
        #except:
          #  print('MessageNotModifed168')
    if call.data=="AnB":
        #try:
        #смотрим, какой этаж до этого выбрал пользователь
        cur.execute('''UPDATE users set button=(%s) ''',['что-то другое'])
        con.commit()
        bot.edit_message_text(chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Что случилось?",
            parse_mode="HTML",
            disable_web_page_preview=1,
            reply_markup=Back_to_Greet_keyboard)
        #except:
         #   print('MessageNotModifed168')
