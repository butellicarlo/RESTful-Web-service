from flask import Flask, url_for, request, json
from flask.json import jsonify
import sqlite3

#Configuration
app = Flask(__name__)

# Create db and open connection to it
conn = sqlite3.connect('../data/names.db', check_same_thread=False)
c = conn.cursor()

#View
@app.route('/')
def api_root():
	return '{}\n'.format('Welcome')

# $curl --request GET http://127.0.0.1:5000/entries
@app.route('/entries', methods = ['GET'])
def api_entries():
	query = c.execute("SELECT count(*) FROM names;")
	conn.commit()
	entries = query.fetchone()
	return '{}\n'.format('{}\n'.format(entries)[1:-3])
	
# $curl --request GET http://127.0.0.1:5000/entry_name?name=Annie
@app.route('/entry_name', methods = ['GET'])
def api_entry_name():
	query = c.execute("SELECT year, gender, count FROM names WHERE name = '%s';" % request.args['name'])
	conn.commit()
	data = query.fetchall()
	return jsonify({'Entries for %s' % request.args['name']: data})


@app.route('/insert', methods = ['POST'])
def api_insert():
	query = c.execute('insert into names (name, year, gender, count) values ( "%s", %d, "%s", %d );' % (request.args['name'], request.args['year'], request.args['gender'], request.args['count']))
	return "{}, {}, {}, {} inserted.\n".format(request.args['name'], request.args['year'], request.args['gender'], request.args['count'])
	
#End view

if __name__ == '__main__':
	#Run the Server
	app.run(debug=True)
