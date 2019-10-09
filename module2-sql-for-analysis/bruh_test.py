import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from tabulate import tabulate

engine = create_engine('sqlite://',echo=False)
conn = sqlite3.connect('titanic.sqlite3')

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

titanic = sl_curs.execute('SELECT * from titanic;').fetchall()
# print(tabulate(titanic))
# print(len(titanic))
titanic_table = '''CREATE TABLE titanic (index SERIAL PRIMARY KEY, Survived INT,
pclass INT, name VARCHAR(30), sex VARCHAR,
age DECIMAL, siblings_spouses_aboar INT,
parents_children_aboard INT, fare DEC);'''

dbname = 'llrxvslu'
user = 'llrxvslu'
password = 'FTQhFlFrI07goJVPM4NrcEUg4T3LNRdt'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
pg_curs = pg_conn.cursor()

pg_curs.execute(titanic_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)

print(titanic[0])

for values in titanic:
    insert_titanic_values = '''
    INSERT INTO titanic
    ('Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
    'Parents/Children Aboard', 'Fare') VALUES ''' + str(titanic[1:]) + ';'
    pg_curs.execute(insert_titanic_values)
    # print(insert_titanic_values)

pg_curs.execute('SELECT * FROM titanic;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()
pg_curs = pg_conn.cursor()
