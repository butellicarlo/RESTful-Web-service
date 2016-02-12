from flask import Flask, url_for, request
import sqlite3

app = Flask(__name__)

# Create db and open connection to it
conn = sqlite3.connect('names.db')
cursor = conn.cursor()

@app.route('/')
def api_root():
    return '{}\n'.format('Welcome')

@app.route('/entries')
def api_entries():
    query = cursor.execute("SELECT count(*) FROM names;")
    entries = query.fetchone()
    return '{}\n'.format('{}\n'.format(entries)[1:-3])

@app.route('/entry-name')
def api_entry_name():
	if 'name' in request.args:
		query = cursor.execute("select * from names where Name = '" + request.args['name'] + "';")
		entries = query.fetchall()
		return entries
	else:
		return 'No entries with this name'

"""
@app.route('/add/<string:name>')
def api_add(name):
    return '{}\n'.format('You are adding ' + name)
"""

if __name__ == '__main__':
     app.run()
