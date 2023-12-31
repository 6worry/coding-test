#6025
# 정수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

# 예시
# a, b = input().split()
# c = int(a) + int(b)
# print(c)

# 참고
# 입력되는 값은 기본적으로 문자열로 인식된다.

# 문자열 + 문자열은 두 문자열을 합친 문자열을 만든다.
# 숫자로 구성된 문자열이나 실수를 정수(integer) 값으로 바꾸기 위해서는 int( ) 를 사용할 수 있다.
# 수 + 수의 결과는 합(addition)이 계산된다.
a, b = input().split()
c = int(a) + int(b)
print(c)

#6026
# 실수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

# 참고
# 입력되는 값은 기본적으로 문자열로 인식된다.

# 숫자로 구성된 문자열이나 정수를 실수(real number) 값으로 바꾸기 위해서는 float( ) 를 사용할 수 있다.
# 소숫점(.)은 그 위치가 정해져있지 않고 이리저리 둥둥 떠다니므로, floating point라고 부른다.
a = input()
b = input()
c = float(a) + float(b)
print(c)

#6027
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

# 예시
# a = input()
# n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
# print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

# 참고
# 10진수 형태로 입력받고
# %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)

# 10진법은 한 자리에 10개(0 1 2 3 4 5 6 7 8 9)의 문자를 사용하고,
# 16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 a b c d e f)의 문자를 사용한다.
# 16진수 a는 10진수의 10, b는 11, c는 12 ... 와 같다.
a = input()
b = int(a)
print('%x' % b)

#6028
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

# 예시
# print('%X' % n)  #n에 저장되어있는 값을 16진수 대문자 형태 문자열로 출력

# 참고
# 10진수 형태로 입력받고
# %X로 출력하면 16진수(hexadecimal)대문자로 출력된다.

# 16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 A B C D E F)의 문자를 사용한다.
# 16진수 A는 10진수의 10, B는 11, C는 12 ... 와 같다.
a = input()
b = int(a)
print('%X' % b)

#6029
# 16진수를 입력받아 8진수(octal)로 출력해보자.

# 예시
# a = input()
# n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
# print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

# 참고
# 8진법은 한 자리에 8개(0 1 2 3 4 5 6 7)의 문자를 사용한다.
# 8진수 10은 10진수의 8, 11은 9, 12는 10 ... 와 같다.
a = input()
b = int(a, 16)
print('%o' % b)

#6030
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.

# 예시
# n = ord(input())
# print(n)

# 참고
# n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.

# ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.  
# 실제로 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여 되어 있다. A:65, B:66, C:67 .... 
# ord(c) : 문자 c 를 10진수로 변환한 값 

# 컴퓨터로 저장되고 처리되는 모든 데이터들은 2진수 형태로 정수화 되어야 하는데,
# 컴퓨터에 문자를 저장하는 방법으로 아스키코드(ASCII Code)나 유니코드(Unicode)가 자주 사용된다.

# 예를 들어, 영문 대문자 'A'는 10진수 값 65 로 표현하고, 
# 2진수(binary digit) 값 1000001 로 바꾸어 컴퓨터 내부에 저장한다. 

# 유니코드(unicode)는 세계 여러 나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준 코드이다.
n = ord(input())
print(n)

#6031
# 10진 정수 1개를 입력받아
# 유니코드 문자로 출력해보자.


# 예시
# c = int(input())
# print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 


# 참고
# 입력은 기본적으로 모두 문자열로 입력되는 것이라고 할 수 있다. 
# 따라서, 입력 값이 문자/문자열/정수/실수인지에 따라서 먼저 정확하게 변환시킨 다음에 사용하거나 계산하는 것이 좋다.

# 예를 들어 123 이 입력 되었다고 한다면, 이건 정수일까? 문자열일까?
# 조금 생각해보면, 입력된 것만 보고는 그 값이 어떤 데이터인지 알 수 없다는 것을 쉽게 이해할 수 있다.
# 따라서, 그 입력 값을 어떻게 해석하고 변환할 지에 대해서 명확하게 작성해 주어야 하는 것이다. 

# chr( )는 정수값->문자, ord( )는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능을 한다.
a = int(input())
print(chr(a))

#6042
# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.


# 예시

# a=input()
# a=float(a)
# print( format(a, ".2f") )


# 참고
# format(수, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다. 

# 여기서 만들어진 값은 소수점 아래 3번째 자리에서 반올림한 값이다.

# 컴퓨터 프로그래밍에서 실수 변환이나 실수를 사용하는 계산은
# 정확하게 변환되거나 계산되는 것이 아니라, 거의 모두 근사값으로 계산되는 것이라고 할 수 있다. 

# 실수가 컴퓨터로 저장되기 위해서는 디지털방식으로 2진 정수화되어 저장되어야 하는데,
# 그 과정에서 아주 작은 부분이 저장되지 않고 사라지는 잘림(truncation) 오차가 자주 발생하기 때문이다.
a = float(input())
print(format(a, ".2f"))