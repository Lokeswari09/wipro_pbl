class Author:
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

class Book:
    def __init__(self, name, author, price, qtyInStock):
        self.name = name
        self.author = author
        self.price = price
        self.qtyInStock = qtyInStock

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_qtyInStock(self):
        return self.qtyInStock

    def set_qtyInStock(self, qtyInStock):
        self.qtyInStock = qtyInStock

author_name = input("Enter author name: ")
author_email = input("Enter author email: ")
author_gender = input("Enter author gender (M/F): ")

author_obj = Author(author_name, author_email, author_gender)

book_name = input("Enter book name: ")
book_price = float(input("Enter book price: "))
book_qty = int(input("Enter book quantity in stock: "))

book_obj = Book(book_name, author_obj, book_price, book_qty)

print("\n--- Book Details ---")
print("Book Name:", book_obj.get_name())
print("Price:", book_obj.get_price())
print("Quantity in Stock:", book_obj.get_qtyInStock())
print("Author Details:")
print("  Name:", book_obj.get_author().name)
print("  Email:", book_obj.get_author().email)
print("  Gender:", book_obj.get_author().gender)