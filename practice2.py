

#반복문

fruits = ['사과','배','감','귤']

# for fruit in fruits:
#     print(fruit)
#

# count = 0
#
# for fruit in fruits:
#     if fruit == '사과':
#         count += 1
#
# print(count)

# 함수로 만들기 todo count_fruit 과일이름을 받아서 과일 숫자를 return

fruits = ['사과','배','감','귤']

def count_fruit(name):
    count = 0

    for fruit in fruits:
        if fruit == name:
            count += 1

    return count  #if문 다 돌고 리턴하기 포문에 있으면 제한되버림.

print(count_fruit('배'))


