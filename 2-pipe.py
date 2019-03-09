#!/usr/bin/env python3

import sys
import json
import statistics

string = ''
for line in open('ppb.bin.log', 'r'):
	words = line.split()
	for word in words:
		string = string + chr(int(word, 2))

data = json.loads(string)

keys = []

for day in data:
	for item in day['readings']:
		conts = item['contaminants']
		total = 0
		for cont in conts:
			total += conts[cont]
			
		keys.append({'id': item['id'], 'val': total, 'day': day['date'], 'time': item['time']})

sd = statistics.stdev([v['val'] for v in keys])
me = statistics.mean([v['val'] for v in keys])

for key in keys:
	if key['val'] > (me + sd):
		print(str(key['id']) + ' ' + str(key['val']) + ' ' + str(key['day']) + ' ' + str(key['time']))
		out = ''
		for i in range(0, len(key['id']), 2):
			substr = key['id'][i:i+2]
			out = out + chr(int(substr, 16))
		print(out)

