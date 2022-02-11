import tkinter as tk

class App:
    def __init__(self):
        self.HEIGHT = 200
        self.WIDTH = 400    
        root = tk.Tk()
        root.title('Jokenpo!')
        root.width = self.WIDTH
        root.height = self.HEIGHT
        self.dialogroot = root
        self.strDialogResult = ""    
        self.canvas = tk.Canvas(root, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()    
        frame = tk.Frame(root, bg='#171717')
        frame.place(relx=0.5, rely=0.02, relwidth=0.96, relheight=0.95, anchor='n')  
        # Here is the button call to the InputBox() function
        login_button = tk.Button(frame, text="Login", bg='#cccccc', font=60, 
        command=lambda: self.InputBox())
        createAcc_button = tk.Button(frame, text="Create Account", bg='#cccccc', font=60, 
        command=lambda: self.InputBox())
        login_button.place(relx=0.05, rely=0.1, relwidth=0.90, relheight=0.4)   
        createAcc_button.place(relx=0.05, rely=0.55, relwidth=0.90, relheight=0.4) 
        root.mainloop()

    def InputBox(self):        
        dialog = tk.Toplevel(self.dialogroot)
        dialog.width = 600
        dialog.height = 100

        frame = tk.Frame(dialog,  bg='#171717', bd=5)
        frame.place(relwidth=1, relheight=1)

        username = tk.Entry(frame, font=40)
        username.place(relwidth=0.65, rely=0.02, relheight=0.4)
        password = tk.Entry(frame, font=40)
        password.place(relwidth=0.65, rely=0.5, relheight=0.4)
        username.focus_set()

        submit = tk.Button(frame, text='OK', font=16, command=lambda: self.DialogResult(username.get(), password.get()))
        submit.place(relx=0.7, rely=0.02, relheight=0.88, relwidth=0.3)



        root_name = self.dialogroot.winfo_pathname(self.dialogroot.winfo_id())
        dialog_name = dialog.winfo_pathname(dialog.winfo_id())

        # These two lines show a modal dialog
        self.dialogroot.tk.eval('tk::PlaceWindow {0} widget {1}'.format(dialog_name, root_name))
        self.dialogroot.mainloop()

        #This line destroys the modal dialog after the user exits/accepts it
        dialog.destroy()

        #Print and return the inputbox result
        print(self.strDialogResult)
        return self.strDialogResult

    def DialogResult(self, username, password):
        self.username = username
        self.password = password
        #This line quits from the MODAL STATE but doesn't close or destroy the modal dialog
        self.dialogroot.quit()