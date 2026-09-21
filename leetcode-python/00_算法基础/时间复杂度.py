def f1(x):
    k=0
    for i in range(n):
        k=k+1

def f2(x):
    k=0
    for i in range(n):
        for j in range(n):
            k=k+1   

def f3(x):
    k=0
    for i in range(n):
        j=1
        while j < n:
            k=k+1
            j=j*2

import time 

n = int(input("输入n："))
t1=time.perf_counter()

f3(n)

t2=time.perf_counter()

print(t2-t1)

# 10000   f1 0.00024589999520685524 n
#          f2 2.3041615999973146 n*n
#           f3 0.005384100004448555 n*log(n)

