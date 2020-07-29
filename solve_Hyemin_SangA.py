from itertools import combinations
# set의 크기와 최대 기어값을 지정해준다
SET_SIZE = 6
MAX_GEAR_NUM = 56

# set1과 set2가 문제 조건을 만족하는 set인지 확인한다
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

# set1과 set2에 고정할 수들을 지정하고 검사해볼 test 수들을 입력한다
set1 = [int(i) for i in input("set1에 고정할 수들을 입력하시오: ").split()]
set2 = [int(i) for i in input("set2에 고정할 수들을 입력하시오: ").split()]
test1 = [int(i) for i in input("검사해볼 수들을 입력하시오: ").split()]
test2 = test1.copy()

# test 수들 중에 이미 set에 들어있는 수가 존재한다면 제거한다
for i in test1:
    if i in set1:
        test1.pop(test1.index(i))
for i in test2:
    if i in set2:
        test2.pop(test2.index(i))

# 각 set에 들어갈 수 있는 test 수의 조합을 만들어낸다
set1_test = list(combinations(test1, SET_SIZE-len(set1)))
set2_test = list(combinations(test2, SET_SIZE-len(set2)))

# 위에서 만든 수 조합들을 모두 대입해보면서 해답이 존재하는지 찾는다
solution_num=0
print()
for test1 in set1_test:
    set1.extend(test1)
    for test2 in set2_test:
        set2.extend(test2)
        # 문제 조건을 만족한다면 해당 set을 출력한다
        if(IsItRight(set1, set2)):
            solution_num+=1
            print("SOLUTION"+str(solution_num)+": ", end="")
            print(sorted(set1), end=", ")
            print(sorted(set2))
        for i in range(len(test2)):
            set2.pop()
    for i in range(len(test1)):
        set1.pop()

if solution_num==0:
    print("가능한 solution 조합이 없습니다.")
else:
    print("%d개의 solution을 발견했습니다." %solution_num)