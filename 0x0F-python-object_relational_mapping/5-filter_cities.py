#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

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

    con_cursor.execute("SELECT cities.id, cities.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id WHERE state.name = %s ORDER BY \
                                cities.id ASC", {'state_name': states_table})
    rows = con_cursor.fetchall()

    # Print the results
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
