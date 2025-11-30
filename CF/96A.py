val = input().strip()
print("YES" if "0000000" in val or "1111111" in val else "NO")

# val = input()
# flag = False

# if len(val)<7:
#     print("NO")
# else:
#     for i in range(len(val)-6):
#         if len(set(val[i:i+7]))==1:
#             flag = True
#             print("YES")
#             break
#     if not flag:
#         print("NO")