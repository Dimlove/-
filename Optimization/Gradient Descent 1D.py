import numpy as np
import matplotlib.pyplot as plt

# 梯度下降法求解 f(x) = x^2 + 2x + 1
# 一维目标函数和梯度
def func_1d(x):
    return x ** 2 + 2 * x + 1  # f(x) = x^2 + 2x + 1


def grad_func_1d(x):
    return 2 * x + 2  # ∇f(x) = 2x + 2


# 梯度下降法（1D）
def gradient_descent_1d(learning_rate=0.1, max_iter=100, tolerance=1e-6):

    # x = np.random.randn()  # 随机初始化x
    x = 4   # 初始化x

    history = [x]  # 记录每次迭代的x值

    for _ in range(max_iter):
        grad = grad_func_1d(x)
        x = x - learning_rate * grad  # 更新x
        history.append(x)

        # 如果变化非常小，提前结束
        if np.abs(grad) < tolerance:
            break

    return x, history


# 执行梯度下降（1D）
min_x, history_1d = gradient_descent_1d(learning_rate=0.1)

# 绘制一维函数的图像
x_vals_1d = np.linspace(-5, 5, 100)
y_vals_1d = func_1d(x_vals_1d)

plt.plot(x_vals_1d, y_vals_1d, label="f(x) = x^2 + 2x + 1")
plt.scatter(history_1d, [func_1d(x) for x in history_1d], color='red', marker='x', label="Iterations")
plt.title("Gradient Descent on a 1D Quadratic Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

# 输出结果
print(f"Minimum found at x = {min_x}")
