#6046
# 정수 1개를 입력받아 2배 곱해 출력해보자.

# 참고
# *2 를 계산한 값을 출력해도 되지만,
# 정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.
# 컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
# 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
# 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
# 가장 오른쪽에 있는 1비트는 사라진다.

# 예시
# n = 10
# print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
# print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
# print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
# print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# 정수 10의 2진수 표현은 ... 1010 이다.
# 10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.
# 10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.

# n = 10 과 같이 키보드로 입력받지 않고 직접 작성해 넣은 코드에서, 숫자로 시작하는 단어(식별자, identifier)는 자동으로 수로 인식된다.  

# n = 10 에서 10 은 10진수 정수 값으로 인식된다.
# 변수 n 에 문자열을 저장하고 싶다면, n = "10" 또는 n = '10'으로 작성해 넣으면 되고,

# n = 10.0 으로 작성해 넣으면 자동으로 실수 값으로 저장된다.
# n = 0o10 으로 작성해 넣으면 8진수(octal) 10으로 인식되어 10진수 8값이 저장되고,
# n = 0xf 나 n = 0XF 으로 작성해 넣으면 16진수(hexadecimal) F로 인식되어 10진수 15값으로 저장된다.

# ** python에서 실수 값에 대한 비트시프트 연산은 허용되지 않고 오류가 발생한다.
# (실수 값도 컴퓨터 내부적으로는 2진수 형태로 저장되고 비트시프트 처리가 될 수 있지만, python 에서는 허용하지 않는다.)
a = int(input())
print(a<<1)

#6047
# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10

# 예시
# a = 2
# b = 10
# print(a << b)  #210 = 1024 가 출력된다.

# 참고
# 예를 들어 1 3 이 입력되면 1을 23(8)배 하여 출력한다.
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)

#6048
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

# 예시
# print(123<456)  #비교 연산자 < 의 계산 결과인 True(참)가 출력된다.
# (123, 456 은 숫자로 작성된 단어이기 때문에 10진수로 인식된다.)

# 참고
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

# 비교/관계연산자 < (less than sign) 는
# 왼쪽의 값이 오른쪽 값 보다 작은 경우 True(참)로 계산하고,
# 그 외의 경우에는 False(거짓)로 계산한다.

# 비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
# 그 결과를 True(참), 또는 False(거짓)로 계산해 주는 연산자이다.

# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.

# True(참) 또는 False(거짓) 값으로만 표현하고 저장하는 값을 불(bool)/불리언(boolean) 값이라고 한다.
# 정수, 실수, 문자, 문자열과 마찬가지로 또 다른 형태의 데이터형(data type)이다.
a, b = input().split()
a = int(a)
b = int(b)
print(a < b)

#6049
# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

# 참고
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

# 비교/관계연산자 == (equal sign 2개) 는
# 왼쪽의 계산 결과값과 오른쪽의 계산 결과값이 같은 경우 True(참)로 계산하고,
# 그 외의 경우에는 False(거짓)로 계산한다.

# 비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
# 그 결과를 True(참), 또는 False(거짓)로 계산해 주는 연산자이다.

# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.

# ** 수학에서 왼쪽과 오른쪽의 계산 결과가 같음(동치)을 나타내는 기호 =(equal sign) 1개는
# 프로그래밍언어에서는 전혀 다른 의미로 사용된다.

# a = 1 와 같은 표현은 a와 1의 값이 같다는 의미가 아니라
# 오른쪽의 계산 결과값인 1을 왼쪽의 변수 a에 저장하라는 의미이다.
a, b = input().split()
a = int(a)
b = int(b)
print(a == b)

#6050
# 두 정수(a, b)를 입력받아
# b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

# 참고
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

# 비교/관계연산자 <= 는
# 오른쪽의 계산 결과값이 왼쪽의 계산 결과값보다 크거나 같은 경우 True(참)로 계산하고,
# 그 외의 경우에는 False(거짓)로 계산한다.

# <=, >= 연산자는 같음(==)을 포함한다. 따라서 “작다/크다” 거나 "같다”는 의미를 가진다.
# 작다(<)/크다(>)/다르다(!) 기호는 등호(=)와 함께 왼쪽에 붙여써야 한다.

# 비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
# 그 결과를 True(참), 또는 False(거짓)로 계산해주는 연산자이다.
# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.
a, b = input().split()
a = int(a)
b = int(b)
print(a <= b)

#6051
# 두 정수(a, b)를 입력받아
# a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.

# 참고
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

# 비교/관계연산자 != 는
# 왼쪽의 계산 결과값이 오른쪽의 계산 결과값이 서로 다른 경우 True(참)로 계산하고,
# 그 외의 경우에는 False(거짓)로 계산한다.

# 비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
# 그 결과를 True(참), 또는 False(거짓)로 계산해주는 연산자이다.
# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.
a, b = input().split()
a = int(a)
b = int(b)
print(a != b)