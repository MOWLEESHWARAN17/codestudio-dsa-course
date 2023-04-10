#factorial of number


def fact(N):
    if N==1:
        return 1
    return N*fact(N-1)
    
N=int(input("Enter the Number:"))
result=fact(N)
print(result)
