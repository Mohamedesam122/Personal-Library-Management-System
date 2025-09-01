class Book:
    next_id=1
    
    def __init__(self, title, author, genre, price, publisher_year):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.publisher_year = publisher_year
        self.__rating=None
        self.__review=None

    def __str__(self):
        rating_str = f"{self.__rating}/5.0" if self.__rating is not None else "No rating yet"
        review_str = self.__review if self.__review else "No review yet"

        return (
            f"Book ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Price: {self.price}\n"
            f"Publisher Year: {self.publisher_year}\n"
            f"Rating: {rating_str}\n"
            f"Review: {review_str}"
        )
    

    def set_rating(self):

     while True:
        try:
            rating = float(input("Enter the rating: "))  
            if 0 <= rating <= 5:
                self.__rating = rating
                break
            else:
                raise ValueError("Rating must be a number between 0 and 5.")
        except Exception:
            print("Invalid input. Please enter a number between 0 and 5.")

              

    def set_review(self):
        while True:
            try:
                review = input("Enter the review: ")
                if review.strip():
                    self.__review = review
                    break
                else:
                    raise ValueError("Invalid review. Please provide a non-empty review.")
            except Exception as ve:
                print(ve)

    def get_rating(self):
        if self.__rating is not None:
            return f"{self.__rating}/5.0"
        return "No rating yet"

    def get_review(self):
        if self.__review:
            return self.__review
        else:
            return "no review yet"

 
class Library:

    def __init__(self):
        self.books=[]

    def add_book(self,b):
        self.books.append(b)
        print("Book added successfully!")


    def remove_book_by_id(self, id):
      for book in self.books:
          if book.id == id:
              self.books.remove(book)
              print("Book removed successfully!")
              return
      print("Book not found.")


    def display_books(self):
        if len(self.books)==0:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)


    def search_books_by_author(self,author):
        flag=False

        for book in self.books:
            if book.author.strip().lower()==author.strip().lower():
                print(book)
                flag=True
        if not flag:
            print("book not found")





    def search_books_by_title(self,title):

        for book in self.books:
            if book.title.strip().lower()==title.strip().lower():
                return book
        return "book not found"



    def search_books_by_genre(self,genre):

        flag=False

        for book in self.books:
            if book.genre.strip().lower()==genre.strip().lower():
                print(book)
                flag=True
        if not flag:
            print("book not found")



    def display_books_sorted_by_year(self):
        if len(self.books)==0:
            print("No books in the library.")
            return
        sorted_books=sorted(self.books,key=lambda x:x.publisher_year)
        for book in sorted_books:
            print(book)         
    


    def display_books_sorted_by_price(self):
        if len(self.books)==0:
            print("No books in the library.")
            return
        sorted_books=sorted(self.books,key=lambda x:x.price,reverse=True)
        for book in sorted_books:
            print(book)


    def display_books_sorted_by_rating(self):
        if len(self.books) == 0:
            print("No books in the library.")
            return

        def rating_value(book):
            if book.get_rating() == "No rating yet":
                return 0
            return float(book.get_rating().split("/")[0])  
        sorted_books = sorted(self.books, key=rating_value, reverse=True)
        for book in sorted_books:
            print(book)




    def display_books_sorted_by_author(self):
        if len(self.books)==0:
            print("No books in the library.")
            return
        sorted_books=sorted(self.books,key=lambda x:x.author)
        for book in sorted_books:
            print(book)



    def display_books_sorted_by_title(self):
        if len(self.books)==0:
            print("No books in the library.")
            return
        sorted_books=sorted(self.books,key=lambda x:x.title)
        for book in sorted_books:
            print(book)


    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.genre},{book.price},{book.publisher_year}\n")
                print("Books saved successfully!")


    def load_from_file(self, filename):            
            with open(filename, "r", encoding="utf-8") as f:
                self.books = [] 
                for line in f:
                    if line.strip():
                        title, author, genre, price, publisher_year = line.strip().split(",")
                        book = Book(title, author, genre, float(price), int(publisher_year))
                        self.add_book(book)
                




def main():
    egyptian_library=Library()

    while True:
         
        print("\n--- Personal Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book by ID")
        print("3. Display All Books")
        print("4. Search Books by Author")
        print("5. Search Books by Title")
        print("6. Search Books by Genre")
        print("7. Display Books Sorted by Year")
        print("8. Display Books Sorted by Price")
        print("9. Display Books Sorted by Rating")
        print("10. Display Books Sorted by Author")
        print("11. Display Books Sorted by Title")
        print("12. set rating and review")
        print("13. get rating and review")
        print("14. Load Books from File")
        print("15. Save Books to File")
        print("16. Exit")

        choice =input("Enter your choice (1-16): ")
        if choice=="1":
            title=input("Enter book title: ")
            author=input("Enter book author: ")
            genre=input("Enter book genre: ")
            while True:
                try:
                    price = float(input("Enter book price: "))
                    break
                except ValueError:
                    print("Invalid price. Please enter a number.")

            while True:
                try:
                    publisher_year = int(input("Enter publisher year: "))
                    break
                except ValueError:
                    print("Invalid year. Please enter a valid integer.")
            new_book=Book(title,author,genre,price,publisher_year)
            egyptian_library.add_book(new_book)



        elif choice=="2":
            while True:
                try:
                    id=int(input("Enter the ID of the book to remove: "))
                    egyptian_library.remove_book_by_id(id)
                    break
                except ValueError:
                    print("Invalid ID. Please enter a number.")

        elif choice=="3":
            egyptian_library.display_books()

        elif choice=="4":
            while True:
                try:
                    author=input("Enter author name to search: ")
                    egyptian_library.search_books_by_author(author)
                    break
                except Exception:
                    print("Invalid author name. Please enter a valid string.")

        elif choice=="5":
            while True:
                try:
                    title=input("Enter book title to search: ")
                    print(egyptian_library.search_books_by_title(title))
                    break
                except Exception:
                    print("Invalid title name. Please enter a valid string.")

        elif choice=="6":
            while True:
                try:
                    genre=input("Enter genre to search: ")
                    egyptian_library.search_books_by_genre(genre)
                    break
                except Exception:
                    print("Invalid genre name. Please enter a valid string.")

        elif choice=="7":
            egyptian_library.display_books_sorted_by_year()

        elif choice=="8":
            egyptian_library.display_books_sorted_by_price()

        elif choice=="9":
            egyptian_library.display_books_sorted_by_rating()

        elif choice=="10":
            egyptian_library.display_books_sorted_by_author()

        elif choice=="11":
            egyptian_library.display_books_sorted_by_title()

        elif choice=="12":
           
           title=input("Enter book title to set rating and review: ")
           book=egyptian_library.search_books_by_title(title)
           if isinstance(book, Book):
               book.set_rating()
               book.set_review()
           else:
               print("Book not found.")

        elif choice=="13":
           title = input("Enter book title to get rating and review: ")
           book=egyptian_library.search_books_by_title(title)
           if isinstance(book, Book):
               print(f"Rating: {book.get_rating()}")
               print(f"Review: {book.get_review()}")
           else:
                 print("Book not found.")
        elif choice=="14":
            while True:
                filename = input("Enter the filename to load books: ")
                try:
                    egyptian_library.load_from_file(filename)
                    print("Books loaded successfully!")
                    break   
                except FileNotFoundError:
                    print("File not found, please try again.")
                except Exception as e:
                    print(f"An error occurred: {e}")

        elif choice=="15":
           filename = input("Enter the filename to save books: ")
           egyptian_library.save_to_file(filename)

        elif choice=="16":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 14.")


if __name__ == "__main__":
    main()
