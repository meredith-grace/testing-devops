import book
import store
import customer

# Creates the book objects
test = book.Book(1, "The Great Gatsby", "F. Scott Fitzgerald", 12)
test2 = book.Book(2, "Moby-Dick", "Herman Melville", 4)
test3 = book.Book(3, "Alice in Wonderland", "Lewis Carroll", 9)
test4 = book.Book(4, "Frankenstein", "Mary Shelley", 8)

# Displays the stores stock
store = store.Store()
store.addToInventory(test, 4)
store.addToInventory(test2, 0)
store.addToInventory(test3, 7)
store.removeInventory(test4)
store.displayStock()

# Add 5 more copies of The great Gatsby, and 3 copies of Frankenstein. Then display
store.addToInventory(test, 5)
store.addToInventory(test4, 3)
store.removeInventory(test3)
store.displayStock()

# Create a wishlist and display it
customer1 = customer.Customer("Matthew")
customer1.addToWishlist(test)
customer1.addToWishlist(test2)
customer1.printWishlist()


# Check availability of books
def checkAvailability(customer):
    for books in customer.wishlist:
        if(store.checkStock(books)):
            print(books.title + "is available")
        else:
            print(books.title + "is not available")

checkAvailability(customer1)