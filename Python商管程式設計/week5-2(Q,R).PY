# past sales
salesStr = "14,23,26,17,17,12,24,19,10,18,22,31,19,16,22,28,20,27,20,32"
sales = salesStr.split(',')
for i in range(len(sales)):
  sales[i] = int(sales[i])

# given information
stgCost = 2
invCost = 1000 * 0.073 / 365
Q = 30
I = 20

# finding the best R
bestR = 0
costOfBestR = 100000000
for R in range(Q):
  totalStgCost = 0
  totalInvCost = 0

  # finding the total cost of this R
  for s in sales:
    I -= s
    if I < 0:
      totalStgCost += -I * stgCost
      I += Q
    elif I < R:
      I += Q
    totalInvCost += I * invCost

  # update bestR when necessary
  totalCost = totalStgCost + totalInvCost
  if totalCost < costOfBestR:
     bestR = R
     costOfBestR = totalCost
  print(R, totalStgCost, int(totalInvCost), int(totalCost))
  
print(bestR)