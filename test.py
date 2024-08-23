
from flask import Flask, send_file, jsonify
from flask_cors import CORS
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key in production
CORS(app)

# You can remove the lines related to MongoDB here


@app.route('/generate_pdf', methods=['GET'])
def generate_pdf():
    # You can create a sample data instead of querying MongoDB
    sample_data = [
        {'name': 'John Doe', 'email': 'john@example.com'},
        {'name': 'Jane Doe', 'email': 'jane@example.com'},
        # Add more sample data as needed
    ]

    pdf_filename = 'customers_list.pdf'
    generate_pdf_report(pdf_filename, sample_data)

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

if __name__ == '__main__':
    app.run(debug=True)