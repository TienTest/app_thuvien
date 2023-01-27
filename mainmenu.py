import wx
import ConfigPara

class PnlMenu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('#008080')
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")
        lblLibTitle = wx.StaticText(self, -1 , 'Thư Viện Giản Đơn')
        lblLibTitle.SetFont(font)
        lblLibTitle.SetForegroundColour("#192f60")
        lblLibTitle.SetBackgroundColour("#ffffff")
        btnFont = wx.Font(22, wx.FONTFAMILY_DEFAULT,
                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")
        btnBookMng = wx.Button(self, wx.ID_ANY, 'Quản lý sách',size=(290, 60))
        btnBookMng.SetFont(btnFont)
        btnAuthMng = wx.Button(self, wx.ID_ANY, 'Quản lý tác giả', size=(290, 60))
        btnAuthMng.SetFont(btnFont)
        btnReaderMng = wx.Button(self, wx.ID_ANY, 'Quản lý đọc giả', size=(290, 60))
        btnReaderMng.SetFont(btnFont)
        btnTTMng = wx.Button(self, wx.ID_ANY, 'Quản lý thủ thư', size=(290, 60))
        btnTTMng.SetFont(btnFont)
        btnBrwBookMng = wx.Button(self, wx.ID_ANY, 'Quản lý mượn sách', size=(290, 60))
        btnBrwBookMng.SetFont(btnFont)
        btnLayout = wx.GridSizer(rows=1, cols=3, gap=(0, 0))
        btnLayout.Add(btnBookMng)
        btnLayout.Add(btnAuthMng)
        btnLayout.Add(btnReaderMng)
        btnLayout2 = wx.GridSizer(rows=1, cols=2, gap=(0, 0))
        btnLayout2.Add(btnBrwBookMng)
        btnLayout2.Add(btnTTMng)
        if ConfigPara.glbUserRole == 0:
            btnTTMng.Hide()

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(-1, 10)
        layout.Add(lblLibTitle, flag = wx.ALIGN_CENTER, border = 10)
        layout.Add(-1, 10)
        layout.Add(btnLayout, flag=wx.ALIGN_CENTER, border=10)
        layout.Add(-1, 5)
        layout.Add(btnLayout2, flag=wx.ALIGN_CENTER, border=10)
        self.SetSizer(layout)

class MainMenu(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(900,300))
        self.panel = PnlMenu(self)
        self.Show()


