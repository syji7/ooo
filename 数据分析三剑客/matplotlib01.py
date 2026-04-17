import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import random

# matplotlib.use('TKAgg')
# # 创建随机的数组
# a = np.random.randint(0, 100, (100, 3))
# # 绘制折线图
# df = pd.DataFrame(a, columns=['x', 'y', 'z'])
# print(df.describe())
# df.plot(kind='line')
# plt.show()

# 导包
# 准备数据
# 模拟半年的销售数据
# matplotlib.use('TKAgg')
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# month = np.array([i for i in range(1, 13)])
# sales = np.array([random.randint(0, 1000) for i in month])
# # 导入数据:
# df = pd.DataFrame({'月份': month, '销量': sales})
# # 可视化及参数
# plt.plot(df['月份'], df['销量'])
# plt.title('2025年销量折线图')
# plt.grid()
# plt.xticks(month)
# plt.xlabel('月份')
# plt.ylabel('销量')
# plt.show()


matplotlib.use('TKAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# (以后这一块就是要导入收集到的数据)
# 模拟50个房屋面积
area = np.array([random.randint(100, 300) for i in range(50)])
# 模拟50个房屋价格
price = np.array([random.randint(6000, 14000) for i in range(50)])
df = pd.DataFrame({'面积': area, '价格': price})
plt.scatter(df['面积'], df['价格'], color='red', s=100, alpha=0.5)
plt.title('房屋面积-价格散点图')
plt.grid()
plt.xlabel('面积')
plt.ylabel('价格')
plt.show()
