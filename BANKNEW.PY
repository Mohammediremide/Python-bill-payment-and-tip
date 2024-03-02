import tkinter as tk
from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Application")
        
        root.configure(background = '')

        root.resizable(width = True, height = True)
        
        self.accounts = {}

        # Input fields
        self.account_number_label = tk.Label(root, text="Account Number:")
        self.account_number_label.grid(row=0, column=0)
        self.account_number_entry = tk.Entry(root)
        self.account_number_entry.grid(row=0, column=1)

        self.balance_label = tk.Label(root, text="Balance:")
        self.balance_label.grid(row=1, column=0)
        self.balance_entry = tk.Entry(root, state="readonly")
        self.balance_entry.grid(row=1, column=1)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=2, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=2, column=1)

        # Buttons
        self.create_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_button.grid(row=3, column=0, columnspan=2)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=4, column=0, columnspan=2)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=5, column=0, columnspan=2)

        self.check_balance_button = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.grid(row=6, column=0, columnspan=2)

    def create_account(self):
        account_number = self.account_number_entry.get()
        if account_number not in self.accounts:
            self.accounts[account_number] = 0
            messagebox.showinfo("Success", "Account created successfully!")
            self.check_balance()
        else:
            messagebox.showerror("Error", "Account already exists.")

    def deposit(self):
        account_number = self.account_number_entry.get()
        amount = self.amount_entry.get()
        if account_number in self.accounts and amount:
            self.accounts[account_number] += float(amount)
            self.check_balance()
        else:
            messagebox.showerror("Error", "Invalid account number or amount.")

    def withdraw(self):
        account_number = self.account_number_entry.get()
        amount = self.amount_entry.get()
        if account_number in self.accounts and amount and float(amount) <= self.accounts[account_number]:
            self.accounts[account_number] -= float(amount)
            self.check_balance()
        else:
            messagebox.showerror("Error", "Invalid account number, insufficient balance, or invalid amount.")

    def check_balance(self):
        account_number = self.account_number_entry.get()
        if account_number in self.accounts:
            self.balance_entry.config(state="normal")
            self.balance_entry.delete(0, tk.END)
            self.balance_entry.insert(0, self.accounts[account_number])
            self.balance_entry.config(state="readonly")
        else:
            messagebox.showerror("Error", "Invalid account number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
