from django.http import HttpResponse
import json;
from django.views.decorators.csrf import csrf_exempt;
from apirestcrud.database.seeUser import seeUser;
from apirestcrud.database.createUserDb import createUserDb;
from apirestcrud.database.updateUserDb import updateUserdb;
from apirestcrud.database.deleteUserDb import deleteUserDb;

def hello(request):
    array = seeUser();
    
    if request.method == "GET":
        try:
            response = json.dumps(array)
        except:
            response = json.dumps({"saludo": "error"})
    return HttpResponse(response, content_type="text/json")

@csrf_exempt
def addEst(request):
    if request.method == "POST":
        add = json.loads(request.body)
        idAlumno = add['idAlumno']
        name = add['name']
        lastName = add['lastName']
        """ print(name);
        print(idAlumno);
        print(lastName); """
        """ est = Est(idAlumno=idAlumno, name=name, LastName=LastName) """
        try:
            if createUserDb(idAlumno, name, lastName):
                response = json.dumps({"saludo" : "Se registró"})
            else:
                response = json.dumps({"saludo" : "No se registró"})
        except:
            response = json.dumps({"saludo": "Error, no se pudo registrar o realizar la operación"})
    return HttpResponse(response, content_type="text/json")

@csrf_exempt
def updateEst(request):
    if request.method == "PUT":
        add = json.loads(request.body)
        idAlumno = add['idAlumno']
        name = add['name']
        lastName = add['lastName']
        try:
            if updateUserdb(idAlumno, name, lastName):
                response = json.dumps({"saludo" : "Actualizado"})
            else:
                response = json.dumps({"saludo" : "No actualizado"})
        except:
            response = json.dumps({"saludos" : "Ocurrió un error"});

    return HttpResponse(response, content_type="text/json");

@csrf_exempt
def deleteEst(request):
    if request.method == "DELETE":
        add = json.loads(request.body)
        idAlumno = add['idAlumno']
        try:
            if deleteUserDb(idAlumno):
                response = json.dumps({"saludo" : "Se borró correctamente"})
            else:
                response = json.dumps({"saludo" : "No borró correctamente"})
        except:
            response = json.dumps({"saludo" : "Ocurrió un error, no se pudo borrar"})
    
    return HttpResponse(response, content_type="text/jsom");
    
