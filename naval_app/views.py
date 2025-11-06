from django.shortcuts import render, redirect, get_object_or_404
from naval_app.forms import *
from .models import Buque
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"naval_app/index.html")
@login_required
def crear_buque(request):
    if request.method == "POST":
        form =BuqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("buque_list")

    else:
        form =BuqueForm()

    return render(request, "naval_app/buque_form.html", {"form": form})


@login_required
def listar_buques(request):
    query = request.GET.get('q')
    if query:
        buques = Buque.objects.filter(nombre__icontains=query)
    else:
        buques = Buque.objects.all()
    return render(request, 'naval_app/buque_list.html', {'buques': buques})
@login_required
def editar_buque(request, pk):
    buque = get_object_or_404(Buque, pk=pk)
    if request.method == "POST":
        form = BuqueForm(request.POST, instance=buque)
        if form.is_valid():
            form.save()
            return redirect("buque_list")  # vuelve a la lista después de guardar
    else:
        form = BuqueForm(instance=buque)

    return render(request, "naval_app/buque_form.html", {"form": form})
@login_required
def borrar_buque(request, pk):
    buque = get_object_or_404(Buque, pk=pk)
    if request.method == "POST":
        buque.delete()
        return redirect("buque_list")
    
    return render(request, "naval_app/buque_confirm_delete.html", {"buque": buque})

def about(request):
    return render(request, 'naval_app/about.html')