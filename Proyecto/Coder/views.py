from django.shortcuts import redirect, render

from . import models

from . import forms

def index(request):
    return render(request, 'Coder/index.html')

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "Coder/profesor_list.html", contexto)

def estudiante_list(request):
    consulta = models.Estudiante.objects.all()
    contexto = {"estudiantes": consulta}
    return render(request, "Coder/estudiante_list.html", contexto)

def curso_list(request):
    consulta = models.Curso.objects.all()
    contexto = {"cursos": consulta}
    return render(request, "Coder/curso_list.html", contexto)

def profesor_form(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor_list")
    else:
        form = forms.ProfesorForm()
    return render(request, "Coder/profesor_form.html", {"form": form})

def estudiante_form(request):
    if request.method == "POST":
        form = forms.EstudiantesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = forms.EstudiantesForm()
    return render(request, "Coder/estudiante_form.html", {"form": form})
