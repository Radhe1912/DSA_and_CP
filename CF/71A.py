n = int(input())
while n>0:
    s = input()
    print(s if len(s)<11 else s[0]+str(len(s[1:-1]))+s[-1])
    n-=1