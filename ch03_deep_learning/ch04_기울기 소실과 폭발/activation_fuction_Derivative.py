import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def relu(x):
    result = []
    for i in x:
        if i > 0:
            result.append(i)
        else:
            result.append(0)     
    return np.array(result)

def relu_derivative(x):
    result = []
    for i in x:
        if i > 0:
            result.append(1)
        else:
            result.append(0)
    return np.array(result)

x = np.array([-2., -0.5, 0., 0.5, 2.])

print("입력값 x:")
print(x)
print("-" * 50)
print("1. Sigmoid 함수 테스트 결과")
print("sigmoid(x):")
print(sigmoid(x))
print("sigmoid_derivative(x):")
print(sigmoid_derivative(x))
print("-" * 50)
print("2. ReLU 함수 테스트 결과")
print("relu(x):")
print(relu(x))
print("relu_derivative(x):")
print(relu_derivative(x))