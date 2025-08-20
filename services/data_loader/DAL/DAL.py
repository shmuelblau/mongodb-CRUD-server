from pymongo import MongoClient
from pymongo.database import Database
class DAL:
    def __init__(self ,host,user,password, dbname) -> None:

         myclient = MongoClient(f"mongodb://{user}:{password}@{host}:27017/{dbname}?authSource=admin")
        
         self.conn = myclient[dbname]
        
           

    def get_conn(self) -> Database:
        
        return self.conn # type: ignore