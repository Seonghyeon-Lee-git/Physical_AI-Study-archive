# 1단계 : 한 걸음 갱신
def update_weight(w_t, learning_rate, gradient):
    """
    경사하강법 공식으로 가중치를 갱신한다.
    """

    w_next = w_t - learning_rate * gradient

    return w_next

# --- 테스트 코드 ---
current_w = 0.5
eta = 0.01  # 학습률
grad = 2.0  # 임의로 계산된 기울기

# 함수 호출
new_w = update_weight(current_w, eta, grad)
print("1단계")
print(f"업데이트된 가중치: {new_w}")


# 2단계 : 종료조건까지 반복
def gradient(w):
    return 2 * (w - 3)  # dE / dw

def gradient_desent(w_init, learning_rate, tolerance, max_iter):
    w = w_init
    history = [w]

    for t in range(max_iter):
        grad = gradient(w)        # (2) 기울기
        w_next = update_weight(w, learning_rate, grad)      # (3) 이동
        history.append(w_next)

        # (4) 종료조건을 여기에 작성하세요
        if abs(w_next - w) < tolerance:
            return w_next, t + 1, history

        w = w_next

    return w, max_iter, history

# --- 테스트 코드 ---
print("2단계")
print(gradient_desent(0, 0.1, 0.000001, 61))