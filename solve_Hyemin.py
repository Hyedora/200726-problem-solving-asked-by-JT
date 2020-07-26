set_size = input("세트 크기: ")
max_gear_size = input("최대 기어값: ")

# 첫 번째 세트에 들어갈 수 있는 수들
firsts=dict()

# 만들어야하는 모든 기어값에 대해서
for g in range(1, max_gear_size+1):
    # 기어값 g가 만들어지기 위해서는 g-1, g, g+1 중 하나라도 만들어지면 됨
    # 그래서  g-1, g, g+1이 만들어질 수 있는 모든 숫자 조합을 찾음
    g_firsts=[]
    g_seconds=[]
    for gear in [g-1, g, g+1]:
        if gear<=0:
            continue
        for i in range(1, gear+1):
            if gear%i==0:
                g_firsts.append(i)
                g_seconds.append(g//i)

    
    for i in range(len(g_firsts)):
        if not g_firsts[i] in firsts:
            firsts[g_firsts[i]] = {g_seconds[i]:[g]}
            continue
        if not g_seconds[i] in firsts[g_firsts[i]]:
            firsts[g_firsts[i]][g_seconds[i]] = [g]
            continue
        firsts[g_firsts[i]][g_seconds[i]].append(g)