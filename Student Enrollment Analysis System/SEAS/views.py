from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

    # Pull data from database
    # Transform Data
    # Send Emails
    # etc
    # return HttpResponse('Hello World')
    #return render(request, 'hello.html', {'name': 'Topu'})

def loginpage(request):
    return render(request, 'login.html')
    
