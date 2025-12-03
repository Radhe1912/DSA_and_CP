n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
ans = float('inf')

for i in range(m - n + 1):
    diff = nums[i + n - 1] - nums[i]
    ans = min(ans, diff)

print(ans)