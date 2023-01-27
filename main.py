# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import wx
from login import Login
from ManageAuthor import MngAuthor

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = wx.App(redirect=True)
    #f1 = Login("Login")
    #f2 = MainMenu("Menu thư viện")
    #f1.frame = f2
    f1 = MngAuthor("Quản lý tác giả")
    f1.Show()
    app.MainLoop()



