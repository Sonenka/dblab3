import sqlite3
import duckdb
import psycopg2
import pandas as pd
import time
from config import libraries

file_name = 'tiny.csv'

queries1 = [
    "SELECT VendorID, count(*) FROM taxi GROUP BY 1",
    "SELECT passenger_count, avg(total_amount) FROM taxi GROUP BY 1",
    "SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM taxi GROUP BY 1, 2",
    "SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 desc"
]

queries2 = [
    """SELECT "VendorID", count(*) FROM "taxi" GROUP BY 1""",
    """SELECT "passenger_count", avg("total_amount") FROM "taxi" GROUP BY 1""",
    """SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM "taxi" GROUP BY 1, 2""",
    """SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM "taxi" GROUP BY 1, 2, 3 ORDER BY 2, 4 desc"""
    ]

def make_db_file():
    df = pd.read_csv(file_name)
    if 'Airport_fee' in df.columns:
        df = df.drop(columns=['Airport_fee'])
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    return df

def make_conn():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    return conn    
    
def test_psycopg(conn):
    cursor = conn.cursor()
    result(1, cursor)
    conn.close()

def test_sqlite(df):
    db_file = 'database.db'
    conn = sqlite3.connect(db_file)
    df.to_sql('taxi', conn, if_exists='replace', index=False)
    cursor = conn.cursor()
    result(2, cursor)
    conn.commit()

def test_duckdb(df):
    conn = duckdb.connect(database=':memory:', read_only = False)
    conn.register('taxi', df)
    result(3, conn)
    conn.close()

def test_pandas(df):
    db_file = 'database.db'
    conn = sqlite3.connect(db_file)
    result(4, conn)
    conn.close()

def result(lib, x):
    if lib == 1:
        print('psycopg2: ', end = "")
        for i in range(4):
            print('%.3f' % time_measure(lib, x, queries2[i]), end = " ")
        print()
    if lib == 2:
        print('SQLite3: ', end = "")
        for i in range(4):
            print('%.3f' % time_measure(lib, x, queries1[i]), end = " ")
        print()
    if lib == 3:
        print('DuckDB: ', end = "")
        for i in range(4):
            print('%.3f' % time_measure(lib, x, queries1[i]), end = " ")
        print()
    if lib == 4:
        print('Pandas: ', end = "")
        for i in range(4):
            print('%.3f' % time_measure(lib, x, queries1[i]), end = " ")
        print()
    
    

def time_measure(lib, x, query):
    start_time = time.time()
    for _ in range(10):
        if lib in [1, 2, 3]:
            x.execute(query)
        elif lib == 4:
            result_df = pd.read_sql_query(query, x)

    return (time.time()-start_time)/10
    
def main():
    flag = 0
    print("Library query1 query2 query3 query4")

    for lib in libraries:
        if not libraries[lib]: continue

        if lib in [2, 3, 4] and flag == 0:
            df = make_db_file()
            flag = 1
        else:
            conn = make_conn()

        if lib == 1: test_psycopg(conn)
        elif lib == 2: test_sqlite(df)
        elif lib == 3: test_duckdb(df)
        elif lib == 4: test_pandas(df)         

if __name__ == "__main__":
    main()



