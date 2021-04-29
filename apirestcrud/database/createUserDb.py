import mysql.connector;
from apirestcrud.database.db import connectDb;

def createUserDb(idAlumno, name, LastName):
    
    db = connectDb();
    mycursor = db.cursor()

    sql = "INSERT INTO alumno (idAlumno, name, LastName) VALUES (%s, %s, %s)"
    val = (idAlumno, name, LastName)
    mycursor.execute(sql, val)
   
    db.commit()

    if(mycursor.rowcount >= 1):
        return True;
    
    return False;
    