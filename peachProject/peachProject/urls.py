"""peachProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from peach import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("base",views.base_pag),
    path("home",views.home_pag, name='home'),
    path('busqueda_servicios', views.busqueda_servicios),
    path("comentarios",views.comentarios, name='comentarios'),
    path('crear_comentario', views.crear_comentario, name='crear'),
    path('editar_comentario', views.editar_comentario, name='editar'),
    path('eliminar_comentario/<int:id>', views.eliminar_comentario, name='eliminar'),
    path('editar_comentario/<int:id>', views.editar_comentario, name='editar'),
    path('busqueda_encuestas', views.busqueda_encuestas, name='encuestas'),
    path('registrar_encuesta', views.registrar_encuesta),
    path('modificar_encuesta/<int:id>', views.modificar_encuesta, name="modificarE"),
    path('eliminar_encuesta/<int:id>', views.eliminar_encuesta, name="eliminarE"),
    path('registrar_contacto', views.registrar_contacto),
    path('guardado', views.guardado, name="guardado"),
    path('borrado', views.borrado, name="borrado"),
    # path('v401', views.v401),
    # path('v403', views.v403),
    # path('v404', views.v404),
    # path('v408', views.v408),
    # path('v502', views.v502),
    # path('v503', views.v503),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler401 = 'peach.views.error_401'
handler403 = 'peach.views.error_403'
handler404 = 'peach.views.error_404'
handler408 = 'peach.views.error_408'
handler502 = 'peach.views.error_502'
handler503 = 'peach.views.error_503'

