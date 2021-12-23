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


# Semester and Year List for Selection Menue
# semesterList = ['Spring', 'Summer', 'Autumn']
# yearList = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
semesterList = []
yearList = []
semesterL = Section_T.objects.order_by().values_list('semester').distinct()
yearL = Section_T.objects.order_by().values_list('year').distinct()
for item in semesterL:
    item = str(item)[2:-3]
    semesterList.append(item)
for item in yearL:
    item = str(item)[2:-3]
    yearList.append(item)


def ClassSizeRequirementView(request):
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
            table.append([rowlabel[count], int(item1), item2, item3])
            classroom6.append(item2)
            classroom7.append(item3)
            count=count+1
        table.append(['Total', int(totalarr[0]), "{:.2f}".format(totalarr[1]), "{:.2f}".format(totalarr[2]) ])

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
    if request.method == "POST":
        # get.year and get.semester from HTML DropDown Selection and put that instead of Spring and 2021
        # Columns: Size(label not values from query), SBE, SELS, SETS, SLASS, SPPH, Total
        # Rows: Enrollment, 1-10, 11-20, 21-30, 31-35, 36-40, 41-50, 51-55, 56-60, 60+

        semester = request.POST['semester']
        year = request.POST['year']
        str = semester + " " + year
        sbe = chartQueries.ClassSizeDistribution(semester, year, "SBE")
        sels = chartQueries.ClassSizeDistribution(semester, year, "SELS")
        sets = chartQueries.ClassSizeDistribution(semester, year, "SETS")
        slass = chartQueries.ClassSizeDistribution(semester, year, "SLASS")
        spph = chartQueries.ClassSizeDistribution(semester, year, "SPPH")
        
        rowlabel = ["1-10", "11-20", "21-30", "31-35", "36-40", "41-50", "51-55", "56-60", "60+"]
        collabel = ["Enrollment", "SBE", "SELS", "SETS", "SLASS", "SPPH", "Total"]

        finalarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
        totalarr = finalarr.sum(axis=1)
        
        table = [collabel]
        count = 0

        for item1, item2, item3, item4, item5 in finalarr:
            table.append([rowlabel[count], item1, item2, item3, item4, item5, totalarr[count]])
            
            count=count+1

        
        return render(request, 'ClassSizeDistribution.html', {
            'semesterList':semesterList,
            'yearList': yearList,
            'table': table,
            'labels': rowlabel,
            'total': totalarr,
            'datavalues': finalarr,
            'str': str,
            'sbe': np.array(sbe),
            'sels': np.array(sels),
            'sets': np.array(sets),
            'slass': np.array(slass),
            'spph': np.array(spph),
        })
    else:
        return render(request, 'ClassSizeDistribution.html', {
            'semesterList':semesterList,
            'yearList': yearList,
        })



def UsageOfTheResourcesView(request):
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
            table.append([rowlabel[count], int(item1), item2, item3, item4, item5])
            if count == 0:
                list_col = [item2, item3, item4, item5]
            count=count+1

        count = 0
        for item in list_col:
            if count == 3:
                table2.append([rowlabel2[count], f'{list_col[count]} %'])
            else:
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



def EnrollmentBreakdownOfSchoolView(request):
    if request.method == "POST":
        semester = request.POST['semester']
        year = request.POST['year']
        strr = semester + " " + year

        collabel = ["Enrollment", "SBE", "SELS", "SETS", "SLASS", "SPPH", "Total"]
        table = [collabel]
        rowlabel = []
        
        for i in range(62):
            num= i+1
            rowlabel.append(f'{num}')
        rowlabel.append('Total')

        sbet = 0
        selst = 0
        setst = 0
        slasst = 0
        sppht = 0
        totalt = 0
        for i in range(63):
            n = i+1
            sbe = chartQueries.EnrollmentBreakdownOfSchool(n, "SBE", year, semester)
            sels = chartQueries.EnrollmentBreakdownOfSchool(n, "SELS", year, semester)
            sets = chartQueries.EnrollmentBreakdownOfSchool(n, "SETS", year, semester)
            slass = chartQueries.EnrollmentBreakdownOfSchool(n, "SLASS", year, semester)
            spph = chartQueries.EnrollmentBreakdownOfSchool(n, "SPPH", year, semester)

            sbe = str(sbe)[2:-3]
            sels = str(sels)[2:-3]
            sets = str(sets)[2:-3]
            slass = str(slass)[2:-3]
            spph = str(spph)[2:-3]

            total =  int(sbe) + int(sels) + int(sets) + int(slass) + int(spph)
            
            sbet += int(sbe)
            selst += int(sels)
            setst += int(sets)
            slasst += int(slass)
            sppht += int(spph)
            totalt += total
            
            if n == 63:
                table.append([rowlabel[i], sbet, selst, setst, slasst, sppht, totalt])
            else:
                table.append([rowlabel[i], sbe, sels, sets, slass, spph, total])

        return render(request, 'enrollmentBreakdownOfSchool.html', {
            'semesterList':semesterList,
            'yearList': yearList,
            'str': strr,
            'table': table,

        })

    else:
        return render(request, 'enrollmentBreakdownOfSchool.html', {
            'semesterList':semesterList,
            'yearList': yearList,
        })



def IUBavailableResourcesView(request):
    if request.method == "POST":
        semester = request.POST['semester']
        year = request.POST['year']
        str = semester + " " + year
        # here Table is row-wise object data
        finalarr = chartQueries.UsageOfTheResources(semester, year)
        count = 0
        percentage = 0
        for item1, item2, item3, item4, item5 in finalarr:
            if count == 0:
                list_col = [item2, item3, item4, item5]
            count=count+1