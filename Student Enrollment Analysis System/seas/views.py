from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

    # Pull data from database
    # Transform Data
    # Send Emails
    # etc
    # return HttpResponse('Hello World')
    #return render(request, 'hello.html', {'name': 'Topu'})

# def loginpage(request):
#     return render(request, 'login.html')
    
def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect('dashboard')
            return render(request, 'dashboard.html')
        else:
            return HttpResponse('<h1>Unsuccessful</h1>')
    else:
        return render(request, 'login.html')

def dashboardpage(request):
    return render(request, 'dashboard.html')
