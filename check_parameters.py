import psycopg2
import sys
f1 = 'scrips/get_main_parameters.sql'

def read_file(text):
    with open(f1, 'r') as f2:
        return f2.read()

con = None

try:

    con = psycopg2.connect(dbname='postgres',user='akatruk', host='')

    cur = con.cursor()
    print('\n\rMain PostgreSQL parameters:')
    cur.execute(read_file(f1))

    version = cur.fetchall()
    for p1 in version:
        print(p1)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()