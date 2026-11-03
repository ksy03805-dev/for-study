##변수 선언 부분##
price, paid, change, c5000, c1000, c500, c100, c10=0, 0, 0, 0, 0, 0, 0, 0

##메인 코드 부분##
M=int(input("구매한 물건은 얼마?"))
N=int(input("지불한 돈은 얼마?"))
change=M-N

if change < 0:
    print("\n지불한 돈이 부족합니다!")
else:
    print(f"\n총 거스름돈: {change}원\n")

c5000=change//5000
change%=5000

c1000=change//1000
change%=1000

c500=change//500
change%=500

c100=change//100
change%=100

c10=change//10
change%=10

print("5000원짜리==> %d개" % c5000)
print("1000원짜리==> %d개" % c1000)
print("500원짜리==> %d개" % c500)
print("100원짜리==> %d개" % c100)
print("10원짜리==> %d개" % c10)
print("바꾸지 못한 잔돈==> %d원\n" % change)
