import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体，确保支持中文和数学符号
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体（SimHei）
rcParams['axes.unicode_minus'] = False    # 解决负号显示为方块的问题

# 定义函数
def f(x):
    return np.floor((x - 1600) / 100) * 10

def g(x):
    return np.floor((x - 1800) / 10) * 0.8

# 生成 x 数据
x = np.arange(1600, 5000, 1)

# 计算 y 数据
y_f = f(x)
y_g = g(x)

# 避免分母为零的情况，计算 g(x)/f(x)
y_ratio = np.zeros_like(y_f)
nonzero_indices = y_f != 0
y_ratio[nonzero_indices] =y_f[nonzero_indices]  - y_g[nonzero_indices]

# 创建图形
fig, axs = plt.subplots(2, 1, figsize=(10, 15))

# 绘制 f(x) 曲线
axs[0].step(x, y_f, where='post', label=r'$f(x) = \left\lfloor \frac{x-1600}{100} \right\rfloor \times 10$')
axs[0].set_xlabel('x')
axs[0].set_ylabel('f(x)')
axs[0].set_title('攻击转击破的曲线图')
axs[0].legend()
axs[0].grid(True)

# 绘制 g(x) 曲线
axs[0].step(x, y_g, where='post', label=r'$g(x) = \left\lfloor \frac{x-1800}{10} \right\rfloor \times 0.8$', linestyle='--')
axs[0].set_xlabel('x')
axs[0].set_ylabel('g(x)')
axs[0].set_title('攻击转击破的曲线图')
axs[0].legend()
axs[0].grid(True)

# 绘制 g(x)/f(x) 曲线
axs[1].step(x, y_ratio, where='post', label=r'$\frac{g(x)}{f(x)}$', color='green')
axs[1].set_xlabel('x')
axs[1].set_ylabel(r'$\frac{g(x)}{f(x)}$')
axs[1].set_title('v3-v4 的曲线图')
axs[1].legend()
axs[1].grid(True)

# 显示图形
plt.tight_layout()
plt.show()