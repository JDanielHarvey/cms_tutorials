"""
    Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries
    https://www.youtube.com/watch?v=pd-0G0MigUA&t=37s
"""

import sqlite3

# conn_mem = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#         first_name text,
#         last_name text,
#         pay integer
#         )""")

# c.execute("INSERT INTO employees VALUES ('Diane', 'McCabe', 50000)")

# employees = [('Rebecca', 'Winter', 70000),('John', 'Marsh', 1000000)]


# def insert_employees(first, last, pay):
#     with conn:
#         c.execute("""INSERT INTO employees
#                     VALUES (:first, :last, :pay)""", {'first': first, 'last': last, 'pay': pay})
#
#
# for index, emp in enumerate(employees):
#     # int_ind = int(index)
#     fn = employees[index][0]
#     ln = employees[index][1]
#     py = employees[index][2]
#
#     insert_employees(fn, ln, py)


# conn.commit()

# c.execute("SELECT * FROM employees WHERE last_name = ?", ('McCabe',))

# c.execute("SELECT * FROM employees WHERE last_name = :first", {'first': 'McCabe'})

# c.execute("DELETE FROM employees WHERE last_name = 'McCabe'")

c.execute("SELECT * FROM employees")

rng = len(c.fetchall())
payload = c.fetchall()

print(payload)
print(rng)

# for i in range(rng):
#     print(payload)

c.execute("SELECT * FROM employees WHERE last_name LIKE :last", {'last': '%Mc%'})


# employees_last = ['Harvey', 'McCabe']
#
def select_employees(lastname):
    c.execute("SELECT * FROM employees WHERE last_name LIKE :last", {'last': lastname})
    return c.fetchall()

# c.fetchone()
# c.fetchmany()


# for employee in employees_last:
#     print(select_employees(employee))


conn.commit()

conn.close()
