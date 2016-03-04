import sqlite3 as sql
from flask import current_app

def total_entries():
    with sql.connect("names.db") as con:
        cur = con.cursor()
        entries = cur.execute("SELECT count(*) FROM names").fetchone()
        con.commit()
    return str(entries)
    
def select_entries_by_name(name):
    with sql.connect("names.db") as con:
        cur = con.cursor()
        query = cur.execute("SELECT id, year, gender, count FROM names WHERE name = '{}';".format(name))
        con.commit()

        cached = current_app.cache.get('a_key')
        if cached:
            return cached #"The value is cached: {}\n".format(cached)
        result = [dict({'id': row[0], 'year': row[1], 'gender': row[2], 'count': row[3]}) for row in query.fetchall()]
        current_app.cache.set('a_key', result, timeout=180)

    return result

def insert_name(name,year,gender,count):
    with sql.connect("names.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO names (name,year,gender,count) VALUES ('{}',{},'{}',{})".format(name,year,gender,count) )
        con.commit()
        new_id = cur.lastrowid
    return str(new_id)

def first_and_last(name):
	with sql.connect("names.db") as con:
		cur = con.cursor()
		last = cur.execute("select MAX(year) from names where name='{}';".format(name) ).fetchone()
		first = cur.execute("select MIN(year) from names where name='{}';".format(name) ).fetchone()
		con.commit()
	return 'Last year is: %s \nFirst year is: %s' % ( \
		'{}'.format('{}\n'.format(last)[1:-3]), \
		'{}'.format('{}\n'.format(first)[1:-3]))


