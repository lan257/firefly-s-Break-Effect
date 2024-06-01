import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体，确保支持中文和数学符号
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体（SimHei）
rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块的问题

# 设置常量
R = 8.314  # 理想气体常数 J/(mol*K)
n = 1      # 物质的量 mol
T1 = 300   # 温度1 K
T2 = 400   # 温度2 K
T3 = 500   # 温度3 K

# 生成体积数据
V = np.linspace(0.1, 10, 400)

# 计算压力数据
P1 = n * R * T1 / V
P2 = n * R * T2 / V
P3 = n * R * T3 / V

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制等温线
plt.plot(V, P1, label=f'T = {T1} K')
plt.plot(V, P2, label=f'T = {T2} K')
plt.plot(V, P3, label=f'T = {T3} K')

# 设置图形
plt.xlabel('体积 V (L)')
plt.ylabel('压力 P (Pa)')
plt.title('理想气体的 P-V 图（等温线）')
plt.legend()
plt.grid(True)

# 显示图形
plt.show()
