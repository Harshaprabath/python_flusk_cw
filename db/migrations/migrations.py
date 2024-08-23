from pymongo import MongoClient
from user_migration import user_migrayion
from TEST import test
from customer_migretiion import  customer 
# Replace 'your_database_name' with your actual database name
DATABASE_NAME = 'cw_db'

    # Connect to MongoDB
# hosted db
client = MongoClient("mongodb+srv://cw_user:d8Y5veXHCUFR6O4Y@cw.3zua9iz.mongodb.net/cw_db?retryWrites=true&w=majority")

#composer db offline
# client = MongoClient("mongodb://localhost:27017/cw_db")

# user_migrayion(client,DATABASE_NAME)
# test(client,DATABASE_NAME)
customer(client,DATABASE_NAME)