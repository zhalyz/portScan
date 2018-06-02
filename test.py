from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///test.db")
meta = MetaData(bind=engine, reflect=True)
class Schedule(object):
    def __init__(self,groupName,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday):
        self.groupName = groupName
        self.Monday = Monday
        self.Tuesday = Tuesday
        self.Wednesday = Wednesday
        self.Thursday = Thursday
        self.Friday = Friday
        self.Saturday = Saturday
        self.Sunday = Sunday
    def __repr__(self):
        return "<Schedule('%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.groupName,self.Monday,
        self.Tuesday,self.Wednesday,self.Thursday,self.Friday,self.Saturday,self.Sunday)

class Users(object):
    def __init__(self,user_id,username,groupName):
        self.user_id = user_id
        self.username = username
        self.groupName = groupName
    def __repr__(self):
        return "<user('%s','%s','%s')>" % (self.user_id,self.username,self.groupName)

print(mapper(Schedule, meta.tables['schedule']))
print(mapper(Users,meta.tables['user']))


