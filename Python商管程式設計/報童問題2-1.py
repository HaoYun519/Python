c = int(input())
r = int(input())
N = int(input())
list = []
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))

exp = 0 # 該進貨量下之預期收益
sum = 0.0
D = 0.0
maxP = 0.0 # 最大利潤
qMax = 0 # 可達最大利潤之進貨數
N = 8


for q in range(0,N+1) :
 sum = 0
 D = 0.0
 for p in range(0,q+1) :
  # p 為 不大於進貨量下之需求量
  exp = r * min(p,q) - c * q
  if p != q :
   sum += list[p] * exp
   D += list[p]
  else:
   sum += (1-D) * exp
   break
 if sum > maxP :
  maxP = sum
  qMax = q
 

profit = int(maxP)
print(str(qMax)+" "+str(profit))