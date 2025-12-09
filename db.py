import pymysql
from pymysql.cursors import DictCursor


def get_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pic",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

def query(sql, params=None):
    conn = get_conn()
    cursor = conn.cursor(DictCursor)  
    cursor.execute(sql, params or ()) 
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def execute(sql, params=None):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params or ())  
    conn.commit()
    cursor.close()
    conn.close()

def fetch_one(sql, params=None):
    conn = get_conn()
    cursor = conn.cursor(DictCursor)  
    cursor.execute(sql, params or ()) 
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

