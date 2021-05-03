import psycopg2
import sys

con = None
# def check_version():
def check_version(dbname,user,host):
    # con = psycopg2.connect(dbname=input('Введите имя базы данных: '),user=input('Введите имя пользователя: '), host=input('Введите имя\IP хоста: '))
    # con = psycopg2.connect(dbname='postgres',user='akatruk', host='')
try:
    con = psycopg2.connect(dbname=dbname, user=user, host=host)


    cur = con.cursor()
    print('Соединение установленно!\n')
    print('Версия базы данных:')
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    return version

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()
