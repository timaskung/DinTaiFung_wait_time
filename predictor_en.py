# This tool is used to predict the waiting time for the Din Tai Fung branches in Taiwan.
from tkinter import *
import csv


# Takes the branch and day of the week and returns a list with the mean waiting times and number of data points used
# Uses the merged CSV of waiting times
def branch_day_mean_table(branch_name, day_short):
    # Index of each branch in the waiting time data CSV
    branches_index_en = {
        'Fuxing': 3,
        'Tienmu': 4,
        'Hsinchu': 5,
        'Taipei 101': 6,
        'Taichung': 7,
        'Banqiao': 8,
        'Kaohsiung': 9,
        'Nanxi': 10,
        'A4': 11,
        'A13': 12,
        'Xinsheng': 13,
    }

    # Open the waiting time data CSV and creates list with each row of CSV as an element
    file_path = 'waiting_time_merged_0713.csv'
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Get a list of unique times
    time_list = []
    for i in range(1, len(rows)):
        time_list.append(rows[i][2])
    time_list = list(set(time_list))
    time_list.sort()

    # Create a new table of all the collected waiting times at a particular branch on a day of the week
    branch_index = branches_index_en[branch_name]
    new_table = []
    for time in time_list:
        new_table.append([time])
        for i in range(1, len(rows)):  # Iterate through the waiting times data, excluding header
            if rows[i][1] == day_short and rows[i][2] == time:
                if rows[i][branch_index] != '':
                    new_table[time_list.index(time)].append(float(rows[i][branch_index]))  # Appends non-empty data

    # Use the previous table to calculate mean waiting time and count number of data points used
    mean_table = []
    for row in new_table:
        wait_time_sum = 0
        for i in range(1, len(row)):
            wait_time_sum += row[i]
        if len(row) > 1:
            waiting_time = round(wait_time_sum/(len(row) - 1))
        else:
            waiting_time = 'NA'
        mean_table.append([row[0], waiting_time, len(row)-1])

    return mean_table


# Use the branch_day_mean_table function to get find waiting time for specific time
def branch_day_time(branch_name, day_short, time):
    mean_table = branch_day_mean_table(branch_name, day_short)
    for row in mean_table:
        if time in row:
            return row[1]


# Gets the values from the Option Menus and uses branch_day_time to get predicted waiting time
def predict():
    global label_result
    branch_var = branch.get()
    day_var = day.get()
    days_convert = {
        "Monday": "M",
        "Tuesday": "T",
        "Wednesday": "W",
        "Thursday": "H",
        "Friday": "F",
        "Saturday": "S",
        "Sunday": "N",
    }
    hour_var = hour.get()
    minute_var = minute.get()
    full_time = hour_var + ':' + minute_var
    waiting_time = branch_day_time(branch_var, days_convert[day_var], full_time)
    label_result.destroy()
    if waiting_time == 'NA':
        label_result = Label(root, text=f'The predicted waiting time for {branch_var} branch on {day_var} at {full_time} '
                                        f'is not available.', bg='Black', fg='white', padx=10)
    else:
        label_result = Label(root, text=f'The predicted waiting time for {branch_var} branch on {day_var} at {full_time} '
                                        f'is {waiting_time} minutes.', bg='Black', fg='white', padx=10)
    label_result.grid(row=6, column=0, columnspan=4, padx=10)


# Initialize window
root = Tk()
root.title("Din Tai Fung waiting time predictor")
root.geometry('560x200')

# Place labels
Label(root, text="Select a branch, a day of the week, and time of day:", padx=5)\
    .grid(row=0, column=0, columnspan=3, sticky='W')
Label(root, text='Branch:', pady=5, padx=5).grid(row=1, column=0, sticky='W')
Label(root, text='Day:', pady=5, padx=5).grid(row=2, column=0, sticky='W')
Label(root, text='Time:', pady=5, padx=5).grid(row=3, column=0, sticky='W')

# Drop down menu to select branch, day, time
branches = ['Fuxing', 'Tienmu', 'Hsinchu', 'Taipei 101', 'Taichung', 'Banqiao',
            'Kaohsiung', 'Nanxi', 'A4', 'A13', 'Xinsheng']
branch = StringVar()
branch.set(branches[0])  # Set default value
drop_branch = OptionMenu(root, branch, *branches)
drop_branch.grid(row=1, column=1, sticky='w')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = StringVar()
day.set(days[0])
drop_day = OptionMenu(root, day, *days)
drop_day.grid(row=2, column=1, sticky='w')

hours = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
hour = StringVar()
hour.set(hours[0])
drop_hour = OptionMenu(root, hour, *hours)
drop_hour.grid(row=3, column=1, sticky='w')

minutes = ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
minute = StringVar()
minute.set(minutes[0])
drop_min = OptionMenu(root, minute, *minutes)
drop_min.grid(row=3, column=2, sticky='w')

# Initialize result label
label_result = Label(root)
label_result.grid(row=6, columnspan=3)

# Buttons to predict waiting time or close window
Button(root, text='Predict!', command=predict).grid(row=4)
Button(root, text='Close', command=root.destroy).grid(row=5)
root.mainloop()
