#!/usr/bin/env python3

import sys
import json
import statistics

data = json.loads(open('flood.txt').read())

results = []

for region in data['regions']:
	last = []
	for reading in region['readings']:
		current = reading['reading']
		maxdiff = 0
		if len(last) > 0:
			for i in range(0, len(current)):
				diff = abs(current[i] - last[i])
				if diff > maxdiff:
					maxdiff = diff
		last = current
		
		results.append({'reg': region['regionID'], 'read': reading['readingID'], 'date': reading['date'], 'max': maxdiff})

me = statistics.mean([m['max'] for m in results])
sd = statistics.stdev([s['max'] for s in results])

out = ''
for res in results:
	if res['max'] > (me + sd):
		out = out + res['read']

print(out)
