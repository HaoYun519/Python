import sys
sys.path.append("modules") #在模組的搜尋路徑列表中【新增路徑】
print(sys.path) # 印出模組的搜尋路徑列表
print("-------------------c")
import geometry
print(geometry.distance(1,1,5,5))