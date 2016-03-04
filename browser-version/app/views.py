from app import app
from flask import render_template, request, flash
from modules import *

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/total")
def total():
    return render_template("total.html")

@app.route("/entry_name", methods=["GET","POST"])
def entry_name():
    return render_template("entry_name.html")

@app.route("/insert", methods=["GET", "POST"])
def insert():
    return render_template("insert.html")

# Manage results

@app.route("/entries", methods=["GET", "POST"])
def entries():
    entries = total_entries()
    return render_template("homepage_total.html",entries=entries)

@app.route("/total_entries_name", methods=["GET", "POST"])
def total_entries_name():
    name = request.form['name']
    if name.isalpha():
        entries = select_entries_by_name(name)
        return render_template("homepage_name.html",name=name,entries=entries)
        #return entries
    else:
        return '{}\n'.format('Please, insert a name with NO spaces, numbers or special characters.')

@app.route("/first_last_year", methods=['GET', 'POST'])
def first_last_year():
    name = request.form['name']
    if name.isalpha():
        entries = first_and_last(name)
        return render_template("homepage_first_last.html",years=entries)
    else:
        return '{}\n'.format('Please, insert a name with NO spaces, numbers or special characters.')

@app.route("/new_insert", methods=["GET", "POST"])
def new_insert():
    
    name = request.form['name']
    year = request.form.get('year')
    gender = request.form.get('gender')
    count = request.form.get('count')
    
    if name.isalpha():
        if year.isnumeric() and 1900 <= int(year) <= 2016:
            if gender == 'M' or gender == 'F':
                if count.isnumeric():
                    newId = insert_name(name,year,gender,count)
                    return render_template("homepage_new_entry.html",id=newId)
                else:
                    return '{}\n'.format('Please, insert a numeric value of count.')
            else:
                return '{}\n'.format('Please, insert "M" for Male or "F" for female.')
        else:
            return '{}\n'.format('Please, insert a numeric value of year grather than 1900 and less then (or equal) to 2016.')
    else:
        return '{}\n'.format('Please, insert a name with NO spaces, numbers or special characters.')
        
