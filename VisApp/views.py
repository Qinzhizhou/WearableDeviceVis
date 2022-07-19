from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "index.html")

def readfile(uploaded_file):  #, experimentid):
    global file_directory
    savefile = FileSystemStorage()
    name = savefile.save(uploaded_file.name, uploaded_file)
    d = os.getcwd()  # current working directory
    file_directory = d + '\media\\' + name
    #if experimentid == "FreeLiving":
    #    file_directory = d + '\media\treadmill\\' + name
    #    print(file_directory)
    #else:
    #    file_directory = d + '\media\freeliving\\' + name
    #    print(file_directory)
    return file_directory

def upload(request):
    # render function takes argument  - request
    # and return HTML as response
    global attribute, file_type, file_directory
    file_type = ""
    context = {}

    if request.method == "POST":
        uploaded_file = request.FILES['document']
        #attribute = request.POST.get('attributeid')
        experimentid = request.POST.get('experimentid')
        print(experimentid)
        #print(uploaded_file)attributeid
        print("experimentid")#,experimentid)
        if uploaded_file.name.endswith('.xlsx') and experimentid == "FreeLiving":
            file_directory = readfile(uploaded_file)#, experimentid)
            readfree_living(file_directory, request)
            return redirect(results_living)

        elif uploaded_file.name.endswith('.xlsx') and experimentid == "Threadmill":
            file_directory = readfile(uploaded_file)#, experimentid)
            pread_living(file_directory, request)
            return redirect(results_thread)
        else:
            messages.warning(request, 'File was not uploaded, please use csv file!')
    return render(request, "upload.html", context)



def readfree_living(filename, request):
    global rows, cols, data, my_file, missing_values
    day = request.POST.get("dayid", None)
    if day == None:
        print("dafault day set as day1")
        day ='day1'

    my_file = pd.ExcelFile(filename)
    data = my_file.parse(day, header=None, names=['Time', 'A', 'B', 'C', 'D', 'E'])
    data['Time'] = pd.to_datetime(data['Time'])
    # make the required change
    without_date = data['Time'].apply(lambda d: d.time())
    data['Time'] = without_date
    # row and colomn
    rows = len(data.axes[0])
    cols = len(data.axes[1])
    # find missing data
    missingvalue = ['', '?']
    null_data = data[data.isnull().any(axis=1)]  # find the missing data
    missing_values = len(null_data)


def addY(Values):
    value_list = []
    for y in Values:
        value_list.append(y)
    return value_list

def results_living(request):
    message = ''
    message = 'I found ' + str(rows) + ' and columns ' + str(cols) + ' columns, Missing data are: ' + str(missing_values)
    messages.warning(request, message)
    keys = data.Time
    valuesA = data.A
    timelines = []
    vA, vB, vC, vD, vE   = addY(data.A),  addY(data.B),  addY(data.C),  addY(data.D),  addY(data.E)
    for x in keys:
        timelines.append(str(x))
    context = {
    'timelines': timelines,
    'vA': vA,
    'vB': vB,
    'vC': vC,
    'vD': vD,
    'vE': vE,
    }
    #print(data[attribute])
    print("loading image")
    return render(request, "results_freeliving.html", context)


def results_thread(request):
    message = ''
    message = 'I found ' + str(rows) + ' and columns ' + str(cols) + ' columns, Missing data are: ' + str(missing_values)
    messages.warning(request, message)

    data.fillna(0)


    keys = data.iloc[:, 0]

    timelines = []
    vA, vB, vC, vD = addY(data.GT),  addY(data['Fitbit Charge HR']),  addY(data['Fitbit Charge 2']),  addY(data['Fitbit Surge'])

    for x in keys:
        timelines.append(str(x))

    context = {
    'timelines': timelines,
    'vA': vA,
    'vB': vB,
    'vC': vC,
    'vD': vD,
    }
    #print(data[attribute])
    print("loading image")
    return render(request, "results_threadmill.html", context)

def renew(request):
    global rows, cols, data, my_file, missing_values
    context = {}
    my_file = pd.ExcelFile(file_directory)
    day = request.POST.get("dayid", None)
    if day == None:
        print("dafault day set as day1")
        day ='day1'
    print("days:", day)
    # Read the excel file and thransform them is pd.data frame
    data = my_file.parse(day, header=None, names=['Time', 'A', 'B', 'C', 'D', 'E'])
    data['Time'] = pd.to_datetime(data['Time'])
    without_date = data['Time'].apply(lambda d: d.time())
    data['Time'] = without_date
    #row and colomn
    rows = len(data.axes[0])
    cols = len(data.axes[1])
    #find missing data
    missingvalue = ['', '?']
    null_data = data[data.isnull().any(axis=1)]  # find the missing data
    missing_values = len(null_data)
    message = ''
    message = 'I found ' + str(rows) + ' and columns ' + str(cols) + ' columns, Missing data are: ' + str(missing_values)
    messages.warning(request, message)
    keys = data.Time
    timelines = []
    vA, vB, vC, vD, vE = addY(data.A), addY(data.B), addY(data.C), addY(data.D), addY(data.E)
    for x in keys:
        timelines.append(str(x))
    context = {
        'timelines': timelines,
        'vA': vA,
        'vB': vB,
        'vC': vC,
        'vD': vD,
        'vE': vE,
    }
    # print(data[attribute])
    print("loading image")
    return render(request, "results_freeliving.html", context)

def pread_living(filename, request):
    global rows, cols, data, my_file, missing_values
    #if file_type == 'csv':
    my_file = pd.ExcelFile(filename)
    # Print the sheet names
    data = my_file.parse("Heart Rate",  header = 1)
    data = data.fillna(0)
    print(data)
    # row and colomn
    rows = len(data.axes[0])
    cols = len(data.axes[1])
    missingvalue = ['', '?']
    null_data = data[data.isnull().any(axis=1)]  # find the missing data
    missing_values = len(null_data)

def renew_pread(request):
    global rows, cols, data, my_file, missing_values
    context = {}
    my_file = pd.ExcelFile(file_directory)
    type = request.POST.get("typeid", None)

    if type == None:
        print("dafault type set as Heart Rate")
        type ='day1'
    print("type:", type)

    # Read the excel file and thransform them is pd.data frame
    data = my_file.parse(type, header=1)
    data = data.fillna(0)
    #row and colomn
    rows = len(data.axes[0])
    cols = len(data.axes[1])
    #find missing data
    missingvalue = ['', '?']
    null_data = data[data.isnull().any(axis=1)]  # find the missing data
    missing_values = len(null_data)
    message = ''
    message = 'I found ' + str(rows) + ' and columns ' + str(cols) + ' columns, Missing data are: ' + str(missing_values)
    messages.warning(request, message)

    keys = data.iloc[:, 0]
    timelines = []
    vA, vB, vC, vD = addY(data.GT), addY(data['Fitbit Charge HR']), addY(data['Fitbit Charge 2']), addY(
        data['Fitbit Surge'])

    for x in keys:
        timelines.append(str(x))
    context = {
        'timelines': timelines,
        'vA': vA,
        'vB': vB,
        'vC': vC,
        'vD': vD,
    }
    # print(data[attribute])
    print("loading image")
    return render(request, "results_threadmill.html", context)