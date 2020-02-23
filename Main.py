#!/usr/bin/env/python3
import requests
import time

URL = 'https://api-v3.mbta.com/schedules'
stop = 70001
route = 'Orange'
direction_id = 1
sort = 'departure_time'
min_time = '17:00'
date = '2020-02-23'
sort = 'departure_time'
limit = 2

PARAMS = {'stop':stop, 'route':route, 'direction_id':direction_id, 'min_time':min_time, 'date':date, 'sort':sort}

r = requests.get(URL, params = PARAMS)

data = r.json()
print(data)

first = data['data'][0]['attributes']['departure_time']
second = data['data'][1]['attributes']['departure_time']


print(first)
print(second)

