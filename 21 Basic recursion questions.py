#Write a program to calculate the sum of numbers from 1 to n using recursion.
def sum(N):
    if N==1:
        return 1
    return N+sum(N-1)
    
N=int(input("Enter the Number:"))
print(sum(N))
