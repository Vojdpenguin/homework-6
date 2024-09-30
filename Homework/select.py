import sqlite3


def execute_sql_file(filename):
    with sqlite3.connect('univ.db') as con:
        cur = con.cursor()
        with open(filename, 'r') as f:
            sql_script = f.read()
        cur.execute(sql_script)
        results = cur.fetchall()
        print(results)

execute_sql_file('query_1.sql')
execute_sql_file('query_2.sql')
execute_sql_file('query_3.sql')
execute_sql_file('query_4.sql')
execute_sql_file('query_5.sql')
execute_sql_file('query_6.sql')
execute_sql_file('query_7.sql')
execute_sql_file('query_8.sql')
execute_sql_file('query_9.sql')
execute_sql_file('query_10.sql')