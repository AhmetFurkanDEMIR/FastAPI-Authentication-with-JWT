import psycopg2

def db():

    conn = psycopg2.connect(
        host="db-postgres",
        database="postgres",
        port="5432",
        user="postgres",
        password="123456789Zz.")

    cursor = conn.cursor()

    return cursor, conn