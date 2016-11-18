import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = None

#databse creation commented out once the database is created.
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "pass", host = "localhost", port = "5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()
cur.execute('DROP DATABASE tcount')
conn.commit()

cur = conn.cursor()
cur.execute('CREATE DATABASE tcount')
conn.commit()

conn.close()

conn2 = psycopg2.connect(database = "tcount", user = "postgres", password = "pass", host = "localhost", port = "5432")

cur2 = conn2.cursor()
#cur2.execute("CREATE TABLE tweetwordcount (word TEXT NOT NULL, count INT NOT NULL);")

cur2.execute('''CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);''')

conn2.commit()
conn2.close()
