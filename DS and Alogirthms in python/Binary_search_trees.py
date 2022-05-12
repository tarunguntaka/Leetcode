class user:
    def __init__(self,username, name, email) -> None:
        self.username = username 
        self.name = name 
        self.email = email


class user_database:
    def __init__(self):
        self.db = []
        
    def insert(self, user):
        i = 0 
        while i < len(self.db):
            if user.username < self.db[i].username:
                break 
            i+=1 
            self.db.insert(i,user)