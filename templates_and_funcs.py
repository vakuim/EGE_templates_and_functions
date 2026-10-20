#общие функции
def convert(a, n):
    d = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = ''
    while a != 0:
        b = d[a%n] + b
        a=a//n
    return b or '0'

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
def alg_r(r):
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
def alg_n(m):
    n = 0
    while True:
        a = bin(n)[2:]
        for i in range(2):
            b = a.count('1')
            a = a + str(b%2)
        if int(a, 2) > m:
            return(n)
        n+=1
################################################################################
#алгоритм N в Z
'''
ans = set()
for n in range(5000):
    a = [int(i) for i in str(n)]
    s = sum(a)
    m = min(a) + max(a)
    l = a[0]
    r = a[-1]
    p1 = s - l
    p2 = m-r
    z = int(str(p1)+str(p2) if p1 > p2 else str(p2)+str(p1))
    if z == 222:
        ans.add(n)
    n+=1
print(max(ans))
'''
def alg_n_to_Z(m):
    ans = set()
    for n in range(5000):
        a = [int(i) for i in str(n)]
        s = sum(a)
        m = min(a) + max(a)
        l = a[0]
        r = a[-1]
        p1 = s - l
        p2 = m-r
        z = int(str(p1)+str(p2) if p1 > p2 else str(p2)+str(p1))
        if z == m:
            ans.add(n)
        n+=1
    print(max(ans))
