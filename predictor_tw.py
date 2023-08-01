# This tool is used to predict the waiting time for the Din Tai Fung branches in Taiwan.
from tkinter import *
import csv


# Takes the branch and day of the week and returns a list with the mean waiting times and number of data points used
# Uses the merged CSV of waiting times
def branch_day_mean_table(branch_name, day_short):
    # Index of each branch in the waiting time data CSV
    branches_index_tw = {
        "復興店": 3,
        "天母店": 4,
        "新竹店": 5,
        "101店": 6,
        "台中店": 7,
        "板橋店": 8,
        "高雄店": 9,
        "南西店": 10,
        "A4店": 11,
        "A13店": 12,
        "新生店": 13,
    }

    # Open the waiting time data CSV and creates list with each row of CSV as an element
    file_path = 'waiting_time_merged.csv'
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
    branch_index = branches_index_tw[branch_name]
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
        "一": "M",
        "二": "T",
        "三": "W",
        "四": "H",
        "五": "F",
        "六": "S",
        "日": "N",
    }
    hour_var = hour.get()
    minute_var = minute.get()
    full_time = hour_var + ':' + minute_var
    waiting_time = branch_day_time(branch_var, days_convert[day_var], full_time)
    label_result.destroy()
    if waiting_time == 'NA':
        label_result = Label(root, text=f'鼎泰豐{branch_var}在星期{day_var} {full_time}預計等候時間目前無法取得。',
                                        bg='Black', fg='white', padx=10)
    else:
        label_result = Label(root, text=f'鼎泰豐{branch_var}在星期{day_var} {full_time}預計等候時間為'
                                        f'{waiting_time}分鐘。', bg='Black', fg='white', padx=10)
    label_result.grid(row=6, column=0, columnspan=4, padx=10)


# Initialize window
root = Tk()
root.title("鼎泰豐等候時間預測")
root.geometry('400x200')

# Place labels
Label(root, text="請選擇門市、星期幾以及時間:", padx=5)\
    .grid(row=0, column=0, columnspan=3, sticky='W')
Label(root, text='門市:', pady=5, padx=5).grid(row=1, column=0, sticky='W')
Label(root, text='星期幾:', pady=5, padx=5).grid(row=2, column=0, sticky='W')
Label(root, text='時間:', pady=5, padx=5).grid(row=3, column=0, sticky='W')

# Drop down menu to select branch, day, time
branches = ["復興店", "天母店", "新竹店", "101店", "台中店", "板橋店", "高雄店", "南西店", "A4店", "A13店", "新生店"]
branch = StringVar()
branch.set(branches[0])  # Set default value
drop_branch = OptionMenu(root, branch, *branches)
drop_branch.grid(row=1, column=1, sticky='w')

days = ['一', '二', '三', '四', '五', '六', '日']
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
Button(root, text='預測!', command=predict).grid(row=4)
Button(root, text='結束', command=root.destroy).grid(row=5)
root.mainloop()
