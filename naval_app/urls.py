from django.urls import path
from naval_app.views import index
from naval_app.views import listar_buques,editar_buque,crear_buque,borrar_buque,about
from django.views.generic import TemplateView
urlpatterns = [
    #path("", index , name="index"),
    path("", TemplateView.as_view(template_name="naval_app/index.html"), name="index"),
    path('buque/nuevo/', crear_buque, name="crear_buque"),
    path('buques/', listar_buques, name='buque_list'),
    path('buque/<int:pk>/editar/', editar_buque, name="editar_buque"),
    path('buque/<int:pk>/borrar/', borrar_buque, name="borrar_buque"),  
     path('about/', about, name='about'),
]