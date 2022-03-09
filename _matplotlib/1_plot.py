import random
from matplotlib import pyplot

pyplot.figure(figsize=(20, 8), dpi=100)

# 显示一个小时里的温度变化
x = range(60)
y_beijing = [random.uniform(10, 15) for i in x]
y_shanghai = [random.uniform(15, 25) for i in x]
pyplot.plot(x, y_beijing, label='beijing', color='r', linestyle='--')
pyplot.plot(x, y_shanghai, label='shanghai')

# x/y轴添加刻度
y_ticks = range(40)
x_ticks = ['10h{}m'.format(i) for i in x]
# 注意：第一个参数必须是数字，若不是，则需要进行值替换
pyplot.yticks(y_ticks[::5])
pyplot.xticks(x[::5], x_ticks[::5])

# 添加网格
pyplot.grid(True, linestyle='--', alpha=1)  # linestyle为线样式(短杠为实线，双短杠为虚线) alpha为线透明度

# 添加描述信息
pyplot.xlabel('time')
pyplot.ylabel('temperature')
pyplot.title('temperature change in an hour', fontsize=20)

# 显示图例
pyplot.legend(loc=1)   # 需要在plot时声明label，loc指定显示位置，默认为0表示适当位置

pyplot.show()
# 中文显示，需要字体包





