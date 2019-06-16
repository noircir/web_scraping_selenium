import sqlite3


def create_table(db):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    cmd = '''CREATE table if not exists PROXY(
    id INTEGER primary key autoincrement,
    ip TEXT,
    port TEXT,
    location TEXT,
    speed TEXT,
    type TEXT,
    anonymity TEXT,
    last TEXT
    )'''
    cursor.execute(cmd)
    db.close()


def insert_into_table(db, proxy_list):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    cmd = '''INSERT into PROXY(ip, port, location, speed, type, anonymity, last) values(?, ?, ?, ?, ?, ?, ?)'''
    for row in proxy_list:
        cursor.execute(cmd, (row.ip, row.port, row.location, row.speed, row.type_, row.anonymity, row.last))
    db.commit()
    db.close()


def select_table(db, request):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    cursor.execute(request)
    print("=" * 50)
    db.close()
#
#
# def research_employee_by_age(db, request, age):
#     db = sqlite3.connect(db)
#     cursor = db.cursor()
#     cursor.execute(request, (age,))
#     print("=" * 50)
#     for row in cursor:
#         print("{}, {}, {}, {}".format(row[0], row[1], row[2], row[3]))
#     db.close()