from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

# MongoDB connection settings
uri = "mongodb+srv://Karan:Patel@cluster0.9ifur.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client["verification_codes"]  # Replace with your actual database name
collection = db["codes"]  # Replace with your actual collection name

def get_verification_code():
    """Fetch the latest verification code from MongoDB, if available."""
    document = collection.find_one({"verification_code": {"$exists": True}})
    if document:
        return document["verification_code"], document["_id"]
    return None, None

def delete_verification_code(doc_id):
    """Delete the verification code document from MongoDB by its ID."""
    collection.delete_one({"_id": doc_id})

if __name__ == "__main__":
    codes, document_id = get_verification_code()
    print(codes, document_id)
    print(delete_verification_code(document_id))   # Replace with your actual document ID
    print(get_verification_code())

    # delete_verification_code("your_document_id")  # Replace with your actual document ID
