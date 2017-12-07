"""
    Created by 花间物语 2017-12-1
    User Login GUI
"""

from tkinter import Frame, Entry, Button, Checkbutton, Canvas, Label,Toplevel,StringVar,W
from tkinter import LEFT,RIGHT,CENTER

class Ulogin(Frame):
    def logincheck(self):
        '''
        Login Checkout
        Bind with login button.If the user click login button it will
        check Username Entry and Password Entry is null or exist in db.
        If Entry is null: notices input info
        If not exists in db: notices error info
        If exists in db: open the main window
        :return:
        '''
        pass

    def usercheck(self):
        """
        Username Chekcout
        Find username in db.
        Exist:return True
        Null:return False
        """
        pass

    def pwcheck(self, flag):
        """
        Password Checkout
        :return:
        """
        pass

    def forgotpw(self):
        """
        Forgot password
        :return:
        """
        pass

    def reguser(self):
        """
        register user
        :return:
        """
        pass



    def createWidget(self):
        username = StringVar()
        username.set("输入账户")
        password = StringVar()
        password.set("输入密码")

        self.iconframe = Frame(self,height=200)
        self.iconframe.pack()

        self.usernameEntry = Entry(self, textvariable=username, width=25, justify='center')
        self.usernameEntry.pack(anchor=CENTER, pady=5, ipady=5)

        self.passwordEntry = Entry(self, textvariable=password, width=25, justify='center', show="*")
        self.passwordEntry.pack(anchor=CENTER, pady=5, ipady=5)

        self.remeberlabel=Label(self,text="记住密码")
        self.remeberlabel.pack(side=LEFT)

        self.autolabel = Label(self, text="自动登录")
        self.autolabel.pack(side=LEFT)

        self.loginbutton = Button(self,text="登录")
        self.loginbutton.pack(side=LEFT,ipadx=5)

        self.forgotbutton = Button(self,text="忘记密码")
        self.forgotbutton.pack(padx=8,ipadx=5,side=LEFT)

        self.registerbutton = Button(self,text="注册")
        self.registerbutton.pack(ipadx=5,side=LEFT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidget()
        self["height"] = 385
        self["width"] = 175
        self.pack_propagate(False)
        self.pack(padx=50)
