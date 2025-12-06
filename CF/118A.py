s = input()
s = s.lower()
ans = ''
for i in s:
    if i in ('aeiouy'):
        continue
    ans+='.'
    ans+=i
print(ans)