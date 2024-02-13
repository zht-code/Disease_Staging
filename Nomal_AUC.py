import matplotlib.pyplot as plt
import numpy as np

# 假设我们有一些数据
# 数据
time = np.array([0,20,45,60,75,90,170])
A = np.array([0,1.458906526,1.019047619,0.770017637,0.591534392,0.540035273,-0.104761905])
R = np.array([0,1.332284456,1.111076149,0.817180617,0.680302077,0.392385148,-0.04562618])
Z = np.array([0,1.261797292,1.321296676,0.805088223,0.659006976,0.403775133,-0.09150595])

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
axs[0].set_title('Normal ZY-1-AFP')
axs[0].set_ylabel('fluorescence intensity ratio')
# 在顶点处添加粗点
axs[0].scatter(time, A, color='black', s=10)  # s参数控制点的大小
# axs[0].set_ylim([0, 120])  # 设置y轴范围

# 绘制Early stage R1图  
axs[1].plot(time, R, color='black')
axs[1].fill_between(time, R, color='pink', alpha=0.5)
axs[1].set_title('Normal Random')
axs[1].set_ylabel('fluorescence intensity ratio')
axs[1].scatter(time, R, color='black', s=10)  # s参数控制点的大小
# axs[1].set_ylim([0, 120])  # 设置y轴范围

# 绘制Late stage R1图
axs[2].plot(time, Z, color='black')
axs[2].fill_between(time, Z, color='pink', alpha=0.5)
axs[2].set_title('Normal ZY-1')
axs[2].set_ylabel('fluorescence intensity ratio')
axs[2].set_xlabel('Time (min)')
axs[2].scatter(time, Z, color='black', s=10)  # s参数控制点的大小
# axs[2].set_ylim([0, 120])  # 设置y轴范围


plt.tight_layout()
plt.show()
