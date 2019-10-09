import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from tabulate import tabulate

dset = pd.read_csv('titanic.csv')

engine = create_engine('sqlite://',echo=False)
conn = sqlite3.connect('titanic.sqlite3')
#dset.to_sql('titanic',conn)

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()
#sl_curs.execute('SELECT COUNT(*) From titanic').fetchall()




dbname = 'llrxvslu'
user = 'llrxvslu'
password = 'FTQhFlFrI07goJVPM4NrcEUg4T3LNRdt'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,host=host)


pg_curs = pg_conn.cursor()

titanic_table = '''CREATE TABLE titanic (index SERIAL PRIMARY KEY, Survived INT,
pclass INT, name VARCHAR(30), sex VARCHAR,
age DECIMAL, siblings_spouses_aboar INT,
parents_children_aboard INT, fare DEC);'''

pg_curs.execute(titanic_table)

show_table = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_table)

print(tabulate(pg_curs.fetchall()))

titanicc = sl_curs.execute('SELECT * from Survived;').fetchall()

for values in titanicc:
    insert_titantic = '''
    INSERT INTO titanic_table
    ('Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
    'Parents/Children Aboard', 'Fare') VALUES''' + str(values[0][1:]) + ';'
    pg_curs.execute(insert_titantic)
