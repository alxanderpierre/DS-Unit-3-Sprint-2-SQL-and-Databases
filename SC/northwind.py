import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


def most_expensive_items():
    most_expensive_query = (''' SELECT ProductName, UnitPrice
                                FROM Product
                                ORDER by UnitPrice DESC
                                LIMIT 10;''')
    curs.execute(most_expensive_query).fetchall()


def avg_hire_age():
    avg_hire_age_query = ('''SELECT BirthDate, HireDate,AVG(HireDate -BirthDate)
                             FROM Employee;''')
    curs.execute(avg_hire_age_query).fetchall()


def most_expensive_items_and_supplier():
    expensive_items_supplier_query = ('''SELECT ProductName, UnitPrice, SupplierId
                                                  FROM Product
                                                  order by UnitPrice DESC
                                                  LIMIT 10;''')
    curs.execute(expensive_items_supplier_query).fetchall()


def largest_category():
    largest_category_query = ('''SELECT DISTINCT(ProductName), (CategoryId)
                                 FROM Product
                                 GROUP BY ProductName
                                 ORDER BY CategoryId DESC;''')
    curs.execute(largest_category_query).fetchall()


# In the Northwind database, what is the type of relationship between the
# `Employee` and `Territory` tables?

# ANSWER: Mnay Employees can be assigned to only one Territory.
# One - To - Many.


# What is a situation where a document store (like MongoDB) is appropriate, and
# what is a situation where it is not appropriate?

# ANSWERS:
# Appropriate: in the case of having a start up and you are looking for High
# scalability with this there is no rigid schema so if you are looking for
# funding its a good choice if you are looking to move FAST!
# Not Appropriate: When you are trying to build the logic of your database.
# there are no functions or stored procedure. So, in our example once start up
# is funded it wise to switch over to a sql db. (elephant)


# What is "NewSQL", and what is it trying to achieve

# ANSWER: New sql is trying to achieve the pros of both Nosql and sql.
# It wants to combine transactional ACID, and the horizontal scalability of Nosql.
