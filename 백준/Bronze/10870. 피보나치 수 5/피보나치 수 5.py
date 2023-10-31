num = int(input())

fib = 0

if num==0:
    fib=0
elif num==1 or num==2:
    fib=1
else:
    prev1=1
    prev2=1
    for i in range(3, num):
        fib = prev1+prev2
        prev2=prev1
        prev1=fib
    fib=prev1+prev2
print(fib)