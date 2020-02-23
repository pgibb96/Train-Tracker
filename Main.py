#!/usr/bin/env/python3
import requests
import time

URL = 'https://api-v3.mbta.com/schedules'
stop = 70001
route = 'Orange'
direction_id = 1
sort = 'departure_time'
limit = 2


t = time.localtime()
year = str(t[0])
month = str(t[1])
if len(month) == 1: month = "0" + month
day = str(t[2])
if len(day) == 1: day = "0" + day
hour = str(t[3])
if len(hour) == 1: hour = "0" + hour
minute = str(t[4])
if len(minute) == 1: minute = "0" + minute

min_time = hour + ":" + minute
date = year + "-" + month + "-" + day

PARAMS = {'stop':stop, 'route':route, 'direction_id':direction_id, 'min_time':min_time, 'date':date, 'sort':sort}

r = requests.get(URL, params = PARAMS)

data = r.json()

first = data['data'][0]['attributes']['departure_time'].split("T")[1].split("-")[0]
second = data['data'][1]['attributes']['departure_time'].split("T")[1].split("-")[0]


print("The next train will leave at: " + first)
print("The following train will leave at: " + second)

