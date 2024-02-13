import matplotlib.pyplot as plt
import numpy as np

# 数据点
normal = np.array([-4.967851657, -4.839360774, -4.901574273], dtype=float)
early = np.array([-2.919252663, -2.697686644, -2.803042244], dtype=float)
late = np.array([-1.843397258, -1.916700101, -1.879554961], dtype=float)

early_auc = np.array([249.7366335,233.6457892,252.5125601], dtype=float)
late_auc = np.array([447.9047302,412.4540988,395.7459496], dtype=float)
normal_auc = np.array([113.5951189,112.483615,92.29688139], dtype=float)

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
plt.ylabel('$AUC_{0-170 min}$ by ZY-1')
plt.title('$AUC_{0-170 min}$ by ZY-1 vs LogitFPA')

# 显示图例
plt.legend()

# 显示图形
plt.show()
