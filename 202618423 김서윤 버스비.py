#승객 나이 입력#
age=int(input("나이를 입력하세요 : "))

#버스 요금 구별#
if age <12 :
    fee = "600"
elif age <19 :
    fee = "1000"
else :
    fee = "1500"

#최종 출력 문장#
print(f"버스 요금은 {fee}원 입니다.")
