n = int(input())
arr = list(map(int, input().split(' ')))
count = 1
prev = 1
for i in range(1, n):
    if arr[i]>=arr[i-1]:
        prev+=1
    else:
        prev = 1
    count = max(count, prev)
print(count)