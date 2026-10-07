import numpy as np

class_prob = np.array([
    [0.8, 0.15, 0.05],
    [0.10, 0.20, 0.70],
    [0.20, 0.70, 0.10]
])

confidences = np.array([
    [0.9], 
    [0.3], 
    [0.8]
    ])

classes = np.array(["자동차", "자전거", "보행자"])
THRESHOLD = 0.5
scores = class_prob * confidences
best_class_indices = np.argmax(scores, axis=1)

for i in range(len(confidences)):
    best_idx = best_class_indices[i]
    max_score = scores[i, best_idx]
    
    if max_score >= THRESHOLD:
        print(f"박스 {i}: {classes[best_idx]} ({max_score:.2f})")
    else:
        print(f"박스 {i}: 제거")

