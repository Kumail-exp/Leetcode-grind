def maxi(n,k):
    return 2**(n-k+1)+2*(k-1)
vals=[]
for i in range(int(input())):
    a, b = map(int, input().split())
    vals.append(maxi(a,b))
for i in vals:
    print(i)