class Comment:
    # Comment(str,str)
    def __init__(self,name,comment):
        self.name = name
        self.comment = comment
    # __str__: void -> str
    def __str__(self):
        return ('%s: %s' % (self.name,self.comment))
    # void -> str
    def getName(self):
        return self.name
    # void -> str
    def getComment(self):
        return self.comment
    # str -> void
    def setName(self,name):
        self.name = name
    # str -> void
    def setComment(self,comment):
        self.comment = comment
