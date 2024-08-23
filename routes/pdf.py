from services.admin import *
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import Flask, jsonify, send_file

def pdf_routs(app, mongo):
    @app.route('/generate_pdf', methods=['GET'])
    def generate_pdfc():
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
            pdf.drawString(100, 800, "Customer Dertels List")

            y_position = 780
          
           
            for customer in customers:
                y_position -= 20
                pdf.drawString(100, y_position, f"{customer['email']}")
                
            pdf.showPage()
            pdf.save()

            # Move the buffer position to the beginning
            buffer.seek(0)

            # Save the buffer to a file in binary mode
            with open(filename, 'wb') as f:
                f.write(buffer.read())