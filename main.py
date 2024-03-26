import psycopg2 as pg2
import classified

conn = pg2.connect(database=classified.psql_database,
                   user=classified.psql_username, password=classified.psql_password)

cur = conn.cursor()

cur.execute(classified.psql_query)

print(cur.fetchone())

conn.close()
