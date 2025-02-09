from pymongo import MongoClient
from dotenv import load_dotenv , find_dotenv
import os 
import pprint
import gridfs
load_dotenv(find_dotenv())
 

password=os.environ.get("mongo_pass")


connection_str= f"mongodb+srv://shahd:{password}@cluster0.uz1ff.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client=MongoClient(connection_str)


db=client.assignments 
coll=db.exam 


fs = gridfs.GridFS(db)  # Initialize GridFS


#Uploads a PDF or Word file to MongoDB

def upload_file(file_path):
    try:
        with open(file_path, "rb") as f:
            file_id = fs.put(f, filename=os.path.basename(file_path))
            print(f"File uploaded successfully with ID: {file_id}")

    except Exception as e:
        print(f"Error uploading file: {e}")


 
if __name__ == "__main__":
    file_path = input("Enter the file path: ")  # Get file path from user
    upload_file(file_path)












