def initialize():
    set_size = input("Insert the size of each number set : ")
    max_gear_size = input("Insert the maximum size of the gear you want : ")
    return set_size, max_gear_size

def factorization(g):
    if g<=0:
        return [],[]
    firsts=[]
    seconds=[]
    for i in range(g):
        if g%i==0:
            firsts.append(i)
            seconds.append(g//i)
    ################ continue with factorization(g-1) and factorization(g+1) #####

    return firsts, seconds


def main():
    set_size, max_gear_size = initialize()
    firsts=dict()
    
    for g in range(1, max_gear_size+1):
        g_firsts, g_seconds = factorization(g)
        for i in range(len(g_firsts)):
            if not g_firsts[i] in firsts:
                firsts[g_firsts[i]] = {g_seconds[i]:[g]}
                continue
            if not g_seconds[i] in firsts[g_firsts[i]]:
                firsts[g_firsts[i]][g_seconds[i]] = [g]
                continue
            firsts[g_firsts[i]][g_seconds[i]].append(g)

        
    
main()