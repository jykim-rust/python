from flask import escape

'''with open('ex') as full:
    for line in full:
        print(line,end='**')
'''
'''
a=[]
with open('ex') as full:
    for line in full:
        a.append(line.split('|'))

print(a)
'''

'''
with open('ex') as full:
    for line in full.readline():
        print(line)
'''


contents=[]
with open('ex') as log:
    for line in log:
        #contents.append([])
        for item in line.split('|'):
            contents.append(item)

print(contents)

