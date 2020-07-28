SET_SIZE = 6
MAX_GEAR_NUM = 56

def IsItRight(set1, set2):
    valid = set()
    for i in range(MAX_GEAR_NUM):
        valid.add(i+1)
    for x in set1:
        for y in set2:
            valid.discard(x*y)
            valid.discard(x*y-1)
            valid.discard(x*y+1)
    if len(valid)==0:
        print("Yeah")
        return 1
    return 0

set1 = [1]
set2 = []
test = [2,3,4,5,6,7,8,9,10,11,12,13,17,19,23,29]

"""for i in test1:
    if i in set1:
        test1.pop(test1.index(i))
for i in test2:
    if i in set2:
        test2.pop(test2.index(i))"""

set1_test_len = SET_SIZE - len(set1)
set2_test_len = SET_SIZE - len(set2)
set1_test=[]
set2_test=[]
for e in range(len(test)-4):
    for i in range(e+1, len(test)-3):
        for j in range(i+1, len(test)-2):
            for k in range(j+1, len(test)-1):
                for l in range(k+1, len(test)):
                    set1_test.append([test[e], test[i], test[j], test[k], test[l]])

for a in range(len(test)-5):
    for e in range(a+1, len(test)-4):
        for i in range(e+1, len(test)-3):
            for j in range(i+1, len(test)-2):
                for k in range(j+1, len(test)-1):
                    for l in range(k+1, len(test)):
                        set2_test.append([test[a], test[e], test[i], test[j], test[k], test[l]])

"""for i in range(len(test1)-3):
    for j in range(i+1, len(test1)-2):
        for k in range(j+1, len(test1)-1):
            for l in range(k+1, len(test1)):
                set1_test.append([test1[i], test1[j], test1[k], test1[l]])"""

for test1 in set1_test:
    set1.extend(test1)
    for test2 in set2_test:
        set2.extend(test2)
        if(IsItRight(set1, set2)):
            print(set1)
            print(set2)
            raise ValueError("FINISHED!!")
        for i in range(len(test2)):
            set2.pop()
    for i in range(len(test1)):
        set1.pop()

print("구")
print(set1)
print(set2)