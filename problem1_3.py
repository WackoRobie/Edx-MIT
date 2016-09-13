#! /usr/bin/env python3

longest_match = ''
match = ''

for i in range(len(s)):
    if match:
        if s[i] >= match[-1]:
            match += s[i]
        else:
            match = s[i]
    else:
        match = s[i]
    if len(match) > len(longest_match):
        longest_match = match
    print(match)
    print(longest_match)
    print(20*'-')

print("Longest substring in alphabetical order is: {}".format(longest_match))
