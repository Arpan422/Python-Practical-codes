def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterm=int(input("how many ters?"))
if nterm<=0:
    print("please enter a positive integer")
else:
    print("fibonacci sequence")
    for i in range(nterm):
        print(recur_fibo(i))