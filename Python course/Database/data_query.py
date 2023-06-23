import psycopg2

conn = psycopg2.connect(
    database="wa_monitoring_dev",
    host="193.178.170.145",
    user="wa_admin",
    password="$wa$m4n0t1r9ng$",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("select * from wa_users")

# print(cursor.fetchone())
# print(cursor.fetchall())
print(cursor.fetchmany(size=10), sep='\n')