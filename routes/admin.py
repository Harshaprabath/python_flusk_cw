
from services.admin import *
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import Flask, jsonify, send_file

def admin_routs(app,mongo):
    @app.route('/')
    def get_Custermer_emeails():
        return getCustermeremeails()
    
    @app.route('/delete_all_customer', methods=['GET'])
    def delete_all_custermer():
        return deleteallcustermer(mongo)
    
    @app.route('/delete_customer/<string:user_id>', methods=['GET'])
    def delete_cus(user_id):
       return delete_custermer(mongo ,user_id)    
   
    # @app.route('/generate_pdf', methods=['GET'])
    # def getCustererPdf():
    #     return pdfcustomer(mongo)
    
        
 