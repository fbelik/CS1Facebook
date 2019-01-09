from comment import *
from status import *
from user import *

class Facebook:
    # Facebook()
    def __init__(self):
        self.users = {}
        self.statuses = []
        self.currentUser = None
    # str,str -> void
    def registerUser(self,name,email):
        if name in self.users:
            print('Error: User already registered')
        else:
            self.users[name] = User(name,email)
    # str -> void
    def login(self,name):
        if self.currentUser == None:
            self.currentUser = name
        else:
            print('Error: Other user must log off first')
    # void -> void
    def logout(self):
        if self.currentUser == None:
            print('Error: No user logged in')
        else:
            self.currentUser = None
    # str -> void
    def addFriend(self,name):
        if self.currentUser == None:
            print('Error: No user logged in')
        elif name not in self.users:
            print('Error: No user with that name')
        for friend in self.users[self.currentUser].friends:
            if friend.name == name:
                print('Error: Already friends with that user')
                break
        else:
            self.users[self.currentUser].addFriend(self.users[name])
    # void -> void
    def viewProfile(self):
        if self.currentUser == None:
            print('Error: No user logged in')
        else:
            print(self.users[self.currentUser])
    # str -> void
    def postStatus(self,message):
        if self.currentUser == None:
            print('Error: No user logged in')
        else:
            self.statuses.append(Status(self.currentUser,message))
    # void -> void
    def viewStatus(self):
        if self.currentUser == None:
            print('Error: No user logged in')
        else:
            for status in self.statuses:
                if (self.users[self.currentUser].isFriend(self.users[status.name]) or status.name == self.currentUser):
                    print('('+str(self.statuses.index(status))+')',status)
    # int -> void
    def likeStatus(self,num):
        if self.currentUser == None:
            print('Error: No user logged in')
        elif (num >= len(self.statuses) or (self.users[self.currentUser] == self.statuses[num].name and not self.users[self.currentUser].isFriend(self.statuses[num].name))):
            print('Error: Current user cannot like this status')
        elif self.statuses[num].name == self.currentUser:
            print('Error: Cannot like your own post')
        elif self.currentUser in self.statuses[num].likes:
            print('User already liked this post')
        elif (not (self.users[self.currentUser].isFriend(self.users[self.statuses[num].name]) or self.statuses[num].name == self.currentUser)):
            print('Error: Cannot like this post')
        else:
            self.statuses[num].addLike(self.currentUser)
    # int,str -> void
    def commentOnStatus(self,num,comment):
        if self.currentUser == None:
            print('Error: No user logged in')
        elif (num >= len(self.statuses) or (self.users[self.currentUser] == self.statuses[num].name and not self.users[self.currentUser].isFriend(self.statuses[num].name))):
            print('Error: Current user cannot comment this status')
        else:
            self.statuses[num].addComment(Comment(self.currentUser,comment))
        
