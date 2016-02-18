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
    entries = select_entries_by_name(name)
    return render_template("homepage_name.html",name=name,entries=entries)
    #return entries

@app.route("/new_insert", methods=["GET", "POST"])
def new_insert():
    
    name = request.form['name']
    year = request.form.get('year')
    gender = request.form.get('gender')
    count = request.form.get('count')
    
    newId = insert_name(name,year,gender,count)
    
    return render_template("homepage_new_entry.html",id=newId)
