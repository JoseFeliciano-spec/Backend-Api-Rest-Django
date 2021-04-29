import mysql.connector;
from apirestcrud.database.db import connectDb;


def updateUserdb(idAlumno, name, lastName):
    db = connectDb();
    mycursor = db.cursor()

    sql = "UPDATE alumno SET name = '{}', lastName = '{}' WHERE idAlumno='{}'".format(name, lastName, idAlumno);


    print(sql);
    mycursor.execute(sql)

    db.commit()

    if(mycursor.rowcount >= 1):
        return True;
    
    return False;
    
