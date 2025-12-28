"""
Banking Application - Organized Version
A simple banking app with login, registration, and transaction features
"""

import time
from datetime import datetime
from tkinter import (
    Toplevel,
    Frame,
    Label,
    Entry,
    Button,
    Listbox,
    messagebox,
    PhotoImage,
    LabelFrame,
)
from customtkinter import CTk, CTkToplevel


class AccountManager:
    """Handles all account-related file operations"""

    ACCOUNTS_FILE = "Accounts.txt"

    @staticmethod
    def load_accounts():
        """Load all accounts from file and return dictionaries"""
        usernames = []
        passwords = []
        balances = []

        try:
            with open(AccountManager.ACCOUNTS_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if len(parts) == 3:
                        usernames.append(parts[0])
                        passwords.append(parts[1])
                        balances.append(parts[2])
        except FileNotFoundError:
            # Create file if it doesn't exist
            open(AccountManager.ACCOUNTS_FILE, "w").close()

        credentials = dict(zip(usernames, passwords))
        account_balances = dict(zip(usernames, balances))

        return credentials, account_balances

    @staticmethod
    def username_exists(username):
        """Check if username already exists"""
        credentials, _ = AccountManager.load_accounts()
        return username in credentials

    @staticmethod
    def create_account(username, password):
        """Create a new account"""
        with open(AccountManager.ACCOUNTS_FILE, "a") as f:
            f.write(f"{username}, {password}, 0\n")

    @staticmethod
    def update_balance(username, new_balance):
        """Update account balance in file"""
        with open(AccountManager.ACCOUNTS_FILE, "r") as f:
            lines = f.readlines()

        with open(AccountManager.ACCOUNTS_FILE, "w") as f:
            for line in lines:
                parts = line.strip().split(", ")
                if parts[0] == username:
                    f.write(f"{parts[0]}, {parts[1]}, {new_balance}\n")
                else:
                    f.write(line)

    @staticmethod
    def get_balance(username):
        """Get current balance for a user"""
        _, balances = AccountManager.load_accounts()
        return float(balances.get(username, 0))


class RegisterWindow(Toplevel):
    """Registration window for creating new accounts"""

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Configure window properties"""
        self.title("Banking app - Sign up")
        self.geometry("1400x550")
        self.config(bg="#fff")
        self.wm_protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        """Create all UI widgets"""
        # Main frame
        self.main_frame = LabelFrame(
            self, text="Welcome!", width=350, height=400, bg="white"
        )
        self.main_frame.place(x=500, y=70)

        # Header
        Label(
            self.main_frame,
            text="Sign up",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 23, "bold"),
        ).place(x=115, y=5)

        # Username field
        Label(
            self.main_frame,
            text="Username:",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 9),
        ).place(x=20, y=50)

        self.username_entry = Entry(
            self.main_frame,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11, "bold"),
        )
        self.username_entry.place(x=30, y=80)

        Frame(self.main_frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Password field
        Label(
            self.main_frame,
            text="Password:",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 9),
        ).place(x=20, y=120)

        self.password_entry = Entry(
            self.main_frame,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11, "bold"),
            show="*",
        )
        self.password_entry.place(x=30, y=150)

        # Password toggle button
        self.eye_img1 = PhotoImage(file="closeye2.png")
        self.eye_btn1 = Button(
            self.main_frame,
            image=self.eye_img1,
            background="white",
            border=0,
            activebackground="white",
            cursor="hand2",
            command=lambda: self.toggle_password(1),
        )
        self.eye_btn1.place(x=285, y=145)

        Frame(self.main_frame, width=295, height=2, bg="black").place(x=25, y=177)

        # Confirm password field
        Label(
            self.main_frame,
            text="Confirm Password:",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 9),
        ).place(x=20, y=190)

        self.confirm_password_entry = Entry(
            self.main_frame,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11, "bold"),
            show="*",
        )
        self.confirm_password_entry.place(x=30, y=220)

        # Confirm password toggle button
        self.eye_img2 = PhotoImage(file="closeye2.png")
        self.eye_btn2 = Button(
            self.main_frame,
            image=self.eye_img2,
            background="white",
            border=0,
            activebackground="white",
            cursor="hand2",
            command=lambda: self.toggle_password(2),
        )
        self.eye_btn2.place(x=285, y=215)

        Frame(self.main_frame, width=295, height=2, bg="black").place(x=25, y=247)

        # Sign up button
        Button(
            self.main_frame,
            width=39,
            pady=7,
            text="Sign up",
            bg="blue",
            fg="white",
            border=0,
            command=self.handle_signup,
        ).place(x=17, y=268)

        # Login link
        Label(
            self.main_frame,
            text="I have an account",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 9),
        ).place(x=90, y=330)

        Button(
            self.main_frame,
            width=6,
            text="Log in",
            border=0,
            bg="white",
            cursor="hand2",
            fg="red",
            command=self.go_back,
        ).place(x=188, y=326)

        # Side images
        try:
            self.signup_img1 = PhotoImage(file="signup.png")
            Label(
                self, image=self.signup_img1, bg="white", width=450, height=450
            ).place(x=0, y=30)

            self.signup_img2 = PhotoImage(file="signup2.png")
            Label(
                self, image=self.signup_img2, bg="white", width=450, height=450
            ).place(x=900, y=30)
        except:
            pass  # Images are optional

    def toggle_password(self, field):
        """Toggle password visibility"""
        if field == 1:
            if self.password_entry.cget("show") == "*":
                self.password_entry.config(show="")
                self.eye_img1.config(file="openeye.png")
            else:
                self.password_entry.config(show="*")
                self.eye_img1.config(file="closeye2.png")
        else:
            if self.confirm_password_entry.cget("show") == "*":
                self.confirm_password_entry.config(show="")
                self.eye_img2.config(file="openeye.png")
            else:
                self.confirm_password_entry.config(show="*")
                self.eye_img2.config(file="closeye2.png")

    def handle_signup(self):
        """Process signup form"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Validation
        if not username or not password:
            messagebox.showerror("Error!", "You need to type something!")
            return

        if password != confirm_password:
            messagebox.showwarning("Warning", "Passwords don't match. Try again.")
            return

        if len(password) <= 6:
            messagebox.showwarning("Warning", "Password too short. Try again.")
            return

        if AccountManager.username_exists(username):
            messagebox.showerror(
                "Error", f"Username '{username}' already exists. Try again."
            )
            return

        # Create account
        AccountManager.create_account(username, password)
        messagebox.showinfo("Success", "Account has been created!")
        self.go_back()

    def go_back(self):
        """Return to login window"""
        self.destroy()
        self.master.deiconify()

    def on_close(self):
        """Handle window close"""
        self.destroy()
        self.master.destroy()


class BankingAppWindow(CTkToplevel):
    """Main banking application window"""

    def __init__(self, master, username):
        super().__init__(master)
        self.master = master
        self.username = username
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Configure window properties"""
        self.title("Bank")
        self.config(bg="white")
        self.geometry("690x550")
        self.wm_protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        """Create all UI widgets"""
        # Header
        header_frame = Frame(self, padx=20, pady=20)
        header_frame.grid(row=0, column=0, sticky="ew")
        Label(
            header_frame, text="Welcome to Our Banking App", font=("Helvetica", 16)
        ).grid(row=0, column=0, sticky="ew")

        # Main content
        main_frame = Frame(self, padx=20, pady=20)
        main_frame.grid(row=1, column=0, sticky="nsew")

        # Account information
        self.create_account_info(main_frame)

        # Transactions list
        self.create_transactions_list(main_frame)

        # Deposit/Withdraw section
        self.create_deposit_withdraw(main_frame)

        # Send money section
        self.create_send_money(main_frame)

    def create_account_info(self, parent):
        """Create account information section"""
        account_frame = LabelFrame(parent, text="Account Information")
        account_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        Label(
            account_frame, text="Account Holder:", font=("Microsoft YaHei UI Light", 9)
        ).grid(row=0, column=0, sticky="w")

        Label(
            account_frame,
            text=f"{self.username}",
            font=("Microsoft YaHei UI Light", 11, "bold"),
        ).grid(row=0, column=1, sticky="w")

        Label(
            account_frame, text="Account Balance:", font=("Microsoft YaHei UI Light", 9)
        ).grid(row=1, column=0, sticky="w")

        balance = AccountManager.get_balance(self.username)
        self.balance_label = Label(
            account_frame,
            text=f"{balance} DH",
            font=("Microsoft YaHei UI Light", 10, "bold"),
        )
        self.balance_label.grid(row=1, column=1, sticky="w")

    def create_transactions_list(self, parent):
        """Create transactions list section"""
        transactions_frame = LabelFrame(
            parent, text="Recent Transactions", font=("Helvetica", 12), bg="#f0f0f0"
        )
        transactions_frame.grid(
            row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew"
        )

        self.transactions_list = Listbox(transactions_frame, width=40, height=10)
        self.transactions_list.pack(fill="both", expand=True)

    def create_deposit_withdraw(self, parent):
        """Create deposit/withdraw section"""
        frame = LabelFrame(parent, text="Withdraw & Deposit")
        frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        Label(frame, text="Amount:", font=("Microsoft YaHei UI Light", 9)).grid(
            row=0, column=0, sticky="w", pady=5
        )

        self.amount_entry = Entry(
            frame,
            width=20,
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 11, "bold"),
        )
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.amount_entry.insert("end", "0")

        Button(
            frame,
            text="Deposit",
            command=lambda: self.deposit(self.username),
            fg="white",
            bg="blue",
        ).grid(row=1, column=0, padx=5, pady=5)

        Button(
            frame, text="Withdraw", command=self.withdraw, fg="white", bg="blue"
        ).grid(row=1, column=1, padx=5, pady=5)

    def create_send_money(self, parent):
        """Create send money section"""
        frame = LabelFrame(parent, text="Send Money")
        frame.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")

        Label(frame, text="Username:", font=("Microsoft YaHei UI Light", 9)).grid(
            row=0, column=0, sticky="w", pady=5
        )

        self.recipient_entry = Entry(frame)
        self.recipient_entry.grid(row=0, column=1, sticky="ew", pady=5)

        Label(frame, text="Amount:", font=("Microsoft YaHei UI Light", 9)).grid(
            row=1, column=0, sticky="w", pady=5
        )

        self.send_amount_entry = Entry(
            frame, font=("Microsoft YaHei UI Light", 11, "bold")
        )
        self.send_amount_entry.grid(row=1, column=1, sticky="ew", pady=5)
        self.send_amount_entry.insert("end", "0")

        Button(frame, text="Send", command=self.send_money, fg="white", bg="blue").grid(
            row=2, column=1, padx=5
        )

    def update_balance_display(self):
        """Update the balance label"""
        balance = AccountManager.get_balance(self.username)
        self.balance_label.config(text=f"{balance} DH")

    def add_transaction(self, description):
        """Add transaction to list"""
        timestamp = datetime.today().date()
        self.transactions_list.insert("end", f"{description} | {timestamp}")

    def deposit(self, target_username):
        """Handle deposit"""
        try:
            amount = float(self.amount_entry.get())

            if amount <= 0:
                messagebox.showwarning("Warning", "Amount must be positive!")
                return

            current_balance = AccountManager.get_balance(target_username)
            new_balance = current_balance + amount
            AccountManager.update_balance(target_username, new_balance)

            if target_username == self.username:
                self.update_balance_display()
                self.add_transaction(f"+{amount} DH | Total: {new_balance} DH")
            else:
                self.add_transaction(f"+{amount} DH to {target_username}")

        except ValueError:
            messagebox.showwarning("Warning", "Please type a valid number!")

    def withdraw(self):
        """Handle withdrawal"""
        try:
            amount = float(self.amount_entry.get())

            if amount <= 0:
                messagebox.showwarning("Warning", "Amount must be positive!")
                return

            current_balance = AccountManager.get_balance(self.username)

            if amount > current_balance:
                messagebox.showwarning("Warning", "You don't have enough funds!")
                return

            new_balance = current_balance - amount
            AccountManager.update_balance(self.username, new_balance)
            self.update_balance_display()
            self.add_transaction(f"-{amount} DH | Total: {new_balance} DH")

        except ValueError:
            messagebox.showwarning("Warning", "Please type a valid number!")

    def send_money(self):
        """Handle sending money to another user"""
        recipient = self.recipient_entry.get().strip()

        if not recipient:
            messagebox.showwarning("Warning", "Please enter a username!")
            return

        if recipient == self.username:
            messagebox.showwarning("Warning", "You can't send money to yourself!")
            return

        if not AccountManager.username_exists(recipient):
            messagebox.showinfo("Info", f"Username '{recipient}' doesn't exist!")
            return

        try:
            amount = float(self.send_amount_entry.get())

            if amount <= 0:
                messagebox.showwarning("Warning", "Amount must be positive!")
                return

            current_balance = AccountManager.get_balance(self.username)

            if amount > current_balance:
                messagebox.showwarning("Warning", "You don't have enough funds!")
                return

            # Withdraw from sender
            sender_new_balance = current_balance - amount
            AccountManager.update_balance(self.username, sender_new_balance)

            # Deposit to recipient
            recipient_balance = AccountManager.get_balance(recipient)
            recipient_new_balance = recipient_balance + amount
            AccountManager.update_balance(recipient, recipient_new_balance)

            # Update UI
            self.update_balance_display()
            self.add_transaction(f"-{amount} DH sent to {recipient}")

            messagebox.showinfo(
                "Success", f"Successfully sent {amount} DH to {recipient}!"
            )

        except ValueError:
            messagebox.showwarning("Warning", "Please type a valid number!")

    def on_close(self):
        """Handle window close"""
        self.destroy()
        self.master.destroy()


class LoginWindow(CTk):
    """Main login window"""

    def __init__(self):
        super().__init__()
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Configure window properties"""
        self.title("Banking app")
        self.geometry("1400x550")
        self.config(bg="#fff")

    def create_widgets(self):
        """Create all UI widgets"""
        # Main frame
        self.main_frame = LabelFrame(
            self, text="Welcome back!", width=350, height=350, bg="white"
        )
        self.main_frame.place(x=800, y=70)

        # Header
        Label(
            self.main_frame,
            text="Log in",
            fg="gray",
            bg="white",
            font=("Microsoft YaHei UI Light", 23, "bold"),
        ).place(x=115, y=5)

        # Username field
        Label(
            self.main_frame,
            text="Username:",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 9),
        ).place(x=20, y=50)

        self.username_entry = Entry(
            self.main_frame,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11, "bold"),
        )
        self.username_entry.place(x=30, y=80)

        Frame(self.main_frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Password field
        Label(
            self.main_frame,
            text="Password:",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 9),
        ).place(x=20, y=120)

        self.password_entry = Entry(
            self.main_frame,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11, "bold"),
            show="*",
        )
        self.password_entry.place(x=30, y=150)

        # Password toggle button
        self.eye_img = PhotoImage(file="closeye2.png")
        self.eye_btn = Button(
            self.main_frame,
            image=self.eye_img,
            background="white",
            border=0,
            activebackground="white",
            cursor="hand2",
            command=self.toggle_password,
        )
        self.eye_btn.place(x=285, y=145)

        Frame(self.main_frame, width=295, height=2, bg="black").place(x=25, y=177)

        # Login button
        Button(
            self.main_frame,
            width=39,
            pady=7,
            text="Log in",
            bg="blue",
            fg="white",
            border=0,
            command=self.handle_login,
        ).place(x=17, y=204)

        # Sign up link
        Label(
            self.main_frame,
            text="Don't have an account?",
            fg="black",
            bg="white",
            font=("Microsoft YaHei UI Light", 9),
        ).place(x=75, y=270)

        Button(
            self.main_frame,
            width=6,
            text="Sign up",
            border=0,
            bg="white",
            cursor="hand2",
            fg="red",
            command=self.open_register,
        ).place(x=215, y=265)

        # Side image
        try:
            self.login_img = PhotoImage(file="login.png")
            Label(self, image=self.login_img, bg="white", width=550, height=550).place(
                x=60, y=30
            )
        except:
            pass  # Image is optional

    def toggle_password(self):
        """Toggle password visibility"""
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
            self.eye_img.config(file="openeye.png")
        else:
            self.password_entry.config(show="*")
            self.eye_img.config(file="closeye2.png")

    def handle_login(self):
        """Process login form"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error!", "You need to type something!")
            return

        credentials, _ = AccountManager.load_accounts()

        if username not in credentials:
            messagebox.showerror("Error", f"Username '{username}' doesn't exist!")
            return

        if password != credentials[username]:
            messagebox.showwarning("Warning", "Password or username incorrect!")
            return

        # Successful login
        messagebox.showinfo("Login", "Login Completed")
        time.sleep(0.5)
        messagebox.showinfo("Welcome", f"Welcome back {username}")

        # Open banking app
        self.withdraw()
        BankingAppWindow(self, username)

    def open_register(self):
        """Open registration window"""
        self.withdraw()
        RegisterWindow(self)


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
