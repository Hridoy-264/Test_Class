import os
from dotenv import load_dotenv

#Load invironment variables from .env file
load_dotenv()

API_KEY = os.getenv("database_url")

print(API_KEY)
print(databaseurl)

"""Hello kacher bondhura"""