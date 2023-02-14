# 多个坐标系展示
import random
from matplotlib import pyplot


# 显示一个小时里的温度变化
x = range(60)
y_beijing = [random.uniform(10, 15) for i in x]
y_shanghai = [random.uniform(15, 25) for i in x]

# pyplot.figure(figsize=(20, 8), dpi=100)
# pyplot.plot(x, y_beijing, label='beijing', color='r', linestyle='--')
# pyplot.plot(x, y_shanghai, label='shanghai')
fig, axes = pyplot.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)
axes[0].plot(x, y_beijing, label='beijing', color='r', linestyle='--')
axes[1].plot(x, y_shanghai, label='shanghai')


# x/y轴添加刻度
y_ticks = range(40)
x_ticks = ['10h{}m'.format(i) for i in x]
# pyplot.yticks(y_ticks[::5])
# pyplot.xticks(x[::5], x_ticks[::5])
axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks[::5])
axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks[::5])

# 添加网格
axes[0].grid(True, linestyle='--', alpha=1)  # linestyle为线样式(短杠为实线，双短杠为虚线) alpha为线透明度
axes[1].grid(True, linestyle='--', alpha=1)

# 添加描述信息
axes[0].set_xlabel('time')
axes[0].set_ylabel('temperature')
axes[0].set_title('temperature change in an hour', fontsize=20)
axes[1].set_xlabel('time')
axes[1].set_ylabel('temperature')
axes[1].set_title('temperature change in an hour', fontsize=20)

# 显示图例
axes[0].legend(loc=1)   # 需要在plot时声明label，loc指定显示位置，默认为0表示适当位置
axes[1].legend(loc=1)

pyplot.show()
# 中文显示，需要字体包








