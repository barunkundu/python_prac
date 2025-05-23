# class student:
#     def __init__(self, mark):
#         self.mark = mark

#     def show(self):
#         print(f"your mark is: {self.mark}")

#     @property # this is getter
#     def mul(self):
#         return self.mark * 3
    
#     @mul.setter     
#     def mul(self, new):
#         self.mark = new/2
        

# s1 = student(3)
# s1.mul = 2
# print(s1.mul)
# s1.show()


"""Write a Library class with two instance variables: no_of_books and books.
Write a program to:
Create a library object from the Library class.
Demonstrate how to print all the books in the library.
Show how to add a book to the library.
Illustrate how to get the number of books in the library using different methods.
Show that the program doesn't persist the books after it stops running."""

class library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add(self, new_book_name):
        self.books.append(new_book_name)
        self.no_of_books += 1
        # print(f"{new_book_name} add to the library")

    def get_no_of_books(self):
        return self.no_of_books
    
    def show_all_book(self):   
        print(f"the library has {self.get_no_of_books()} book")
        for book in self.books:
            print(f" book name is: {book}")



my_lib = library()
my_lib.add("barun")
my_lib.add("kundu")
my_lib.add("niten")

my_lib.show_all_book()
# print(f"no of book: {my_lib.no_of_books}")

# print(f"no of book: {my_lib.get_no_of_books()}")