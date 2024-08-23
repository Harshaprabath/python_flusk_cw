
from services.auth import *

def auth_routs(app,mongo):
    @app.route('/admin')
    def home():
        return handle_home(mongo)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return handle_login(mongo)

    @app.route('/logout')
    def logout():
        return handle_logout()
    
    @app.route('/forgetpassword', methods=['GET'])
    def reset_user():
        return fogetpassword()

    @app.route('/resetpassword', methods=['GET','POST'])
    def reset_passwword():
        return resetpassword(mongo)

    @app.route('/profile', methods=['GET'])
    def user():
        return profile()

    @app.route('/update_user', methods=['GET','POST'])
    def update_user():
        return updateuser(mongo)
    
    @app.route('/getuser', methods=['GET'])
    def get_user():
        return getuser(mongo)

    
  