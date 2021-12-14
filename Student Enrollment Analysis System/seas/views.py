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
        # get.year and get.semester from HTML DropDown Selection put that instead of Spring and 2021
        arr1 = chartQueries.ClassSizeRequirement("Spring", '2021')
        arr2 = chartQueries.ClassSizeRequirement("Spring", '2021')
        arr3 = np.concatenate((arr1, arr2), axis=1)
        totalarr = arr3.sum(axis=0)
        #line 47 not working= ValueError:all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
        table = np.concatenate((arr3, totalarr), axis=0)

    # Note here "result" is the variable by which the HTML will recognize "table"   
    return render(request, 'chartLayout.html', {"result":table})


def ClassSizeDistributionView(request):
    if request.method == 'POST':
        # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
        sbe = chartQueries.ClassSizeDistribution("Spring", '2021', "SBE")
        sels = chartQueries.ClassSizeDistribution("Spring", '2021', "SELS")
        sets = chartQueries.ClassSizeDistribution("Spring", '2021', "SETS")
        slass = chartQueries.ClassSizeDistribution("Spring", '2021', "SLASS")
        spph = chartQueries.ClassSizeDistribution("Spring", '2021', "SPPH")
        allarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
        totalarr = allarr.sum(axis=1)
        #line 63 not working= ValueError:all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
        finalarr = np.concatenate((allarr,totalarr),axis=1)
    
    # Note here "result" is the variable by which the HTML will recognize "finalarr" 
    return render(request, 'filename.html', {"result": finalarr})


