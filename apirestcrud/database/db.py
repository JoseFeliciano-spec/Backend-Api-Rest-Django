import mysql.connector;

def connectDb():
    db = mysql.connector.connect(
        host = "mysql-josespec.alwaysdata.net",
        user = "josespec",
        password = "29035683JA",
        database="josespec_prueba"
    )
    return db