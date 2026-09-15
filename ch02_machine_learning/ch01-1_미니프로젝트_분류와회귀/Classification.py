from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, confusion_matrix)

X, y = load_diabetes(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# 1단계 - 숫자 정답을 예/아니오 정답으로 바꾸기
y_train_c = (y_train > 140).astype(int)     # 140점 넘으면 1
y_test_c = (y_test > 140).astype(int)

# 2단계 - 모델을 만들고 학습시키기
clf = LogisticRegression(max_iter = 100)
clf.fit(X_train, y_train_c)      # TODO: 정답 자리에 무엇을 넣어야 할까요?

# 3단계 - 시험용 데이터로 예측하기
pred = clf.predict(X_test)       # TODO

# 4단계 - 채점하기
print("정확도 = %.4f" % accuracy_score(y_test_c,pred))      # TODO
# TODO: 정밀도, 재현율, 네 칸짜리 표도 같은 방식으로 출력하세요
print("정밀도 = %.4f" % precision_score(y_test_c,pred)) 
print("재현율 = %.4f" % recall_score(y_test_c,pred))
print("표 =") 
print(confusion_matrix(y_test_c,pred)) 

# 5단계 - 기준 모델과 비교하기
base = DummyClassifier(strategy = "most_frequent")
# TODO: base를 학습시키고 정확도를 구해 내 모델과 비교하세요
base.fit(X_train, y_train_c)
pred2 = base.predict(X_test)

print("정확도 = %.4f" % accuracy_score(y_test_c,pred2))
print("정밀도 = %.4f" % precision_score(y_test_c,pred2)) 
print("재현율 = %.4f" % recall_score(y_test_c,pred2))
print("표 =") 
print(confusion_matrix(y_test_c,pred2)) 