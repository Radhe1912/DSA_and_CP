t = int(input())
ans = []

def check_vals(num):
    # if num is power of 2 → NO
    if (num & (num - 1)) == 0:
        return "NO"
    else:
        return "YES"

while t:
    num = int(input())
    ans.append(check_vals(num))
    t -= 1

for x in ans:
    print(x)

# t = int(input())
# ans = []

# def check_vals(num):
#     # keep dividing by 2 until num is odd
#     while num % 2 == 0:
#         num //= 2
    
#     # now num is odd
#     if num > 1:
#         return "YES"
#     else:
#         return "NO"

# while t:
#     num = int(input())
#     ans.append(check_vals(num))
#     t -= 1

# for i in ans:
#     print(i)