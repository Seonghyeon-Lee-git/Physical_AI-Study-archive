a = "20260823Sunny"
year = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]


print(year, month, day, weather)
print(f"{year}년 {month}월 {day}일의 날씨는 {weather}입니다.")
print(a[::-1])