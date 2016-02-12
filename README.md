# RESTful-Web-service
web service that can be queried by other parties

Requirements for RESTful web service:
- python 2.5+
- sqlite3
- flask

Procedure to set up:

1) Create a database and import NationalNames.csv file in it:
sqlite3 names.db
sqlite>create table names(Id integer, Name text, Year integer, Gender text, Count integer)
sqlite>.mode csv
sqlite>.separator ','
sqlite>.import NationalNames.csv names

2) Call the web service (which has to be in the same directory of names.db just created):
$ python app.py

3) Retrieve information with curl:
$ curl http://127.0.0.1:5000/entries // to get the total numbero of entries


