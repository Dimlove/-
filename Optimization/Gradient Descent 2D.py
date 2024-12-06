import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 二维目标函数和梯度
def func_2d(x1, x2):
    return x1 ** 2 + x2 ** 2  # f(x1, x2) = x1^2 + x2^2

def grad_func_2d(x1, x2):
    return np.array([2 * x1, 2 * x2])  # ∇f(x1, x2) = [2x1, 2x2]

# 梯度下降法（2D）
def gradient_descent_2d(learning_rate=0.1, max_iter=100, tolerance=1e-6):

    # x1 , x2 = np.random.randn(2)  # 随机初始化x, y
    x1, x2 = 4, 4  # 初始化x1, x2
    history = [(x1, x2)]  # 记录每次迭代的(x1, x2)

    for _ in range(max_iter):
        grad = grad_func_2d(x1, x2)
        x1, x2 = np.array([x1, x2]) - learning_rate * grad  # 更新(x1, x2)
        history.append((x1, x2))

        # 如果变化非常小，提前结束
        if np.linalg.norm(grad) < tolerance:
            break

    return (x1, x2), history

# 执行梯度下降（2D）
min_xy, history_2d = gradient_descent_2d(learning_rate=0.1)

# 绘制二维函数的图像
x_vals_2d = np.linspace(-5, 5, 100)
y_vals_2d = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals_2d, y_vals_2d)
Z = func_2d(X, Y)

# 创建图像
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制函数表面，设置透明度和背景颜色
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.3)

# 绘制梯度下降路径
history_2d = np.array(history_2d)
ax.scatter(history_2d[:, 0], history_2d[:, 1], func_2d(history_2d[:, 0], history_2d[:, 1]),
           color='r', marker='x', s=50, label="Gradient Descent Path")

# 标题和轴标签
ax.set_title("Gradient Descent on a 2D Quadratic Function")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("f(x1, x2)")

# 添加网格
ax.grid(True)

# 显示图例
ax.legend()

# 显示图像
plt.show()

# 输出结果
print(f"Minimum found at (x1, x2) = {min_xy}")
