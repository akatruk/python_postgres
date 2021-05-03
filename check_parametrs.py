import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = psycopg2.connect(dbname=input('Введите имя базы данных: '),user=input('Введите имя пользователя: '), host=input('Введите имя\IP хоста: '))

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = con.cursor()
print(cur.execute('SELECT version();'))

# cur.execute(sql.SQL("CREATE DATABASE {}").format(
#         sql.Identifier('python'))
#     )
con.close()


    cur.execute('''select name, setting::integer / 1024 val from pg_settings where name in 
('shared_buffers', 'effective_cache_size', 'work_mem' )
union all
select name, setting::integer val from pg_settings where name in 
('max_connections' );''')
