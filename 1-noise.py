#!/usr/bin/env python3

import collections
import base64

noise = open('noise.txt').read()

for i in range(0, len(noise) - 16):
	substr = noise[i:i+16]
	if len(collections.Counter(collections.Counter(substr).values()).values()) == 1:
		print(str(base64.b64decode(substr)))


