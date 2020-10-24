# s = input()
# s = s[::-1]

# p1 = 'dream'
# p2 = 'dreamer'
# p3 = 'erase'
# p4 = 'eraser'

# e_flag = True

# while True :
#   if s[:5] == p1[::-1] :
#     s = list(s)
#     del s[:5]
#     s = ''.join(s)
#     e_flag = False
#   elif s[:7] == p2[::-1] :
#     s = list(s)
#     del s[:7]
#     s = ''.join(s)
#     e_flag = False
#   elif s[:5] == p3[::-1] :
#     s = list(s)
#     del s[:5]
#     s = ''.join(s)
#     e_flag = False
#   elif s[:6] == p4[::-1] :
#     s = list(s)
#     del s[:6]
#     s = ''.join(s)
#     e_flag = False

#   if e_flag :
#     print('NO')
#     break
  
#   if s == '' :
#     print('YES')
#     break

#   e_flag = True

s=input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
if s:
  print("NO")
else:
  print("YES")
