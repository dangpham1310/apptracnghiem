from flask import Flask, render_template,request,session,redirect,url_for
from routes import routes
from routes.db import *
from datetime import datetime, timedelta
app = Flask(__name__)
app.secret_key = 'n9b9monkey1234567812233333333333333'
app.register_blueprint(routes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)  # Example: 30 days

db.init_app(app)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create main.db tables
    app.run(debug=True,host = "0.0.0.0",port = 5005)
