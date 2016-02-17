# RESTful-Web-service
A simple Web service that can be queried by other parties by using curl.

Requirements for RESTful web service:
- python 2.5+
- sqlite3
```
pip install sqlite3
```
- pysqlite
```
pip install pysqlite
```
- flask
```
pip install Flask
```
Procedure to set up:

1) Create a database and import the csv file in it:

- Open the terminal, go to the "data" folder then execute the following: 
```
$ sqlite3 names.db < schema.sql
sqlite>.mode csv
sqlite>.separator ','
sqlite>.import NationalNames.csv names
```

2) Call the web service:

- Go in the "script" folder then execute:
```
$ python app.py
```
3) Retrieve information with curl:
- Total number of entries:
```
$ curl http://127.0.0.1:5000/entries
```
- Total entries from specific name:
```
$ curl --request GET http://127.0.0.1:5000/entry_name?name=Annie
```
- Insert a new entry:
```
$ curl --request POST http://127.0.0.1:5000/insert/Ronnie,1987,M,102
```
