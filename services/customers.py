from flask import render_template, request, redirect, url_for, session,jsonify,send_file
from db.connection import conn
from pymongo.errors import PyMongoError
from pymongo.errors import PyMongoError 
from reportlab.pdfgen import canvas

def addcustermeremails(mongo):
      if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']

        # Insert data into MongoDB
        new_data = {'name': name,'email': email,'no':mobile}
        mongo.db.customer.insert_one(new_data)

        return render_template('x.html')