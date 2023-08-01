# Collects the waiting time at 5-minute intervals for Din Tai Fung branches in Taiwan
import requests
import json
from time import sleep, gmtime
import csv


# Takes the branch ID and obtains the current wait time from API
def get_wait_time(branch_id):
    # Define the URL of the server-side API
    url = "https://www.dintaifung.tw/Queue/Home/WebApiTest"

    # Define the data payload to send in the POST request
    payload = {
        "storeid": branch_id,
    }

    # Parse the JSON-formatted string into a Python object
    data = json.loads(requests.post(url, data=payload).content.decode('utf-8'))
    return data[0]['wait_time']


class Branch:

    def __init__(self, name, store_id):
        self.name = name
        self.store_id = store_id


# Define the store ID that we want to get data for
branches = [Branch("復興店", "0003"), Branch("天母店", "0005"), Branch("新竹店", "0006"),
            Branch("101店", "0007"), Branch("台中店", "0008"), Branch("板橋店", "0009"), Branch("高雄店", "0010"),
            Branch("南西店", "0011"), Branch("A4店", "0012"), Branch("A13店", "0013"), Branch("新生店", "0015")]

current_day = 13  # Enter a day that is not the current date to initiate data capture
dir_path = ''  # Adjust to desired path for data capture CSV file
days = ['M', 'T', 'W', 'H', 'F', 'S', 'N']
header = ["Date", "Day", "Time", "復興店", "天母店", "新竹店", "101店", "台中店", "板橋店", "高雄店", "南西店", "A4店", "A13店", "新生店"]

print("Entering loop..")

while True:
    # Initialize parameters
    if gmtime().tm_mon < 10:
        str_month = "0" + str(gmtime().tm_mon )
    else:
        str_month = str(gmtime().tm_mon )
    if gmtime().tm_mday < 10:
        str_day = "0" + str(gmtime().tm_mday)
    else:
        str_day = str(gmtime().tm_mday)

    filename = str_month + str_day + '.csv'
    filepath = dir_path + filename

    # Create new file for a new day and add header
    if gmtime().tm_mday != current_day:
        current_day = gmtime().tm_mday
        with open(filepath, mode='a', newline='') as csv_file:
            print(filename + " created!")
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_file.close()

    # During open hours (10-22 TW time, 2-14 GM time), retrieve waiting time every 5 minutes
    if 2 <= gmtime().tm_hour <= 13:
        if gmtime().tm_min % 5 == 0:
            with open(filepath, mode='a', newline='') as csv_file:
                # Create a CSV writer object
                csv_writer = csv.writer(csv_file)
                if gmtime().tm_min < 10:
                    str_min = "0" + str(gmtime().tm_min)
                else:
                    str_min = str(gmtime().tm_min)
                new_row = [f"{gmtime().tm_year}/" + str_month + "/" + str_day,
                           days[gmtime().tm_wday], f"{gmtime().tm_hour+8}:" + str_min]
                for i in range(len(branches)):
                    if get_wait_time(branches[i].store_id) == "已停止內用取號" or get_wait_time(branches[i].store_id) == "-1":
                        new_row.append("")
                    else:
                        new_row.append(get_wait_time(branches[i].store_id))
                csv_writer.writerow(new_row)
                print(new_row)
                csv_file.close()
                sleep(41)
        sleep(20)
