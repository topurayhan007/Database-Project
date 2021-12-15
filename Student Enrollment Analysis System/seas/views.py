from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from seas import chartQueries
import numpy as np
from seas.models import *


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
    if request.method == "POST":
        # get.year and get.semester from HTML DropDown Selection put that instead of Spring and 2021
        # Columns: Class Size(label not values from query), Sections, Classroom 6, Classroom 7
        # Rows: 1-10, 11-20, 21-30, 31-35, 36-40, 41-50, 51-55, 56-65
        semester = request.POST['semester']
        year = request.POST['year']
        finalarr = chartQueries.ClassSizeRequirement(semester, year)
        finalarr = np.array(finalarr)
        rowlabel = ["1-10", "11-20", "21-30", "31-35", "36-40", "41-50", "51-55", "56-65", "Total"]
        collabel = ["Class Size", "Sections", "Classroom 6", "Classroom 7"]
        # Row last: Total (This row found using code below)
        totalarr = finalarr.sum(axis=0)
        #line 49 not working= ValueError:all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
        # table = np.concatenate((finalarr, totalarr), axis=0)
        # Note here "result" is the variable by which the HTML will recognize "table"
        return render(request, 'classSizeRequirement.html', {
            'result':finalarr,
            'total': totalarr,
            'colLabel': collabel,
            'rowLabel': rowlabel,
        })
    else:
        return render(request, 'classSizeRequirement.html')
       
    



def ClassSizeDistributionView(request):
    if request.method == "POST":
        # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
        semester = request.POST['semester']
        year = request.POST['year']
        sbe = chartQueries.ClassSizeDistribution(semester, year, "SBE")
        sels = chartQueries.ClassSizeDistribution(semester, year, "SELS")
        sets = chartQueries.ClassSizeDistribution(semester, year, "SETS")
        slass = chartQueries.ClassSizeDistribution(semester, year, "SLASS")
        spph = chartQueries.ClassSizeDistribution(semester, year, "SPPH")
        # Columns: Size(label not values from query), SBE, SELS, SETS, SLASS, SPPH, Total
        # Rows: Enrollment, 1-10, 11-20, 21-30, 31-35, 36-40, 41-50, 51-55, 56-60, 60+
        rowlabel = ["Enrollment", "1-10", "11-20", "21-30", "31-35", "36-40", "41-50", "51-55", "56-60", "60+"]
        allarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
        # Column: Total (This column found using code below)
        totalarr = allarr.sum(axis=1)
        # schoolList = ["Size", School_T.objects.order_by().values_list('schoolTitle').distinct(), "Total"]
        schoolList = ["Size", "SBE", "SELS", "SETS", "SLASS", "SPPH", "Total"]
        #line 70 not working= ValueError:all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
        # finalarr = np.concatenate((allarr,totalarr),axis=1)
        
        # Note here "result" is the variable by which the HTML will recognize "finalarr" 
        return render(request, 'ClassSizeDistribution.html', {
            'result': allarr,
            'total': totalarr,
            'colLabel': schoolList,
            'rowLabel': rowlabel,
            'sbe':sbe,
            'sels':sels,
            'sets':sets,
            'slass':slass,
            'spph':spph,
        })
    else:
        return render(request, 'ClassSizeDistribution.html')



def UsageOfTheResourcesView(request):
    if request.method == "POST":
        # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
        # columns areas follows: Sum, Avg Enroll, Avg Room, Difference, Unused%
        # rows are as follows: Selected Semester, SBE, SELS, SETS, SLASS, SPPH
        semester = request.POST['semester']
        year = request.POST['year']
        table = chartQueries.UsageOfTheResources(semester, year)
        rowlabel = [semester, "SBE", "SELS", "SETS", "SLASS", "SPPH"]
        collabel = ["Sum", "Avg Enroll", "Avg Room", "Difference", "Unused%"]

        # Note here "result" is the variable by which the HTML will recognize "table" 
        return render(request, 'usageOfTheResources.html', {
            'result': table,
            'rowLabel': rowlabel,
            'colLabel': collabel, 
        
        })
    
    else:
        return render(request, 'usageOfTheResources.html')

