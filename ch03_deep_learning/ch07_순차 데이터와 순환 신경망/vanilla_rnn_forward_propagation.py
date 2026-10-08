import numpy as np


Max_time_step = 5
np.random.seed(42)  
x_seq = [np.random.randn(2, 1) for _ in range(Max_time_step)] # 입력 벡터 (2x1)
U = np.random.randn(4, 2)      # 입력-은닉 가중치 (4x2)
W = np.random.randn(4, 4)      # 은닉-은닉 가중치 (4x4)
V = np.random.randn(2, 4)      # 은닉-출력 가중치 (2x4)
output = np.array([])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return 2 * sigmoid(x*2) - 1

def softmax(z):
    exp_z = np.exp(z - np.max(z))
    return exp_z / np.sum(exp_z, axis=0, keepdims=True)

def Vanilla_RNN(t, x_seq, output, h_prev = None):
    if h_prev is None:
        h_prev = np.zeros((4, 1))

    if t > Max_time_step:
        print(output)
        return output

    xt = x_seq[t - 1]
    
    print(f"타임스탭 t = {t}")
    ht = tanh(np.dot(U, xt) + np.dot(W ,h_prev))
    print("[은닉 상태 ht]")
    print(ht)

    print("[출력값 ot]")
    ot = softmax(np.dot(V , ht))
    print(ot)

    output = np.append(output, ot)
    print("-" * 30)
    return Vanilla_RNN(t+1, x_seq, output, h_prev=ht)

print("=== 바닐라 RNN 순전파 테스트 결과 ===")
Vanilla_RNN(1, x_seq, output)