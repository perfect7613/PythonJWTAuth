from Database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)

#class POI(Base):
 #   __tablename__ = 'POI'

  #  name = Column(String, unique=True)
  #  pointgeom = Column()



