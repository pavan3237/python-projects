🏦 Bank Account Management System (Python OOP Project)
This is a simple Bank Account Management System built using Object-Oriented Programming (OOP) concepts in Python. It simulates real-world banking operations like deposit, withdrawal, transaction history, and balance checking.

📌 Features
🔐 Password-protected bank accounts (stored securely via encapsulation)

💰 Deposit and Withdraw funds

📜 Transaction history log

📊 Check account balance

🗂 Manage multiple accounts using a Bank class

🛠️ Technologies Used
Python 3.6+

Core concepts of Object-Oriented Programming (OOP):

Classes & Objects

Encapsulation

Data abstraction

📁 Project Structure
plaintext
Copy
Edit
BankAccount.py     # Contains all class definitions and test cases
README.md          # Project documentation (this file)
📌 Code Overview
🔹 BankAccount class
Handles individual account operations:

python
Copy
Edit
account = BankAccount("pavan", 123, 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
account.get_history()
🔹 Bank class
Handles storage and management of multiple user accounts.

python
Copy
Edit
bank = Bank()
bank.add_account(account)
🚀 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/BankAccountOOP.git
cd BankAccountOOP
Run the Python script:

bash
Copy
Edit
python BankAccount.py
🧠 Concepts Practiced
Encapsulation using __password

Class interaction (Bank → BankAccount)

Method organization and reuse

Input validation and error handling

📸 Sample Output
vbnet
Copy
Edit
Deposited ₹500. New balance: ₹1500
Withdrew ₹200. New balance: ₹1300
pavan, your balance is ₹1300
Transaction History:
Deposited ₹500
Withdrew ₹200
✍️ Author
Pavan Kumar

GitHub:pavan3237
