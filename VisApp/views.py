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
            messages.warning(request, 'File was not uploaded, please use xlsx file!')
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
    missingvalue = ['', '?', '0', '-']

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
    print("keys ",keys)
    valuesA = data.A
    timelines = []
    vA, vB, vC, vD, vE   = addY(data.A),  addY(data.B),  addY(data.C),  addY(data.D),  addY(data.E)
    nA = normalize_list(vA)
    nB = normalize_list(vB)
    nC = normalize_list(vC)
    nE = normalize_list(vE)
    nD = normalize_list(vD)
    for x in keys:
        timelines.append(str(x))
    context = {
    'timelines': timelines,
    'vA': vA,
    'vB': vB,
    'vC': vC,
    'vD': vD,
    'vE': vE,
    'nA': nA,
    'nB': nB,
    'nC': nC,
    'nD': nD,
    'nE': nE,
    }
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
    nA = normalize_list(vA)
    nB = normalize_list(vB)
    nC = normalize_list(vC)
    nD = normalize_list(vD)

    for x in keys:
        timelines.append(str(x))

    context = {
    'timelines': timelines,
    'vA': vA,
    'vB': vB,
    'vC': vC,
    'vD': vD,
        'nA': nA,
        'nB': nB,
        'nC': nC,
        'nD': nD,
    }
    #print(data[attribute])
    print("loading image")
    return render(request, "results_threadmill.html", context)

def normalize_list(list):
    max_value = max(list)
    min_value = min(list)
    norm_list = []
    if max_value - min_value == 0:
        norm_list.append(0)
    else:
        for i in range(0, len(list)):
            norm_list.append((list[i] - min_value) / (max_value - min_value))
    return norm_list

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
    nA = normalize_list(vA)
    nB = normalize_list(vB)
    nC = normalize_list(vC)
    nE = normalize_list(vE)
    nD = normalize_list(vD)
    for x in keys:
        timelines.append(str(x))
    context = {
        'timelines': timelines,
        'vA': vA,
        'vB': vB,
        'vC': vC,
        'vD': vD,
        'vE': vE,
        'nA': nA,
        'nB': nB,
        'nC': nC,
        'nD': nD,
        'nE': nE,
    }
    # print(data[attribute])
    print("loading image")
    print(nA)
    return render(request, "results_freeliving.html", context)

def pread_living(filename, request):
    global rows, cols, data, my_file, missing_values
    #if file_type == 'csv':
    my_file = pd.ExcelFile(filename)
    # Print the sheet names
    data = my_file.parse("Heart Rate",  header = 1)
    data = data.fillna(0)

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
        type ='Heart Rate'
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
    nA = normalize_list(vA)
    nB = normalize_list(vB)
    nC = normalize_list(vC)
    nD = normalize_list(vD)

    for x in keys:
        timelines.append(str(x))

    context = {
        'timelines': timelines,
        'vA': vA,
        'vB': vB,
        'vC': vC,
        'vD': vD,
        'nA': nA,
        'nB': nB,
        'nC': nC,
        'nD': nD,
    }


    # print(data[attribute])
    print("loading image")
    return render(request, "results_threadmill.html", context)

def dashboard(request):
    return render(request, "dashboard.html")

def compare(request):
    # render function takes argument  - request
    # and return HTML as response
    global uploaded_files, file_directory_list, experimentid
    file_type = ""
    context = {}

    if request.method == "POST":
        uploaded_files = []
        for file_id, file in enumerate(request.FILES.getlist("files")):
            uploaded_files.append(file)
        experimentid = request.POST.get('experimentid')
        length_list = []

        if len(uploaded_files) <= 4 and experimentid == "FreeLiving":
            data = pd.DataFrame(columns=['Time', 'A', 'B', 'C', 'D', 'E'])
            file_directory_list = []
            for i in uploaded_files:
                    file_directory = readfile(i)  # read the i th file
                    file_directory_list.append(file_directory)
            for directory in file_directory_list:
                if i.name.endswith('.xlsx'):
                    length_list.append(len(read_com_free(directory, request)))
                    data = pd.concat([data, read_com_free(directory, request)], ignore_index=True)
            while len(length_list) < 4:
                length_list.append(0)

            l1 = length_list[0]
            l2 = length_list[0] + length_list[1]
            l3 = length_list[0] + length_list[1] + length_list[2]
            l4 = length_list[0] + length_list[1] + length_list[2] + length_list[3]

            timelines = addY(data[:, 0])

            vA, vB, vC, vD, vE = addY(data.iloc[:l1].A), addY(data.iloc[:l1].B), addY(
                data.iloc[:l1].C), addY(data.iloc[:l1].D), addY(data.iloc[:l1].E)
            vF, vG, vH, vI, vJ = addY(data.iloc[l1:l2].A), addY(data.iloc[l1:l2].B), addY(
                data.iloc[l1:l2].C), addY(data.iloc[l1:l2].D), addY(data.iloc[l1:l2].E)
            vK, vL, vM, vN, vO = addY(data.iloc[l2:l3].A), addY(data.iloc[l2:l3].B), addY(
                data.iloc[l2:l3].C), addY(data.iloc[l2:l3].D), addY(data.iloc[l2:l3].E)
            vP, vQ, vR, vS, vT = addY(data.iloc[l3:l4].A), addY(data.iloc[l3:l4].B), addY(
                data.iloc[l3:l4].C), addY(data.iloc[l3:l4].D), addY(data.iloc[l3:l4].E)

            context = {
                'timelines': timelines,
                'vA': vA,
                'vB': vB,
                'vC': vC,
                'vD': vD,
                'vE': vE,
                'vF': vF,
                'vG':vG,
                'vH':vH,
                'vI':vI,
                'vJ': vJ,
                'vK': vK,
                'vL': vL,
                'vM': vM,
                'vN': vN,
                'vO': vO,
                'vP': vP,
                'vQ': vQ,
                'vR': vR,
                'vS': vS,
                'vT': vT
            }
            print("loading compare image")
            return render(request, "compare_freeliving.html", context)
        elif len(uploaded_files) <= 4 and experimentid == "Threadmill":
            data = pd.DataFrame(columns=['Time Count(Every 10 seconds)', 'GT', 'Fitbit Charge HR', 'Fitbit Charge 2', 'Fitbit Surge'])
            file_directory_list = []
            for i in uploaded_files:
                file_directory = readfile(i)  # read the i th file
                file_directory_list.append(file_directory)
            for directory in file_directory_list:
                if i.name.endswith('.xlsx'):
                    length_list.append(len(read_com_threa(directory, request)))
                    data = pd.concat([data, read_com_threa(directory, request)], ignore_index=True)
            while len(length_list) < 4:
                length_list.append(0)
            print(length_list)

            while len(length_list) < 4:
                length_list.append(0)
            keys = data.iloc[:181]['Time Count(Every 10 seconds)']
            timelines = []

            for x in keys:
                timelines.append(str(x))

            l1 = length_list[0]
            l2 = length_list[0] + length_list[1]
            l3 = length_list[0] + length_list[1] + length_list[2]
            l4 = length_list[0] + length_list[1] + length_list[2] + length_list[3]

            vA, vB, vC, vD = addY(data.iloc[:l1].GT), addY(data.iloc[:l1]['Fitbit Charge HR']), addY(data.iloc[:l1]['Fitbit Charge 2']), addY(
                data.iloc[:l1]['Fitbit Surge'])
            vE, vF, vG, vH = addY(data.iloc[l1:l2].GT), addY(data.iloc[l1:l2]['Fitbit Charge HR']), addY(data.iloc[l1:l2]['Fitbit Charge 2']), addY(
                data.iloc[l1:l2]['Fitbit Surge'])
            vI, vJ, vK, vL = addY(data.iloc[l2:l3].GT), addY(data.iloc[l2:l3]['Fitbit Charge HR']), addY(
                data.iloc[l2:l3]['Fitbit Charge 2']), addY(data.iloc[l2:l3]['Fitbit Surge'])
            vM, vN, vO, vP = addY(data.iloc[l3:l4].GT), addY(data.iloc[l3:l4]['Fitbit Charge HR']), addY(
                data.iloc[l3:l4]['Fitbit Charge 2']), addY(data.iloc[l3:l4]['Fitbit Surge'])
            context = {
                'timelines': timelines,
                'vA': vA,
                'vB': vB,
                'vC': vC,
                'vD': vD,

                'vE': vE,
                'vF': vF,
                'vG': vG,
                'vH': vH,

                'vI': vI,
                'vJ': vJ,
                'vK': vK,
                'vL': vL,

                'vM': vM,
                'vN': vN,
                'vO': vO,
                'vP': vP
            }
            print("loading compare image")
            return render(request, "compare_pthread.html", context)


        else:
            messages.warning(request, 'You uploaded too much files!')
    return render(request, "compare.html")


def read_com_free(directory, request):
    global rows, cols, data, my_file, missing_values
    day = request.POST.get("dayid", None)
    if day == None:
        print("dafault day set as day1")
        day = 'day1'
    print("the day set as :", day)
    my_file = pd.ExcelFile(directory)
    data = my_file.parse(day, header=None, names=['Time', 'A', 'B', 'C', 'D', 'E'])
    data['Time'] = pd.to_datetime(data['Time'])
    # make the required change
    without_date = data['Time'].apply(lambda d: d.time())
    data['Time'] = without_date
    null_data = data[data.isnull().any(axis=1)]  # find the missing data
    missing_values = len(null_data)
    return data

def read_com_threa(directory, request):
    global rows, cols, data, my_file, missing_values
    # if file_type == 'csv':
    type = request.POST.get("typeid", None)
    my_file = pd.ExcelFile(directory)
    if type == None:
        print("dafault type set as Heart Rate")
        type = 'Heart Rate'
    # Print the sheet names
    data = my_file.parse(type, header=1)
    data = data.fillna(0)
    # row and colomn
    rows = len(data.axes[0])
    cols = len(data.axes[1])
    missingvalue = ['', '?']
    null_data = data[data.isnull().any(axis=1)]  # find the missing data
    missing_values = len(null_data)
    return data



def renew_com_living(request):
    context = {}
    day = request.POST.get("dayid", None)
    if day == None:
        day ='day1'
    print("the day set as: ", day)
    print("file directory list: ", file_directory_list)

    length_list = []
    data = pd.DataFrame(columns=['Time', 'A', 'B', 'C', 'D', 'E'])

    for directory in file_directory_list:
        print('The directory: ', directory)
        length_list.append(len(read_com_free(directory, request)))
        data = pd.concat([data, read_com_free(directory, request)], ignore_index=True)


    while len(length_list) < 4:
        length_list.append(0)

    print(length_list)

    keys = data.iloc[:920].Time
    timelines = []

    l1 = length_list[0]
    l2 = length_list[0] + length_list[1]
    l3 = length_list[0] + length_list[1] + length_list[2]
    l4 = length_list[0] + length_list[1] + length_list[2] + length_list[3]

    print(l1, l2, l3,l4)


    vA, vB, vC, vD, vE = addY(data.iloc[:l1].A), addY(data.iloc[:l1].B), addY(
            data.iloc[:l1].C), addY(data.iloc[:l1].D), addY(data.iloc[:l1].E)
    vF, vG, vH, vI, vJ = addY(data.iloc[l1:l2].A), addY(data.iloc[l1:l2].B), addY(
            data.iloc[l1:l2].C), addY(data.iloc[l1:l2].D), addY(data.iloc[l1:l2].E)
    vK, vL, vM, vN, vO = addY(data.iloc[l2:l3].A), addY(data.iloc[l2:l3].B), addY(
            data.iloc[l2:l3].C), addY(data.iloc[l2:l3].D), addY(data.iloc[l2:l3].E)
    vP, vQ, vR, vS, vT = addY(data.iloc[l3:l4].A), addY(data.iloc[l3:l4].B), addY(
            data.iloc[l3:l4].C), addY(data.iloc[l3:l4].D), addY(data.iloc[l3:l4].E)

    for x in keys:
        timelines.append(str(x))
    context = {
                'timelines': timelines,
                'vA': vA,
                'vB': vB,
                'vC': vC,
                'vD': vD,
                'vE': vE,
                'vF': vF,
                'vG':vG,
                'vH':vH,
                'vI':vI,
                'vJ': vJ,
                'vK': vK,
                'vL': vL,
                'vM': vM,
                'vN': vN,
                'vO': vO,
                'vP': vP,
                'vQ': vQ,
                'vR': vR,
                'vS': vS,
                'vT': vT
            }

    print("loading compare image")

    return render(request, "compare_freeliving.html", context)

def renew_com_pread(request):
    context = {}
    type = request.POST.get("typeid", None)
    if type == None:
        print("dafault type set as Heart Rate")
        type = 'Heart Rate'
    print("type:", type)
    length_list = []
    if type == 'Heart Rate':
        data = pd.DataFrame(columns=['Time Count(Every 10 seconds)', 'GT', 'Fitbit Charge HR', 'Fitbit Charge 2', 'Fitbit Surge'])
    else:
        data = pd.DataFrame(
            columns=['Time Count(Every 60 seconds)', 'GT', 'Fitbit Charge HR', 'Fitbit Charge 2', 'Fitbit Surge'])
    for directory in file_directory_list:
        print('The directory: ', directory)
        length_list.append(len(read_com_threa(directory, request)))
        print(read_com_threa(directory, request))
        data = pd.concat([data, read_com_threa(directory, request)], ignore_index=True)
    while len(length_list) < 4:
        length_list.append(0)

    while len(length_list) < 4:
        length_list.append(0)

    l1 = length_list[0]
    l2 = length_list[0] + length_list[1]
    l3 = length_list[0] + length_list[1] + length_list[2]
    l4 = length_list[0] + length_list[1] + length_list[2] + length_list[3]

    if type == 'Heart Rate':
        keys = data.iloc[:181]['Time Count(Every 10 seconds)']
    else:
        #keys = data.iloc[:181]['Time Count(Every 60 seconds)']
        keys = data.iloc[:, 0][:30]
    timelines = []
    for x in keys:
        timelines.append(str(x))
    print(timelines)
    vA, vB, vC, vD = addY(data.iloc[:l1].GT), addY(data.iloc[:l1]['Fitbit Charge HR']), addY(
        data.iloc[:l1]['Fitbit Charge 2']), addY(data.iloc[:l1]['Fitbit Surge'])
    vE, vF, vG, vH = addY(data.iloc[l1:l2].GT), addY(data.iloc[l1:l2]['Fitbit Charge HR']), addY(
        data.iloc[l1:l2]['Fitbit Charge 2']), addY(data.iloc[l1:l2]['Fitbit Surge'])
    vI, vJ, vK, vL = addY(data.iloc[l2:l3].GT), addY(data.iloc[l2:l3]['Fitbit Charge HR']), addY(
        data.iloc[l2:l3]['Fitbit Charge 2']), addY(data.iloc[l2:l3]['Fitbit Surge'])
    vM, vN, vO, vP = addY(data.iloc[l3:l4].GT), addY(data.iloc[l3:l4]['Fitbit Charge HR']), addY(
        data.iloc[l3:l4]['Fitbit Charge 2']), addY(data.iloc[l3:l4]['Fitbit Surge'])
    print('vM:', vM)

    context = {
        'timelines': timelines,
        'vA': vA,
        'vB': vB,
        'vC': vC,
        'vD': vD,
        'vE': vE,
        'vF': vF,
        'vG': vG,
        'vH': vH,
        'vI': vI,
        'vJ': vJ,
        'vK': vK,
        'vL': vL,
         'vM': vM,
        'vN': vN,
        'vO': vO,
        'vP': vP
    }
    print("loading compare image")
    return render(request, "compare_pthread.html", context)




