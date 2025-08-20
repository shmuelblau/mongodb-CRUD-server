import pymongo
from DAL.DAL import DAL


class Eagle_DAL:
    
    def __init__(self,host,user,password, dbname ,collecsion_name):
        db= DAL(host,user,password, dbname)
        self.collecsion_conn = collecsion_name
        conn = db.get_conn()
        self.collecsion = conn[self.collecsion_conn]
        

   
# ---------------------------------------------------------------------------------------

    def Select(self):
        
        return list(self.collecsion.find({}, {"_id": False}))
# ---------------------------------------------------------------------------------------
    def add(self , person):

        new_person = {"id":person.id , "first_name" :person.first_name , "last_name": person.last_name , "phone_number":person.phone_number , "rank":person.rank}

        self.collecsion.insert_one(new_person)
        
# ---------------------------------------------------------------------------------------

    def edit(self, person):
        myquery ={"id":person.id}
        newvalues = {"$set" : {"first_name" :person.first_name , "last_name": person.last_name , "phone_number":person.phone_number , "rank":person.rank}}

        self.collecsion.update_one(myquery , newvalues)
        


# ---------------------------------------------------------------------------------------

    def delete(self ,person):
        self.collecsion.delete_one({"id":person.id})
               

    def c(self):
        pass