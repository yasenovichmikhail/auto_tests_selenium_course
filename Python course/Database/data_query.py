from sqlite3 import OperationalError
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    database="wa_monitoring_dev",
    host="193.178.170.145",
    user="wa_admin",
    password="$wa$m4n0t1r9ng$",
    port="5432"
)

# cursor = conn.cursor()

# cursor.execute("select user_id, login_token from wa_users")

# print(cursor.fetchone())
# print(cursor.fetchall())
# print(*cursor.fetchmany(size=10), end='\n')

# pd.read_sql("select user_id, login_token from wa_users", cursor)


def execute_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchmany(size=10)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT user_id, login_token FROM wa_users"

users = execute_query(conn, select_users)

print(len(users))

