from flask import render_template, request, redirect, url_for, session,jsonify, send_file
from db.connection import conn
from pymongo.errors import PyMongoError
from pymongo.errors import PyMongoError 
from services.auth import *
from bson import ObjectId
from reportlab.pdfgen import canvas

def getCustermeremeails():
       
    return render_template('x.html')

def deleteallcustermer(mongo:object):

    try:
           
        result = mongo.db.customer.delete_many({})
        if result.deleted_count > 0:
           
            return handle_home(mongo)
        
        else:
             return handle_home(mongo)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


def delete_custermer(mongo:object,user_id):
    try:
        # Convert the user_id to ObjectId, as MongoDB uses ObjectId for _id field
        obj_id = ObjectId(user_id)
        collection = mongo.db.customer

        
        # Find the user by ID and delete
        result = collection.delete_one({'_id': obj_id})

        if result.deleted_count > 0:
                     
            return handle_home(mongo)
        
        else:
             return handle_home(mongo)
             
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

    # report_generator.py
# def generate_report(data):
#     # Your report generation logic here
#     report = [{"name": item.get("name"), "value": item.get("value")} for item in data]
#     return report

def pdfcustomer(mongo):
    def generate_pdf():
        customers = list(mongo.db.customer.find({}, {'_id': 0}))

        pdf_filename = 'customers_list.pdf'
        generate_pdf_report(pdf_filename, customers)

        return send_file(pdf_filename, as_attachment=True)

def generate_pdf_report(filename, customers):
        from io import BytesIO

        buffer = BytesIO()

        # Create the PDF object using ReportLab
        pdf = canvas.Canvas(buffer)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 800, "Customer List")

        y_position = 780
        for customer in customers:
            y_position -= 20
            pdf.drawString(100, y_position, f"Name: {customer['name']}")
            pdf.drawString(100, y_position - 15, f"Email: {customer['email']}")
            pdf.drawString(100, y_position - 30, "-------------------------")

        pdf.showPage()
        pdf.save()

        # Move the buffer position to the beginning
        buffer.seek(0)

        # Save the buffer to a file in binary mode
        with open(filename, 'wb') as f:
            f.write(buffer.read())
