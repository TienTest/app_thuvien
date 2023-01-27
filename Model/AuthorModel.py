import pyodbc

class AuthorModel:
    strConnect = "Server=localhost\MSSQLSERVER03;Database=manage_library;Trusted_Connection=True;PORT=1433;DRIVER={SQL Server}"

    def __init__(self):
        self.Connection = pyodbc.connect(self.strConnect)

    def getAuthorList(self):
        cursor = self.Connection.cursor()
        cursor.execute("select a.author, a.name, a.birthday, a.nationality from author as a ")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def searchAuthor(self, whereString ):
        cursor = self.Connection.cursor()
        cursor.execute("select a.author, a.name, a.birthday, a.nationality from author as a " + whereString )
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def closeSqlServerConnection(self):
        self.Connection.close()
