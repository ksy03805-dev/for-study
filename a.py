'''
mytuple = (10, 20, 30)
print(mytuple)
mylist = list(mytuple)
print(mylist)
mylist.append(40)
print(mylist)
mytuple = tuple(mylist)
print(mytuple)
'''

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
