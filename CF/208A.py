s = input()
res = ""
i = 0

while i < len(s):
    if s[i:i+3] == "WUB":
        res += " "
        i += 3
    else:
        res += s[i]
        i += 1

print(" ".join(res.split()))

# print(' '.join(input().replace("WUB", " ").split()))