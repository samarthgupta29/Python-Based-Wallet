import sqlite3

def createTable():
    connection=sqlite3.connect("login.db")

    #connection.execute("CREATE TABLE USERS(USERNAME NOT NULL,EMAIL TEXT,PASSWORD TEXT) ")
    #connection.execute("INSERT INTO USERS VALUES(?,?,?)",('samarth','lordsamarth@gmail.com','samarth123'))
    #connection.execute("CREATE TABLE USERS2(USERNAME NOT NULL,EMAIL TEXT,PASSWORD TEXT,BALANCE INT)")
    #connection.execute("CREATE TABLE TRANSACTIONTABLE(TID INTEGER IDENTITY(1,1) PRIMARY KEY,SEMAIL TEXT,REMAIL TEXT,AMT INTEGER)")
    #connection.execute("INSERT INTO USERS2 VALUES(?,?,?,?)",('samarth','lordsamarth@gmail.com','samarth123',1000))
    #connection.execute("INSERT INTO USERS2 VALUES(?,?,?,?)", ('samarth29', 'samarthgupta29@gmail.com', 'samarth321', 1000))
    #connection.execute("INSERT INTO USERS2 VALUES(?,?,?,?)", ('tony', 'tony@gmail.com', 'tony123', 1000))
    # connection.execute("INSERT INTO USERS2 VALUES(?,?,?,?)", ('', '', '', 1000))
    #connection.execute("CREATE TABLE TRANSACTIONTABLE2(SEMAIL NOT NULL,REMAIL TEXT,AMT TEXT)")
    #connection.execute("CREATE TABLE TRANSACTIONTABLE3(SEMAIL TEXT,REMAIL TEXT,AMT INTEGER)")
    connection.commit()
    result=connection.execute("SELECT * FROM USERS2")
    for data in result:
        #print("Transaction ID : ",data[0])
        print(" ",data[0])
        print(" ",data[1])
        print(" ",data[2])
        print(" ",data[3])
        #print(" ",data[3])


    connection.close()
createTable()