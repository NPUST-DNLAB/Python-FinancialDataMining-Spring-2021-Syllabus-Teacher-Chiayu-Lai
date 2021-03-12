# -*- coding: utf-8 -*-

CH6

#1、
def is_odd(i):
    if type(i) == int:
        return(i if i%2==1 else 0)
    else:
        print('ERROR：Please input an integer.')

is_odd(7)


  
#4、
for i in (-1,0,1,2,39):
    print(i in range(1,5))
    

cH7
def fibo(n):
    if(n<3):
        a=1
    else:
        a=fibo(n-1)+fibo(n-2)
    return(a)

def seqfibo(n):
    for i in range(1,n+1):
        print(fibo(i))


seqfibo(5)
        
#5、
def multi_abs(*numbers):
    return(list(map(abs,numbers)))

multi_abs(-5,55,-6,0,-7)
    
