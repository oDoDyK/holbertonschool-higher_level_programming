#!/usr/bin/python3
"""
Script that takes arguments and displays all cities of a given state
from the database hbtn_0e_4_usa.
Results are sorted by cities.id and safe from SQL injection.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()
