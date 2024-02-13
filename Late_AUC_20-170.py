import matplotlib.pyplot as plt
import numpy as np

# 假设我们有一些数据
# 数据
time = np.array([0,20,45,60,75,90,130,170])
A = np.array([0, 2.59048197, 3.3397743, 3.80100707, 2.85933545, 3.25251939, 0.39601476,0.089927044])
R = np.array([0,0.890740975,0.861323561,0.711781527,0.648606915,0.57420297,0.163505947,-0.058625267])
Z = np.array([0,3.255660735,4.119060969,4.527914492,2.416478211,3.345613489,1.816424677,-0.000363108])
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
axs[0].set_title('Late ZY-1-AFP')
axs[0].set_ylabel('fluorescence intensity ratio')
# 在顶点处添加粗点
axs[0].scatter(time, A, color='black', s=10)  # s参数控制点的大小

# 绘制Early stage R1图
new_R = np.interp(new_time, time, R)
new_mask = (new_time >= 20) & (new_time <= 130)
axs[1].plot(time, R, color='black')
axs[1].fill_between(new_time, new_R, R[1], where=new_mask & (new_R >= R[1]), color='pink', alpha=0.5)
axs[1].fill_between(new_time, new_R, R[1], where=new_mask & (new_R <= R[1]), color='#96cde0', alpha=0.5)
# axs[1].fill_between(time, R, 65.39, where=mask, color='#96cde0', alpha=0.5)
axs[1].set_title('Late Random')
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
axs[2].fill_between(new_time, new_Z, Z[4], where=(new_time >= 75) & (new_time <= 130) & (new_Z >= Z[4]), color='pink', alpha=0.5)
axs[2].set_title('Late ZY-1')
axs[2].set_ylabel('fluorescence intensity ratio')
axs[2].set_xlabel('Time (min)')
axs[2].scatter(time, Z, color='black', s=10)  # s参数控制点的大小

plt.tight_layout()
plt.show()
