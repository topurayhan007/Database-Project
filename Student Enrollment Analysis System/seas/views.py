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
            return redirect('dashboardpage')
            # return render(request, 'dashboard.html')
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
	return redirect('loginpage')


def ClassSizeRequirementView(request):
    # if request.method == "POST":
    # get.year and get.semester from HTML DropDown Selection put that instead of Spring and 2021
    # Columns: Class Size(label not values from query), Sections, Classroom 6, Classroom 7
    # Rows: 1-10, 11-20, 21-30, 31-35, 36-40, 41-50, 51-55, 56-65
    finalarr = chartQueries.ClassSizeRequirement("Spring", '2021')
    finalarr = np.array(finalarr)
    # Row last: Total (This row found using code below)
    totalarr = finalarr.sum(axis=0)
    #line 49 not working= ValueError:all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
    # table = np.concatenate((finalarr, totalarr), axis=0)

    # Note here "result" is the variable by which the HTML will recognize "table"   
    return render(request, 'classSizeRequirement.html', {
        'result':finalarr,
        'total': totalarr,
    })



def ClassSizeDistributionView(request):
    # if request.method == "POST":
    # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
    sbe = chartQueries.ClassSizeDistribution("Spring", '2021', "SBE")
    sels = chartQueries.ClassSizeDistribution("Spring", '2021', "SELS")
    sets = chartQueries.ClassSizeDistribution("Spring", '2021', "SETS")
    slass = chartQueries.ClassSizeDistribution("Spring", '2021', "SLASS")
    spph = chartQueries.ClassSizeDistribution("Spring", '2021', "SPPH")
    # Columns: Size(label not values from query), SBE, SELS, SETS, SLASS, SPPH, Total
    # Rows: 1-10, 11-20, 21-30, 31-35, 36-40, 41-50, 51-55, 56-60, 60+
    allarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
    # Column: Total (This column found using code below)
    totalarr = allarr.sum(axis=1)
    #line 70 not working= ValueError:all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
    # finalarr = np.concatenate((allarr,totalarr),axis=1)
    
    # Note here "result" is the variable by which the HTML will recognize "finalarr" 
    return render(request, 'ClassSizeDistribution.html', {
        'result': allarr,
        'total': totalarr,

        
    })



def UsageOfTheResourcesView(request):
    # if request.method == "POST":
    # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
    # columns areas follows: Sum, Avg Enroll, Avg Room, Difference, Unused%
    # rows are as follows: Selected Semester, SBE, SELS, SETS, SLASS, SPPH
    table = chartQueries.UsageOfTheResources("Spring", '2021')

    # Note here "result" is the variable by which the HTML will recognize "table" 
    return render(request, 'usageOfTheResources.html', {
        'result': table
    
    })

