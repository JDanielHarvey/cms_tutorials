"""
    Connect to SQL Server with Python
    https://www.youtube.com/watch?v=aF552bMEcO4
"""

import pyodbc
import datetime

# -- 'check the available drivers'
# for driver in pyodbc.drivers():
#     print(driver)

# -- 'connect to Fratmen'
# conn = pyodbc.connect(
#     '''
#     Driver={SQL Server Native Client 11.0};
#     Server=54.187.115.114;
#     Database=Fratmen;
#     UID=sqluser_FRATMEN;
#     PWD=8UUw7^gHHw3w3lxxx0o0;
#     '''
# )

# -- 'connect to AVP GCSQL'
conn_string = '''
    DRIVER={SQL Server Native Client 11.0};
    SERVER=34.94.213.153;Database=avp_marketing;
    UID=sqlserver;PWD=AvP2020!;
    '''

# -- an alternative option is to use 'list comprehension' to obtain tables from cur.tables()
read_query_tables = "select * from SYS.SYSOBJECTS where xtype = 'U' and [name] LIKE '%google%'"

# -- the table_name variable can't be used outside the with statement. query needs to be within the with statement
read_query_googreview = 'select * from [google_avg-review_cm] where [review_count] >= ? and [rating] > ?'

insert_query = "INSERT INTO python_test (month, rating, review_count, date_added) VALUES(?,?,?,?)"

# -- reads the tables in the database
with pyodbc.connect(conn_string) as conn:
    cur = conn.cursor()
    cur.execute(read_query_tables)
    table_name = cur.fetchall()[0][0]


    # print(table_name + '''
    # ''')

    # query2 = "execute sp_executesql N'select top 10 * from " + table_name + "'"
    # -- table name variables can not be used with tuple or dict as parameters


    cur.execute(read_query_googreview, (3000, 4.78))
    array = cur.fetchall()


    print(array)
    print('''
    ''')

    # for item in array:
    #     row = item
    #     # data = f"({row.call_id}, {row.start_datetime})"
    #     print(row)


with pyodbc.connect(conn_string) as conn:
    cur = conn.cursor()
    cur.executemany(insert_query, array)

    cur.execute("select * from [python_test]")
    goog_data = cur.fetchall()


for row in goog_data:
    print(row)


    # -- uses a list comprehension to obtain the columns
    # columns = [row.column_name for row in cur.columns(table='callcap_calls')]
    # print(columns)
    #
    # print('''
    # ''')
    #
    # tables = [row.table_name for row in cur.tables()]
    # print(tables)

    # def fetch_rows(tabes):
    #     cur.execute(query2, (' + tabes + ',))
    #     return cur.fetchall()

# print(fetch_rows(table_name))

# for row in cur:
#     desired_table = row[0]


# print(fetch_rows(desired_table))


# for row in cur:
#     print(row)

# print(cur.fetchall())


# rows = cur.fetchall()

# print(rows)





