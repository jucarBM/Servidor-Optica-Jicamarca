from django.shortcuts import render

# Create your views here.
def signin(request):
    """
    Función vista para la página signin del sitio.
    """
    return render(
        request,
        'signin.html')

def signup(request):
    """
    Función vista para la página signup del sitio.
    """
    return render(
        request,
        'signup.html')