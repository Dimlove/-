# 牛顿法
import numpy as np
import matplotlib.pyplot as plt

# 二维目标函数及其梯度和海森矩阵
def func_2d(x1, x2):
    return x1 ** 2 + x2 ** 2 - 4 * x1 - 4 * x2 + 4


def grad_func_2d(x1, x2):
    return np.array([2 * x1 - 4, 2 * x2 - 4])


def hessian_func_2d(x1, x2):
    return np.array([[2, 0], [0, 2]])


# 牛顿法（2D）
def newton_method_2d(learning_rate=0.1, max_iter=100, tolerance=1e-6):
    x1, x2 = 4, 4  # 初始点
    history = [(x1, x2)]

    for _ in range(max_iter):
        grad = grad_func_2d(x1, x2)
        hessian = hessian_func_2d(x1, x2)
        hessian_inv = np.linalg.inv(hessian)  # 海森矩阵的逆
        step = np.dot(hessian_inv, grad)  # 更新公式
        x_new = np.array([x1, x2]) - learning_rate * step  # 更新
        history.append(tuple(x_new))

        if np.linalg.norm(x_new - np.array([x1, x2])) < tolerance:
            break
        x1, x2 = x_new

    return tuple(x_new), history


# 执行牛顿法
min_x_2d, history_2d = newton_method_2d()

# 绘制二维函数图像
x_vals_2d = np.linspace(0, 6, 100)
y_vals_2d = np.linspace(0, 6, 100)
X, Y = np.meshgrid(x_vals_2d, y_vals_2d)
Z = func_2d(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制函数的表面图
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

# 绘制牛顿法路径
history_2d = np.array(history_2d)
ax.scatter(history_2d[:, 0], history_2d[:, 1], func_2d(history_2d[:, 0], history_2d[:, 1]),
           color='r', marker='x', label="Newton's Method Path")

# 设置标签和标题
ax.set_title("Optimization of $f(x_1, x_2) = x_1^2 + x_2^2 - 4x_1 - 4x_2 + 4$ using Newton's Method")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("f(x1, x2)")
ax.legend()
plt.show()

print(f"Minimum found at (x1, x2) = {min_x_2d}")
