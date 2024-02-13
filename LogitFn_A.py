import matplotlib.pyplot as plt
import numpy as np

# 数据点
normal = np.array([-4.967851657, -4.839360774, -4.901574273], dtype=float)
early = np.array([-2.919252663, -2.697686644, -2.803042244], dtype=float)
late = np.array([-1.843397258, -1.916700101, -1.879554961], dtype=float)

early_auc = np.array([202.5666469,219.8728814,235.6794085], dtype=float)
late_auc = np.array([375.9980198,345.0906464,314.6326182], dtype=float)
normal_auc = np.array([103.5655533,97.66327247,95.09082892], dtype=float)

# 绘制数据点
plt.scatter(early, early_auc, color='red', label='Early')
plt.scatter(late, late_auc, color='blue', label='Late')
plt.scatter(normal, normal_auc, color='green', label='Normal')

# 最佳拟合线
x = np.concatenate((normal, early, late), axis=None)
y = np.concatenate((normal_auc, early_auc, late_auc), axis=None)
m,b=np.polyfit(x,y ,1) 
plt.plot(x,m*x+b,color="black")

# 添加标签和标题
plt.xlabel('LogitFPA')
plt.ylabel('$AUC_{0-170 min}$ by ZY-1-AFP')
plt.title('$AUC_{0-170 min}$ by ZY-1-AFP vs LogitFPA')

# 显示图例
plt.legend()

# 显示图形
plt.show()
