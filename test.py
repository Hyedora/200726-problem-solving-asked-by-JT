SET_SIZE = 3
MAX_GEAR_NUM = 19

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
    print("힝", end="")
    return 0

set1 = [1, 3]
set2 = [2, 3]
test = [4,5,6,7]

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
for l in range(len(test)):
    set1_test.append([test[l]])
    set2_test.append([test[l]])


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