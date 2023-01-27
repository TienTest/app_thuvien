import wx
import bcrypt
import ConfigPara
from userModel import UserModel
from mainmenu import MainMenu

class PnlLogin(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('#008080')

        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.lblError = wx.StaticText(self, -1, '', size=(440, 50))
        lblUserID = wx.StaticText(self, -1, 'User ID:', size=(140, 50))
        self.txtUserID = wx.TextCtrl(self, wx.ID_ANY, size=(300, 50))
        self.txtPassW = wx.TextCtrl(self, wx.ID_ANY, size=(300, 50), style=wx.TE_PASSWORD)
        lblPassW = wx.StaticText(self, -1, 'Password:', size=(140, 50))
        self.btnLogin = wx.Button(self, label="Login", size=(250, 50))

        self.txtPassW.SetFont(font)
        lblPassW.SetFont(font)
        self.txtUserID.SetFont(font)
        self.lblError.SetFont(font)
        lblUserID.SetFont(font)
        self.btnLogin.SetFont(font)
        self.lblError.SetForegroundColour((255, 0, 0))

        layoutUserId = wx.BoxSizer(wx.HORIZONTAL)
        layoutUserId.Add(lblUserID, border=10)
        layoutUserId.Add(self.txtUserID, border=10)
        layoutpass = wx.BoxSizer(wx.HORIZONTAL)
        layoutpass.Add(lblPassW, border=10)
        layoutpass.Add(self.txtPassW, border=10)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add((-1, 30))
        layout.Add(self.lblError, flag=wx.ALIGN_CENTER, border=10)
        layout.Add(layoutUserId, flag=wx.ALIGN_CENTER, border=10)
        layout.Add((-1, 10))
        layout.Add(layoutpass, flag=wx.ALIGN_CENTER, border=10)
        layout.Add((-1, 20))
        layout.Add(self.btnLogin, flag=wx.ALIGN_CENTER, border=10)

        self.SetSizer(layout)


class Login(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(600, 400))
        self.panel = PnlLogin(self)
        self.Bind(wx.EVT_BUTTON, self._OnButtonClick,self.panel.btnLogin)
        self.Show()

    def _OnButtonClick(self, event):
        sqlServer = UserModel()
        strHashedpassW = ""
        strUserId = self.panel.txtUserID.GetValue()
        strPassW = self.panel.txtPassW.GetValue()
        conn = sqlServer.connect2SqlServer()
        strHashedpassW, iRole = sqlServer.getUserPassW(conn, strUserId)
        sqlServer.closeSqlServerConnection(conn)
        strPassW = strPassW.encode('utf-8')
        strHashedpassW = strHashedpassW.encode('utf-8')
        if len(strHashedpassW) > 0 and bcrypt.checkpw(strPassW, bytes(strHashedpassW)):
            ConfigPara.glbUserId = strUserId
            ConfigPara.glbUserRole = iRole
            f2 = MainMenu("Main Menu")
            f2.Show()
            self.Hide()
        else:
            self.panel.lblError.SetLabelText('UserID or Password is Wrong!')
        # ----------------------------------------------------------------------



