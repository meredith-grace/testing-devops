#Grace Meredith & Matthew Stenvold 
#Activity 4 test script

#to run: python3 test_bookstore.py

import unittest

from customer import Customer
from store import Store
from book import Book

class TestBookStore(unittest.TestCase):
	
	def test_integrate_customer_wishlist_and_books(self):
		c = Customer("bob")
		b = Book(1, "Frankenstein", "Mary Shelley", 1)

		c.addToWishlist(b)

		self.assertEqual(c.wishlist[0], b) #check the wishlist has the book we created for it
		self.assertEqual(c.wishlistCost(), b.cost)
		c.removeFromWishlist(b)

		self.assertEqual(c.wishlist, []) #check the wishlist is empty once removed

	def test_integrate_store_inventory_and_books(self):
		s = Store()
		b = Book(4, "Green Eggs and Ham", "Dr. Seuss", 1)

		s.addToInventory(b, 2)

		self.assertEqual(s.bookIndex[b.idNumber], b) #check the inventory has the book we created and added to it
		self.assertTrue(s.checkStock(b)) #checkstock should return true

		s.removeInventory(b)

		self.assertEqual(s.inventory[b.idNumber], 1) #quantity should have decremented after removing the book once.

		b2 = Book(5, "Horton Hears a Who", "Dr. Seuss", 1)
		self.assertFalse(s.removeInventory(b2)) #removeing should return false, since it was never added.
		self.assertFalse(s.checkStock(b2))

		s.addToInventory(b, 4) #add book that was already created in catalog
		self.assertEqual(s.inventory[b.idNumber], 5)

if __name__ == '__main__':
	unittest.main()