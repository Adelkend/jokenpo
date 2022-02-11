from logging import root
import sqlite3
import sys
import tkinter as tk

con = sqlite3.connect("accounts.db")
cur = con.cursor()

def create_account(username, password):
    cur.execute(f"INSERT INTO logins VALUES ('{username}', '{password}')")

    con.commit()

def login(username, password):
    for row in cur.execute('SELECT * FROM logins'):
        if str(row) == str((f"('{username}', '{password}')")):
            return "menu"

    return "login"

class App:
    def __init__(self):
        self.HEIGHT = 400
        self.WIDTH = 400    
        root = tk.Tk()
        root.title('Jokenpo!')
        root.width = self.WIDTH
        root.height = self.HEIGHT
        self.dialogroot = root
        self.username = ""
        self.password = "" 
        self.result = "login"
        self.canvas = tk.Canvas(root, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()    
        frame = tk.Frame(root, bg='#171717')
        frame.place(relx=0.5, rely=0.02, relwidth=0.96, relheight=0.95, anchor='n')  
        login_button = tk.Button(frame, text="Login", bg='#cccccc', font=60, 
        command=lambda: self.LoginBox())
        createAcc_button = tk.Button(frame, text="Create Account", bg='#cccccc', font=60, 
        command=lambda: self.CreationBox())
        exit_button = tk.Button(frame, text="Exit", bg='#cccccc', font=60, 
        command=lambda: self.exit())
        login_button.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.3)   
        createAcc_button.place(relx=0.05, rely=0.35, relwidth=0.90, relheight=0.3)
        exit_button.place(relx=0.05, rely=0.65, relwidth=0.90, relheight=0.3)
        root.mainloop()

    def LoginBox(self):        
        dialog = tk.Toplevel(self.dialogroot)
        dialog.width = 600
        dialog.height = 100

        frame = tk.Frame(dialog,  bg='#171717', bd=5)
        frame.place(relwidth=1, relheight=1)

        username = tk.Entry(frame, font=40)
        username.place(relwidth=0.65, rely=0.02, relheight=0.15)
        password = tk.Entry(frame, font=40)
        password.place(relwidth=0.65, rely=0.5, relheight=0.15)
        username.focus_set()

        submit = tk.Button(frame, text='OK', font=16, command=lambda: self.DialogResult(username.get(), password.get()))
        submit.place(relx=0.7, rely=0.02, relheight=0.88, relwidth=0.3)

        self.dialogroot.mainloop()

        #This line destroys the modal dialog after the user exits/accepts it
        dialog.destroy()

        #Return the inputbox result
        self.result = login(self.username, self.password)

    def DialogResult(self, username, password):
        self.username = username
        self.password = password
        #This line quits from the MODAL STATE but doesn't close or destroy the modal dialog
        self.dialogroot.quit()

    def get_result(self):
        self.dialogroot.quit()
        return self.result

    def CreationBox(self):
        dialog = tk.Toplevel(self.dialogroot)
        dialog.width = 600
        dialog.height = 100

        frame = tk.Frame(dialog,  bg='#171717', bd=5)
        frame.place(relwidth=1, relheight=1)

        username = tk.Entry(frame, font=40)
        username.place(relwidth=0.65, rely=0.02, relheight=0.15)
        password = tk.Entry(frame, font=40)
        password.place(relwidth=0.65, rely=0.5, relheight=0.15)
        username.focus_set()

        submit = tk.Button(frame, text='OK', font=16, command=lambda: self.DialogResult(username.get(), password.get()))
        submit.place(relx=0.7, rely=0.02, relheight=0.88, relwidth=0.3)

        self.dialogroot.mainloop()

        #This line destroys the modal dialog after the user exits/accepts it
        dialog.destroy()

        #Return the inputbox result
        self.result = create_account(self.username, self.password)

    def exit(self):
        self.dialogroot.quit()
        sys.exit()