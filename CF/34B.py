n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = 0
i = 0
while i<m:
    if arr[i]>=0:
        break
    count+=arr[i]
    i+=1
print(abs(count))