from django.shortcuts import render, redirect
from django.http import HttpResponse
from peach.models import *
from peachProject.formularios import ComentarioFormulario
from peachProject.formularios import EncuestaFormulario
from peachProject.formularios import ContactoFormulario

#def base_pag(request):
    #return render(request, "base.html", {})

#HOME
def home_pag(request):
    return render(request, "home.html", {})

#SERVICIOS
def busqueda_servicios(request):
    mensaje= "No has realizado una busqueda."
    servicios=[]

    if request.method == "GET":
        busqueda= request.GET.get("txtBusqueda", "")
        if busqueda:
            mensaje= "Servicio buscado: %s" %busqueda
            servicios= Servicio.objects.filter(nombre__icontains=busqueda)

    return render(request, 'buscar_servicios.html', {"msj": mensaje, "servicios": servicios})

#CRUD COMENTARIOS
def comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'comentarios/index.html', {'comentarios': comentarios})

def crear_comentario(request):
    formulario = ComentarioFormulario(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('comentarios')
    return render(request, 'comentarios/crear.html', {'formulario': formulario})

def editar_comentario(request, id):
    comentario = Comentario.objects.get(id=id)
    formulario = ComentarioFormulario(request.POST or None, request.FILES or None, instance=comentario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('comentarios')
    return render(request, 'comentarios/editar.html', {'formulario': formulario})

def eliminar_comentario(request, id):
    comentario= Comentario.objects.get(id=id)
    comentario.delete()
    return redirect('comentarios')

#CRUD ENCUESTAS
def busqueda_encuestas(request):
    mensaje= "No has realizado una busqueda."
    encuestas=[]

    if request.method == "GET":
        busqueda= request.GET.get("txtBusquedaE", "")
        if busqueda:
            mensaje= "Encuesta buscada: %s" %busqueda
            encuestas= Encuesta.objects.filter(ocupacion__icontains=busqueda)

    return render(request, 'encuestas/buscar_encuesta.html', {"msj": mensaje, "encuestas": encuestas})


def registrar_encuesta(request):
    if request.method =="POST":
        encuestaFormulario= EncuestaFormulario(request.POST)
        if encuestaFormulario.is_valid():
            ocupacion= encuestaFormulario.cleaned_data.get("ocupacion", "")
            experiencia= encuestaFormulario.cleaned_data.get("experiencia", "")
            estado= encuestaFormulario.cleaned_data.get("estado", "")
            a = Encuesta(ocupacion = ocupacion, experiencia = experiencia, estado = Estado.objects.get(id=estado))
            a.save()
            return redirect('guardado')
    else:
        encuestaFormulario = EncuestaFormulario()

    return render(request, 'encuestas/registrar_encuesta.html', {"form":encuestaFormulario})

def modificar_encuesta(request, id):
    id_encuesta= Encuesta.objects.get(id=id)
    if request.method == "POST":
        encuestaFormulario = EncuestaFormulario(request.POST)
        if encuestaFormulario.is_valid():
            ocupacion = encuestaFormulario.cleaned_data.get("ocupacion", "")
            experiencia = encuestaFormulario.cleaned_data.get("experiencia", "")
            estado = encuestaFormulario.cleaned_data.get("estado", "")

            id_encuesta.ocupacion = ocupacion
            id_encuesta.experiencia = experiencia
            id_encuesta.estado = Estado.objects.get(id=estado)
            id_encuesta.save()
            return redirect('guardado')
    else:
        dict_encuesta={"ocupacion": id_encuesta.ocupacion,
                       "experiencia": id_encuesta.experiencia,
                       "estado": id_encuesta.estado.id
                       }
        encuestaFormulario = EncuestaFormulario(dict_encuesta)
    return render(request, "encuestas/modificar_encuesta.html", {"form": encuestaFormulario})

def eliminar_encuesta(request, id):
    id_encuesta= Encuesta.objects.get(id=id)
    if request.method == "POST":
        if id_encuesta:
            id_encuesta.delete()
            return redirect('borrado')
    else:
        dict_encuesta={"ocupacion": id_encuesta.ocupacion,
                       "experiencia": id_encuesta.experiencia,
                       "estado": id_encuesta.estado.id
                       }
        encuestaFormulario = EncuestaFormulario(dict_encuesta)
    return render(request, 'encuestas/eliminar_encuesta.html', {"form": encuestaFormulario})

#CONTACTO
def registrar_contacto(request):
    if request.method =="POST":
        contactoFormulario= ContactoFormulario(request.POST)
        if contactoFormulario.is_valid():
            nombres= contactoFormulario.cleaned_data.get("nombres", "")
            apellidos= contactoFormulario.cleaned_data.get("apellidos", "")
            empresa= contactoFormulario.cleaned_data.get("empresa", "")
            descripcion = contactoFormulario.cleaned_data.get("descripcion", "")
            direccion = contactoFormulario.cleaned_data.get("direccion", "")
            telefono = contactoFormulario.cleaned_data.get("telefono", "")
            correo = contactoFormulario.cleaned_data.get("correo", "")
            interes = contactoFormulario.cleaned_data.get("interes", "")
            a = Contacto(nombres = nombres, apellidos = apellidos, empresa = empresa, descripcion = descripcion, direccion = direccion, telefono = telefono, correo = correo, interes = interes)
            a.save()
            return redirect('guardado')
    else:
        contactoFormulario = ContactoFormulario()

    return render(request, 'registrar_contacto.html', {"form":contactoFormulario})

def guardado(request):
    return render(request, "guardado.html", {})

def borrado(request):
    return render(request, "borrado.html", {})

# def v401(request):
#     return render(request, "errores/401.html", {})
# def v403(request):
#     return render(request, "errores/403.html", {})
# def v404(request):
#     return render(request, "errores/404.html", {})
# def v408(request):
#     return render(request, "errores/408.html", {})
# def v502(request):
#     return render(request, "errores/502.html", {})
# def v503(request):
#     return render(request, "errores/503.html", {})
#ERRORES

def error_401(request, exception):
    return render(request, 'errores/401.html', {})

def error_403(request, exception):
    return render(request, 'errores/403.html', {})

def error_404(request, exception):
    return render(request, 'errores/404.html', {})

def error_408(request, exception):
    return render(request, 'errores/408.html', {})

def error_502(request, exception):
    return render(request, 'errores/502.html', {})

def error_503(request, exception):
    return render(request, 'errores/503.html', {})

