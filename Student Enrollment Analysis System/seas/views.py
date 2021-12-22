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


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('loginpage')


def dashboardpage(request):
    school = School_T.objects.all().count()
    dept = Department_T.objects.all().count()
    course = Course_T.objects.all().count()
    faculty = Faculty_T.objects.all().count()
    classroom = Classroom_T.objects.all().count()
    return render(request, 'dashboard.html',{
        'school':school,
        'dept':dept,
        'course':course,
        'faculty':faculty,
        'classroom':classroom,
    })


def ClassSizeRequirementView(request):
    semesterList = ['Spring', 'Summer', 'Autumn']
    yearList = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

    if request.method == "POST":
        # get.year and get.semester from HTML DropDown Selection put that instead of Spring and 2021
        # Columns: Class Size(labels, not values from query), Sections, Classroom 6, Classroom 7
        # Rows: 1-10, 11-20, 21-30, 31-35, 36-40, 41-50, 51-55, 56-65

        semester = request.POST['semester']
        year = request.POST['year']
        str = semester + " " + year
        finalarr = chartQueries.ClassSizeRequirement(semester, year)
        finalarr = np.array(finalarr)
        rowlabel = ["1-10", "11-20", "21-30", "31-35", "36-40", "41-50", "51-55", "56-65"]
        collabel = ["Class Size", "Sections", "Classroom 6", "Classroom 7"]
        totalarr = finalarr.sum(axis=0)

        table = [collabel]
        count = 0
        classroom6 = []
        classroom7 = []

        for item1, item2, item3 in finalarr:
            table.append([rowlabel[count], item1, item2, item3])
            classroom6.append(item2)
            classroom7.append(item3)
            count=count+1
        table.append(['Total', totalarr[0], totalarr[1], totalarr[2]])

        return render(request, 'classSizeRequirement.html', {
            'semesterList':semesterList,
            'yearList': yearList,
            'table': table,
            'labels': rowlabel,
            'datavalues': classroom6,
            'datavalues2': classroom7,
            'str': str,
        })

    else:
        return render(request, 'classSizeRequirement.html', {
            'semesterList':semesterList,
            'yearList': yearList,
        })
       
    



def ClassSizeDistributionView(request):
    semesterList = ['Spring', 'Summer', 'Autumn']
    yearList = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

    if request.method == "POST":
        # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
        semester = request.POST['semester']
        year = request.POST['year']
        str = semester + " " + year
        sbe = chartQueries.ClassSizeDistribution(semester, year, "SBE")
        sels = chartQueries.ClassSizeDistribution(semester, year, "SELS")
        sets = chartQueries.ClassSizeDistribution(semester, year, "SETS")
        slass = chartQueries.ClassSizeDistribution(semester, year, "SLASS")
        spph = chartQueries.ClassSizeDistribution(semester, year, "SPPH")
        # Columns: Size(label not values from query), SBE, SELS, SETS, SLASS, SPPH, Total
        # Rows: Enrollment, 1-10, 11-20, 21-30, 31-35, 36-40, 41-50, 51-55, 56-60, 60+
        rowlabel = ["1-10", "11-20", "21-30", "31-35", "36-40", "41-50", "51-55", "56-60", "60+"]
        # allarr has row wise data
        allarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
        # Column: Total (This column found using code below)
        # totalarr is a column-wise data
        totalarr = allarr.sum(axis=1)
        # schoolList = ["Size", School_T.objects.order_by().values_list('schoolTitle').distinct(), "Total"]
        collabel = ["Enrollment", "SBE", "SELS", "SETS", "SLASS", "SPPH", "Total"]
        #line 70 not working= ValueError:all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
        # finalarr = np.concatenate((allarr,totalarr),axis=1)
        
        # Note here "result" is the variable by which the HTML will recognize "finalarr" 
        
        return render(request, 'ClassSizeDistribution.html', {
            'semesterList':semesterList,
            'yearList': yearList,
            'result': allarr,
            'total': totalarr,
            'colLabel': collabel,
            'rowLabel': rowlabel,
            'sbe':sbe,
            'sels':sels,
            'sets':sets,
            'slass':slass,
            'spph':spph,
            'str': str,
        })
    else:
        return render(request, 'ClassSizeDistribution.html', {
            'semesterList':semesterList,
            'yearList': yearList,
        })



def UsageOfTheResourcesView(request):
    semesterList = ['Spring', 'Summer', 'Autumn']
    yearList = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

    if request.method == "POST":
        # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
        # columns areas follows: Sum, Avg Enroll, Avg Room, Difference, Unused%
        # rows are as follows: Selected Semester, SBE, SELS, SETS, SLASS, SPPH
        semester = request.POST['semester']
        year = request.POST['year']
        str = semester + " " + year
        # here Table is row-wise object data
        finalarr = chartQueries.UsageOfTheResources(semester, year)
        rowlabel = [semester, "SBE", "SELS", "SETS", "SLASS", "SPPH"]
        collabel = ["-", "Sum", "Avg Enroll", "Avg Room", "Difference", "Unused%"]
        table = [collabel]
        table2 = []
        count = 0
        rowlabel2 = ["Average of ENROLLED", "Average of ROOM CAPACITY", "Average of Unused Space", "Unused Percent"]
        list_col = []
        for item1, item2, item3, item4, item5 in finalarr:
            table.append([rowlabel[count], item1, item2, item3, item4, item5])
            if count == 0:
                list_col = [item2, item3, item4, item5]
            count=count+1

        count = 0
        for item in list_col:
            table2.append([rowlabel2[count], list_col[count]])
            count+=1
        
        return render(request, 'usageOfTheResources.html', {
            'semesterList':semesterList,
            'yearList': yearList,
            'table': table,
            'table2': table2,
            'str': str,
        
        })
    
    else:
        return render(request, 'usageOfTheResources.html', {
            'semesterList':semesterList,
            'yearList': yearList,
        })



# def RevenueTrendOfTheSchoolsView(request):
#     if request.method == "POST":
#         # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
#         # columns areas follows: Sum, Avg Enroll, Avg Room, Difference, Unused%
#         # rows are as follows: Selected Semester, SBE, SELS, SETS, SLASS, SPPH
#         semester = request.POST['semester']
#         year = request.POST['year']
#         # here Table is row-wise object data
#         table = chartQueries.UsageOfTheResources(semester, year)
#         rowlabel = [semester, "SBE", "SELS", "SETS", "SLASS", "SPPH"]
#         collabel = ["-", "Sum", "Avg Enroll", "Avg Room", "Difference", "Unused%"]

#         # Note here "result" is the variable by which the HTML will recognize "table" 
#         return render(request, 'revenueTrendOfTheSchools.html', {
#             'result': table,
#             'rowLabel': rowlabel,
#             'colLabel': collabel, 
        
#         })
    
#     else:
#         return render(request, 'revenueTrendOfTheSchools.html')

##########chartviews edited by Zannat
def pie_chart(request):
    labels = []
    data = []

    queryset = chartQueries.ClassSizeRequirement("Summer", "2020")
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'classSizeRequirementChart', {
        'labels': labels,
        'data': data,
    })