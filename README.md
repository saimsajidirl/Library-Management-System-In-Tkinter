# Library-Management-System-In-Tkinter
Documentation for Library Management System
Overview

The Library Management System is a simple graphical user interface (GUI) application built using Python's tkinter module. The system allows the user to manage a collection of books by adding new books, viewing the list of books, and searching for specific books in the collection.

This program provides basic functionalities for managing books within a library, but does not include the ability to save or load the books to/from an external file (this functionality is indicated but not implemented in the current version).
Features

    Add Books: Allows users to add new books to the library collection.
    View Books: Displays all the books currently stored in the library.
    Search for Books: Allows users to search for specific books in the library.
    Status Bar: Shows the current status of the system, such as success messages or warnings.
    Menu Options: Includes a basic menu with "Save", "Load", and "Exit" options (though the "Save" and "Load" functionalities are not implemented).

Program Structure
Class: LibraryApp

The main class that represents the Library Management System. It contains all the methods and GUI components used to interact with the user.
Constructor: __init__(self, root)

    Parameters:
        root: The root Tk window which represents the main window of the application.
    Description:
        Initializes the main window, book list, and GUI components.
        Initializes the list of books with some default books.
        Calls the create_widgets() method to set up the UI components.

Method: create_widgets(self)

    Description:
        Sets up the GUI components, including a menu bar, buttons, and a status bar.
        Menu Bar:
            The menu bar includes options for Save, Load, and Exit.
        Main Frame:
            A frame that holds the three primary buttons for the application:
                Add Book: Opens a dialog box to enter a new book name.
                View Books: Displays a message box with the current list of books.
                Search Book: Prompts the user to enter a book name to search for.
        Status Bar:
            Displays the current status of the application (e.g., when a book is added, or when the user performs an action).

Method: add_book(self)

    Description:
        Prompts the user to enter a new book name using simpledialog.askstring.
        If the book name is not empty and does not already exist in the library, it adds the book to the list and updates the status.
        If the book already exists, it updates the status to indicate that the book is already in the library.
        If no name is entered, it sets the status to "No book name entered!"

Method: view_books(self)

    Description:
        Displays a message box that shows the list of all books in the library and the total number of books.
        If no books are available, it notifies the user with a message stating "No books available."

Method: search_book(self)

    Description:
        Prompts the user to enter a book name to search for.
        If the book exists, it shows a message saying the book is in the library.
        If the book does not exist, it shows a message stating that the book is not in the library.
        If no search term is entered, it warns the user that no search term was provided.

Method: save_books(self)

    Description:
        Currently, this method does not have any functionality implemented because the pickle module (which could be used to save data) is not used in this version.
        The user is notified with a message stating "Save functionality is not available in this version."

Method: load_books(self)

    Description:
        Similar to the save_books method, this method is also not implemented due to the lack of external file handling.
        The user is notified that the load functionality is not available.

Method: update_status(self)

    Description:
        Updates the status bar with the current status message.

GUI Components
Menu Bar

    File Menu:
        Save: Placeholder for saving the books (currently non-functional).
        Load: Placeholder for loading books (currently non-functional).
        Exit: Closes the application.

Main Frame

    Add Book Button:
        Opens a dialog where the user can enter a new book name. If valid, the book is added to the library.
    View Books Button:
        Displays a list of all books in the library, along with the total count.
    Search Book Button:
        Opens a dialog where the user can enter a search term to find a specific book in the library.

Status Bar

    A label at the bottom of the window that shows the current status of the application, such as when a book is added or if no books exist.

Example Workflow

    Add a New Book:
        Click the Add Book button.
        Enter a book name in the prompt that appears.
        The new book is added to the library, and the status updates with a message like 'Book Name' has been added.

    View Books:
        Click the View Books button.
        A message box will show the current list of books and the total number of books.

    Search for a Book:
        Click the Search Book button.
        Enter the name of the book you want to search for.
        A message box will indicate whether the book is in the library or not.

    Save and Load:
        These buttons are present but currently do not do anything in this version.

    Exit:
        Click the Exit option from the menu or close the window directly to quit the application.

Error Handling and User Input

    No Book Name Entered: When the user tries to add a book without entering a name, the status updates with "No book name entered!".
    Duplicate Book: If the user tries to add a book that already exists in the library, the status updates with "Book already exists!".
    Search Empty Input: If the user tries to search for a book without entering a search term, the program shows a warning with the message "No search term entered!".
