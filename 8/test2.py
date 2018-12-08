#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-28 11:12:51
from urllib import request
from bs4 import BeautifulSoup


with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
event_div = soup.find(attrs={'class': 'shrubbery'})
# event_names=event_div.findAll(attrs={'class':'event-title'})
# event_locations=event_div.findAll(attrs={'class':'event-location'})
# event_times=event_div.findAll('time')
# for name in event_names:
#     print(name.string)
# for time in event_times:
#     print(''.join(list(time.strings)))
events = event_div.findAll('li')
for event in events:
    event_list = list(event.strings)
    print('Event name:%s \nEvent time:%s \nEvent location:%s' %
          (event_list[1], ''.join(event_list[4:6]), event_list[7]))
    print('------------------------------------')
