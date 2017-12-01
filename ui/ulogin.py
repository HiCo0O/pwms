"""
    Created by 花间物语 2017-12-1
    User Login GUI
"""

from tkinter import Frame,Entry,Button,Checkbutton,Canvas

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

    def pwcheck(self,flag):
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
        username = Entry()
        password = Entry()
        login = Button()
        register = Button()
        forgot = Button()
        icon = Canvas() # or simple pic

        pass


    def __init__(self,master=None):
        Frame.__init__(self,master)
        self['height'] = 400
        self['width'] = 290
        self.pack()