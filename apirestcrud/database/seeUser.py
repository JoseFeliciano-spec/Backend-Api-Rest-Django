import mysql.connector;
from apirestcrud.database.db import connectDb;

def seeUser():
    array = [];

    dbs = connectDb();
    mycursor = dbs.cursor()

    mycursor.execute("SELECT * FROM alumno")

    myresult = mycursor.fetchall()

    for x in myresult:
        map = {
            "idAlumno": x[0],
            "name" : x[1],
            "lastName" : x[2]
        };
        array.append(map);

    return array;