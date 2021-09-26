# console.log
print('Hello world')

# let a =3  /자바스크립트
name = '임상하'
print(name)
print(type(name))

#typeof()  자바스크립에서는
a = 3
print(type(a))

#True 대문자
c = True
print(type(c))


#python List
li = []
fruit_list = ['감','사과','배']
print(fruit_list)

#javascript push
fruit_list.append('딸기')
print(fruit_list)

fruit_list.append(['사과','배'])
print(fruit_list[4][0])

#파이썬 딕셔러니리
dic = {'name': '상하', 'age':31}  #자바는 let 을 붙임

print(dic)
print(type(dic))

dic['height'] = 180 #사전 추가
print(dic)

people = [{'name':'상하'},{'name':'상하'}]

print(people)

people1 = {'name':'혁찬'}

people.append(people1)

print(people)



#자바 함수
# funtion sum(a,b){
#     return a+b
# }

def sum(a,b):
    return a+b  #4칸 뛰어야함 1tap

print(sum(2,3))

def mul(a, b):
    return a*b

result = sum(2,3) + mul(2,3)
print(result)


# # 자바 이프문
# function check_age(age){
#     if (age>10)
#      얼럿 어쩌구
#     }

def check_age(age):
    if age > 10:
        print('청소년이에요')
        return '청소년'
    elif age <10:
        print('어린이에요')
        return '어린이'

print(check_age(5))

#짝수 판별 함수
def is_even(num):
    if num % 2 ==0:
        return True
    else:
        return False

print(is_even(10))


함수 만들어보기  어린이 청소년 성인을 판별하는 함수 만드러보세요
check_age  (0~10 어린이 11~19 청소년 20세 이상 성인0
def check_age(age):
    if age <10 and age >0:  # 최근 0<age <10 이런식으로 패치됨
        print('어린이입니다')
        return '어린이'
    elif 10 <= age <20:
        print('청소년입니다')
        return '청소년'
    else:  #수식이 따로 없음 걍 else: 끝
        print('성인입니다')
        return '성인'

print(check_age(22))
