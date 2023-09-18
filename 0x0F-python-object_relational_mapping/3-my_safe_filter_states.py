#!/usr/bin/python3
"""
Once again, a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, one that is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    states_table = sys.argv[4]

    connects = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password, db=database)

    con_cursor = connects.cursor()

    con_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY \
                %(name)s ORDER BY states.id ASC", {'name': states_table})
    rows = con_cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)
