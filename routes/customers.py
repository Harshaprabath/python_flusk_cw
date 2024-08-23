from services.customers import *

def customer_routs(app,mongo):
    @app.route('/add_customer', methods=['POST'])
    def add_custermer_emeails():
        return addcustermeremails(mongo)
    

   