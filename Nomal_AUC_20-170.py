import matplotlib.pyplot as plt
import numpy as np

# 假设我们有一些数据
# 数据
time = np.array([0,20,45,60,75,90,130,170])
A = np.array([0, 1.39046421, 0.99496808, 0.74944677, 0.54665018, 0.46179214, 0.34460064,-0.10181919])
R = np.array([0,1.302407379,1.068290429,0.832018929,0.684032993,0.461120067,0.159080849,-0.023076329])
Z = np.array([0,1.391317749,1.208640963,0.843624117,0.698427078,0.580338292,0.400870774,-0.001227506])

# 创建一个布尔数组，只有在20-170分钟内的值为True
mask = (time >= 20) & (time <= 130)

fig, axs = plt.subplots(3, figsize=(6, 6))

# 绘制Normal R1图
axs[0].plot(time, A, color='black')
axs[0].fill_between(time, A, A[1], where=mask, color='#96cde0', alpha=0.5)
axs[0].set_title('Normal ZY-1-AFP')
axs[0].set_ylabel('fluorescence intensity ratio')
# 在顶点处添加粗点
axs[0].scatter(time, A, color='black', s=10)  # s参数控制点的大小
# axs[0].set_ylim([0, 120])  # 设置y轴范围

# 绘制Early stage R1图  
axs[1].plot(time, R, color='black')
axs[1].fill_between(time, R, R[1], where=mask, color='#96cde0', alpha=0.5)
axs[1].set_title('Normal Random')
axs[1].set_ylabel('fluorescence intensity ratio')
axs[1].scatter(time, R, color='black', s=10)  # s参数控制点的大小
# axs[1].set_ylim([0, 120])  # 设置y轴范围

# 绘制Late stage R1图
axs[2].plot(time, Z, color='black')
axs[2].fill_between(time, Z, Z[1], where=mask, color='#96cde0', alpha=0.5)
axs[2].set_title('Normal ZY-1')
axs[2].set_ylabel('fluorescence intensity ratio')
axs[2].set_xlabel('Time (min)')
axs[2].scatter(time, Z, color='black', s=10)  # s参数控制点的大小
# axs[2].set_ylim([0, 120])  # 设置y轴范围


plt.tight_layout()
plt.show()