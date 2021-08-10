#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa """


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base
    from model_state import State
    from model_city import City

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(my_user, my_pass, my_db),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    results = session.query(City, State).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    for inst_c, inst_s in results:
        print("{}: ({}) {}".format(inst_s.name, inst_c.id, inst_c.name))

    session.close()
