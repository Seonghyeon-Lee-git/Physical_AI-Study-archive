import numpy as np


def conv2d(image, kernel):
    pad_width = 1
    kernel_w, kernel_h = kernel.shape
    image_w, image_h = image.shape

    padding_image = np.pad(image, pad_width, mode='constant')
    output = np.zeros((image_w, image_h))
    for i in range(image_h):
        for j in range(image_w):
            window = padding_image[i:i+kernel_h, j:j+kernel_w]
            output[i, j] = np.sum(window * kernel)
    return output

    

# 1. 테스트용 입력 이미지 생성 (5x5 크기)
test_image = np.array([
    [10, 10, 10, 0, 0],
    [10, 10, 10, 0, 0],
    [10, 10, 10, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

# 2. 3x3 커널 정의 (예: 라플라시안 외곽선 검출 필터)
test_kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

# 3. 합성곱 연산 수행
result_feature_map = conv2d(test_image, test_kernel)

# 4. 결과 출력
print("=== 원본 입력 이미지 (5x5) ===")
print(test_image)

print("\n=== 적용된 커널 (3x3) ===")
print(test_kernel)

print("\n=== 합성곱 연산 결과 특징 맵 (5x5) ===")
print(result_feature_map)