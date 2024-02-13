import matplotlib.pyplot as plt
import numpy as np

# 假设我们有九组数据，每组数据包含早、中、晚期的A、R、Z适配体
normal_data = [
    np.array([0, 1.39046421, 0.99496808, 0.74944677, 0.54665018, 0.46179214, 0.34460064,-0.10181919]),
    np.array([0,1.302407379,1.068290429,0.832018929,0.684032993,0.461120067,0.159080849,-0.023076329]),
    np.array([0,1.391317749,1.208640963,0.843624117,0.698427078,0.580338292,0.400870774,-0.001227506])
]

early_data = [
    np.array([0, 1.0407955, 2.06025209, 0.93609188, 0.73261531, 0.56216121, 0.34908609,-0.081125694]),
    np.array([0,1.016607503,0.469140022,0.340394605,0.319069385,0.243729585,-0.107881668,-0.124288388]),
    np.array([0,2.551680869,3.419905259,1.68644493,1.294151704,1.087960032,0.793965115,0.577508795])
]

late_data = [
    np.array([0, 2.59048197, 3.3397743, 3.80100707, 2.85933545, 3.25251939, 0.39601476,0.089927044]),
    np.array([0,0.890740975,0.861323561,0.711781527,0.648606915,0.57420297,0.163505947,-0.058625267]),
    np.array([0,3.255660735,4.119060969,4.527914492,2.416478211,3.345613489,1.816424677,-0.000363108])
]

# 生成时间数据
time = np.array([0, 20, 45, 60, 75, 90, 130, 170])

# 创建包含九个子图的网格，共享相同的纵坐标轴
fig, axs = plt.subplots(3, 3, figsize=(12, 10), sharex=True, sharey=True)


datasets = [normal_data, early_data, late_data]
categories = ['Normal', 'Early', 'Late']
variables = ['ZY-1-AaFp', 'Random', 'ZY-1-Cy5']

# 遍历每个子图，绘制对应的数据
for i, category in enumerate(categories):
    for j, variable in enumerate(variables):
        index = i * 3 + j
        axs[i, j].plot(time, datasets[i][j], color='black', label=f'{variable} - {category}')
        axs[i, j].fill_between(time, datasets[i][j], color='pink',alpha=0.5)
        axs[i, j].set_title(f'{variable} - {category}')
        axs[i, j].set_xlabel('Time (min)')
        axs[i, j].set_ylabel('fluorescence intensity ratio')
        axs[i, j].scatter(time, datasets[i][j], color='black', s=10)  # s参数控制点的大小

# 设置共享的横坐标轴和纵坐标轴标签
axs[2, 1].set_xlabel('Time (min)')
axs[1, 0].set_ylabel('fluorescence intensity ratio')

# 调整子图之间的间距
plt.tight_layout()

# 显示图例
plt.legend()

# 显示图形
plt.show()
