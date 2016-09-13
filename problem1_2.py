#! /usr/bin/env python3

bobs = 0

for i in range(len(s)):
    if s[i:i+3] == 'bob':
        bobs += 1

print("Number of times bob occures is: {}".format(bobs))
