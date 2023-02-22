#здесь описана функция для добавления в базу новых проблем

def problem(bot, cur, con, floor, room, typeofproblem, numberofproblem):
    #Сначала проверяем что такой проблемы в базе ещё нет
    cur.execute('''SELECT * from problems 
        WHERE floor=(%s),
        room=(%s),
        typeofproblem=(%s),
        numberofproblem=(%s)
        ''',
        [floor, room, typeofproblem, numberofproblem])
    #Если нет то сообщаем в чат сената и добавляем в базу
    if not cur.fetchall():
        s=str(floor)+'\n'+room+'\n'+typeofproblem
        if numberofproblem in [1,2,3,4,5,6]:
            s+='\nРаковина номер '+numberofproblem
        if numberofproblem==0:
            s+='\nЛень уточнять раковину'
        bot.send_message(-1001759376814,
            "Новая поломка в базе, этаж " + s, parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) 
            VALUES (%s, %s, %s,%s)''',
            [floor, room, typeofproblem, numberofproblem])
        con.commit()

def deletequery(bot, call):
    #после получения жалобы сообщение возвращается к изначальному меню
    try:
        bot.edit_message_text(chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=open('texts/Начало.txt','r').read(),
            reply_markup=Greet_keyboard)
        bot.send_message(call.message.chat.id, 'Сенат получил твоё сообщение. Спасибо!')
        cur.execute('''DELETE from users 
            WHERE chat_id=(%s) AND 
            message_id=(%s)''',
            [call.message.chat.id, call.message.message_id])
        con.commit()
    except:
        print('MessageNotModifed8')


