import matplotlib.pyplot as plt
import numpy as np

# 样本数据，分别对应早期，晚期和正常阶段
normal = np.array([0.271459735,0.698427078,1.391317749]) 
early = np.array([0.793965115,1.68644493, 2.711159659])
late = np.array([1.816424677,2.131626584,3.207920792])

data = [normal, early, late]
labels = ['normal', 'early', 'late']

# 创建一个图形实例和轴实例
fig, ax = plt.subplots()
# 创建带有标签和标题的箱线图
# 设置whis参数为1.5，表示须线延伸至四分位数范围的1.5倍
# 设置showfliers参数为True，表示显示最小值和最大值
# 设置medianprops参数为一个字典，表示设置中线的颜色和宽度
ax.boxplot(data, whis=1.5, showfliers=True, medianprops=dict(color='red', linewidth=2))
ax.set_xticklabels(labels)
ax.set_title('$AUC_{20-130}$ min Boxplots by ZY-1')
ax.set_ylabel('$AUC_{20-130}$ (ZY-1)')

# 通过调整Y轴范围来限制须线的长度
ax.set_ylim([-1, 4])  # 根据数据范围调整，这里设置为[-1, 4]，根据实际情况调整
plt.show()
