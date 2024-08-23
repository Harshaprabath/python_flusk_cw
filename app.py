# app.py

from flask import Flask, render_template, request, redirect, url_for, session , send_file ,jsonify
from flask_mail import Mail, Message
from routes.auth import *
from routes.admin import *
from routes.customers import *
from routes.pdf import *
import requests
from bson import ObjectId
from flask_cors import CORS 
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key in production
CORS(app)
mongo = conn(app)
#admin gI0bopwHhdHJlG1T
auth_routs(app,mongo)
admin_routs(app,mongo)
customer_routs(app,mongo)
pdf_routs(app,mongo)



if __name__ == '__main__':
    app.run(debug=True, port=8000)