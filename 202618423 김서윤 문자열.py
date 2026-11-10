# 문자열 입력받기
inStr = input("영문 문장을 입력하세요: ")

# 대소문자 구분을 없애기 위해 소문자로 변환한 문자열 준비
lowerStr = inStr.lower()

# 모음 개수 세기
count = 0
for i in ['a', 'e', 'i', 'o', 'u']:
    count += lowerStr.count(i)

# 모음을 '*'로 치환하기
outStr = inStr
for i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    outStr = outStr.replace(i, "*")

# 결과 출력
print("모음의 총 개수:", count)
print("변환된 문자열:", outStr)