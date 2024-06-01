import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体，确保支持中文和数学符号
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体（SimHei）
rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块的问题

# 范德瓦尔斯常数（以二氧化碳为例）
a = 3.59  # L^2 atm / mol^2
b = 0.0427  # L / mol
R = 0.0821  # L atm / K mol

# 定义温度和摩尔体积范围
temperatures = [300, 400, 500]  # 温度（K）
V_m = np.linspace(0.05, 1, 500)  # 摩尔体积（L/mol）

# 绘制图形
plt.figure(figsize=(10, 6))

for T in temperatures:
    P = (R * T) / (V_m - b) - a / (V_m ** 2)
    plt.plot(V_m, P, label=f'T = {T} K')

# 设置图形
plt.xlabel('摩尔体积 $V_m$ (L/mol)')
plt.ylabel('压力 $P$ (atm)')
plt.title('范德瓦尔斯方程的 $P$-$V_m$ 曲线')
plt.legend()
plt.grid(True)
plt.ylim(20, 500)  # 限制 y 轴范围以更好地显示曲线
plt.show()
