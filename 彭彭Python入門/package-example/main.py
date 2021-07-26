# 主程式
import geometry.point
result=geometry.point.distance(3,4) # 使用模組中底下的函式
print("距離",result)
import geometry.line as line # 定義模組別名
result=line.slope(1,1,3,3)
print("斜率",result)