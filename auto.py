from action import *
import pandas as pd


# 读取Excel文件
df = pd.read_excel("配置文档.xlsx")

# 遍历数据
for index, row in df.iterrows():
    type = row["指令类型(1左键 2双击 3右键 4滚动 5等待 6输入 7 按键 8 组合按键)"]
    num = row["循环次数(-1 代表一直重复)"]
    message = row[
        "内容(点击的图片 滚动的距离:正上负下 等待时间 输入内容 按键 组合按键:用逗号隔开)"
    ]
    do_cycle_type(type, num, message)
