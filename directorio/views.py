from django.shortcuts import render
from django.utils import timezone
from .models import Directorio

def directorio_list(request):
    directorios = Directorio.objects.order_by('persona')
    return render(request, 'directorio/directorio_list.html', {'directorios':directorios})