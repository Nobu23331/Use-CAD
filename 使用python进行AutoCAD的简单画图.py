from pyautocad import Autocad, APoint
import math

#1.连接AutoCAD（若未打开则自动启动）
pyacad = Autocad(create_if_not_exists=True)
pyacad.prompt("AutoCAD图纸生成中...\n")  # 在CAD命令行显示提示信息
print(f"当前文档：{pyacad.doc.Name}")  # 当前CAD文档名称

base_point = APoint(0, 0)
#2.1生成直线
startpoint = APoint(10, 20)  # 使用APoint类定义起点
endpoint = APoint(30, 22)#定义直线终点坐标
line= pyacad.model.AddLine(startpoint, endpoint)#添加直线

#2.2生成圆
circle_center = APoint(30, 20)#定义圆心
circle = pyacad.model.AddCircle(circle_center, 15)

#2.3生成红色文本
start_point = APoint(100,100 )# 定义文本起点
text = pyacad.model.AddText("我是AuoCad", start_point, 8)#文本，起点，字号
text.color=1#定义颜色，“1”为红色

#2.4 绘制圆弧
arc_center = APoint(45, 10)#定义圆心
arc = pyacad.model.AddArc(
    arc_center,  # 圆心
    20,  # 半径
    math.radians(45),  # 起始弧度（45度）
    math.radians(270)  # 终止弧度（270度）
)

#3.建立图层
try:
    layer = pyacad.doc.Layers.Add("RedLayer")
    layer.color = 1  # 1 代表红色
except Exception:
    layer = doc.Layers.Item("RedLayer")

#使用红色图层画线
pyacad.ActiveDocument.ActiveLayer = layer  # 切换当前图层
vertical_line = pyacad.model.AddLine(
    APoint(50, -20),
    APoint(50, 40)
)
pyacad.ActiveDocument.ActiveLayer = pyacad.doc.Layers.Item(0)#切换回默认图层
#4.自动缩放视图以显示所有内容
pyacad.app.ZoomAll
print("图纸生成完成！")
