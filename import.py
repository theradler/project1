import csv
import os
from uuid import uuid4
import psycopg2
from psycopg2 import extras

#connect to Database
db_string = "postgres://rfiyeehknxkzti:fcd541969aee3f6c579001a4769f90bb3d27c6e5194c31478217c5010e016a22@ec2-54-227-243-210.compute-1.amazonaws.com:5432/d4dhnjm6dcg7mm"
os.environ["DATABASE_URL"] = db_string

conn = psycopg2.connect(db_string)
cur = conn.cursor()

#Pull CSV into Context
zipListFile = open("zips.csv")
reader = csv.reader(zipListFile)
firstline = True
for ZipCode, City, State, Lat, Long, Population in reader:
    if firstline:
        firstline = False
        continue
    GUID = uuid4()
    psycopg2.extras.register_uuid()
    Lat = float(Lat)
    Long = float(Long)
    cur.execute("INSERT INTO location VALUES (%s, %s, %s, %s, %s, %s, %s)", ( GUID, ZipCode, City, State, Lat, Long, Population ))
    conn.commit()