from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1.단계 - 데이터 불러오고 나누기
X, y = load_diabetes(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# 2단계 - 모델을 만들고 학습시키기
model = LinearRegression()
model.fit(X_train, y_train)         # TODO: 학습용 입력과 학습용 정답을 넣으세요

# 3단계 - 시험용 데이터로 예측하기
pred = model.predict(X_test)      # TODO: 시험용 입력을 넣으세요

# 4단계 - 저장하기
print("평균오차 = %6.2f" % mean_absolute_error(y_test, pred))
print("설명력 = %7.4f" % r2_score(y_test, pred))

# 5단계 기준 모델과 비교하기
base = DummyRegressor(strategy = "mean")
# TODO: base를 학습시키고 예측한 뒤 4단계와 같은 방식으로 채점하세요
base.fit(X_train, y_train)
pred2 = base.predict(X_test)
print("기준 모델 평균오차 = %6.2f" % mean_absolute_error(y_test, pred2))
print("기준 모델 설명력 = %7.4f" % r2_score(y_test, pred2))

