n = int(input())
arr = list(map(int, input().split()))

first = second = None
third = None

for i in range(n):
    num = arr[i]

    if first is None or num < first[0]:
        first = (num, i+1)

    elif num>first[0] and (second is None or num<second[0]):
        second = (num, i+1)

    elif second is not None and num>second[0]:
        third = (num, i+1)
        print(first[1], second[1], third[1])
        exit()

print(-1, -1, -1)