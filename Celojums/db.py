import psycopg2
import psycopg2.extras

# need to connect with DB
# create 2.nd table

DB_HOST='abul.db.elephantsql.com'
DB_NAME='etieprry'
DB_USER='etieprry'
DB_PASS='d2WSx5J6dKXsbH-IfPAwnKbIudUSvps_'


conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


cur.execute('DROP TABLE bumba')
cur.execute('CREATE TABLE bumba(id SERIAL PRIMARY KEY,name VARCHAR(100))')
cur.execute('INSERT INTO  bumba (name) VALUES (%s)',('Kārlis',))
cur.execute('INSERT INTO  bumba (name) VALUES (%s)',('Jānis',))
cur.execute('SELECT * FROM bumba')
print(cur.fetchall())

with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute('SELECT FROM bumba WHERE id=%s',(1,))
        cur.execute('SELECT FROM bumba;')
        print(cur.fetchall())
        print(cur.fetchone()['name'])

conn.commit()
cur.close()
conn.close()