注:该代码基于python生成，使用时需导入pyautocad数据库

from pyautocad import Autocad, APoint
import math

acad = Autocad(create_if_not_exists=True)
acad.prompt("正在生成轴承俯视图...\n")

def draw_enhanced_bearing(inner_dia, ball_dia, num_balls):
    # 计算基础参数
    inner_radius = inner_dia / 2
    ball_radius = ball_dia / 2
    
    # 计算新几何关系
    groove_radius = inner_radius + ball_radius  # 滚道半径（滚珠中心位置）
    outer_groove_radius = groove_radius + ball_radius  # 外圈滚道半径
    
    center = APoint(0, 0)
    
    # 绘制三层结构
    acad.model.AddCircle(center, inner_radius)                # 内圈
    acad.model.AddCircle(center, outer_groove_radius)         # 新增外滚道
    acad.model.AddCircle(center, outer_groove_radius * 1.2)  # 外圈（扩大比例）
    acad.model.AddCircle(center, inner_radius * 0.8)
    # 绘制滚珠（部分被覆盖）
    for i in range(num_balls):
        angle = math.radians(i * (360 / num_balls))
        x = groove_radius * math.cos(angle)
        y = groove_radius * math.sin(angle)
        ball_center = APoint(x, y)
        ball = acad.model.AddCircle(ball_center, ball_radius)
        
        # 设置滚珠颜色（红色增强可视化）
        ball.Color = 1

# 新参数设置（单位：毫米）
bearing_inner_dia = 30  # 轴承内孔直径
ball_diameter = 6       # 滚珠直径
number_of_balls = 12    # 滚珠数量

# 执行绘图
draw_enhanced_bearing(bearing_inner_dia, ball_diameter, number_of_balls)

print("轴承俯视图生成完成！")
