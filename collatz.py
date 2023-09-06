def collatz(n):
    i=0
    while True: 
        if n==1:
            return i
        if n%2==0: 
            n=n/2
        else: 
            n=3*n+1
        i+=1
        