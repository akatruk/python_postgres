import psycopg2
import sys

con = None

try:

    # con = psycopg2.connect(dbname=input('Введите имя базы данных: '),user=input('Введите имя пользователя: '), host=input('Введите имя\IP хоста: '))
    con = psycopg2.connect(dbname='postgres',user='akatruk', host='')

    cur = con.cursor()
    print('Соединение установленно!\n')
    print('Версия базы данных:')
    cur.execute('SELECT version()')
    # Audit OS:
    # checking basic parameters:

    version = cur.fetchall()
    print(version)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()
