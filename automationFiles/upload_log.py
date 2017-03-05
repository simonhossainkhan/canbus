#!/usr/bin/python

import requests
import sys

def car_data_save_request(file_location):
    with open(file_location, 'r') as myfile:
        data=myfile.read()
        r = requests.post("http://iotcanbus.pythonanywhere.com/api/save-pi-data/", data=data)
    return r.status_code

print "-----Starting Python-----"
file_name=sys.argv[1]
print file_name
file_path = "/home/pi/pyobd-pi/log/" + file_name
print file_path
status_code = car_data_save_request(file_path)
if(status_code == 200):
    print "Successful upload"
else:
    print "Upload failed"
    print status_code
print "-----End Python-----"
