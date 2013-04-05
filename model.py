from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

engine = create_engine("sqlite:///ratings.db", echo = False)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

def authenticate(email, password):
	print "0000000000000000000000000000000000000000000000"
	user_info = session.query(User).filter_by(email=email, password=password).one()
	print user_info.email, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
	print user_info.password, "BBBBBBBBBBBBBBBBBBBBBBBBBBB"

	return user_info.id


	# if result:
	# 	fields = ["id", "email", "password", "username"]
	# 	print "You've been authorized!"
	# 	return dict(zip(fields, result))
	# else:
	# 	return None

### Class declarations go here


class User(Base):
	# informs SQLAlchemy that instances of this class will be stored in table named users
	__tablename__ = "users"

	# tells SQLAlchemy to add column to table named "id" as primary key
	id = Column(Integer, primary_key = True)
	# nullable = True means that the information isn't required
	email = Column(String(64), nullable = True)
	password = Column(String(64), nullable = True)
	age = Column(Integer, nullable = True)
	gender = Column(String(15), nullable = True)
	occupation = Column(String(64), nullable = True)
	zipcode = Column(String(15), nullable = True)


class Movies(Base):
	__tablename__ = "movies"

	id = Column(Integer, primary_key = True)
	movie_id = Column(Integer)
	movie_title = Column(String(64))
	release_date = Column(Date)
	video_release_date = Column(Date, nullable = True)
	imdb_url = Column(String(128))

	# def __init__(self, age, zipcode, email = None, password = None):
	# 	self.email = email
	# 	self.password = password
	# 	self.age = age
	# 	self.zipcode = zipcode
	# 	# need gender and occupation here?

class Ratings(Base):
	__tablename__ = "ratings"

	id = Column(Integer, primary_key = True)
	# declaring it to be a ForeignKey = references another column in another table (the users.id column)
	user_id = Column(Integer, ForeignKey('users.id'))
	movie_id = Column(Integer, ForeignKey('movies.id'))# DOES NOT WORK Why?
	rating = Column(Integer)
	timestamp = Column(Date)


	user = relationship("User", backref=backref("ratings", order_by=id))
	movie = relationship("Movies", backref = backref("ratings", order_by = id))

	# def __init__(self, age, zipcode, email = None, password = None):
	# 	self.email = email
	# 	self.password = password
	# 	self.age = age
	# 	self.zipcode = zipcode
	# 	# need gender and occupation here?

### End class declarations


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
