import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import matplotlib as mpl
import math

np.random.seed(1000)
y = np.random.standard_normal((20,2))
x = range(len(y))
# plt.plot(x,y)
#
#
# yAgain = np.random.standard_normal(20)
# plt.plot(x,yAgain)
#
#
# # PPI:
# # Low: 800*600   Middle: 1024*768   High: 1920*1080
# plt.figure(figsize=(8, 6))
# plt.plot(y[:, 0], lw=1.5, label='1st')
# plt.plot(y[:, 1], lw=3, label='2nd')
# # Color:  b, g, r, c, m, y, k, w
# # Line Style: -, _, -., :, ., ,, o, v, ^
# plt.grid(True)
# plt.axis('tight')
# # .axis Parameters:
# # Empty, off, equal, scaled, tight, image
# plt.xlim(-1,30)
# plt.ylim(-3,3)
# plt.xlabel('index')
# plt.ylabel('value')
# plt.title('A Simple Plot')
# legend_loc = {
#     'BestPossible': 0,
#     'UpperRight': 1,
#     'UpperLeft': 2,
#     'LowerLeft': 3,
#     'LowerRight': 4,
#     'Right': 5,
#     'CenterLeft': 6,
#     'CenterRight': 7,
#     'LowerCenter': 8,
#     'UpperCenter': 9,
#     'Center': 10
# }
# plt.legend(loc=legend_loc['Right'])

# ---------------------------------------------------------------
# 双轴折线图
# PPI:
# Low: 800*600   Middle: 1024*768   High: 1920*1080
subplots_figsize = {
    'Low': (8,6),
    'Middle': (10.24, 7.68),
    'High': (19.20, 10.8)
}
fig, ax1 = plt.subplots(figsize=subplots_figsize['Middle'])
plt.sca(ax=ax1)
plt.plot(y[:, 0], 'g', lw=1.5, label='1st')
plt.plot(y[:, 0], 'bo')
# Color:  b, g, r, c, m, y, k, w
# Line Style: -, _, -., :, ., ,, o, v, ^
plt.grid(True)
plt.axis('tight')
# .axis Parameters:
# Empty, off, equal, scaled, tight, image
plt.xlim(-1,30)
plt.ylim(-3,3)
legend_loc = {
    'BestPossible': 0,
    'UpperRight': 1,
    'UpperLeft': 2,
    'LowerLeft': 3,
    'LowerRight': 4,
    'Right': 5,
    'CenterLeft': 6,
    'CenterRight': 7,
    'LowerCenter': 8,
    'UpperCenter': 9,
    'Center': 10
}
plt.legend(loc=legend_loc['Right'])
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
ax2 = ax1.twinx()
plt.sca(ax=ax2)
plt.plot(y[:, 1] * 1000, 'r', lw=3, label='2nd')
plt.plot(y[:, 1] * 1000, 'co')
plt.legend(loc=legend_loc['LowerCenter'])
plt.ylabel('value 2nd')




# ---------------------------------------------------------
# 对齐双趋势图
# PPI:
# Low: 800*600   Middle: 1024*768   High: 1920*1080
plt.figure(figsize=(8,6))
plt.subplot(211)
plt.plot(y[:, 0], 'g', lw=1.5, label='1st')
plt.plot(y[:, 0], 'bo')
# Color:  b, g, r, c, m, y, k, w
# Line Style: -, _, -., :, ., ,, o, v, ^
plt.grid(True)
plt.axis('tight')
# .axis Parameters:
# Empty, off, equal, scaled, tight, image
plt.xlim(-1,30)
plt.ylim(-3,3)
legend_loc = {
    'BestPossible': 0,
    'UpperRight': 1,
    'UpperLeft': 2,
    'LowerLeft': 3,
    'LowerRight': 4,
    'Right': 5,
    'CenterLeft': 6,
    'CenterRight': 7,
    'LowerCenter': 8,
    'UpperCenter': 9,
    'Center': 10
}
plt.legend(loc=legend_loc['Right'])
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.subplot(212)
plt.plot(y[:, 1] * 1000, 'r', lw=3, label='2nd')
plt.plot(y[:, 1] * 1000, 'co')
plt.legend(loc=legend_loc['Right'])
plt.xlabel('index')
plt.ylabel('value 2nd')
plt.title('Second Simple Plot')
plt.axis('tight')
plt.grid(True)




# -----------------------------------------------
# 左右对比图
subplots_figsize = {
    'Low': (8,6),
    'Middle': (10.24, 7.68),
    'High': (19.20, 10.8)
}
plt.figure(figsize=subplots_figsize['Middle'])
plt.subplot(121)
plt.plot(y[:, 0], 'g', lw=1.5, label='1st')
plt.plot(y[:, 0], 'bo')
# Color:  b, g, r, c, m, y, k, w
# Line Style: -, _, -., :, ., ,, o, v, ^
plt.grid(True)
plt.axis('tight')
# .axis Parameters:
# Empty, off, equal, scaled, tight, image
plt.xlim(-1,30)
plt.ylim(-3,3)
legend_loc = {
    'BestPossible': 0,
    'UpperRight': 1,
    'UpperLeft': 2,
    'LowerLeft': 3,
    'LowerRight': 4,
    'Right': 5,
    'CenterLeft': 6,
    'CenterRight': 7,
    'LowerCenter': 8,
    'UpperCenter': 9,
    'Center': 10
}
plt.legend(loc=legend_loc['Right'])
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], width=0.5, color='r', label='2nd')
plt.grid(True)
plt.legend(loc=legend_loc['Right'])
plt.axis('tight')
plt.xlabel('index')
plt.title('Second Simple Plot')




# -----------------------------------------------------
# 简单散点图
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=subplots_figsize['Middle'])
plt.plot(y[:,0], y[:,1], 'ro')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')



# -----------------------------------------------------
# 色温散点图
c = np.random.randint(0, 10, len(y))
plt.figure(figsize=subplots_figsize['Middle'])
plt.scatter(y[:, 0], y[:, 1], c=c, marker='o')
plt.colorbar()
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')


# ------------------------------------------------------
# 左右对比直方图
plt.figure(figsize=subplots_figsize['Middle'])
plt.hist(y, label=['1st', '2nd'], bins=25)
plt.grid(True)
plt.legend(loc=legend_loc['Right'])
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')


# -----------------------------------------------------
# 重合对比直方图
plt.figure(figsize=subplots_figsize['Middle'])
plt.hist(y, label=['1st', '2nd'], color=['r', 'g'], bins=25, stacked=True)
plt.grid(True)
plt.legend(loc=legend_loc['Right'])
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')

# -----------------------------------------------------
# 为图像添加形状
# 生成数据
import random
samples = []
for i in range(0, 50):
    x1 = random.randint(-30, 30)
    x2 = random.randint(-30, 30)
    label = x1*x1 + x2*x2 - 23*23 
    if label < 50 and label > -30:
        i -= 1
        continue
    if math.fabs(x1) > 28 or math.fabs(x2) > 28:
        i -= 1
        continue
    if label > 0:
        label = 1
    else:
        label = -1
    samples.append((x1, x2, label))
# 作图
subplots_figsize = {
    'Low': (8,6),
    'Middle': (10.24, 7.68),
    'High': (19.20, 10.8)
}
plt.figure(figsize=(16, 6))
# 子图1
plt.subplot(121)
plt.title("Data")
X = [[], []]
Y = [[], []]
for tmp_list in samples:
    if tmp_list[2] == 1:
        X[0].append(tmp_list[0])
        Y[0].append(tmp_list[1])
    else:
        X[1].append(tmp_list[0])
        Y[1].append(tmp_list[1])
plt.plot(X[0], Y[0], 'ro')
plt.plot(X[1], Y[1], 'go')

cir = mpatches.Circle((0,0), radius=23,  facecolor="none",
                edgecolor="blue", linewidth=2)
#    c = mpatches.Circle((0.5, 0.5), 0.25, facecolor="green", edgecolor="red", linewidth=3)
#    pylab.gca().add_patch(cir)
ax = plt.gca()    
plt.gca().add_patch(cir)
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
plt.text(-2, -35, "${x_1}$", {'color':'b','fontsize' : 20})
plt.text(-37, 0, "${x_2}$", {'color':'b','fontsize' : 20})
ax.yaxis.set_ticks_position('left')
# 子图2
plt.subplot(122)
X = [[], []]
Y = [[], []]
for tmp_list in samples:
    if tmp_list[2] == 1:
        X[0].append(tmp_list[0] ** 2)
        Y[0].append(tmp_list[1] ** 2)
    else:
        X[1].append(tmp_list[0] ** 2)
        Y[1].append(tmp_list[1] ** 2)
plt.plot(X[0], Y[0], 'ro')
plt.plot(X[1], Y[1], 'go')

p1=[0,23*23]
p2 = [23*23,0]
plt.gca().plot(p1,p2,'b')
plt.gca().set_xlabel("${x_1^2}$",{'color':'b','fontsize' : 20})
plt.text(-100, 500, "${x_2^2}$",{'color':'b','fontsize' : 20})
plt.gca().set_xlim(0,1000)
plt.gca().set_ylim(0,1000)
plt.title("After $x_i^2$")
plt.show()