import numpy as np

listt = []
file = open('input1.txt', 'r')
list_input = file.readlines()
n, d = map(int,list_input[0].split())
list_input.pop(0)
for i in range(0,len(list_input)):
  x, y = map(int,list_input[i].split())
  listt.append(int(x))
  listt.append(int(y))

arr = np.array(listt)
newarr = arr.reshape(int(n), int(d), int(d))

listdet = []
counter2 = 0
mat_dic = {}
for k in newarr:
  for z in newarr:
    if np.mean(k) == np.mean(z):
      pass
    else:
      multy = np.dot(k, z)
      det = np.linalg.det(multy)
      mat_dic[det] = k, z
      listdet.append(det)
biggest = max(listdet)

lst = []
A = mat_dic[biggest][0]
B = mat_dic[biggest][1]
detk = np.linalg.det(mat_dic[biggest][0])
detz = np.linalg.det(mat_dic[biggest][1])
if detk > detz:
  C = np.dot(A, B)
  Inv_C = np.linalg.inv(C)
  for row in Inv_C:
    for num in row:
        lst.append(round(num, 3))
  for j in range(0, len(lst), int(d)):
    print(' '.join(map(str, lst[j:j+int(d)])))
elif detz > detk:
  C1 = np.dot(B, A)
  Inv_C1 = np.linalg.inv(C1)
  for row in Inv_C1:
    for num in row:
        lst.append(round(num, 3))
  for j in range(0, len(lst), int(d)):
    print(' '.join(map(str, lst[j:j+int(d)])))
else:
  C2 = np.dot(A, B)
  Inv_C2 = np.linalg.inv(C2)
  for row in Inv_C2:
    for num in row:
        lst.append(round(num, 3))
  for j in range(0, len(lst), int(d)):
    print(' '.join(map(str, lst[j:j+int(d)])))
file.close()