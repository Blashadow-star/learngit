import matplotlib.pyplot as plt
import numpy as np

N = 7
x = np.arange(N)  # 即array([0,1,2...N])
# 随机生成N个0到100之间的整数
data = np.random.randint(low=0, high=100, size=N)
# 随机生成几种颜色，reshape第二个参数-1指随着N变化，第一维度填满有剩就来填第二维
# 生成的是随机的N组三通道(r,g,b)的颜色
colors = np.random.rand(N*3).reshape(N, -1)
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.title("Weekday Data")  # 设置窗格标题
plt.bar(x, data, alpha=0.8, color=colors, tick_label=labels)
plt.show()
