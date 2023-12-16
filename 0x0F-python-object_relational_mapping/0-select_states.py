#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def list_states(username, password, database):
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
if __name__ == '__main__':
    username=sys.argv[1]
    password=sys.argv[2]
    database=sys.argv[3]

    list_states(username, password, database)
