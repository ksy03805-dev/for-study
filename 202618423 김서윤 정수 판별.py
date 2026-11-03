#정수 입력#
num=int(input("정수를 입력하세요 : "))

#양수음수 판별#
if num >0 :
    sign = "양수"
elif num <0 :
    sign = "음수"
else :
    sign = "0"

#짝수홀수 판별#
if num%2==0: 
    evenodd = "짝수"
else :
    evenodd = "홀수"

##최종출력문장#
print(f"입력한 숫자 {num}은 {sign}이고 {evenodd}이다")
