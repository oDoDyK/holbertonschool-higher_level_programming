#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa sorted by id.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def list_all_states():
    """
    Lists all states from the database hbtn_0e_0_usa sorted by id.
    Usage: ./0-select_states.py <mysql username> <mysql password>
    <database name>
    """
    try:
        user1 = sys.argv[1]
        pass1 = sys.argv[2]
        db1 = sys.argv[3]
        database = None
        c = None
        database = MySQLdb.connect(
            port=3306, host="localhost", user=user1, passwd=pass1, db=db1
        )
        c = database.cursor()
        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' "\
                "ORDER BY states.id ASC"
        c.execute(query)
        [print(state) for state in c.fetchall()]
    except MySQLdb.Error as e:
        print(f"Error connecting to databse, {e}")
    finally:
        if c:
            c.close()
        if database:
            database.close()


if __name__ == "__main__":
    list_all_states()
