import requests
import json
from time import localtime, sleep


def get_wait_time(store_id):

    # Define the URL of the server-side API
    url = "https://www.dintaifung.tw/Queue/Home/WebApiTest"

    # Define the data payload that we want to send in the POST request
    payload = {
        "storeid": store_id,
    }

    # Make the POST request and get the response
    # response = requests.post(url, data=payload)
    # print(response.content)

    # Convert the byte string to a regular string
    # json_str = response.content.decode('utf-8')

    # Parse the JSON-formatted string into a Python object
    data = json.loads(requests.post(url, data=payload).content.decode('utf-8'))
    return data[0]['wait_time']


class Store:

    def __init__(self, name, store_id):
        self.name = name
        self.store_id = store_id


# Define the store ID that we want to get data for
stores = [Store("信義店", "0001"), Store("復興店", "0003"), Store("天母店", "0005"), Store("新竹店", "0006"),
          Store("101店", "0007"), Store("台中店", "0008"), Store("板橋店", "0009"), Store("高雄店", "0010"),
          Store("南西店", "0011"), Store("A4店", "0012"), Store("A13店", "0013"), Store("新生店", "0015")]


# Access the data in the object
# store_id = data[0]['store_id']
# wait_time = data[0]['wait_time']
# num_1 = data[0]['num_1']
# num_2 = data[0]['num_2']
# num_3 = data[0]['num_3']
# num_4 = data[0]['num_4']
# togo_numbers = data[0]['togo_numbers']
# last_time = data[0]['last_time']

print(f"Current ({localtime().tm_year}/{localtime().tm_mon}/{localtime().tm_mday} {localtime().tm_hour}:"
      f"{localtime().tm_min}) wait time for {stores[1].name} is {get_wait_time(stores[1].store_id)}")

while True:
    if localtime().tm_min % 5 == 0:
        # for i in range(len(stores)):
        print(f"Current ({localtime().tm_year}/{localtime().tm_mon}/{localtime().tm_mday} {localtime().tm_hour}:"
              f"{localtime().tm_min}) wait time for {stores[1].name} is {get_wait_time(stores[1].store_id)}")
        sleep(65)
    sleep(30)
