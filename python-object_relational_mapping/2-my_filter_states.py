#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa filtered by name.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
import MySQLdb


def list_all_states():
    if len(sys.argv) != 5:
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    match = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=database_name,
        port=3306
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC"
    ).format(match)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_all_states()
