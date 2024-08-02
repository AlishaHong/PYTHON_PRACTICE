# -*- coding: utf-8 -*-
"""파이썬기초1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LD-QDF7zb6bcHV1HWNdzULZuAZK89oke
"""

#별찍기

#for i in range(n) : 와 아래 코드는 동일
#for i in range(0,n,1)

n = int(input())

for i in range(n):
    print(" " * (n-i) + "*" * (2*i+1))

for i in range(n,-1,-1):
    print(" " * (n-i) + "*" * (2*i+1))

for i in range(n):
    print(" " * i + "*" * (n-i))


n = 5
print(type(range(n)))

#range는 클래스!!!!!!!!!!!


#3번 별찍기

#       *
#      * *
#     *   *
#    *     *
#   *********

#   *********
#    *     *
#     *   *
#      * *
#       *

# 속 빈 역삼각형
# 안이 비어있는 다이아몬드


n = 5
#케이스를 3가지로 나눈다


for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1 or i == n:
        print("*" * (2 * i - 1))
    else:
        print("*" + " " * (2 * i - 3) + "*")


n=5
for i in range(0,5,1):
  if (i==0):
    print(" "*((n-1)-i) + "*")
  elif (i<n-1):
    print(" "*((n-1)-i) + "*" + " "*(2*i-1) + "*")
  else:
    print("*"* (2*i+1))


for i in range(n):
  if i == 0:
    print(" " * (n - 1) + "*" + " " * (n - 1))
  elif i < n:
    print(" " * (n - 1 - i) + "*" + " " * (2 * i - 1) + "*")

for i in range(n - 2, -1, -1):
  if i == 0:
    print(" " * (n - 1) + "*" + " " * (n - 1))
  else:
    print(" " * (n - 1 - i) + "*" + " " * (2 * i - 1) + "*")

n = 5
for i in range(n):
    if i == 0:
        print(" " * (n-1) + "*")
    elif i<n-1:
        print(" " * (n-1-i) + "*" + " " * (i*2-1) + "*")
    else:
        print("*" * (i*2+1))


for i in range(n-1,-1,-1):
    if i == 0:
        print(" " * (n-1) + "*")
    elif i<n-1:
        print(" " * (n-1-i) + "*" + " " * (i*2-1) + "*")
    else:
        print("*"* (i*2+1))
print()

n = 5

for i in range(n):
    if i == 0:
        print(" " * (n-1) + "*")
    elif i<n:
        print(" " * (n-1-i) + "*" + " " * (i*2-1) + "*")

for i in range(n-1,-1,-1):
    if i == 0:
        print(" " * (n-1) + "*")
    elif i<n-1:
        print(" " * (n-1-i) + "*" + " " * (i*2-1) + "*")


#i = 0 공백:8 별:1
#i = 1 공백:7 별:3
#i = 2 공백:6 별:5
#i = 3 공백:5 별:7
#i = 4 공백:4 별:1 공백 7 별:1
#i = 5 공백:3 별:3 공백:5 별:3
#i = 6 공백:2 별:5 공백:3 별:5
#i = 7 공백:1 별:7 공백:1 별:7


n = 8

for i in range(n):
    if i<n//2:
        print(" " * (n-i) + "*" * (i*2+1))
    else:
        print(" " * (n-i) + "*" * (i*2+1-n) + " " * (n-(i*2+1-n)) + "*" * (i*2+1-n))


n = 5  # 다이아몬드의 높이

# 다이아몬드의 윗부분을 출력
for i in range(n-1):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("*" * (n*2-1))
# 다이아몬드의 아랫부분을 출력

import time

def measure_if():
    n = 5
    for i in range(n):
        if i == 0:
            print(" " * (n-1) + "*")
        elif i < n-1:
            print(" " * (n-1-i) + "*" + " " * (i*2-1) + "*")
        else:
            print("*" * (i*2+1))

def measure_for():
    n = 5
    for i in range(n-1):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("*" * (n*2-1))

# 측정을 여러 번 수행하여 평균 시간 계산
repeats = 50
if_times = []
for_times = []

for _ in range(repeats):
    start = time.time()
    measure_if()
    end = time.time()
    if_times.append(end - start)

    start1 = time.time()
    measure_for()
    end1 = time.time()
    for_times.append(end1 - start1)

avg_if_time = sum(if_times) / repeats
avg_for_time = sum(for_times) / repeats

print(f'if문 평균 시간: {avg_if_time}')
print(f'for문 평균 시간: {avg_for_time}')

# n x n 크기의 사각형에 숫자를 순차적으로 채웁니다. n이 5인 경우 출력은 다음과 같습니다
#  1  2  3  4  5
#  6  7  8  9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25



#n 입력받기
n=int(input())

num = 1

table = []

for i in range(n):
  row = []
  for j in range(n):
    row.append(num)
    num +=1
  table.append(row)

digitNum = 1
if n*n < 10:
  digitNum = 1
elif n*n < 100:
  digitNum = 2
elif n*n < 1000:
  digitNum = 3
elif n*n < 10000:
  digitNum = 4
elif n*n < 100000:
  digitNum = 5

for row in table:
  for i in row:
    print(f'{i: >{digitNum}}', end=' ')
  print()


# n x n 크기의 사각형에 숫자를 위에서 아래로, 그리고 아래에서 위로 번갈아가면서 채웁니다. n이 5인 경우 출력은 다음과 같습니다.
#  1 10 11 20 21
#  2  9 12 19 22
#  3  8 13 18 23
#  4  7 14 17 24
#  5  6 15 16 25



def create_empty_matrix(n):
    matrix = []
    for _ in range(n):
        row = [0] * n
        matrix.append(row)
    return matrix

def fill_snake_matrix(n):
    matrix = create_empty_matrix(n)
    num = 1

    for col in range(n):
        if (col % 2 == 0):
            for row in range(n):
                matrix[row][col] = num
                num += 1
        else:
            for row in range(n - 1, -1, -1):
                matrix[row][col] = num
                num += 1

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# n 값을 설정합니다.
n = 5
matrix = fill_snake_matrix(n)
print_matrix(matrix)

a=10
b=30
print(a+b)

"""   
##**변수**를 선언합니다.
###<u>변수</u>를 선언합니다.
####*변수*를 ~선언~합니다.
#####1.변수를 선언합니다.

|제목|내용|설명|
|---|---|---|
|테스트1|테스트2|테스트3|



1. 파이썬 리스트
2. 마크다운

[GOOGLE](https://google.com)


"""



"""##데이터타입
####파이썬:리스트

"""

a = 123
b = 123.

type(a)
type(b)

c = a+b
type(c)
print(c)

#데이터타입
#int+int = int
#int+float = float
#int+float = int가 되려면?
#int함수 사용해서 숫자타입 변경하기

c = a + int(b)
c


# +,-,*,/
# ** 제곱

#x^y
x = 10
y = 2
result = x**y
result

# % 나머지 // 몫

#a+b
#a,b는 operand, +는 operation
op1 = 30
op2 = 4

result1 = op1//op2
result2 = op1%op2

print(result1)
print(result2)


#복합연산자
# +=,-=.*=,/=,%=,//=,**=

"""####복합연산자에는 +=, -=. *=, /=, %=, //=, **= 와 같은것이있다."""

#비어있는 리스트 생성
#myList변수 : 리스트변수
myList = []
#타입확인
type(myList)

a=10
b=20
c=a+b
d=a-b

c
d
#항상 마지막줄만 출력해준다.(마지막줄은 print함수없어도 출력)

myList = [1,2,3,4]
print(type(myList))
print(myList)

#인덱싱
myList[2]
myList[2:]
myList[:2]
myList[::2]
myList[::-1]

myList[0] + myList[3]
myList[0] * 5
myList[0] / 2
myList[0] ** 2
myList[0] % 2

#인덱스에서 -의 의미는 '뒤에서' -1(뒤에서 첫번쨰)
myList[-1]
myList[-2]
print(myList[-2:])
print(myList[:-2])
print(myList[::2])
myList[::-1]


a= [1,2,3,['a','b','c']]
a[0]
a[3]
a[3][0]

n = []
a = int(input())
n.append(a)

print(n)

"""##문자열"""

#파이썬에서는 문자열을 표현할 때 쌍따옴표와 홑따옴표 두가지를 모두 사용한다.
#이유는 상호보완

str1 =  '"hello world"'
str2 =  "'hello world'"
print(str1)
print(str2)

str3 = "It's a book!"
print(str3)

myStr="""
"죽는 날"까지 하늘을 우러러
한 점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어 가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.

오늘 밤에도 별이 바람에 스치운다.
"""

print(myStr)

#'\'와 함께 쓰면 기호 그대로 입력 가능
#역슬래쉬+n -> 개행문자(줄바꿈)

multiline = "Life is too short\nYou need python"
print(multiline)
print("\n")


#python에서 시스템의 운영체제 확인하기
import platform
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())
print(platform.platform())

from platform import platform, release
print(platform())
print(release())

#test1  test2 test3


print("test1\ttest2\ttest3")

multiline1 = "Life is too short\rYou need python"
print(multiline1)

print("=" * 50)
print("My Program")
print("=" * 50)

print("1.test1")
print("2.test2")

#문자열 길이 구하기
#공백문자도 더한다
multiline = "Life is too short\rYou need python"

print(len(multiline))

for i in multiline:
  print(i,end="")
print()

test = ['a','b','c']
for i in test:
  print(i,end="")
print()
#print 함수에는 end 매개변수에 줄바꿈을 해주는 \n이 디폴트값으로 들어가있다.

#문자열 인덱싱
a = "Life is too short"
print(a[0:4])

#문자열 인덱싱
a = "Life is too short"
print(a[0:4])

#리스트 인덱싱

myList = ['123','234',123, 234.]
myList[0]
type(myList[0])

print(a[:4])
print(a[4:])

print(a[::])
print(a[::-1])

"I eat %d apples." % 3

n = int(input())
print(f'{n}개의 사과')
print("%d개의 사과"%n)

#문자포맷팅
#1.%d(숫자) / %s(문자) /%변수도 가능

#부동소수 : 소수점의 위치가 움직이는 개념
#고정소수보다 큰 실수를 표현할 수 있음
#(고정소수는 표현할 수 있는 정수가 정해져 있기 때문)

# %문자 자체를 표현하고 싶을때 : %%

#default : 오른쪽정렬
"%10s" % "hi"

#왼쪽정렬
"%-10s" % "hi"

#혼합
"%-10sjane" %"hi"

#소수점(0을 생략할수있다. %.4f)
"%0.4f" % 3.42134234
floatNum = "%.4f" %3.42134234
a = float(floatNum)
int(a)

#문자열을 실수로 바꾸고 실수를 정수로 바꿈!


#전체 자리수가 10임
#%10.4f에서 10은 전체 자릿수를 의미
#.4f는 소수점 4자리
"%10.4f" % 3.42134234

"""###format함수"""

"I eat {0} apples".format(3)

"I eat {0} apples".format("five")

number = 3
"I eat {0} apples".format(number)

a=10
b=20
c=a+b

print("{}+{}={}".format(a,b,c))

money = int(input())

if money >= 10000:
    print("택시타라")
elif money>2000 and money<3000:
    print("버스타라")
else:
    print("걸어 인마")



#구구단
#구구단 2~4단
# 5~7단
# 8~9단
# 구구단 작성해보고 자릿수 맞추기

#오른쪽 정렬로 해서 자릿수를 2자리로 확보한다.
#2단과 3단 사이에 tab(스페이스4개정도)
#3단과 4단 사이에도 tab
#2,3,4단
#5,6,7단
#8,9단

#포맷팅 연습

for i in range(1,10):
    for j in range(2,10):
        print(f'{j}*{i}={i*j:2}', end='\t')
    print('')


for i in range(2,5):
    for j in range(1,10):
        print(f'{i}*{j}={i*j:2}')
    print()

def factorial(n):
    number = 1
    while n>0:
        number *= n
        n = n - 1
    return number

factorial(5)