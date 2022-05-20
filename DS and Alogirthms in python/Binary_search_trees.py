




from numpy import insert
from regex import E


class user:
    def __init__(self,username, name, email) -> None:
        self.username = username 
        self.name = name 
        self.email = email

    def __repr__(self) -> str:
        return "User(username={un}, name ={n}, email = {e})".format(un=self.username,n=self.name,e=self.email)
    def __str__(self) -> str:
        return self.__repr__()

class user_database:
    def __init__(self):
        self.db = []
    
    def insert(self,user):
        i = 0
        while i <len(self.db):
            if user.username < self.db[i].username:
                break
            i+=1
        self.db.insert(i,user)
    
    def find(self,username):
        # i = 0
        # while i < len(self.db):
        #     if self.db[i].username == username:
        #         return self.db[i]
        #     i+=1
        for users in self.db:
            if users.username == username:
                print(users.username)
    
    def update(self,user):
        t = self.find(user.username)
        t.name = user.name 
        t.email = user.email

    def list_all(self):
        return self.db


if __name__ == '__main__':
    userdb = user_database()
    aakash = user('aakash', 'Aakash Rai', 'aakash@example.com')
    biraj = user('biraj', 'Biraj Das', 'biraj@example.com')
    hemanth = user('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    jadhesh = user('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    siddhant = user('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    sonaksh = user('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
    vishal = user('vishal', 'Vishal Goel', 'vishal@example.com')
    vishal1 = user('vishal', 'Vishal Goel1', 'vishal1@example.com')


    userdb.insert(aakash)
    userdb.insert(vishal)
    userdb.insert(sonaksh)

    print(userdb.find(aakash))
    # print(userdb.list_all())
    # userdb.update(vishal1)
    # print(userdb.list_all())


