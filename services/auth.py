from flask import render_template, request, redirect, url_for, session,jsonify
from db.connection import conn
from pymongo.errors import PyMongoError
from pymongo.errors import PyMongoError 


def handle_login(mongo :object):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            users_collection = mongo.db.user
            user_data = users_collection.find_one({'email': username})

           

            if user_data and user_data['password'] == password:
                session['username'] = username
                session['password']= password 
                return redirect(url_for('home'))

        except PyMongoError as e:
            # Handle MongoDB errors
            return render_template('error.html', error_message=f'MongoDB error: {str(e)}')

    return render_template('login.html')


def handle_home(mongo):
    if 'username' in session:
        data = mongo.db.customer.find()
        return render_template('index.html', username=session['username'], data=data)
        
    return render_template('login.html')


def handle_logout():
    session.pop('username', None)
    return redirect(url_for('home'))

def fogetpassword():
    return render_template('password.html') 

def resetpassword(mongo :object):
 
    try:
        if request.method == 'POST':
            email = request.form['email']
            users_collection = mongo.db.user
            user_data = users_collection.find_one({'email': email})
            
            
            if user_data and user_data['email'] == email:
                password =user_data['password']
                return password
            
            elif user_data:
                # Assuming the password is stored in the user_data dictionary
                password = user_data.get('password', 'Password not found')

                # You can return the password or render a template with the password
                return render_template('password.html', password=password)
            else:
                return render_template('password.html', message='Email not found')
                      
    except PyMongoError as e:
        # Handle MongoDB errors
        return render_template('error.html', error_message=f'MongoDB error: {str(e)}')

    # Render the default template for the reset password page
    return render_template('password.html')

def profile():
    return render_template('edit-profile.html', username=session['username']    )




def updateuser(mongo:object):
     try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            newemail = request.form['newemail']
            newpassword = request.form['newpassword']

            users_collection = mongo.db.user  # Assuming mongo is a PyMongo object
            user_data = users_collection.find_one({'email': email})

            if user_data and user_data['email'] == email and user_data['password'] == password:
                # Update the user's password in MongoDB
                result = users_collection.update_one({'email': email}, {'$set': {'email':newemail,'password': newpassword}})

                if result.modified_count > 0:
                   return handle_logout()
                else:
                    return render_template('edit-profile.html', username=session['username'])

            elif user_data:
                # Assuming the password is stored in the user_data dictionary
                stored_password = user_data.get('password', 'Password not found')

                # You can return the stored password or render a template with the password
                return render_template('edit-profile.html', username=session['username'])

            else:
                  return render_template('edit-profile.html', username=session['username'])

     except PyMongoError as e:
        # Handle MongoDB errors
        return render_template('error.html', error_message=f'MongoDB error: {str(e)}')

    # Render the default template for the reset password page
     return render_template('password.html') 

def getuser(mongo:object):
        try:
            # Assuming you have a collection named 'your_collection_name'
            collection = mongo.db.user

            # Retrieve all documents in the collection
            data_list = list(collection.find())

            # Convert ObjectId to string for JSON serialization
            for data in data_list:
                data['_id'] = str(data['_id'])

            return jsonify({'data': data_list})

        except Exception as e:
            return jsonify({'error': str(e)})