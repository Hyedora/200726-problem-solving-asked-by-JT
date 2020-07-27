SET_SIZE = 6
MAX_GEAR_NUM = 56

set1 = []
set2 = []
test=[]

for i in input("set1의 고정요소: ").split(" "):
    set1.append(i)
for i in input("set2의 고정요소: ").split(" "):
    set2.append(i)
for i in input("test요소: ").split(" "):
    test.append(i)

set1_test_len = SET_SIZE - len(set1)
set2_test_len = SET_SIZE - len(set2)
set1_test=[]
set2_test=[]
for i in range(len(test)-3):
    for j in range(i+1, len(test)-2):
        for k in range(j+1, len(test)-1):
            for l in range(k+1, len(test)):
                set1_test.append([test[i], test[j], test[k], test[l]])

for i in range(len(test)-2):
    for j in range(i+1, len(test)-1):
        for k in range(j+1, len(test)):
            set2_test.append([test[i], test[j], test[k]])

for test1 in set1_test:
    for test2 in set2_test:
        