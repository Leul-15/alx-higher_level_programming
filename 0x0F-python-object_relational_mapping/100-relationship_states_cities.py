#!/usr/bin/python3
"""adds the State object “California”
with the City “San Francisco”
"""

if __name__ == "__main__":

    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
