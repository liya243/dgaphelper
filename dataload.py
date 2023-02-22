#здесь описана функция для добавления в базу новых проблем

def problem(cur, con, floor, room, typeofproblem, numberofproblem):
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
        if numberofproblem!=NULL:
            s+='\nРаковина номер '+numberofproblem
        bot.send_message(-1001759376814,
            "Новая поломка в базе, этаж " + s, parse_mode="HTML", disable_web_page_preview=1, reply_markup=Fix_keyboard)
        cur.execute('''INSERT INTO problems (floor,room,typeofproblem,numberofproblem) 
            VALUES (%s, %s, %s,%s)''',
            [floor, room, typeofproblem, numberofproblem])
        con.commit()
