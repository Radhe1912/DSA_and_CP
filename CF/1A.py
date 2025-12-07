import math

ans = list(map(int, input().split()))
print(math.ceil(ans[0]/ans[2])*math.ceil(ans[1]/ans[2]))