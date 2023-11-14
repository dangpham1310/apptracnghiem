from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import User
from routes.db import *

@routes.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    if request.method == 'POST':
        link = request.form.get('link')  # Use request.form.get to handle missing key
        user = User.query.filter_by(username=session['username']).first()
        f = open(f"{user.id}link.txt","w")
        f.write(link)
        f.close()
    user = User.query.filter_by(username=session['username']).first()
    f = open(f"{user.id}link.txt","r")
    link = f.readlines()
    f.close()
    print(link[0])
    return render_template('dashboard.html', id=user.id,link = link[0])


@routes.route('/api/<id>', methods=["POST", "GET"])
def api(id):
    if request.method == 'POST':
        value = request.form['value']
        f = open(f"{id}.txt","w")
        f.write(value)
        f.close()

        return redirect(url_for('routes.dashboard'))
    f = open(f"{id}.txt","r")
    values = f.readlines()
    f.close()
    return values
    

