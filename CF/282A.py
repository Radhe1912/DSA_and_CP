n = int(input())
x = 0

for i in range(n):
    val = input()
    x = x+1 if '+' in val else x-1
    
print(x)