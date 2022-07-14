from django.shortcuts import render, redirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

import os
import pandas as pd


# Create your views here.
def index(request):
    return render(request, "index.html")

def upload(request):
    # render function takes argument  - request
    # and return HTML as response
    global attribute, file_type
    file_type = ""
    context = {}

    if request.method == "POST":
        uploaded_file = request.FILES['document']
        #attribute = request.POST.get('attributeid')
        experimentid = request.POST.get('experimentid')
        print(experimentid)

        #print(uploaded_file)attributeid
        print("experimentid",experimentid)
        if uploaded_file.name.endswith('.xlsx'):
            savefile = FileSystemStorage()
            name = savefile.save(uploaded_file.name, uploaded_file)
            d = os.getcwd()  # current working directory
            file_directory = d + '\media\\'+name
            print(file_directory)
            # readfile(file_directory)
            file_type = 'xlsx'
            readfile_xlsx(file_directory, request)
            return redirect(results)
        else:
            messages.warning(request, 'File was not uploaded, please use csv file!')
    return render(request, "upload.html", context)


def readfile_xlsx(filename, request):
    global rows, cols, data, my_file, missing_values
    #if file_type == 'csv':

    #day = request.POST.get('dayid')
    day = 'day2'
    print("days:", day)

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
    missingvalue = ['','?']
    null_data = data[data.isnull().any(axis=1)] # find the missing data
    missing_values = len(null_data)

def addY(Values):
    value_list = []
    for y in Values:
        value_list.append(y)
    return value_list

def results(request):
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
    return render(request, "results.html",context)

def change_day(request):
    dayid = request.POST.get('dayid')
    print("days id: ", dayid)