class Customer:

    def __init__(self, name):
        self.wishlist = []
        self.name = name

    def addToWishlist(self, book):
        self.wishlist.append(book)

    def removeFromWishlist(self, book):
        self.wishlist.remove(book)

    def wishlistCost(self):
        totalCost = 0

        for books in self.wishlist:
            totalCost += books.cost
        return totalCost

    def printWishlist(self):
        print(self.name + "'s wishlist: ")

        count = 1
        for books in self.wishlist:
            print(str(count) + ") ", end="")
            print(books)
            count += 1
        print("Total Cost: $" + str(self.wishlistCost()) + "\n")