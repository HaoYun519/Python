a = input()
b = a.split()
print(b)

for i in range(len(b)):
  print(len(b))
  b[i] = int(b[i]) * 2
print(b)