class User:
    # User(str,str)
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.friends = []
    # __str__: void -> str
    def __str__(self):
        result = ('%s (%s)\nFriends: ' % (self.name,self.email))
        if len(self.friends)==0:
            result = result + 'None'
        elif len(self.friends)==1:
            result = result + ('%s' % self.friends[0].name)
        elif len(self.friends)==2:
            result = result + ('%s and %s' % (self.friends[0].name,self.friends[1].name))
        else:
            for friend in self.friends[:-1]:
                result += ('%s, ' % friend.name)
            result += ('and %s' % self.friends[-1].name)
        return result
    # void -> str
    def getName(self):
        return self.name
    # void -> str
    def getEmail(self):
        return self.email
    # str -> void
    def setName(self,name):
        self.name = name
    # str -> void
    def setEmail(self,email):
        self.email = email
    # list of object -> void
    def setFriends(self,newFriends):
        self.friends = newFriends
    # str -> void
    def addFriend(self,friend):
        self.friends.append(friend)
        friend.friends.append(self)
    # void -> list of str
    def getFriends(self):
        return self.friends
    # str -> bool
    def isFriend(self,user):
        return (user in self.friends)
