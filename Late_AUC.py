import matplotlib.pyplot as plt
import numpy as np

# 假设我们有一些数据
# 数据
time = np.array([0,20,45,60,75,90,170])
A = np.array([0,2.007404595,3.040250617,3.355420543,2.381431555,2.690905639,-0.130244921])
R = np.array([0,0.879356022,0.795394335,0.667617689,0.600163032,0.530670471,-0.072957])
Z = np.array([0,2.877137714,3.891989199,4.245274527,2.330333033,3.207920792,0.054005401])

# 用梯形法则计算曲线下面积
area_A = np.trapz(A, time)
area_R = np.trapz(R, time)
area_Z = np.trapz(Z, time)

# 打印结果
print("Area under curve of A by trapezoidal rule:", area_A)
print("Area under curve of R by trapezoidal rule:", area_R)
print("Area under curve of Z by trapezoidal rule:", area_Z)

fig, axs = plt.subplots(3, figsize=(6, 6), sharex=True, sharey=True)

# 绘制Normal R1图
axs[0].plot(time, A, color='black')
axs[0].fill_between(time, A, color='pink', alpha=0.5)
axs[0].set_title('Late ZY-1-AFP')
axs[0].set_ylabel('fluorescence intensity ratio')
axs[0].scatter(time, A, color='black', s=10)  # s参数控制点的大小

# 绘制Early stage R1图
axs[1].plot(time, R, color='black')
axs[1].fill_between(time, R, color='pink', alpha=0.5)
axs[1].set_title('Late Random')
axs[1].set_ylabel('fluorescence intensity ratio')
axs[1].scatter(time, R, color='black', s=10)  # s参数控制点的大小

# 绘制Late stage R1图
axs[2].plot(time, Z, color='black')
axs[2].fill_between(time, Z, color='pink', alpha=0.5)
axs[2].set_title('Late ZY-1')
axs[2].set_ylabel('fluorescence intensity ratio')
axs[2].set_xlabel('Time (min)')
axs[2].scatter(time, Z, color='black', s=10)  # s参数控制点的大小

plt.tight_layout()
plt.show()
