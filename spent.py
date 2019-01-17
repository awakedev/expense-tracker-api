import sqlite3 as db


def init():
    con = db.connect("spent.db")
    cursor = con.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
    )
    '''
    cursor.execute(sql)
    con.commit()


def log(amount, category, message=""):
    from datetime import datetime
    date = str(datetime.now())
    con = db.connect("spent.db")
    cursor = con.cursor()
    sql = '''
    insert into expenses values (
         {},
        '{}',
        '{}',
        '{}'
        )
    '''.format(amount, category, message, date)
    cursor.execute(sql)
    con.commit()


def view(category=None):
    con = db.connect("spent.db")
    cursor = con.cursor()
    if category:
        sql = '''
        select * from expenses where category = '{}'
        '''.format(category)
        sql2 = '''
             select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''.format(category)
    cursor.execute(sql)
    results = cursor.fetchall()
    #total_amount = cursor.fetchone()[0]

    return results

#log(120, "Theatre", "Hello")



print (view())