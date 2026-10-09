s=int(input())
def parse(s):
    return (s[0]=='1' and s[2]=='1') or (s[0]=='1' and s[4]=='1') or (s[2]=='1' and s[4]=='1')
c=0
for i in range(s):
    if(parse(input())):
        c+=1
print(c)