import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapz

# 提供示例数据，替换为你的实际数据
time = np.array([0, 20, 45, 60, 75, 90, 170])
data_A = np.random.rand(9, 7)
data_R = np.random.rand(9, 7)
data_Z = np.random.rand(9, 7)

# 创建函数计算曲线下面积
def calculate_auc(x, y):
    mask = (x >= 20) & (x <= 170)
    x_subset = x[mask]
    y_subset = y[mask]
    auc = trapz(y_subset, x=x_subset)
    return auc

# 创建子图，共享纵坐标轴
fig, axs = plt.subplots(3, 3, figsize=(12, 10), sharex=True, sharey=True)

# 遍历每个子图，绘制对应的数据
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        time_subset = time
        data_subset = data_A[index]  # 选择适配体（A、R、Z）的数据
        auc_value = calculate_auc(time_subset, data_subset)
        
        axs[i, j].plot(time_subset, data_subset, label=f'Dataset {index+1}')
        axs[i, j].fill_between(time_subset, data_subset, alpha=0.3)
        axs[i, j].set_title(f'Dataset {index+1}\nAUC: {auc_value:.2f}')
        axs[i, j].set_xlabel('Time (min)')
        axs[i, j].set_ylabel('Radiation rate (%)')

# 设置共享的横坐标轴和纵坐标轴标签
axs[2, 1].set_xlabel('Time (min)')
axs[1, 0].set_ylabel('Radiation rate (%)')

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()
