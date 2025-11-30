n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
count = 0
s = sum(arr)
for i in range(len(arr)):
    count+=arr[i]
    s-=arr[i]
    if count>s:
        print(i+1)
        break