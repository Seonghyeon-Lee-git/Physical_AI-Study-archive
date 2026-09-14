a = [1, 2, 3]
b = a
c = [1, 2, 3]


print(a is b, a is c, a == c)
print(id(a) == id(b), id(a) == id(c))


b.append(4)
print(a)


# 예상 결과
# True False True
# True False
# [1, 2, 3, 4]

# a와 b가 같은 주소값을 가지므로 
# b 리스트에 4를 추가하면 a에서도 4가 추가된다