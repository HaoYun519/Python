"""
第五週作業：基地臺位址選擇
"""

init = input().split(' ')

NumTowns = int(init[0])   #城鎮數量
beacons = int(init[1])    #基地台數量
coverage = int(init[2])   #基地台距離

data = []  #紀錄城鎮座標x, y, 人數, 編號
distance = float() #距離變數
covered = int()  #覆蓋數
coveredTown = [] #現在涵蓋的城鎮
maxCovered = int()  #最大覆蓋數
maxCoveredTown = [] #最大涵蓋的城鎮
maxTown = int() #統算中的城鎮
TotalCovered = int() #所有涵蓋人數
toplist = []  #紀錄涵蓋最多人的城鎮與人數

#把城鎮資料送進data List
for i in range(NumTowns):	
	towninfo = input().split(' ')
	for j in range(len(towninfo)):
		towninfo[j] = int(towninfo[j])
	towninfo.append(i) #資料加上城鎮編號
	data.append(towninfo)

#輪基地台數
for k in range(beacons):
	maxCovered = 0
	maxCoveredTown.clear()
  
  #輪城鎮數i
	for i in data:
		covered = 0
		coveredTown.clear()

		#輪城鎮數j
		for j in data:
			#比較城鎮i, j 並記錄下i 城鎮在含蓋範圍內的城鎮
			distace = ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5
			if distace <= coverage:
				coveredTown.append(j)
				covered += j[2]

		#比較所有i 涵蓋範圍, 並保留最大的城鎮i
		if covered > maxCovered:
			maxTown = i[3]
			maxCovered = covered
			maxCoveredTown = coveredTown.copy()  #!!! 因為是list, 所以要用複製的 !!!

	#基地台統整
	TotalCovered += maxCovered #紀錄涵蓋人數
	toplist.append(maxTown+1) #紀錄最大涵蓋城鎮
	for i in maxCoveredTown: #移除以涵蓋城鎮
		data.remove(i)

#最後輸出
toplist.append(TotalCovered)
print("-------------------")
print(*toplist, sep=' ')