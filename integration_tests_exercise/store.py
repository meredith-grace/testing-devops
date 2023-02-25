import book

class Store:

    def __init__(self):
        self.bookIndex = { }

        self.inventory = { }

            # Try to merge the two dictionaries into 1
            #1: {3, book.Book(1, "The Great Gatsby", "F. Scott Fitzgerald")},
            #2: {2, book.Book(2, "Moby-Dick", "Herman Melville")},
            #3: {7, book.Book(3, "Alice in Wonderland", "Lewis Carroll")}


    def displayStock(self):
        count = 1

        print("Store's current stock: ")
        for books in self.bookIndex:
            print(str(count) + ") ", end="")
            print(self.bookIndex.get(books), end="")
            print(" | " + str(self.inventory.get(books)) + " copies")
            count += 1
        print()

    def addToInventory(self, book, numAdded):
        bookId = book.idNumber

        if(bookId in self.inventory):
            self.inventory.update({bookId: (self.inventory.get(bookId) + numAdded)})
        else:
            self.inventory[bookId] = numAdded
            self.bookIndex[bookId] = book

    def removeInventory(self, book):
        bookId = book.idNumber
        
        if(bookId in self.inventory):
            if(not self.inventory.get(bookId) == 0):
                self.inventory.update({bookId: (self.inventory.get(bookId) - 1)})
                return True
        
        return False

    def checkStock(self, book):
        bookId = book.idNumber

        if(bookId in self.inventory):
            if(self.inventory.get(bookId) > 0):
                return True
        
        return False
        