from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formularioPacientes import FormularioPacientes

from web.models import Medicos,Pacientes

# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def consultoriomedico(request):
    medicosConsultados=Medicos.objects.all()

    datosMedicos={
        "medicos":medicosConsultados
    }
    return render(request,'consultoriomedico.html',datosMedicos)

def consultoriopacientes(request):
    pacientesConsultados=Pacientes.objects.all()

    datosPacientes={
        "pacientes":pacientesConsultados
    }
    return render(request,'consultoriopacientes.html',datosPacientes)

def MedicosVista(request):

    #creamos una variable para controlar la
    #ejec de la alerta
    lanzandoAlerta=False

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario,
        "bandera":lanzandoAlerta
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
            #LLevar mis datos hacia la BD
            medicoNuevo=Medicos(
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"]
            )
            medicoNuevo.save()
            diccionario["bandera"]=True
           


    return render(request,'registromedicos.html',diccionario)

def PacientesVista(request):

    #debo utilizar la clase formularioMedico
    # Creamos asi un objeto 
    formulario = FormularioPacientes()
    diccionario = {
        "formulario" : formulario
    }

    #Activar la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioPacientes(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            pacienteNuevo = Pacientes (
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tipo=datos["tipo_afiliado"],
                regimen=datos["regimen"],
                grupo=datos["grupo_ingreso"],
                celular=datos["celular"],
                correo=datos["correo"]
            )
            pacienteNuevo.save()
            print("Sus datos han sido guardados con éxito")

    return render(request,'registropacientes.html',diccionario)