from test import engine
from test import Schedule
from test import Users
from sqlalchemy.orm import sessionmaker

def find(groupName,days):
    Session = sessionmaker(bind=engine)
    session = Session()
    for day in days:
        print('help')
    session.close()
    return

def add(list):
    Session = sessionmaker(bind=engine)
    session = Session()
    losser = Users(list[0],list[1],list[2])
    session.add(losser)
    session.commit()
    session.close()
    return

def check():
    Session = sessionmaker(bind=engine)
    session = Session()
    for user in session.query(Users):
        temp = user.user_id
    session.close()
    return temp
