import mysql.connector;
from apirestcrud.database.db import connectDb;

def deleteUserDb(idAlumno):
    db = connectDb();
    mycursor = db.cursor()

    sql = "DELETE from alumno WHERE idAlumno='{}'".format(idAlumno);

    print(sql);
    mycursor.execute(sql)

    db.commit()

    if(mycursor.rowcount >= 1):
        return True;
    
    return False;
    

