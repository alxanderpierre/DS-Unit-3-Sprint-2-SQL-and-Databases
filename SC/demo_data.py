import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
conn
curs = conn.cursor()
query = 'CREATE TABLE demo (s varchar(30), x int, y int);'
insert_query = 'INSERT INTO demo (s,x,y) VALUES ("g",3,9);'
insert_query2 = 'INSERT INTO demo (s,x,y) VALUES ("v",5,7);'
insert_query3 = 'INSERT INTO demo (s,x,y) VALUES ("f",8,7);'
curs.execute(query)
curs.execute(insert_query)
curs.execute(insert_query2)
curs.execute(insert_query3)
curs.close()
conn.commit()


def row_count():
    row_count_query = ('''SELECT count(*)
                         from demo;''')
    curs.execute(row_count_query).fetchall()


def row_count_at_five():
    row_count_at_least_five_query = (''' SELECT count(x and y) from demo
                                        where demo.x AND demo.y >=5;''')
    curs.execute(row_count_at_least_five_query).fetchall()


def unique_y_values():
    unique_y_values_query = (''' SELECT count(DISTINCT(y))
                                 from demo:''')
    curs.execute(unique_y_values_query).fetchall()
