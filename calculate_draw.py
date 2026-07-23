import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 雷达数据
z=np.array([
30171,
30353,
30756,
30799,
31018,
31278,
31276,
31379,
31748,
32175
])


# 真实值
real=np.array([
30200,
30400,
30600,
30800,
31000,
31200,
31400,
31600,
31800,
32000
])


dt=5

# alpha beta参数
alpha=0.60
beta=0.005


# 初始化
x=z[0]
v=40


x_est=[x]
v_est=[v]
x_predict_est=[]
v_predict_est=[]
for i in range(1,len(z)):

   


    # 预测
    x_predict=x+v*dt
    v_predict=v
    x_predict_est.append(x_predict)
    v_predict_est.append(v_predict)


    # 误差
    error=z[i]-x_predict


    # 更新
    x=x_predict+alpha*error

    v=v_predict+beta/dt*error
    # 保存估计
    x_est.append(x)
    v_est.append(v)
# 根据第10帧状态预测第11帧
x_predict = x + v * dt
v_predict = v

x_predict_est.append(x_predict)
v_predict_est.append(v_predict)

print("距离估计:")
print(x_est)

print("速度估计:")
print(v_est)

print("预测距离:")
print(x_predict_est)
print("预测速度:")
print(v_predict_est)
#表格

import pandas as pd
pd.set_option('display.max_columns', None)      # 显示所有列
pd.set_option('display.width', None)            # 自动调整宽度，不省略
table = pd.DataFrame(
    [
        z,
        real,
        np.round(x_est,2),
        np.round(v_est,2),
        np.round(x_predict_est,2),
        np.round(v_predict_est,2)
    ],
    index=[
        "zn",
        "真实值",
        "x^(n,n)",
        "v^(n,n)",
        "x^(n+1,n)",
        "v^(n+1,n)"
    ],
    columns=np.arange(1,11)
)
print(table)


# 绘图
time = np.arange(5, 55, 5)
time_predict=np.arange(10,60,5)

plt.figure(figsize=(10,6))

plt.plot(time, real, '-D', linewidth=2, markersize=6, label='True values')

plt.plot(time, z, '-s', linewidth=2, markersize=6, label='Measurements')

plt.plot(time, x_est, '-o', linewidth=2, markersize=6, label='Estimates')

plt.plot(time_predict, x_predict_est, '-^', linewidth=2, markersize=6, color='gray', label='Prediction')

plt.title("Range vs. Time",
          fontsize=18,
          color='darkred',
          fontweight='bold')

plt.xlabel("Time (s)", fontsize=12)

plt.ylabel("Range (m)", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.4)

plt.legend()

plt.tight_layout()

plt.show()