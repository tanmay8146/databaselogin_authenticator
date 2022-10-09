import mysql.connector as msql

class Login:
    def __init__(self, host, AccessUser, AccessPass, database, loginTable, userName, userPass):
        self.host = host                    #Hostname of mySQL Server
        self.AccessUser = AccessUser        #Database User Account
        self.AccessPass = AccessPass        #Database User Password
        self.database = database            #Database Name
        self.loginTable = loginTable        #Login credentials table
        self.userName = userName            #Login Username
        self.userPass = userPass            #Login Password

    def loginAuthentication(self):
        conn = msql.connect(host=self.host, username=self.AccessUser, password=self.AccessPass, database=self.database)
        cursor = conn.cursor()

        loginQuery = ('select * from {table} where username= %s and password= %s').format(table=self.loginTable)
        loginData = (self.userName, self.userPass)

        cursor.execute(loginQuery, loginData)

        authenticator = cursor.fetchall()

        if authenticator:
            print("LOGIN SUCCESSFULL!")
        else:
            print("LOGIN FAILED!")

if __name__ == "__main__":
    print("Login module...")
    dbHost = input("Enter host name: ")
    dbUsername = input("Enter Database username: ")
    dbPassword = input("Enter Database password: ")
    dbName = input("Enter Database name: ")
    checkerTable = input("Enter Login Data Table Name: ")
    userAuth = input("Enter login username: ")
    passAuth = input("Enter login password: ")

    loginInformation = Login(host=dbHost, AccessUser=dbUsername, AccessPass=dbPassword, database=dbName, userName=userAuth, userPass=passAuth, loginTable=checkerTable)

    checkLoging = Login.loginAuthentication(loginInformation)