from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from seas import chartQueries
import numpy as np


# def loginpage(request):
#     return render(request, 'login.html')
def home(request):
    return render(request, 'login.html')


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
            # messages.success(request, "Invalid Credentials.") 
            return HttpResponse('<h1>Invalid Credentials!</h1>')
    else:
        return render(request, 'login.html')

def dashboardpage(request):
    return render(request, 'dashboard.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')

def ClassSizeRequirementView(request):
    if request.method == "POST":
        # get.year from HTML DropDown Selection
        arr1 = chartQueries.ClassSizeRequirement("Spring", '2021')
        arr2 = chartQueries.ClassSizeRequirement("Spring", '2021')
        arr3 = np.concatenate((arr1, arr2), axis=1)
        sumarr = arr3.sum(axis=0)
        table = np.concatenate((arr3, sumarr), axis=0)
        return render(request, 'chartLayout.html', {"result":table})
