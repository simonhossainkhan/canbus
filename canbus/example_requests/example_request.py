import requests


def car_data_save_request(file_location):
    with open(file_location, 'r') as myfile:
        data=myfile.read()

        r = requests.post("http://localhost:8000/api/save-pi-data/", data=data)

    return r.status_code

car_data_save_request("car_log.log")