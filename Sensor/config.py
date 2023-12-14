import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os 

#Provide the mongodb localhost url to connect python to mongodb

@dataclass
class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key

    client = pymongo.MongoClient()