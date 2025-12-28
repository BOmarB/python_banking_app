import fileinput
import random
import re
import time
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from re import *


class Register(Toplevel):
    s = []
    u = []
    p = []
    c = []

    def __init__(self, master, p=None, a=None, g=None, n=None):
        super().__init__(master)
        self._sold = 0
        self._Nom = n
        # self._Age = a
        # self._Gender = g
        # self._Prenom = p
        # self._Cin = random.randrange(10000, 99999)
        # self.U_D = []
        w = self
        # Title, size
        w.title("Banking app")
        w.geometry('1400x550')
        w.config(bg="#fff")

        # Create some widgets
        w.fram = LabelFrame(w,
                            text="Welcome!",
                            width=350,
                            height=400,
                            bg="white", )
        w.fram.place(x=500, y=70)
        w.Frame1 = Frame(w.fram,
                         width=295,
                         height=2,
                         bg='black')
        w.Frame1.place(x=25, y=107)
        w.Frame2 = Frame(w.fram,
                         width=295,
                         height=2,
                         bg='black')
        w.Frame2.place(x=25, y=177)
        w.Frame3 = Frame(w.fram,
                         width=295,
                         height=2,
                         bg='black')
        w.Frame3.place(x=25, y=247)

        # btn labels
        w.heading = Label(w.fram,
                          text="Sign up",
                          fg="black",
                          bg='white',
                          font=("Microsoft YaHei UI Light", 23, 'bold'))
        w.heading.place(x=115, y=5)

        self.User = Entry(w.fram,
                          width=25,
                          fg='black',
                          border=0,
                          bg='white',
                          font=("Microsoft YaHei UI Light", 11, 'bold'))
        self.User.place(x=30, y=80)

        self.labelU = Label(w.fram,
                            text="Username :",
                            fg='black',
                            bg='white',
                            font=("Microsoft YaHei UI Light", 9))
        self.labelU.place(x=20, y=50)

        self.code = Entry(w.fram,
                          width=25,
                          fg='black',
                          border=0,
                          bg='white',
                          font=("Microsoft YaHei UI Light", 11, 'bold'),
                          show='*')
        self.code.place(x=30, y=150)

        self.o_img = PhotoImage(file="closeye2.png")
        self.o_img2 = PhotoImage(file="closeye2.png")
        self.opeyebtn1 = Button(w.fram,
                                image=self.o_img,
                                background='white',
                                border=0,
                                activebackground='white',
                                cursor='hand2',
                                command=self.show)
        self.opeyebtn1.place(x=285, y=145)

        self.labelU = Label(w.fram,
                            text="Password :",
                            fg='black',
                            bg='white',
                            font=("Microsoft YaHei UI Light", 9))
        self.labelU.place(x=20, y=120)

        self.code2 = Entry(w.fram,
                           width=25,
                           fg='black',
                           border=0,
                           bg='white',
                           font=("Microsoft YaHei UI Light", 11, 'bold'),
                           show='*')
        self.code2.place(x=30, y=220)

        self.opeyebtn2 = Button(w.fram,
                                image=self.o_img2,
                                background='white',
                                border=0,
                                activebackground='white',
                                cursor='hand2',
                                command=self.show2)
        self.opeyebtn2.place(x=285, y=215)

        self.labelU = Label(w.fram,
                            text="Confirm Password :",
                            fg='black',
                            bg='white',
                            font=("Microsoft YaHei UI Light", 9))
        self.labelU.place(x=20, y=190)

        self.label1 = Label(w.fram,
                            text="I have an account",
                            fg='black',
                            bg='white',
                            font=("Microsoft YaHei UI Light", 9))
        self.label1.place(x=90, y=330)

        self.sign_up = Button(w.fram,
                              width=6,
                              text='Log in',
                              border=0,
                              bg='white',
                              cursor='hand2',
                              fg="red",
                              command=self.go_back)
        self.sign_up.place(x=188, y=326)

        self.wm_protocol("WM_DELETE_WINDOW", self.on_close)

        # img
        w.img = PhotoImage(file='signup.png')
        w.lb_img = Label(w, image=w.img,
                         bg="white",
                         width=450,
                         height=450)
        w.lb_img.place(x=0, y=30)

        w.img2 = PhotoImage(file='signup2.png')
        w.lb_img2 = Label(w, image=w.img2,
                          bg="white",
                          width=450,
                          height=450)
        w.lb_img2.place(x=900, y=30)

        w.btn_s = Button(w.fram,
                         width=39,
                         pady=7,
                         text="Sign up",
                         bg='blue',
                         fg='white',
                         border=0,
                         command=lambda: h())
        w.btn_s.place(x=17, y=268)

        def h():
            # print(w.User.get())
            # print(w.code.get())
            o = open('Accounts.txt', 'r')
            self._Nom = self.User.get()
            password = self.code.get()
            password1 = self.code2.get()
            if password == "" or self._Nom == "":
                messagebox.showerror('Error !', 'You need to type somthing !')
            else:
                for i in o:
                    us, pa, so = i.split(", ")
                    pa = pa.strip()
                    # ci = ci.strip()
                    so = so.strip()
                    Register.u.append(us)
                    Register.p.append(pa)
                    # Register.c.append(ci)
                    Register.s.append(so)
                data = dict(zip(Register.u, Register.p))
                # data2 = dict()
                # print(data)
                # print(data2)
                # print(Register.c)
                # print(Register.s)
                if password != password1:
                    messagebox.showwarning('Warning', "Passwords don't match, Try again")
                else:
                    if len(str(password)) <= 6:
                        messagebox.showwarning('Warning', "Password too short, Try again")
                    elif self._Nom in data:
                        messagebox.showerror('Error', f"This Username : '{self._Nom}' exist, Try again")
                    else:
                        o = open('Accounts.txt', 'a')
                        o.write(f"{self._Nom}, {password}, {self._sold}\n")
                        messagebox.showinfo('Login', "Account has been created!")

    def hide(self):
        self.o_img.config(file="closeye2.png")
        self.code.config(show="*")
        self.opeyebtn1.config(command=self.show)

    def hide2(self):
        self.o_img2.config(file="closeye2.png")
        self.code2.config(show="*")
        self.opeyebtn2.config(command=self.show2)

    def show2(self):
        self.o_img2.config(file="openeye.png")
        self.code2.config(show='')
        self.opeyebtn2.config(command=self.hide2)

    def show(self):
        self.o_img.config(file="openeye.png")
        self.code.config(show='')
        self.opeyebtn1.config(command=self.hide)

    def go_back(self):
        self.destroy()  # destroy only current window
        self.master.deiconify()  # show again main window

    def on_close(self):
        self.destroy()  # destroy current window
        self.master.destroy()  # destroy main window

    def app(self):
        # open('Accounts.txt', 'r')
        data2 = dict(zip(Register.u, Register.s))
        # print(data2[self._Nom])
        # Create the application window
        app = CTkToplevel(self)
        app.wm_protocol("WM_DELETE_WINDOW", lambda: on_close2())

        def on_close2():
            app.destroy()  # destroy current window
            self.destroy()  # destroy main window

        app.title("Bank")
        app.config(bg="white")
        app.geometry('690x550')

        # Create the main frame
        app.header_frame = Frame(app, padx=20, pady=20)
        app.header_frame.grid(row=0, column=0, sticky="ew")
        header_label = Label(app.header_frame, text="Welcome to Our Banking App", font=("Helvetica", 16))
        header_label.grid(row=0, column=0, sticky="ew")

        # Main content
        app.main_frame = Frame(app, padx=20, pady=20)
        app.main_frame.grid(row=1, column=0, sticky="nsew")

        # Account info
        app.account_frame = LabelFrame(app.main_frame, text="Account Information")
        app.account_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        Label(app.account_frame, text="Account Holder:", font=("Microsoft YaHei UI Light", 9)).grid(row=0, column=0, sticky="w")
        Label(app.account_frame, text=f"{self._Nom}", font=("Microsoft YaHei UI Light", 11, "bold")).grid(row=0, column=1, sticky="w")
        Label(app.account_frame, text="Account Balance:", font=("Microsoft YaHei UI Light", 9)).grid(row=1, column=0, sticky="w")
        app.l1 = Label(app.account_frame, text=f"{data2[self._Nom]} DH", font=("Microsoft YaHei UI Light", 10, "bold"))
        app.l1.grid(row=1, column=1, sticky="w")

        # Transactions
        transactions_frame = LabelFrame(app.main_frame, text="Recent Transactions", font=("Helvetica", 12), bg="#f0f0f0")
        transactions_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")
        app.transactions_list = Listbox(transactions_frame, width=40, height=10)
        app.transactions_list.pack(fill="both", expand=True)

        # add&take_frame
        app.add_take_frame = LabelFrame(app.main_frame, text="Withdraw & deposit")
        app.add_take_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Create an entry for adding money
        app.adde_label = Label(app.add_take_frame, text="Amount:", font=("Microsoft YaHei UI Light", 9))
        app.adde_label.grid(row=0, column=0, sticky="w", pady=5)
        app.add1 = Entry(app.add_take_frame, width=20, fg='black', bg='white',
                         font=("Microsoft YaHei UI Light", 11, 'bold'))
        app.add1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        app.add1.insert('end', '0')

        # Buttons for actions

        action_buttons_frame = Frame(app.add_take_frame, height=55)
        action_buttons_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        Button(app.add_take_frame, text="Deposit", command=lambda: deposit(self._Nom, app.add1.get()), fg="white", bg="blue").grid(row=1, column=0, padx=5, pady=5)
        Button(app.add_take_frame, text="Withdraw", command=lambda: withdraw(app.add1.get()), fg="white", bg="blue").grid(row=1, column=1, padx=5, pady=5)

        # send frame
        app.send_frame = LabelFrame(app.main_frame, text="Send money")
        app.send_frame.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")

        # user entry
        app.user_label = Label(app.send_frame, text="Username:", font=("Microsoft YaHei UI Light", 9))
        app.user_label.grid(row=4, column=0, sticky="w", pady=5)
        app.user_entry = Entry(app.send_frame)
        app.user_entry.grid(row=4, column=1, sticky="ew", pady=5)

        # Amount entry
        app.amount_label = Label(app.send_frame, text="Amount:", font=("Microsoft YaHei UI Light", 9))
        app.amount_label.grid(row=5, column=0, sticky="w", pady=5)
        app.amount_entry = Entry(app.send_frame, font=("Microsoft YaHei UI Light", 11, 'bold'))
        app.amount_entry.grid(row=5, column=1, sticky="ew", pady=5)
        app.amount_entry.insert('end', '0')

        # send button
        app.deposit_button = Button(app.send_frame, text="Send", command=lambda: send((app.user_entry.get())), fg="white", bg="blue")
        app.deposit_button.grid(row=6, column=1, padx=5)

        def send(username):
            if username in data2 :
                if username != self._Nom:
                    with open('Accounts.txt', 'r+') as data:
                        accounts = data.readlines()
                    for line in accounts:
                        splitlines = line.split(', ')
                        if self._Nom in splitlines:
                            break
                    if float(app.amount_entry.get()) <= float(splitlines[2]):

                        deposit(app.user_entry.get(), app.amount_entry.get())
                    withdraw(app.amount_entry.get())
                else:
                    messagebox.showwarning('Warning', "You can't send to your self :(")
            else:
                messagebox.showinfo('info', f"{username} doesn't exist ! ")

        def withdraw(amount):
            with open('Accounts.txt', 'r+') as data:
                accounts = data.readlines()
            for line in accounts:
                splitlines = line.split(', ')
                if self._Nom in splitlines:
                    main = line
                    break
            try:
                if float(amount) >= 0:
                    n = float(splitlines[2])
                    if float(amount) <= n:
                        newsold = n - float(amount)
                        app.l1.config(text=f"{float(newsold)} DH")
                        main2 = main
                        main2 = main2.split(', ')
                        main2 = main2[:2] + [str(newsold)]
                        main2 = ', '.join(main2)

                        with open('Accounts.txt', 'r') as file:
                            filedata = file.read()

                        filedata = filedata.replace(main, main2+"\n")

                        with open('Accounts.txt', 'w') as file:
                            file.write(filedata)
                        if float(amount) == 0:
                            pass
                        else:
                            app.transactions_list.insert('end',
                                                         f"-{float(amount)} DH | Total : {float(newsold)} DH | {datetime.today().date()}")
                    else:
                        messagebox.showwarning('warning', "You don't have enough !")
                else:
                    messagebox.showwarning('warning', 'The amount needs to be positif !')
            except ValueError:
                messagebox.showwarning('Warning', 'Please type a number !')

        def deposit(username, amount):
            with open('Accounts.txt', 'r+') as data:
                accounts = data.readlines()
            for line in accounts:
                splitlines = line.split(', ')
                if username in splitlines:
                    main = line
                    break
            try:
                n = float(splitlines[2])
                newsold = n + float(amount)
                if username == self._Nom:
                    app.l1.config(text=f"{float(newsold)} DH")
                # print(data2[self._Nom])
                # if username == self._Nom or float(amount) < float(data2[self._Nom]):
                print(data2[self._Nom])
                print("h")
                main2 = main
                main2 = main2.split(', ')
                main2 = main2[:2] + [str(newsold)]
                main2 = ', '.join(main2)

                with open('Accounts.txt', 'r') as file:
                    filedata = file.read()

                filedata = filedata.replace(main, main2 + "\n")

                with open('Accounts.txt', 'w') as file:
                    file.write(filedata)
                if float(amount) == 0:
                    pass
                else:
                    if username != self._Nom:
                        app.transactions_list.insert('end',
                                                     f"+{float(amount)} DH to {username} | {datetime.today().date()}")
                    else:
                        app.transactions_list.insert('end',
                                                     f"+{float(amount)} DH | Total : {float(newsold)} DH | {datetime.today().date()}")
                # print(data2[self._Nom])
            except ValueError:
                messagebox.showwarning('Warning', 'Please type a number !')

        # Button(app,
        #        width=39,
        #        pady=7,
        #        text="Add money",
        #        bg='blue',
        #        fg='white',
        #        border=0
        #        # ,command=add
        #        ).place(x=750, y=250)
        # Button(app,
        #        width=39,
        #        pady=7,
        #        text="Take money",
        #        bg='blue',
        #        fg='white',
        #        border=0,
        #        # command=take
        #        ).place(x=150, y=180)


class Utilisateur(CTk, Register):
    # file = 'All.txt'
    def __init__(self):
        super().__init__()

        # Title, size
        self.title("Banking app")
        self.geometry('1400x550')
        self.config(bg="#fff")
        # Create some widgets
        # self.my_label = CTkLabel(self,
        # text="Username",
        # text_color="white").place(relx=0.5,
        #                           rely=0.5,
        #                           anchor='center')
        # frame
        self.fram = LabelFrame(self,
                               text="Welcome back!",
                               width=350,
                               height=350,
                               bg="white", )
        self.fram.place(x=800, y=70)
        self.Frame1 = Frame(self.fram,
                            width=295,
                            height=2,
                            bg='black')
        self.Frame1.place(x=25, y=107)
        self.Frame2 = Frame(self.fram,
                            width=295,
                            height=2,
                            bg='black')
        self.Frame2.place(x=25, y=177)
        # btn labels
        self.heading = Label(self.fram,
                             text="Log in",
                             fg="gray",
                             bg='white',
                             font=("Microsoft YaHei UI Light", 23, 'bold'))
        self.heading.place(x=115, y=5)

        self.User = Entry(self.fram,
                          width=25,
                          fg='black',
                          border=0,
                          bg='white',
                          font=("Microsoft YaHei UI Light", 11, 'bold'))
        self.User.place(x=30, y=80)
        self.labelU = Label(self.fram,
                            text="Username :",
                            fg='black',
                            bg='white',
                            font=("Microsoft YaHei UI Light", 9))
        self.labelU.place(x=20, y=50)

        self.code = Entry(self.fram,
                          width=25,
                          fg='black',
                          border=0,
                          bg='white',
                          font=("Microsoft YaHei UI Light", 11, 'bold'),
                          show="*")
        self.code.place(x=30, y=150)
        self.o_img3 = PhotoImage(file="closeye2.png")
        self.opeyebtn3 = Button(self.fram,
                                image=self.o_img3,
                                background='white',
                                border=0,
                                activebackground='white',
                                cursor='hand2',
                                command=self.show3,
                                )
        self.opeyebtn3.place(x=285, y=145)
        self.labelU = Label(self.fram,
                            text="Password :",
                            fg='black',
                            bg='white',
                            font=("Microsoft YaHei UI Light", 9))
        self.labelU.place(x=20, y=120)
        self.btn_s = Button(self.fram,
                            width=39,
                            pady=7,
                            text="Log in ",
                            bg='blue',
                            fg='white',
                            border=0,
                            command=self.access)
        self.btn_s.place(x=17, y=204)

        self.label1 = Label(self.fram,
                            text="Don't have an account ?",
                            fg='black',
                            bg='white',
                            font=("Microsoft YaHei UI Light", 9))
        self.label1.place(x=75, y=270)
        self.sign_up = Button(self.fram,
                              width=6,
                              text='Sign up',
                              border=0,
                              bg='white',
                              cursor='hand2',
                              fg="red",
                              command=self.d)
        self.sign_up.place(x=215, y=265)
        # img
        # self.img2 = PhotoImage(file='bank.png')
        # self.iconphoto(True, self.img2)
        self.img = PhotoImage(file='login.png')
        self.lb_img = Label(self, image=self.img,
                            bg="white",
                            width=550,
                            height=550)
        self.lb_img.place(x=60, y=30)
        # self.User.insert(0, 'username')
        # self.User.bind('<FocusIn>', self.on_entre)
        # self.User.bind('<FocusOut>', self.on_leave)
        # self.my_button = CTkButton(self, text="Login",
        #                            corner_radius=32,
        #                            fg_color='#0000FF',
        #                            hover_color="#FF0000",).place(relx=0.5,
        #                                                          rely=0.5,
        #                                                          anchor='center')
        # self.my_button2 = CTkButton(self, text="Register",
        #                             corner_radius=32,
        #                             fg_color='#0000FF',
        #                             hover_color="#FF0000", command=self.register).place(relx=0.5,
        #                                                                                 rely=0.45,
        #                                                                                 anchor='center')

    # with open(file, 'w') as file:
    #     write = file.writelines()

    # def on_entre(self):
    #     self.User.delete(0, 'end')
    #
    # def on_leave(self):
    #     name = self.User.get()
    #     if name == '':
    #         self.User.insert(0, 'username')

    def d(self):
        self.withdraw()
        self.app = Register(self)  # send main window as argument

    def access(self):
        o = open('Accounts.txt', 'r')
        self._Nom = self.User.get()
        password = self.code.get()
        if len(self._Nom or password) < 1:
            messagebox.showerror('Error !', 'You need to type somthing !')
        else:
            for i in o:
                us, pa, so = i.split(", ")
                pa = pa.strip()
                # ci = ci.strip()
                so = so.strip()
                Register.u.append(us)
                Register.p.append(pa)
                # Register.c.append(ci)
                Register.s.append(so)

            data = dict(zip(Register.u, Register.p))
            data2 = dict(zip(Register.u, Register.s))
            # print(data)
            print(data2)
            if self._Nom in data:
                if password == data[self._Nom]:
                    print(self._Nom)
                    print(data[self._Nom])
                    messagebox.showinfo('Login', 'Login Completed')
                    time.sleep(0.5)
                    messagebox.showinfo('Welcome', f"Welcome back {self._Nom}")
                    time.sleep(0.5)
                    self.withdraw()
                    Register.app(self)
                else:
                    messagebox.showwarning('Warning', '"Password or username incorrect !"')
            else:
                messagebox.showerror('Error', f"This Username : '{self._Nom}' doesn't exist")

    def hide3(self):
        self.o_img3.config(file="closeye2.png")
        self.code.config(show="*")
        self.opeyebtn3.config(command=self.show3)

    def show3(self):
        self.o_img3.config(file="openeye.png")
        self.code.config(show='')
        self.opeyebtn3.config(command=self.hide3)

    # def __repr__(self):
    #     return f"\n|{self._Nom} | {self._Prenom} | {self._Age} | {self._Gender} | {self._Cin} | "

    # def register(self, **kwargs):
    #     o = open('Accounts.txt', 'r')
    #     self._Nom = self.User.get()
    #     password = self.code.get()
    #     password1 = self.code2.get()
    #     c = []
    #     s = []
    #     for i in o:
    #         us, pa, ci, so = i.split(", ")
    #         pa = pa.strip()
    #         ci = ci.strip()
    #         so = so.strip()
    #         Utilisateur.u.append(us)
    #         Utilisateur.p.append(pa)
    #         c.append(ci)
    #         s.append(so)
    #     data = dict(zip(Utilisateur.u, Utilisateur.p))
    #     # data2 = dict()
    #     print(data)
    #     # print(data2)
    #     print(c)
    #     print(s)
    #     if password != password1:
    #         print("Passwords don't match, Try again")
    #         self.register()
    #     else:
    #         if password == "" or self._Nom == "":
    #             print("You need to type something !")
    #             self.register()
    #         if len(password) <= 6:
    #             print("Password too short, Try again")
    #             self.register()
    #         elif self._Nom in data:
    #             print("User name exists, Try again")
    #             self.register()
    #         else:
    #             o = open('Accounts.txt', 'a')
    #             o.write(f"{self._Nom}, {password}, {self._Cin}, {self._sold}\n")
    #             print("Account has been created!")

    # def show_details(self):
    #     info = ""
    #     info += "Personal Details\n"
    #     info += f"Nom : {self._Nom}\n"
    #     info += f"Prenom : {self._Prenom}\n"
    #     info += f"Age : {self._Age}\n"
    #     info += f"Gender : {self._Gender}\n"
    #     info += f"Cin : {self._Cin}\n"
    #     return info

if __name__ == "__main__":
    app = Utilisateur()
    app.mainloop()

