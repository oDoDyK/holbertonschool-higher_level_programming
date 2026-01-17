#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Safe from SQL injections.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    querry = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(querry, (state_name,))
    result = cursor.fetchall()
    print(", ".join([row[0] for row in result]))
    cursor.close()
    db.close()
