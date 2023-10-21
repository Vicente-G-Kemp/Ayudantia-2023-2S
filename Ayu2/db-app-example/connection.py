from psycopg2 import connect

def init_db():
    conn = connect(
        dbname='proyecto',
        user='postgres',
        password='postgres',
        host='postgres',
    )
    return conn