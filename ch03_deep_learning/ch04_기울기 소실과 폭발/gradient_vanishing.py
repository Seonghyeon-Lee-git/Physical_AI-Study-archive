import numpy as np

def sigmoid_derivative(x):
    return x * 0.25

def relu_derivative(x):
    if x > 0:
        return 1
    else:
        return 0

hidden_layer = 10
gradient = 1.0

def sigmoid_network(gradient):
    for _ in range(hidden_layer):
        gradient = sigmoid_derivative(gradient)
    return gradient

def relu_network(gradient):
    for _ in range(hidden_layer):
        gradient = relu_derivative(gradient)
    return gradient

print("--- 기울기 소실 시뮬레이션 테스트 ---")
print(f"설정: 은닉층 수 = {hidden_layer}, 초기 기울기 = {gradient}\n")
print(f"Sigmoid 네트워크 {hidden_layer}층 통과 후 최종 기울기: {sigmoid_network(gradient):0.10f}")
print("결과 분석: 기울기가 0에 가깝게 매우 작아져 기울기 소실(Gradient Vanishing)이 발생함을 확인할 수 있습니다.\n")
print(f"Relu 네트워크 {hidden_layer}층 통과 후 최종 기울기: {relu_network(gradient)}")
print("결과 분석: 기울기가 1.0으로 유지되어 깊은 층에서도 기울기 소실 없이 학습이 가능함을 확인할 수 있습니다.")
