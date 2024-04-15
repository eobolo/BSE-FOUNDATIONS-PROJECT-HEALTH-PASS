# Import necessary modules 
from django.shortcuts import render


# Define the custom 500 error handler view
<<<<<<< HEAD
def custom_server_error(request):
    return render(request, 'healthpass/error.html')
=======
def custom_error_500(request):
    return render(request, 'healthpass/error_500.html', status=500)

def custom_error_404(request, exception=None):
    return render(request, 'healthpass/error_404.html', status=404)

def custom_error_403(request, exception=None):
    return render(request, 'healthpass/error_403.html', status=403)

def custom_error_400(request, exception=None):
    return render(request, 'healthpass/error_400.html', status=400)
>>>>>>> d4587570eb2ea87af95454b8da0f2e7052f05c11
