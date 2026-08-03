# Python Projects

Building Python projects from fundamentals to real-world applications, focusing on problem-solving, OOP, and backend development.

---

## Project 1: CLI Quiz Game(V1)

### Description
A command-line based quiz game built using Python. The user selects the number of questions, answers multiple-choice questions, and receives a final score based on performance.

#### Features
- Multiple questions using structured data (list & dictionary)
- Input validation (handles invalid inputs)
- Score calculation (+4 for correct, -1 for wrong)
- User-controlled number of questions
- User-controlled level for the quiz
- Giving Performance Feedback
- Replay Feature after completing one round of Quiz


## Project 2: CLI Result Management System(V1)

### Description
This is a simple Result Management System built using Python.  
It takes student details, allows input of subject-wise marks based on stream, and calculates total, percentage, grade, and result.

#### Features
- Stream-based subject selection (Science / Commerce / Arts)
- User input for subject-wise marks
- Automatic total and percentage calculation
- Grade assignment based on performance
- Pass/Fail result generation
- Average , Percentage Calculator
- Maximum, Minimum marks by subjects
- Clean output formatting
- Replay Feature


## Bank System (CLI) - Python
A Command-Line Banking System built using Python that simulates basic banking operations such as account creation, login, deposits, withdrawals, and balance management. The project stores account information persistently using a JSON file, allowing users to access their accounts even after restarting the program.

### Features
- Account Management
- Create a new bank account
- Automatically generates unique account numbers
- Login using account number
- Displays account details after successful login

### Banking Operations
- Deposit money
- Withdraw money
- Check current account balance
- Logout from the account
- Exit the application

### Data Persistence
- Stores account information in a JSON file
- Account data is preserved even after the application is closed
- Updates account balance after every transaction

### Exception Handling
- Handles invalid menu inputs
- Prevents non-numeric inputs
- Prevents invalid deposit amounts
- Prevents withdrawing more than available balance
- Displays user-friendly error messages

### Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON File Handling
- File I/O
- Exception Handling

## Project Structure

```text
Bank-System/
│
├── main.py              # Main program
├── account.py           # Account class and banking methods
├── accounts.json        # Stores user account data
├── .gitignore
└── README.md
```
  
### Demo Accounts
You can use the following demo accounts to test the application.

- Account Number	Name	Balance
- 1001	Demo	₹15,000
- 1002	Demo_2	₹10,000

### How to Run
#### Clone the repository
- bash
- git clone https://github.com/ayanb22/Bank-System

#### Navigate to the project folder
- bash
- cd Bank-System

#### Run the application
- bash
- python main.py


### Application Workflow
#### Main Menu
- Create New Account
- Login to Existing Account
- Exit

#### Banking Menu
- Check Balance
- Deposit Money
- Withdraw Money
- Logout

### Concepts Used
- Classes & Objects
- Static Methods
- Class Variables
- Constructors
- JSON Serialization
- Lists & Dictionaries
- While Loops
- Nested Loops
- Exception Handling (try-except)
- File Handling

### Future Improvements
- Password-protected login
- Account deletion
- Money transfer between accounts
- Transaction history
- Interest calculation
- Admin panel
- SQLite/MySQL database integration
- GUI using Tkinter or PyQt
- Django/Flask Web Version

### Author

- Ayan Banerjee GitHub: https://github.com/ayanb22 LinkedIn: https://linkedin.com/in/ayan-banerjee-dev
