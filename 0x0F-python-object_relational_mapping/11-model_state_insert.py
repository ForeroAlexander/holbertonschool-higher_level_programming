#!/usr/bin/python3
""" script that adds the State object
    “Louisiana” to the database hbtn_0e_6_usa """


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base
    from model_state import State

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(my_user, my_pass, my_db),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    st_add = State(name="Louisiana")
    session.add(st_add)
    print(session.query(State).filter_by(name="Louisiana").first().id)
    session.commit()

    session.close()
