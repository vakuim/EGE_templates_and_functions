#алгоритм R, N
'''
n = 0
while True:
    a = bin(n)[2:]
    for i in range(2):
        b = a.count('1')
        a = a + str(b%2)
    if int(a, 2) > 137:
        print(n)
        break
    n+=1
'''
#алгоритм, получить R
def alg_R(r):
    n = 0
    while True:
        a = bin(n)[2:]
        for i in range(2):
            b = a.count('1')
            a = a + str(b%2)
        if int(a, 2) > r:
            return(int(a, 2))
        n+=1
#алгоритм, получить N
def alg_N(m):
    n = 0
    while True:
        a = bin(n)[2:]
        for i in range(2):
            b = a.count('1')
            a = a + str(b%2)
        if int(a, 2) > m:
            return(n)
        n+=1

def 
