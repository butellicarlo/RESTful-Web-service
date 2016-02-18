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
Procedure to set up the environment:

1) Create a database to work with (the NationalNames.csv file has to be in the root folder):

- Open the terminal, go in the root folder then execute the following: 
```
$ sqlite3 names.db < schema.sql
$ sqlite3 names.db
sqlite>.mode csv
sqlite>.separator ','
sqlite>.import NationalNames.csv names
sqlite>.quit
```

2) Call the web service:

- In the root folder execute the following to start the web server:
```
$ python run.py
```

3) Retrieve information with curl:
- Total number of entries:
```
$ curl http://<Server_address>/entries
```
- Total entries from specific name:
```
$ curl --request GET http://<Server_address>/entry_name/<name>
```
- Insert a new baby:
```
$ curl --request POST http://<Server_address>/insert/<name>,<year>,<gender>,<count>
```
3.1) In version 2 of the web service, you can retrieve all the information by typing directly in the Web browser.
```
http://<Server_address>/<instruction>
```

4) Issues DB realted:

If you get the error `OperationalError: unable to open database file` when you run a `curl` command as client,
you have to make sure the directory containing the database file also has write access allowed to the process.
So, in the terminal, type:
```
$ sudo chmod 775 <root>/
$ sudo chmod 664 <root>/<name_db>.db
$ sudo chown -R <username> <root>/
```
This should solve that issue.