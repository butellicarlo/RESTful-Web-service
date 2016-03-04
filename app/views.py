from app import app
from flask.json import jsonify
import re
from modules import *

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    return '{}\n{}\n{}\n{}\n{}\n'.format('Welcome in the Query DB Web Service!', 'How to use it:', \
                                     '1) Total entries: curl http://<Server_address>/entries', \
                                     '2) Total entries for name: curl --request GET http://<Server_address>/entry_name/<name>', \
                                     '3) Insert new name: curl --request POST http://<Server_address>/insert/<name>,<year>,<gender(M/F)>,<count>', \
                                     '4) First and last year where name appear: curl http://<Server_address>/max_min/<name>')

@app.route("/entries")
def entries():
    entries = total_entries()
    return '{}\n'.format('{}\n'.format(entries)[1:-3])

@app.route("/entry_name/<name>", methods=["GET"])
def entry_name(name):
    if name.isalpha():
        entries = select_entries_by_name(name)
        return jsonify({'Entries for %s' % name: entries})
    else:
        return '{}\n'.format('Please, insert a name with NO spaces, numbers or special characters.')

#Check entry values
@app.route("/insert/<name>,<year>,<gender>,<count>", methods=["POST"])
def insert(name,year,gender,count):
    new_id = insert_name(name,year,gender,count)
    return '{}\n'.format(str(new_id))

@app.route("/max_min/<name>", methods=['GET'])
def max_min(name):
    if name.isalpha():
    	years = first_and_last(name)
    	return '{}\n'.format(years)
    else:
        return '{}\n'.format('Please, insert a name with NO spaces, numbers or special characters.')
