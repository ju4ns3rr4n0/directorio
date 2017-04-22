from django.shortcuts import render

def directorio_list(request):
    return render(request, 'directorio/directorio_list.html', {})
