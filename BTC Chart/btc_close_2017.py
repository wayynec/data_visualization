# import requests

# json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)

# with open('btc_close_2017.json', 'w') as f:
# 	f.write(req.text)

# file = req.json()
# print(file)
# above is how to use requests library to read file from internet

import json
import pygal
import math
from itertools import groupby

# def draw_line(x_data, y_data, title, y_legend):
# 	"""function to draw a line over a period of time"""
# 	xy_map = []
# 	for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda pair:pair[0]):
# 		y_list = [v for pair, v in y]
# 		xy_map.append([x, sum(y_list)/len(y_list)])
# 	x_unique, y_mean = [*zip(*xy_map)]
# 	line_chart = pygal.Line()
# 	line_chart.title = title
# 	line_chart.x_labels = x_unique
# 	line_chart.add(y_legend, y_mean)
# 	line_chart.render_to_file(title+'.svg')
# 	return line_chart

# # add the data to a list
# filename = 'btc_close_2017.json'
# with open(filename) as f:
# 	btc_data = json.load(f)
# # need 5 lists to store values
# dates = []
# months = []
# weeks = []
# weekdays = []
# closes = [] 
# # each entry in this list is a dictionary, extract all keys
# for btc_dict in btc_data:
# 	dates.append(btc_dict['date'])
# 	months.append(int(btc_dict['month']))
# 	weeks.append(int(btc_dict['week']))
# 	weekdays.append(btc_dict['weekday'])
# 	closes.append(int(float(btc_dict['close'])))
# 	#print("{} is in month {} and week {} on {}. It has a close price of {} RMB.".format(date, month, week, weekday, close))
# # now all info is in correct lists
# # line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) # rotate x label clockwise 20 degrees
# # line_chart.title = "Closing Prices (After Log Transformation)"
# # line_chart.x_labels = dates
# # line_chart.x_labels_major = dates[::30]
# # close_log = [math.log10(price) for price in closes]
# # line_chart.add('Close Price Log', close_log)
# # line_chart.render_to_file('close_prices.svg')

# # weekly average close price, we need to define a function to group them into certain duration of time
# # idx_month = dates.index('2017-12-01')
# # line_chart_month = draw_line(months[:idx_month], closes[:idx_month], 'Close Price Monthly Average', 'Monthly Average')
# #line_chart_month

# # idx_week = dates.index('2017-12-11')
# # line_chart_month = draw_line(weeks[1:idx_week], closes[1:idx_week], 'Close Price Weekly Average', 'Weekly Average')

# idx_week = dates.index('2017-12-11')
# wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# weekday_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
# line_chart_day = draw_line(weekday_int, closes[1:idx_week], 'Close Price Weekday Average', 'Weekday Average')
# line_chart_day.x_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# line_chart_day.render_to_file('Close Price Weekday Average.svg')

with open('Close Price Dashboard.html', 'w', encoding='utf8') as f:
	f.write('<html><head><title>"Close Price Dashboard"</title><metacharset="utf-8"></head><body>\n')
	for svg in [
			'close_prices.svg', 'Close Price Monthly Average.svg', 'Close Price Weekly Average.svg',
			'Close Price Weekday Average.svg'
	]:
		f.write('	<object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
	f.write('</body></html>')