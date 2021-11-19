import itertools

class Player:
    newidP = itertools.count()
    def __init__(self, id, name, email):
        self.__playerID = id
        self.__name = name
        self.__email = email
    
    def get_id(self):
        return self.__playerID
    
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def set_name(self, newName):
        self.__name = newName

    def set_email(self, newEmail):
        self.__email = newEmail