#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connects = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password, db=database)

    con_cursor = connects.cursor()

    con_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows = con_cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)
