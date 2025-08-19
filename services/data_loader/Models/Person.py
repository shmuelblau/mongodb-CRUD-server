
class Person:

    def __init__(self, id=None, first_name='', last_name=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        


    
    
    @staticmethod
    def from_post_request(form):
        return Person(
            id=form.get('id'),
            first_name=form.get('first_name'),
            last_name=form.get('last_name'),
            
        )
    


    def __repr__(self):
        return (f"<Agent id={self.id}, codeName='{self.first_name}', realName='{self.last_name}'>")