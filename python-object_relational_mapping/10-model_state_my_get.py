#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name, state_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
    )
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True,
    )
    session = Session(engine)
    state_id = (
        session.query(State).filter_by(name=f"{state_name}")
        .order_by(State.id).all()
    )
    if state_id:
        for state in state_id:
            print(f"{state.id}")
    else:
        print("Not found")
    session.close()
