
from django.http import HttpResponse
from django.shortcuts import render
"""importo los modelos de la app_coder"""
from app_coder.models import Curso
from django.template import loader

# Create your views here.
def cursos(request):
    """traigo todos los datos de esa base de datos que esten en la Base de datos en la SQL"""
    cursos = Curso.objects.all()
    
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("plantilla.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alta_curso(request , nombre):
    #Creo una nueva instancia de curso
    curso = Curso (nombre=nombre , camada=123)
    """guardo en la base de datos"""
    curso.save()
    #Cada vez que creemos un campo en esa base de datos dejaremos este mensaje.
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada : {curso.camada}"
    return HttpResponse(texto)
    #Creo un objeto curso y se crea una nueva fila, primary key.



