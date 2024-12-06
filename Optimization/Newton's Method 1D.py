# 牛顿法
import numpy as np
import matplotlib.pyplot as plt


# 一维目标函数及其一阶导数和二阶导数
def func_1d(x):
    return x ** 2 - 4 * x + 4


def grad_func_1d(x):
    return 2 * x - 4


def grad_grad_func_1d(x):
    return 2  # 二阶导数


# 牛顿法（1D）
def newton_method_1d(learning_rate=0.1, max_iter=100, tolerance=1e-6):
    x = 4.0  # 初始点
    history = [x]

    for _ in range(max_iter):
        grad = grad_func_1d(x)
        grad_grad = grad_grad_func_1d(x)
        step = grad / grad_grad  # 牛顿法更新公式
        x_new = x - learning_rate * step  # 更新
        history.append(x_new)

        if abs(x_new - x) < tolerance:
            break
        x = x_new

    return x, history


# 执行牛顿法
min_x_1d, history_1d = newton_method_1d()

# 绘制函数图像
x_vals_1d = np.linspace(0, 6, 100)
y_vals_1d = func_1d(x_vals_1d)

plt.figure(figsize=(8, 6))
plt.plot(x_vals_1d, y_vals_1d, label="Objective Function $f(x) = x^2 - 4x + 4$", color='b')
history_1d = np.array(history_1d)
plt.scatter(history_1d, func_1d(history_1d), color='r', marker='x', label="Newton's Method Path")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Optimization of $f(x) = x^2 - 4x + 4$ using Newton's Method")
plt.legend()
plt.grid(True)
plt.show()

print(f"Minimum found at x = {min_x_1d}")
