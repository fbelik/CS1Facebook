class Status:
    # Status(str,str)
    def __init__(self,name,message):
        self.name = name
        self.message = message
        self.likes = []
        self.comments = []
    # __str__: void -> str
    def __str__(self):
        result = ('%s %s\n' % (self.name,self.message))
        if len(self.likes)==1:
            result = result + ('%s likes this\n' % self.likes[0])
        elif len(self.likes)==2:
            result = result + ('%s and %s like this\n' % (self.likes[0],self.likes[1]))
        elif len(self.likes)>2:
            for name in self.likes[:-1]:
                result += ('%s, ' % name)
            result += ('and %s like this\n' % self.likes[-1])
        for comment in self.comments:
            result += ('%s\n' % (comment))
        return result[:-1]
    # void -> str
    def getName(self):
        return self.name
    # str -> void
    def setName(self,name):
        self.name = name
    # void -> str
    def getMessage(self):
        return self.message
    # str -> void
    def setMessage(self,message):
        self.message = message
    # void -> list of str
    def getLikes(self):
        return self.likes
    # list of str -> void
    def setLikes(self,newLikes):
        self.likes = newLikes
    # list of str -> void
    def addLike(self,name):
        self.likes.append(name)
    # void -> list of object
    def getComments(self):
        return self.comments
    # list of object -> void
    def setComments(self,newComments):
        self.comments = newComments
    # list of object -> void
    def addComment(self,comment):
        self.comments.append(comment)
