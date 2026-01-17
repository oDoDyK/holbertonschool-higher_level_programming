
#!/usr/bin/python3
"""
Module 100-relationship_states_cities.py
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # create state "California" with city attribute "San Francisco"
    new_st = State(name="California")
    new_cy = City(name="San Francisco")
    new_st.cities.append(new_cy)

    session.add(new_st)
    session.add(new_cy)

    session.commit()
    session.close()
