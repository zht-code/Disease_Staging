import matplotlib.pyplot as plt
import numpy as np

# 数据点
normal = np.array([-4.967851657, -4.839360774, -4.901574273], dtype=float)
early = np.array([-2.919252663, -2.697686644, -2.803042244], dtype=float)
late = np.array([-1.843397258, -1.916700101, -1.879554961], dtype=float)

early_auc = np.array([81.50000005,83.26893358,84.4932131], dtype=float)
late_auc = np.array([83.43749998,87.37462524,76.99867538], dtype=float)
normal_auc = np.array([100.2808303,91.41846924,91.47341098], dtype=float)

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
plt.ylabel('$AUC_{0-170 min}$ by Random')
plt.title('$AUC_{0-170 min}$ by Random vs LogitFPA')
# 设置纵坐标范围
plt.ylim(0, 120)
# 显示图例
plt.legend()

# 显示图形
plt.show()
