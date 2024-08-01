import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.books = ["English", "Chemistry", "Math", "Physics", "Computer", "Software"]
        self.create_widgets()

    def create_widgets(self):
        # Create Menu Bar
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save", command=self.save_books)  # This will not work without pickle
        self.file_menu.add_command(label="Load", command=self.load_books)  # This will not work without pickle
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Create Main Frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Add Book Button
        self.add_book_button = ttk.Button(self.main_frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=0, column=0, padx=10, pady=5)

        # View Books Button
        self.view_books_button = ttk.Button(self.main_frame, text="View Books", command=self.view_books)
        self.view_books_button.grid(row=0, column=1, padx=10, pady=5)

        # Search Book Button
        self.search_book_button = ttk.Button(self.main_frame, text="Search Book", command=self.search_book)
        self.search_book_button.grid(row=0, column=2, padx=10, pady=5)

        # Status Bar
        self.status = tk.StringVar()
        self.status.set("Ready")
        self.status_bar = ttk.Label(self.root, textvariable=self.status, relief="sunken", anchor='w', padding="5")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def add_book(self):
        book_name = simpledialog.askstring("Add Book", "Enter the book name:")
        if book_name:
            if book_name not in self.books:
                self.books.append(book_name)
                self.status.set(f"'{book_name}' has been added.")
            else:
                self.status.set(f"'{book_name}' already exists.")
            self.update_status()
        else:
            self.status.set("No book name entered!")
            self.update_status()

    def view_books(self):
        if self.books:
            books_list = "\n".join(self.books)
            number_of_books = len(self.books)
            messagebox.showinfo("Books in Library", f"Books:\n{books_list}\n\nTotal number of books: {number_of_books}")
        else:
            messagebox.showinfo("Books in Library", "No books available.")

    def search_book(self):
        search_term = simpledialog.askstring("Search Book", "Enter book name to search:")
        if search_term:
            if search_term in self.books:
                messagebox.showinfo("Search Result", f"'{search_term}' is in the library.")
            else:
                messagebox.showinfo("Search Result", f"'{search_term}' is not in the library.")
        else:
            messagebox.showwarning("Input Error", "No search term entered!")

    def save_books(self):
        # Functionality removed as pickle is not used
        messagebox.showinfo("Save Functionality", "Save functionality is not available in this version.")

    def load_books(self):
        # Functionality removed as pickle is not used
        messagebox.showinfo("Load Functionality", "Load functionality is not available in this version.")

    def update_status(self):
        self.status_bar.config(text=self.status.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
