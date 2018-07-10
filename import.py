import csv
import os
import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from uuid import uuid4

#connect to Database
db_string = "postgres://rfiyeehknxkzti:fcd541969aee3f6c579001a4769f90bb3d27c6e5194c31478217c5010e016a22@ec2-54-227-243-210.compute-1.amazonaws.com:5432/d4dhnjm6dcg7mm"
os.environ["DATABASE_URL"] = db_string


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#Pull CSV into Context
zipListFile = open("zips.csv")
reader = csv.reader(zipListFile)
for ZipCode, City, State, Lat, Long, Population in reader:
    db.execute('INSERT INTO location (locationid, zipcode, city, state, latitude, longitude) VALUES ( :locationid, :Zipcode, :City, :State, :Latitude, :Longitude)',
                  {"locationid": uuid4(), "Zipcode": ZipCode, "City" : City, "State": State, "Latitude": Lat, "Longitude": Long })
