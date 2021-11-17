import itertools

class Player:
    newidP = itertools.count()
    def __init__(self, id, name, email):
        self.playerID = id
        self.name = name
        self.email = email
    
    def get_id(self):
        return self.playerID
    
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_name(self, newName):
        self.name = newName

    def set_email(self, newEmail):
        self.email = newEmail