import wx
import wx.adv
import wx.grid
from Model.AuthorModel import AuthorModel
import datetime
import ConfigPara

class PnlMngAuthor(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('#008080')
        arrNationality = ('Viet Nam', 'Nhat', 'My', 'Anh', 'Phap')
        self.font = wx.Font(14, wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial")
        staticBox = wx.StaticBox(self, -1, "Tìm kiếm tác giả:")
        staticBox.SetFont(self.font)
        searchBox = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        lblAuthorName = wx.StaticText(self, -1, 'Tên tác giả:', size=(140, 30))
        lblAuthorName.SetFont(self.font)
        self.txtAuthorName = wx.TextCtrl(self, wx.ID_ANY, size=(300, 30))
        self.txtAuthorName.SetFont(self.font)
        layoutAuthorName = wx.BoxSizer(wx.HORIZONTAL)
        layoutAuthorName.Add(lblAuthorName)
        layoutAuthorName.Add(self.txtAuthorName)
        lblBirthdayF = wx.StaticText(self, -1, 'Ngày sinh từ:', size=(140, 30))
        lblBirthdayT = wx.StaticText(self, -1, 'Ngày sinh đến:', size=(140, 30))
        lblBirthdayF.SetFont(self.font)
        lblBirthdayT.SetFont(self.font)
        self.dtmBirthdayF = wx.adv.DatePickerCtrl(self, wx.ID_ANY, style=wx.adv.DP_DROPDOWN)
        self.dtmBirthdayT = wx.adv.DatePickerCtrl(self, wx.ID_ANY, style=wx.adv.DP_DROPDOWN)
        self.dtmBirthdayF.SetFont(self.font)
        self.dtmBirthdayT.SetFont(self.font)
        lblNation = wx.StaticText(self, -1, 'Quốc tịch:', size=(140, 30))
        lblNation.SetFont(self.font)
        self.cmbNation = wx.ComboBox(self, wx.ID_ANY, '',
                                     choices=arrNationality, style=wx.CB_DROPDOWN)
        self.cmbNation.SetFont(self.font)
        self.btnSearch = wx.Button(self, label="Tìm kiếm", size=(120, 30))
        self.btnSearch.SetFont(self.font)
        layoutNational = wx.BoxSizer(wx.HORIZONTAL)
        layoutNational.Add(lblNation)
        layoutNational.Add(self.cmbNation)
        layoutBirthday = wx.BoxSizer(wx.HORIZONTAL)
        layoutBirthday.Add(lblBirthdayF)
        layoutBirthday.Add(self.dtmBirthdayF)
        layoutBirthday.Add(5, -1)
        layoutBirthday.Add(lblBirthdayT)
        layoutBirthday.Add(self.dtmBirthdayT)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutAuthorName)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutBirthday)
        searchBox.Add(-1, 10)
        searchBox.Add(layoutNational)
        searchBox.Add(-1, 10)
        searchBox.Add(self.btnSearch, flag=wx.ALIGN_RIGHT)
        searchBox.Add(-1, 10)
        layoutSearch = wx.BoxSizer(wx.VERTICAL)
        layoutSearch.Add(searchBox)

        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(15, 3)
        self.grid.SetFont(self.font)

        # Set column labels.
        self.grid.SetColLabelValue(0, "Tên tác giả")
        self.grid.SetColSize(0, 300)
        self.grid.SetColLabelValue(1, "Ngày sinh")
        self.grid.SetColSize(1, 120)
        self.grid.SetColLabelValue(2, "Quốc tịch")
        self.grid.SetColSize(2, 280)
        self.grid.SetLabelFont(self.font)

        #Set cell values.
        author = AuthorModel()
        rows = author.getAuthorList()
        count = 0
        for r in rows:
            self.grid.SetCellValue(count, 0 , r[1])
            self.grid.SetCellValue(count, 1, r[2])
            self.grid.SetCellValue(count, 2, r[3])
            attr = wx.grid.GridCellAttr()
            attr.SetFont(self.font)
            self.grid.SetRowAttr(count, attr)
            self.grid.SetRowSize(count, 30)
            count = count + 1

        #author.closeSqlServerConnection()

        layoutList = wx.BoxSizer(wx.VERTICAL)
        layoutList.Add(self.grid)

        mainLayout = wx.BoxSizer(wx.VERTICAL)
        mainLayout.Add(-1, 10)
        mainLayout.Add(layoutSearch)
        mainLayout.Add(layoutList)
        self.SetSizer(mainLayout)

class MngAuthor(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
        self.panel = PnlMngAuthor(self)
        self.Bind(wx.EVT_BUTTON, self._OnButtonClick, self.panel.btnSearch)
        self.Show()

    def _OnButtonClick(self, event):
        author = AuthorModel()
        strAuthorName = self.panel.txtAuthorName.GetValue()
        strBirthdayF = self.panel.dtmBirthdayF.GetValue().Format('%Y-%m-%d')
        strBirthdayT = self.panel.dtmBirthdayT.GetValue().Format('%Y-%m-%d')
        strCountryname = self.panel.cmbNation.GetValue()
        whereString = " WHERE 1 = 1 "
        if len(strAuthorName) > 0:
            whereString += "AND a.name LIKE '%" + strAuthorName + "%' "
        if len(strBirthdayF) > 0:
            whereString += "AND a.birthday >= '" + strBirthdayF + "' "
        if len(strBirthdayT) > 0:
            whereString += "AND a.birthday <= '" + strBirthdayT + "' "
        if len(strCountryname) > 0:
            whereString += "AND a.nationality = '" + strCountryname + "' "

        rows = author.searchAuthor(whereString)
        count = 0
        self.panel.grid.ClearGrid()
        for r in rows:
            self.panel.grid.SetCellValue(count, 0, r[1])
            self.panel.grid.SetCellValue(count, 1, r[2])
            self.panel.grid.SetCellValue(count, 2, r[3])
            attr = wx.grid.GridCellAttr()
            attr.SetFont(self.panel.font)
            self.panel.grid.SetRowAttr(count, attr)
            self.panel.grid.SetRowSize(count, 30)
            count = count + 1
