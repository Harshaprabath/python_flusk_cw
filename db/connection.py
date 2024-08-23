from flask_pymongo import PyMongo

def conn(app: object):
  # hosted db
  app.config['MONGO_URI'] = "mongodb+srv://cw_user:d8Y5veXHCUFR6O4Y@cw.3zua9iz.mongodb.net/cw_db?retryWrites=true&w=majority"

  # db composer offline
  # app.config['MONGO_URI'] = "mongodb://localhost:27017/cw_db"

  mongo = PyMongo(app)
  return mongo     
