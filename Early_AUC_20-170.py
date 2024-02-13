import matplotlib.pyplot as plt
import numpy as np


# 数据
time = np.array([0,20,45,60,75,90,130,170])
A = np.array([0, 1.0407955, 2.06025209, 0.93609188, 0.73261531, 0.56216121, 0.34908609,-0.081125694])
R = np.array([0,1.016607503,0.469140022,0.340394605,0.319069385,0.243729585,-0.107881668,-0.124288388])
Z = np.array([0,2.551680869,3.419905259,1.68644493,1.294151704,1.087960032,0.793965115,0.577508795])
# 创建一个布尔数组，只有在20-170分钟内的值为True
mask = (time >= 20) & (time <= 130)
# 创建一个布尔数组，只有在20-170分钟内的值为True
# 创建新的时间数组，包含更多的数据点
new_time = np.linspace(time.min(), time.max(), 500)


# 对A进行插值
new_A = np.interp(new_time, time, A)
# 创建新的布尔数组
new_mask = (new_time >= 20) & (new_time <= 130)
fig, axs = plt.subplots(3, figsize=(6, 6))
# 绘制Normal R1图
axs[0].plot(new_time, new_A, color='black')
axs[0].fill_between(new_time, new_A, A[1], where=new_mask & (new_A >= A[1]), color='pink', alpha=0.5)
axs[0].fill_between(new_time, new_A, A[1], where=new_mask & (new_A <= A[1]), color='#96cde0', alpha=0.5)
# axs[0].plot(time, A, color='black')
# axs[0].fill_between(time, A, 258.61, where=mask & a, color='pink', alpha=0.5)
# axs[0].fill_between(time, A, 258.61, where=mask & b, color='#96cde0', alpha=0.5)
axs[0].set_title('Early ZY-1-AFP')
axs[0].set_ylabel('fluorescence intensity ratio')
# 在顶点处添加粗点
axs[0].scatter(time, A, color='black', s=10)  # s参数控制点的大小

# 绘制Early stage R1图
axs[1].plot(time, R, color='black')
axs[1].fill_between(time, R, R[1], where=mask, color='#96cde0', alpha=0.5)
axs[1].set_title('Early Random')
axs[1].set_ylabel('fluorescence intensity ratio')
axs[1].scatter(time, R, color='black', s=10)  # s参数控制点的大小

# 绘制Late stage R1图
# 对A进行插值
new_Z = np.interp(new_time, time, Z)
# 创建新的布尔数组
new_mask = (new_time >= 20) & (new_time <= 130)
axs[2].plot(new_time, new_Z, color='black')
axs[2].fill_between(new_time, new_Z, Z[1], where=new_mask & (new_Z >= Z[1]), color='pink', alpha=0.5)
axs[2].fill_between(new_time, new_Z, Z[1], where=new_mask & (new_Z <= Z[1]), color='#96cde0', alpha=0.5)
axs[2].set_title('Early ZY-1')
axs[2].set_ylabel('fluorescence intensity ratio')
axs[2].set_xlabel('Time (min)')
axs[2].scatter(time, Z, color='black', s=10)  # s参数控制点的大小

plt.tight_layout()
plt.show()
