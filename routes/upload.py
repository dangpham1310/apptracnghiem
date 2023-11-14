from flask import render_template, request
from . import routes
from .db import *
from routes.db import db
from flask import Flask,jsonify, render_template, request, redirect, url_for, session,send_from_directory
import os
from datetime import datetime, timedelta
@routes.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('files')
        uploadcode = request.form['upload_code']
        target_folder = f'./code/{uploadcode}'
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        for file in uploaded_files:
            if file:
                file.save(os.path.join(target_folder, file.filename))
        # Get a list of image files in the folder
        image_files = [f for f in os.listdir(target_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp',".txt"))]
        return render_template('upload.html', image_files=image_files)
    return render_template('upload.html', image_files=[])


@routes.route('/view/<code>/<image>', methods=['GET'])
def view(code, image):
    code_directory = "code"
    return send_from_directory(code_directory, f"{code}/{image}")


@routes.route('/view/<code>/dapan.txt', methods=['GET'])
def dapan(code):
    with open(f"./code/{code}/dapan.txt", 'r') as file:
        ads_content = file.readlines()
    print(ads_content)
    return render_template('dapan.html', ads_content=ads_content)


@routes.route('/<code>/<name>/<lophoc>/<socau>', methods=['GET'])
def senddapan(code,name,lophoc,socau):

    current_utc_time = datetime.utcnow()
    current_gmt_plus_7_time = current_utc_time + timedelta(hours=7)
    user = User(code=code,name = name,lophoc = lophoc,socau = socau,time = current_gmt_plus_7_time)
    db.session.add(user)
    db.session.commit()
    return "OK"

@routes.route('/ketqua', methods=['GET',"POST"])
def ketqua():
    if request.method == 'POST':
        code = request.form['code']
        # user = User(code=code)
        user = User.query.filter_by(code=code).all()

        return render_template('ketqua.html', ketqua=user)

    return render_template('ketqua.html')



