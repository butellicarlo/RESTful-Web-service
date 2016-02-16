from flask import Flask, url_for, request, json
from flask.json import jsonify
import sqlite3

#Configuration
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# Create db and open connection to it
conn = sqlite3.connect('../data/names.db', check_same_thread=False)
cur = conn.cursor()

#View
@app.route('/')
def api_root():
	return '{}\n'.format('Welcome')

# $curl --request GET http://127.0.0.1:5000/entries
@app.route('/entries', methods = ['GET'])
def api_entries():
	query = cur.execute("SELECT count(*) FROM names;")
	conn.commit()
	entries = query.fetchone()
	return '{}\n'.format('{}\n'.format(entries)[1:-3])
	
# $curl --request GET http://127.0.0.1:5000/entry_name?name=Annie
@app.route('/entry_name', methods = ['GET'])
def api_entry_name():
    query = cur.execute("SELECT id, year, gender, count FROM names WHERE name = '%s';" % request.args['name'])
    conn.commit()
    entries = [dict({'id': row[0], 'year': row[1], 'gender': row[2], 'count': row[3]}) for row in query.fetchall()]
    return jsonify({'Entries for %s' % request.args['name']: entries})

@app.route('/insert')
def api_insert():
    #query = 'INSERT INTO names (name, year, gender, count) VALUES ( ?, ?, ?, ? )', (request.args['name'], request.args['year'], request.args['gender'], request.args['count'])
    cur.execute('INSERT INTO names (name, year, gender, count) VALUES ( "Carlo", 1984, "M", 12 )')
    conn.commit()
    id = cur.lastrowid
    #c.close()
    return id

#End view

if __name__ == '__main__':
	#Run the Server
	app.run(debug=True)
