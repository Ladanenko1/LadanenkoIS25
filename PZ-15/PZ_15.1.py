# приложение контроль исполения
# поручения для некоторой организации бд
# дожна содеражать порядковый номер поручения название поручения
# дата выдачи поручения срок исполения исполнитель


import sqlite3 as sq
from info_por import info_all
with sq.connect('poruch.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS poruchenie")
    cur.execute("CREATE TABLE IF NOT EXISTS poruchenie("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "naz_por TEXT NOT NULL,"
                "data_por TEXT NOT NULL,"
                "srok_por TEXT NOT NULL,"
                "ispoln TEXT NOT NULL)")


    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO poruchenie  VALUES(?,?,?,?,?)", info_all)

    with sq.connect('poruch.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM  poruchenie WHERE ispoln LIKE 'П%'")
            result_1 = cur.fetchall()
            print(f"\n{result_1}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM poruchenie WHERE id%2==0 ")
        result_2 = cur.fetchall()
        print(f"\n{result_2}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("SELECT ispoln FROM poruchenie   ")
        result_3 = cur.fetchall()
        print(f"\n{result_3}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE poruchenie SET ispoln  = 'Мансуров Сашка' WHERE id == 2 ")
        cur.execute("SELECT * FROM poruchenie")
        result_4 = cur.fetchall()
        print(f"\n{result_4}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE poruchenie SET ispoln='Мансуров Сашка' WHERE id=7")
        cur.execute("SELECT * FROM poruchenie")
        result_5 = cur.fetchall()
        print(f"\n{result_5}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE poruchenie SET srok_por='2024-11-11' WHERE srok_por LIKE '2023%'")
        cur.execute("SELECT * FROM poruchenie")
        result_6 = cur.fetchall()
        print(f"\n{result_6}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM poruchenie WHERE srok_por =  '2%'")
        cur.execute("SELECT * FROM poruchenie")
        result_7 = cur.fetchall()
        print(f"\n{result_7}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM poruchenie WHERE id==3")
        cur.execute("SELECT * FROM poruchenie")
        result_8 = cur.fetchall()
        print(f"\n{result_8}")

    with sq.connect('poruch.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM poruchenie WHERE ispoln = 'Мансуров Сашка'")
        cur.execute("SELECT * FROM poruchenie")
        result_9 = cur.fetchall()
        print(f"\n{result_9}")
