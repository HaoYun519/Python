# read input data
cost = int(input())      #進貨成本
price = int(input())     #零售價
maxDemand = int(input()) #單日需求量
salvage = int(input())   #報紙變賣殘值

prob = [0] * (maxDemand + 1)   # the list to store probabilities
                               #賣掉每份機率
for i in range(maxDemand + 1):
  prob[i] = float(input())     #機率為浮點數

# prepare to search for an optimal quantity
optQty = 0       #最佳訂購量
optProfit = 0.0  #最佳預期利潤

# in each iteration, we calculate the expected profit
# of that order quantity
for quantity in range(maxDemand + 1):
  # calculate the expected profit
  # this part is similar to that in
  # the practice quiz in Week 4
  expSales = 0.0   #預期賣出量
  expUnsold = 0.0  #預期未賣出量

  for demand in range(maxDemand + 1):
    if demand < quantity:
      expSales += prob[demand] * demand
      expUnsold += prob[demand] * (quantity - demand)
    else:
      expSales += prob[demand] * quantity

  profit = expSales * price - quantity * cost + expUnsold * salvage
  #上面公式為 預期利潤 = 預期銷售 - 進貨成本 + 殘值收入
  # check whether this quantity is currently an optimal one
  if profit > optProfit:
    optProfit = profit
    optQty = quantity

# print out the result
print(optQty, int(optProfit))