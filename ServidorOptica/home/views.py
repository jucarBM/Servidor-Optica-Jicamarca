from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    return render(
        request,
        'home.html')