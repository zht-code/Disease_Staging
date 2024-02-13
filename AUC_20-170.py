import matplotlib.pyplot as plt
import numpy as np

# 假设我们有九组数据，每组数据包含早、中、晚期的A、R、Z适配体
normal_data = [
    np.array([0,1.43369890329013,1.19990029910269,0.869641076769691,0.629860418743769,0.488035892323031,0.0408773678963111]),
    np.array([0,1.21886446886447,1.0521978021978,0.886446886446886,0.791514041514041,0.565018315018315,-0.00488400488400488]),
    np.array([0,1.35575719649562,1.13767209011264,0.851689612015019,0.741551939924906,0.714956195244055,0.0619524405506884])
]

early_data = [
    np.array([0,0.928515007898894,2.37085308056872,0.95695102685624,0.732227488151659,0.690165876777251,-0.096563981042654]),
    np.array([0,1.4913844325609,0.669043374925728,0.509209744503862,0.398692810457516,0.363042186571598,-0.132501485442662]),
    np.array([0,2.88989578613502,3.24558223833258,1.51699139102855,1.36746714997734,1.2091073855913,0.47757136384232])
]

late_data = [
    np.array([0,2.46059405940594,3.1980198019802,3.63366336633663,2.71207920792079,3.13861386138614,0.31009900990099]),
    np.array([0,0.848195329087049,0.815286624203822,0.736464968152866,0.714968152866242,0.573513800424628,-0.0241507430997877]),
    np.array([0,3.69020652898068,4.33977348434377,4.70619586942039,2.78747501665556,3.51032644903398,-0.0266489007328448])
]

# 生成时间数据
time = np.array([0, 20, 45, 60, 75, 90, 170])

# 创建包含九个子图的网格，共享相同的纵坐标轴
fig, axs = plt.subplots(3, 3, figsize=(12, 10), sharex=True, sharey=True)


datasets = [normal_data, early_data, late_data]
categories = ['Normal', 'Early', 'Late']
variables = ['ZY-1-AAFP', 'Random', 'ZY-1-Cy5']
# 创建一个布尔数组，只有在20-170分钟内的值为True
mask = (time >= 20) & (time <= 170)
# 遍历每个子图，绘制对应的数据
for i, category in enumerate(categories):
    for j, variable in enumerate(variables):
        index = i * 3 + j
        axs[i, j].plot(time, datasets[i][j], color='black', label=f'{variable} - {category}')
        # axs[i, j].fill_between(time, datasets[i][j], color='pink',alpha=0.5)

        time_new = np.linspace(time.min(), time.max(), 500)
        data = np.interp(time_new, time, datasets[i][j])
        condition = mask & (datasets[i][j] >= datasets[i][j][1])
        condition_new = np.interp(time_new, time, condition)
        axs[i, j].fill_between(time_new, data, datasets[i][j][1], where=condition_new, color='pink', alpha=0.5)
        axs[i, j].fill_between(time_new, data, datasets[i][j][1], where=condition_new, color='#96cde0', alpha=0.5)
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
