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

# $ curl --request GET http://127.0.0.1:5000/entries
@app.route('/entries', methods = ['GET'])
def api_entries():
	query = cur.execute("SELECT count(*) FROM names;").fetchone()
	conn.commit()
	return '{}\n'.format('{}\n'.format(query)[1:-3])
	
# $ curl --request GET http://127.0.0.1:5000/entry_name/Annie
@app.route('/entry_name/<name>', methods = ['GET'])
def api_entry_name(name):
    query = cur.execute("SELECT id, year, gender, count FROM names WHERE name = '%s';" % name)
    conn.commit()
    entries = [dict({'id': row[0], 'year': row[1], 'gender': row[2], 'count': row[3]}) for row in query.fetchall()]
    return jsonify({'Entries for %s' % name: entries})

# $ curl --request POST http://127.0.0.1:5000/insert/Ronnie,1987,M,102
@app.route('/insert/<name>,<year>,<gender>,<count>', methods = ['POST'])
def api_insert(name,year,gender,count):
    cur.execute('INSERT INTO names (name, year, gender, count) VALUES (?,?,?,?)', (name,year,gender,count))
    conn.commit()
    id = cur.lastrowid
    return '{}\n'.format(str(id))

#End view

if __name__ == '__main__':
	#Run the Server
    #app.run(debug=True)
    app.run()