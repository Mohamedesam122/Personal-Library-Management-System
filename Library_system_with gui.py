import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
from tkinter import font as tkfont

class Book:
    next_id = 1

    def __init__(self, title, author, genre, price, publisher_year):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.publisher_year = publisher_year
        self.__rating = None
        self.__review = None

    def __str__(self):
        rating_str = f"{self.__rating}/5.0" if self.__rating is not None else "No rating yet"
        review_str = self.__review if self.__review else "No review yet"

        return (
            f"Book ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Price: ${self.price:.2f}\n"
            f"Publisher Year: {self.publisher_year}\n"
            f"Rating: {rating_str}\n"
            f"Review: {review_str}\n"
            f"{'-'*40}\n"
        )

    def set_rating(self, rating):
        if 0 <= rating <= 5:
            self.__rating = rating
            return True
        return False

    def set_review(self, review):
        if review.strip():
            self.__review = review
            return True
        return False

    def get_rating(self):
        if self.__rating is not None:
            return f"{self.__rating}/5.0"
        return "No rating yet"

    def get_review(self):
        if self.__review:
            return self.__review
        else:
            return "No review yet"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, b):
        self.books.append(b)
        return "Book added successfully!"

    def remove_book_by_id(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                return "Book removed successfully!"
        return "Book not found."

    def display_books(self):
        if len(self.books) == 0:
            return "No books in the library."
        result = ""
        for book in self.books:
            result += str(book)
        return result

    def search_books_by_author(self, author):
        result = ""
        found = False
        for book in self.books:
            if book.author.strip().lower() == author.strip().lower():
                result += str(book)
                found = True
        if not found:
            return "No books found by this author."
        return result

    def search_books_by_title(self, title):
        for book in self.books:
            if book.title.strip().lower() == title.strip().lower():
                return book
        return None

    def search_books_by_genre(self, genre):
        result = ""
        found = False
        for book in self.books:
            if book.genre.strip().lower() == genre.strip().lower():
                result += str(book)
                found = True
        if not found:
            return "No books found in this genre."
        return result

    def display_books_sorted_by_year(self, ascending=True):
        if len(self.books) == 0:
            return "No books in the library."
        sorted_books = sorted(self.books, key=lambda x: x.publisher_year, reverse=not ascending)
        result = ""
        for book in sorted_books:
            result += str(book)
        return result

    def display_books_sorted_by_price(self, ascending=True):
        if len(self.books) == 0:
            return "No books in the library."
        sorted_books = sorted(self.books, key=lambda x: x.price, reverse=not ascending)
        result = ""
        for book in sorted_books:
            result += str(book)
        return result

    def display_books_sorted_by_rating(self, ascending=True):
        if len(self.books) == 0:
            return "No books in the library."

        def rating_value(book):
            if book.get_rating() == "No rating yet":
                return 0
            return float(book.get_rating().split("/")[0])

        sorted_books = sorted(self.books, key=rating_value, reverse=not ascending)
        result = ""
        for book in sorted_books:
            result += str(book)
        return result

    def display_books_sorted_by_author(self, ascending=True):
        if len(self.books) == 0:
            return "No books in the library."
        sorted_books = sorted(self.books, key=lambda x: x.author, reverse=not ascending)
        result = ""
        for book in sorted_books:
            result += str(book)
        return result

    def display_books_sorted_by_title(self, ascending=True):
        if len(self.books) == 0:
            return "No books in the library."
        sorted_books = sorted(self.books, key=lambda x: x.title, reverse=not ascending)
        result = ""
        for book in sorted_books:
            result += str(book)
        return result

    def display_books_sorted_by_genre(self, ascending=True):
        if len(self.books) == 0:
            return "No books in the library."
        sorted_books = sorted(self.books, key=lambda x: x.genre, reverse=not ascending)
        result = ""
        for book in sorted_books:
            result += str(book)
        return result

    def save_to_file(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for book in self.books:
                    f.write(f"{book.title},{book.author},{book.genre},{book.price},{book.publisher_year}\n")
            return "Books saved successfully!"
        except Exception as e:
            return f"Error saving file: {str(e)}"

    def load_from_file(self, filename):
        try:
            if not os.path.exists(filename):
                return "File not found."

            with open(filename, "r", encoding="utf-8") as f:
        
                for line in f:
                    if line.strip():
                        data = line.strip().split(",")
                        if len(data) == 5:
                            title, author, genre, price, publisher_year = data
                            book = Book(title, author, genre, float(price), int(publisher_year))
                            self.add_book(book)
            return "Books loaded successfully!"
        except Exception as e:
            return f"Error loading file: {str(e)}"


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Library Management System")
        
        # Set fullscreen mode
        self.root.attributes('-fullscreen', True)
        
        # Add a way to exit fullscreen (Escape key)
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        
        # Configure elegant color scheme
        self.bg_color = "#f8f6f2"  # Soft off-white
        self.sidebar_color = "#3a506b"  # Deep blue-gray
        self.accent_color = "#5c6bc0"  # Soft blue
        self.secondary_accent = "#3ca420"  # Coral accent
        self.text_color = "#37474f"  # Dark gray
        self.light_text = "#ffffff"  # White
        self.button_color = "#5c6bc0"  # Soft blue
        self.highlight_color = "#7986cb"  # Lighter blue
        self.entry_bg = "#ffffff"  # White
        self.header_color = "#1c313a"  # Dark blue
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        # Red button style (for dangerous actions)
        self.style.configure('Danger.TButton',
                    background='#d32f2f',   # Red
                    foreground=self.light_text,
                    font=('Verdana', 10, 'bold'))
        self.style.map('Danger.TButton',
              background=[('active', '#b71c1c')],
              foreground=[('active', self.light_text)])
        # Green button style (for Add Book)
        self.style.configure('Success.TButton',
                    background='#43a047',   # أخضر متوسط
                    foreground=self.light_text,
                    font=('Verdana', 10, 'bold'))
        self.style.map('Success.TButton',
                       
                       
                      background=[('active', '#66bb6a')],   # أخضر فاتح عند الضغط
                      foreground=[('active', self.light_text)])



        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('Sidebar.TFrame', background=self.sidebar_color)
        self.style.configure('Header.TLabel', 
                            background=self.bg_color, 
                            foreground=self.header_color,
                            font=('Georgia', 18, 'bold'))
        self.style.configure('Title.TLabel', 
                            background=self.sidebar_color, 
                            foreground=self.light_text,
                            font=('Georgia', 16, 'bold'))
        self.style.configure('Normal.TLabel', 
                            background=self.sidebar_color, 
                            foreground=self.light_text,
                            font=('Verdana', 10))
        self.style.configure('TButton', 
                            background=self.button_color,
                            foreground=self.light_text,
                            font=('Verdana', 10, 'bold'),
                            borderwidth=0,
                            focuscolor=self.button_color)
        self.style.map('TButton',
                      background=[('active', self.highlight_color)],
                      foreground=[('active', self.light_text)])
        self.style.configure('Accent.TButton', 
                            background=self.secondary_accent,
                            foreground=self.light_text,
                            font=('Verdana', 10, 'bold'))
        self.style.map('Accent.TButton',
                      background=[('active', '#ff8a65')],
                      foreground=[('active', self.light_text)])
        self.style.configure('TLabelframe', 
                            background=self.sidebar_color,
                            foreground=self.light_text,
                            bordercolor=self.sidebar_color,
                            lightcolor=self.sidebar_color,
                            darkcolor=self.sidebar_color)
        self.style.configure('TLabelframe.Label', 
                            background=self.sidebar_color,
                            foreground=self.light_text,
                            font=('Georgia', 12, 'bold'))
        self.style.configure('TCombobox', 
                            fieldbackground=self.entry_bg,
                            background=self.entry_bg,
                            foreground=self.text_color,
                            selectbackground=self.accent_color)
        self.style.configure('TEntry', 
                            fieldbackground=self.entry_bg,
                            foreground=self.text_color,
                            selectbackground=self.accent_color)
        self.style.configure('TScrollbar', 
                            background=self.sidebar_color,
                            troughcolor=self.bg_color,
                            bordercolor=self.sidebar_color,
                            arrowcolor=self.light_text)
        
        self.library = Library()

        # Main container
        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Configure grid weights
        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Create left and right panels
        self.create_left_panel(main_frame)
        self.create_right_panel(main_frame)
        
        # Display initial status
        self.status_var.set("Ready")
        self.display_all_books()

    def create_left_panel(self, parent):
        # Left panel for controls
        left_frame = ttk.Frame(parent, width=350, style='Sidebar.TFrame')
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        left_frame.columnconfigure(0, weight=1)
        
        # Create a canvas with scrollbar for the left panel
        canvas = tk.Canvas(left_frame, bg=self.sidebar_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas, style='Sidebar.TFrame')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Title
        title_label = ttk.Label(self.scrollable_frame, text="Library Manager", style='Title.TLabel')
        title_label.pack(pady=(15, 20))
        
        # Add Book Section
        add_frame = ttk.LabelFrame(self.scrollable_frame, text="Add New Book", padding="10")
        add_frame.pack(fill="x", pady=5, padx=10)
        
        labels = ["Title:", "Author:", "Genre:", "Price:", "Year:"]
        self.entries = {}
        for i, text in enumerate(labels):
            ttk.Label(add_frame, text=text, style='Normal.TLabel').grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(add_frame, width=20, font=('Verdana', 9))
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.entries[text[:-1].lower()] = entry
        
        add_frame.columnconfigure(1, weight=1)

        ttk.Button(add_frame, text="Add Book", command=self.add_book, style='Success.TButton').grid(
            row=len(labels), column=0, columnspan=2, pady=10, sticky="ew"
        )

        # Search Section
        search_frame = ttk.LabelFrame(self.scrollable_frame, text="Search Books", padding="10")
        search_frame.pack(fill="x", pady=5, padx=10)
        
        ttk.Label(search_frame, text="Search by:", style='Normal.TLabel').grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.search_var = tk.StringVar(value="Title")
        search_combo = ttk.Combobox(search_frame, textvariable=self.search_var, 
                                   values=["Title", "Author", "Genre"], state="readonly", width=17)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(search_frame, text="Search term:", style='Normal.TLabel').grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.search_entry = ttk.Entry(search_frame, width=20, font=('Verdana', 9))
        self.search_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Button(search_frame, text="Search", command=self.search_books, style='TButton').grid(
            row=2, column=0, columnspan=2, pady=10, sticky="ew"
        )
        
        search_frame.columnconfigure(1, weight=1)

        # Sort Section
        sort_frame = ttk.LabelFrame(self.scrollable_frame, text="Sort Books", padding="10")
        sort_frame.pack(fill="x", pady=5, padx=10)
        
        # Sort options with order
        sort_options_frame = ttk.Frame(sort_frame)
        sort_options_frame.pack(fill="x", pady=5)
        
        ttk.Label(sort_options_frame, text="Sort by:", style='Normal.TLabel').grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.sort_var = tk.StringVar(value="Title")
        sort_combo = ttk.Combobox(sort_options_frame, textvariable=self.sort_var, 
                                 values=["Title", "Author", "Genre", "Year", "Price", "Rating"], 
                                 state="readonly", width=15)
        sort_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(sort_options_frame, text="Order:", style='Normal.TLabel').grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.order_var = tk.StringVar(value="Ascending")
        order_combo = ttk.Combobox(sort_options_frame, textvariable=self.order_var, 
                                  values=["Ascending", "Descending"], 
                                  state="readonly", width=15)
        order_combo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Button(sort_frame, text="Sort Books", command=self.sort_books, style='TButton').pack(fill="x", pady=5)

        # File Operations
        file_frame = ttk.LabelFrame(self.scrollable_frame, text="File Operations", padding="10")
        file_frame.pack(fill="x", pady=5, padx=10)
        
        ttk.Label(file_frame, text="Filename:", style='Normal.TLabel').grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.filename_entry = ttk.Entry(file_frame, font=('Verdana', 9))
        self.filename_entry.insert(0, "library.txt")
        self.filename_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Button(file_frame, text="Load from File", command=self.load_from_file, style='TButton').grid(
            row=1, column=0, columnspan=2, pady=5, sticky="ew"
        )
        ttk.Button(file_frame, text="Save to File", command=self.save_to_file, style='TButton').grid(
            row=2, column=0, columnspan=2, pady=5, sticky="ew"
        )
        
        file_frame.columnconfigure(1, weight=1)

        # Rating & Review
        rating_frame = ttk.LabelFrame(self.scrollable_frame, text="Rating & Review", padding="10")
        rating_frame.pack(fill="x", pady=5, padx=10)
        
        ttk.Label(rating_frame, text="Book Title:", style='Normal.TLabel').grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.rating_title_entry = ttk.Entry(rating_frame, font=('Verdana', 9))
        self.rating_title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(rating_frame, text="Rating (0-5):", style='Normal.TLabel').grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.rating_entry = ttk.Entry(rating_frame, font=('Verdana', 9))
        self.rating_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Label(rating_frame, text="Review:", style='Normal.TLabel').grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.review_entry = ttk.Entry(rating_frame, font=('Verdana', 9))
        self.review_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        button_frame = ttk.Frame(rating_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Set", command=self.set_rating_review, style='TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Get", command=self.get_rating_review, style='TButton').pack(side=tk.LEFT, padx=5)
        
        rating_frame.columnconfigure(1, weight=1)

        # Remove Book
        remove_frame = ttk.LabelFrame(self.scrollable_frame, text="Remove Book", padding="10")
        remove_frame.pack(fill="x", pady=5, padx=10)
        
        ttk.Label(remove_frame, text="Book ID:", style='Normal.TLabel').grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.remove_id_entry = ttk.Entry(remove_frame, font=('Verdana', 9))
        self.remove_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        ttk.Button(remove_frame, text="Remove Book", command=self.remove_book, style='Danger.TButton').grid(
            row=1, column=0, columnspan=2, pady=10, sticky="ew"
        )
        
        remove_frame.columnconfigure(1, weight=1)

        # Display All Books
        ttk.Button(self.scrollable_frame, text="Display All Books", command=self.display_all_books, style='TButton').pack(
            fill="x", pady=10, padx=10
        )
        
        # Exit fullscreen button
        ttk.Button(self.scrollable_frame, text="Exit Fullscreen (Esc)", 
                  command=lambda: self.root.attributes('-fullscreen', False), style='TButton').pack(
            fill="x", pady=10, padx=10
        )

    def create_right_panel(self, parent):
        # Right panel for displaying books
        right_frame = ttk.Frame(parent, style='TFrame')
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(1, weight=1)
        
        # Header
        header = ttk.Label(right_frame, text="Library Contents", style='Header.TLabel')
        header.grid(row=0, column=0, sticky=tk.W, pady=(10, 5), padx=10)
        
        # Text area for displaying books
        text_frame = ttk.Frame(right_frame, style='TFrame')
        text_frame.grid(row=1, column=0, sticky="nsew", pady=5, padx=10)
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(
            text_frame, width=80, height=30, wrap=tk.WORD, 
            font=('Consolas', 10), bg=self.entry_bg, fg=self.text_color,
            insertbackground=self.text_color, selectbackground=self.accent_color,
            relief='flat', bd=2
        )
        self.output_text.grid(row=0, column=0, sticky="nsew")
        
        # Status bar
        status_frame = ttk.Frame(right_frame, style='TFrame', height=25)
        status_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 5))
        status_frame.columnconfigure(0, weight=1)
        status_frame.grid_propagate(False)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(status_frame, textvariable=self.status_var, 
                              style='Normal.TLabel', background=self.sidebar_color,
                              foreground=self.light_text, font=('Verdana', 9))
        status_bar.grid(row=0, column=0, sticky="ew")

    def add_book(self):
        try:
            title = self.entries["title"].get()
            author = self.entries["author"].get()
            genre = self.entries["genre"].get()
            price = float(self.entries["price"].get())
            year = int(self.entries["year"].get())
            
            if not title or not author or not genre:
                messagebox.showerror("Error", "Title, Author, and Genre cannot be empty")
                return
                
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for Price and Year")
            return

        book = Book(title, author, genre, price, year)
        result = self.library.add_book(book)
        self.status_var.set(result)
        for e in self.entries.values():
            e.delete(0, tk.END)
        
        self.display_all_books()

    def remove_book(self):
      

      try:

        book_id = int(self.remove_id_entry.get())
      except ValueError:
        messagebox.showerror("Error", "Book ID must be an integer")
        return
    
    
      confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete book ID {book_id}?")
      if not confirm:

        return  
    
      result = self.library.remove_book_by_id(book_id)
      self.status_var.set(result)
      self.remove_id_entry.delete(0, tk.END)
      self.display_all_books()

    def display_all_books(self):
        result = self.library.display_books()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)
        self.status_var.set("Displaying all books")

    def search_books(self):
        search_type = self.search_var.get()
        term = self.search_entry.get().strip()
        
        if not term:
            messagebox.showwarning("Warning", "Please enter a search term")
            return
            
        if search_type == "Title":
            result = self.library.search_books_by_title(term)
            result = str(result) if result else "No book found with that title"
        elif search_type == "Author":
            result = self.library.search_books_by_author(term)
        else:
            result = self.library.search_books_by_genre(term)
            
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)
        self.status_var.set(f"Search results for {search_type}: {term}")

    def sort_books(self):
        sort_type = self.sort_var.get()
        ascending = self.order_var.get() == "Ascending"
        
        if sort_type == "Year":
            result = self.library.display_books_sorted_by_year(ascending)
        elif sort_type == "Price":
            result = self.library.display_books_sorted_by_price(ascending)
        elif sort_type == "Rating":
            result = self.library.display_books_sorted_by_rating(ascending)
        elif sort_type == "Author":
            result = self.library.display_books_sorted_by_author(ascending)
        elif sort_type == "Genre":
            result = self.library.display_books_sorted_by_genre(ascending)
        else:
            result = self.library.display_books_sorted_by_title(ascending)
            
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)
        self.status_var.set(f"Books sorted by {sort_type} ({'Ascending' if ascending else 'Descending'})")

    def save_to_file(self):
        filename = self.filename_entry.get().strip()
        if not filename:
            messagebox.showwarning("Warning", "Please enter a filename")
            return
            
        result = self.library.save_to_file(filename)
        self.status_var.set(result)

    def load_from_file(self):
        filename = self.filename_entry.get().strip()
        if not filename:
            messagebox.showwarning("Warning", "Please enter a filename")
            return
            
        result = self.library.load_from_file(filename)
        self.status_var.set(result)
        self.display_all_books()

    def set_rating_review(self):
        title = self.rating_title_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Please enter a book title")
            return
            
        book = self.library.search_books_by_title(title)
        if not book:
            messagebox.showerror("Error", "Book not found")
            return
            
        try:
            rating_text = self.rating_entry.get().strip()
            if rating_text:  # Only set rating if provided
                rating = float(rating_text)
                if not 0 <= rating <= 5:
                    raise ValueError
                book.set_rating(rating)
                
            review = self.review_entry.get().strip()
            if review:  # Only set review if provided
                book.set_review(review)
                
            self.status_var.set("Rating & review updated")
            self.display_all_books()
            
        except ValueError:
            messagebox.showerror("Error", "Rating must be a number between 0 and 5")

    def get_rating_review(self):
        title = self.rating_title_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Please enter a book title")
            return
            
        book = self.library.search_books_by_title(title)
        if not book:
            messagebox.showerror("Error", "Book not found")
            return
            
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Title: {book.title}\n")
        self.output_text.insert(tk.END, f"Rating: {book.get_rating()}\n")
        self.output_text.insert(tk.END, f"Review: {book.get_review()}\n")
        self.status_var.set(f"Rating and review for: {title}")


def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

