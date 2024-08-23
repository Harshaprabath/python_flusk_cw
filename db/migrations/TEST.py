
def test (client,DATABASE_NAME):
    COLLECTION_NAME = 'test'

        # Access or create the database
    db = client[DATABASE_NAME]

        # Check if the collection already exists    
    print(f"Collection '{COLLECTION_NAME}' CREAT OR UPDATE in database '{DATABASE_NAME}'.")
    default_data = [
                {"name": "Default Item 1", "value": 100},
                {"name": "Default Item 2", "value": 200},
                # Add more default data as needed
            ]
    collection = db[COLLECTION_NAME]
            # Insert the default data into the collection
    collection.insert_many(default_data)

    print(f"Default data added to '{COLLECTION_NAME}'.")


