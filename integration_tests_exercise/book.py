class Book:

    def __init__(self, idNumber, title, author, cost):
        self.idNumber = idNumber
        self.title = title
        self.author = author
        self.cost = cost

    def __eq__(self, id):
        return id == self.idNumber

    def __repr__(self):
        return str(self.title + " by " + self.author + ", id:" + str(self.idNumber))