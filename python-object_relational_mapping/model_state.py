#!/usr/bin/python3
"""
Script that takes arguments and displays all cities of a given state
from the database hbtn_0e_4_usa.
Results are sorted by cities.id using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db_name}')

    # Bind session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities for the given state
    result = session.query(City).join(State).filter(State.name == state_name)\
        .order_by(City.id).all()

    print(", ".join([city.name for city in result]))

    session.close()
