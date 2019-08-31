import sqlite3
from sqlite3 import Error
from flask import jsonify
import json

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #cur.execute("INSERT INTO customers (name, address) VALUES ('karlo', 'skok')")
    cur.execute("SELECT * FROM Trosak")


    rows = cur.fetchall()
    #print(rows)

    # convert into JSON:
    y = json.dumps(rows)

    # the result is a JSON string:
    print(y)

   # p = json.dumps(rows)
    #p = jsonify({'data': rows})

    #print (p)

    return y

def main():
    database = 'C:\\Users\\MS Studio\\WebstormProjects\\untitled1\\db.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        #print("1. Query all tasks")
        select_all_tasks(conn)



if __name__ == '__main__':
    main()