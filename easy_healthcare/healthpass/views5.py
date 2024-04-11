# Import necessary modules 
from django.shortcuts import render


# Define the custom 500 error handler view
def custom_server_error(request):
    return render(request, 'healthpass/error.html')
