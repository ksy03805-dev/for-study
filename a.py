'''
mytuple = (10, 20, 30)
print(mytuple)
mylist = list(mytuple)
print(mylist)
mylist.append(40)
print(mylist)
mytuple = tuple(mylist)
print(mytuple)


animals = {"닭":"병아리",
         "개":"강아지",
         "곰":"능소니",
         "고등어":"고도리",
         "명태":"노가리",
         "말":"망아지",
         "호랑이":"개호주"}
while(True):
    myanimal=input(str(list(animals.keys()))+"중 새끼 이름을 알고 싶은 동물은?")
    if myanimal in animals:
        print("<%s>의 새끼는 <%s>입니다" % (myanimal, animals.get(myanimal)))
    elif myanimal == "끝":
        break
    else:
        print("그런 동물이 없습니다. 확인해보세요.")

ss = '파이썬짱!' 
sslen  = len(ss)
for i in range(sslen):
    print(ss[i] + '$', end=' ')


ss = '파이썬은완전재미있어요' 
sslen  = len(ss)
for i in range(sslen):
    if i % 2 == 0:
        print(ss[i], end=' ')
    else:
        print('#', end=' ')

inStr, outStr = "", ""
count, i = 0, 0
inStr = input("문자열을 입력하세요: ")
count = len(inStr)
for i in range(0, count):
    outStr +=inStr[count-(i+1)]
print("내용을 꺼꾸로 출력 --> %s" % outStr)

ss = input("입력 문자열 ==>")
print("출력 문자열 ==> ", end="")
if ss.startswith('(') == False:
    print("(", end="")
print(ss, end="")
if ss.endswith(')') == False:
    print(")", end="")

ss = ' 파 이 썬 '
ss = ss.replace(' ', '')
print(ss)

inStr = " 한글 Python 프로그래밍 "
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]
print("원래 문자열 ==>" + '[' + inStr + ']')
print("공백 삭제 문자열 ==>" + '[' + outStr + ']')

inStr = "<<<파<<이>>썬>>>"
outStr = ""

for i in range(0, len(inStr)):
    if (inStr[i] != '<') and (inStr[i] != '>'):
        outStr += inStr[i]
print("원래 문자열 ==>" + '[' + inStr + ']')
print("공백 삭제 문자열 ==>" + '[' + outStr + ']')

ss = input("입력 문자열 ==> ")
print("출력 문자열 ==> ", end="")
for i in range(len(ss)):
    if ss[i] != 'o':
        print(ss[i], end="")
    else:
        print("$", end="")

ss = input("날짜(연/월/일)==> ")
ssList = ss.split('/')
print("입력한 날짜의 10년 후 ==>", end = ' ')
print(str(int(ssList[0]) + 10) + '년', end = ' ')
print(ssList[1] + '월', end = ' ')
print(ssList[2] + '일')
'''

inStr = input("문자열 입력: ")
if inStr.isdigit():
    print("숫자입니다.")
elif inStr.isalpha():
    print("문자입니다.")
elif inStr.isalnum():
    print("숫자와 문자가 섞여 있습니다.")
else:
    print("모르겠습니다")