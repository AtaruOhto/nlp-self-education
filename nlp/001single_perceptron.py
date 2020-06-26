import numpy as np

# 1層のみのパーセプトロン


def actiivate(z):
    # シグモイド関数 (sigmoid関数)
    return 1.0 / (1.0 + np.exp(-z))


def perceptron(x):
    w = np.array([-1.5, -0.99, 1.45])
    b = - 0.06
    z = b + np.dot(x, w)
    return actiivate(z)


print(perceptron(np.array([0.2, 0.3, -0.1])))
print(perceptron(np.array([0.6, -0.23, 0.11])))
print(perceptron(np.array([0.8, 0.1, 0.88])))
