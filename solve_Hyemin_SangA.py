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
        return 1
    return 0

set1 = []
set2 = []
test1=[]

for i in input("set1의 고정요소: ").split(" "):
    set1.append(int(i))
for i in input("set2의 고정요소: ").split(" "):
    set2.append(int(i))
for i in input("test요소: ").split(" "):
    test1.append(int(i))
test2=test1.copy()

for i in test1:
    if i in set1:
        test1.pop(test1.index(i))
for i in test2:
    if i in set2:
        test2.pop(test2.index(i))

set1_test_len = SET_SIZE - len(set1)
set2_test_len = SET_SIZE - len(set2)
set1_test=[]
set2_test=[]
for i in range(len(test1)-3):
    for j in range(i+1, len(test1)-2):
        for k in range(j+1, len(test1)-1):
            for l in range(k+1, len(test1)):
                set1_test.append([test1[i], test1[j], test1[k], test1[l]])

for i in range(len(test2)-2):
    for j in range(i+1, len(test2)-1):
        for k in range(j+1, len(test2)):
            set2_test.append([test2[i], test2[j], test2[k]])

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

print("You are fool.")