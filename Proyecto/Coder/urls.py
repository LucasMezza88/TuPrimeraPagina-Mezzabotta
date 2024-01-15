from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profesor/list', views.profesor_list, name='profesor_list'),
    path('estudiante/list', views.estudiante_list, name='estudiante_list'),
    path('curso/list', views.curso_list, name='curso_list'),
    path('profesor/form', views.profesor_form, name='profesor_form'),
    path('estudiante/form', views.estudiante_form, name='estudiante_form'),
]
