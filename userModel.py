import pyodbc

class UserModel:
    strConnect = "Server=localhost\MSSQLSERVER03;Database=manage_library;Trusted_Connection=True;PORT=1433;DRIVER={SQL Server}"

    def connect2SqlServer(self):
        conn = pyodbc.connect(self.strConnect)
        return conn

    def getUserPassW(self, conn, userId):
        strhashPass = ""
        cursor = conn.cursor()
        cursor.execute("select a.password, a.role from mst_user as a where a.user_id ='" + userId + "'")
        rows = cursor.fetchall()
        for r in rows:
            strhashPass = r[0]
            iRole = r[1]
        cursor.close()
        return strhashPass, iRole

    def closeSqlServerConnection(self, conn):
        conn.close()
