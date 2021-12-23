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
            'sbe': np.array(sbe).flatten(),
            'sels': np.array(sels).flatten(),
            'sets': np.array(sets).flatten(),
            'slass': np.array(slass).flatten(),
            'spph': np.array(spph).flatten(),
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

        rowlabel2 = ["Average of ENROLLED", "Average of ROOM CAPACITY", "Average of Unused Space", "Unused Percent"]
        count = 0
        percentage = 0.0
        list_col = []
        for item1, item2, item3, item4, item5 in finalarr:
            table.append([rowlabel[count], int(item1), item2, item3, item4, item5])
            if count == 0:
                percentage = item5
                list_col = [item2, item3, item4, item5]
            count=count+1

        count = 0
        for item in list_col:
            if count == 3:
                table2.append([rowlabel2[count], f'{list_col[count]} %'])
            else:
                table2.append([rowlabel2[count], list_col[count]])
            count+=1
        
        ##########################################################################################################
        # For IUB Available Recources
        ##########################################################################################################
        rowlabel3 = ["20", "30", "35", "40", "50", "54", "64", "124", "168", "Total"]
        collabel2 = ["Class Size", "IUB resource", "Capacity"]
        factor = (100-percentage)/100
        arr = chartQueries.IUBavailableResources()
        arr = np.array(arr)
        count = 0
        iubt = 0
        capacityt = 0
        table3 = [collabel2]
        table4 = []
        for item1, item2 in arr:
            iubt+=item1
            capacityt+=item2
            table3.append([rowlabel3[count], item1, item2])
            count+=1
            

        table3.append([rowlabel3[9], iubt, capacityt])

        rowlabel4 = ["Total Capacity with 6 slot 2 days", "Total Capacity with 7 slot 2 days",
                    "Considering 3.5 average course load (6 slot)", "Considering 3.5 average course load (7 slot)",
                    "Considering free % for 6 slots capacity", "Considering free % for 7 slots capacity"]
        
        for i in range(6):
            if i == 0:
                table4.append([ rowlabel4[i], capacityt*12])
            elif i == 1:
                table4.append([ rowlabel4[i], capacityt*14])
            elif i == 2:
                table4.append([ rowlabel4[i], int((capacityt*12)/3.5) ])
            elif i == 3:
                table4.append([ rowlabel4[i], int((capacityt*14)/3.5) ])
            elif i == 4:
                table4.append([ rowlabel4[i], int(((capacityt*12)/3.5)*factor) ])
            elif i == 5:
                table4.append([ rowlabel4[i], int(((capacityt*14)/3.5)*factor) ])

        
        return render(request, 'usageOfTheResources.html', {
            'semesterList':semesterList,
            'yearList': yearList,
            'table': table,
            'table2': table2,
            'table3': table3,
            'table4': table4,
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



def AvailabilityAndCourseOfferingComparisonView(request):
    if request.method == "POST":
        semester1 = request.POST['semester1']
        year = request.POST['year']
        semester2 = request.POST['semester2']
        strr = semester1 + " and " + semester2 + " in " + year

        arr = chartQueries.IUBavailableResources()
        arr = np.array(arr)
        sem1 = chartQueries.AvailabilityAndCourseOfferingComparison(semester1, year)
        sem1 = np.array(sem1)
        sem2 = chartQueries.AvailabilityAndCourseOfferingComparison(semester2, year)
        sem2 = np.array(sem2)

        sem1 = sem1.flatten()         
        sem2 = sem2.flatten()
        collabel = ["Class size", "IUB resource", semester1, "Difference", semester2, "Difference"]
        rowlabel = ["20", "30", "35", "40", "50", "54", "64", "124", "168", "Total"]

        count = 0
        iubt = 0
        sem1t = 0
        sem2t = 0
        diff1t = 0
        diff2t = 0
        table = [collabel]

        iublist = []
        for item1, item2 in arr:
            diff1 = item1 - sem1[count]
            diff2 = item1 - sem2[count]

            iubt+=item1
            sem1t+= sem1[count]
            sem2t+= sem2[count]
            diff1t += diff1
            diff2t += diff2
            iublist.append(item1)
            table.append([ rowlabel[count], item1, sem1[count], "{:.2f}".format(diff1), sem2[count], "{:.2f}".format(diff2) ])  
            count+=1

        table.append([rowlabel[9], "{:.2f}".format(iubt), "{:.2f}".format(sem1t), "{:.2f}".format(diff1t), "{:.2f}".format(sem2t), "{:.2f}".format(diff2t) ])
        labels = ["20", "30", "35", "40", "50", "54", "64", "124", "168"]

        return render(request, 'availabilityAndCourseOfferingComparison.html', {
            'semesterList':semesterList,
            'yearList': yearList,
            'str': strr,
            'table': table,
            'iub': iublist,
            'datavalues1': sem1,
            'datavalues2': sem2,
            'labels': labels,
            'Semester1': semester1,
            'Semester2': semester2,

        })

    else:
        return render(request, 'availabilityAndCourseOfferingComparison.html', {
            'semesterList':semesterList,
            'yearList': yearList,
        })



def RevenueTrendOfTheSchoolsView(request):
    if request.method == "POST":
        collabel = ["-", "SBE", "SETS", "SELS", "SLASS", "SPPH", "Total", "Change %"]
        rowlabel = ["2009 Spring", "2009 Summer", "2009 Autumn", "2010 Spring", "2010 Summer", "2010 Autumn", "2011 Spring", "2011 Summer", "2011 Autumn", 
                    "2012 Spring", "2012 Summer", "2012 Autumn", "2013 Spring", "2013 Summer", "2013 Autumn", "2014 Spring", "2014 Summer", "2014 Autumn", 
                    "2015 Spring", "2015 Summer", "2015 Autumn", "2016 Spring", "2016 Summer", "2016 Autumn", "2017 Spring", "2017 Summer", "2017 Autumn", 
                    "2018 Spring", "2018 Summer", "2018 Autumn", "2019 Spring", "2019 Summer", "2019 Autumn", "2020 Spring", "2020 Summer", "2020 Autumn", 
                    "2021 Spring", "2021 Summer"]

        sbe = []
        sets = []
        sels = []
        slass = []
        spph = []

        for i in range(38):
            temp = rowlabel[i].split()
            year = temp[0]
            semester = temp[1]
            sbe.append(chartQueries.RevenueTrendOfTheSchools("SBE", semester, year))
            sets.append(chartQueries.RevenueTrendOfTheSchools("SETS", semester, year))
            sels.append(chartQueries.RevenueTrendOfTheSchools("SELS", semester, year))
            slass.append(chartQueries.RevenueTrendOfTheSchools("SLASS", semester, year))
            spph.append(chartQueries.RevenueTrendOfTheSchools("SPPH", semester, year))

        table = [collabel]
        sbe = np.array(sbe).flatten()
        sets = np.array(sets).flatten()
        sels = np.array(sels).flatten()
        slass = np.array(slass).flatten()
        spph = np.array(spph).flatten()
        print(sbe)
        totalarr = []
        changearr= []

        for i in range(38):
            total = sbe[i] + sets[i] + sels[i] + slass[i] + spph[i]
            totalarr.append(total)
            change = 0
            table.append([rowlabel[i], sbe[i], sets[i], sels[i], slass[i], spph[i], total, change])
        print(totalarr)

        return render(request, 'revenueTrendOfTheSchools.html', { 
            'sbe': sbe,
            'sets': sets,
            'sels': sels,
            'slass': slass,
            'spph': spph,
            'table': table,
            'labels': rowlabel,
        })

    else:
        return render(request, 'revenueTrendOfTheSchools.html')





def RevenueInEngineeringSchoolView(request):
    if request.method == "POST":
        print("success")
    
        return render(request, 'revenueInEngineeringSchool.html', { 
            
        })

    else:
        return render(request, 'revenueInEngineeringSchool.html')