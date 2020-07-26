d = dict()

if not 1 in d:
    d[1]={2:[3]}    
d[1][2].append(5)

print(d)