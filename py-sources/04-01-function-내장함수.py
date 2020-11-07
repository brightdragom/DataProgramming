# 내장함수
# len()     : 문자의 길이
# max()     : ASCII코드값이 가장 큰 문자 -> 소문자 > 대문자
# min()     : ASCII코드값이 가장 작은 문자
# sum()     : 문자열에는 적용 x
# sorted()  : 문자열의 ASCII코드값으로 정렬하여 리스트로 결과 반환
# reversed(): 문자열을 역순으로 정렬, 반드시 리스트 함수 적용

x = 'python'
y = 'computer'
z = 'acbfhged'

x2 = [2, 6, 9, 3, 7]

print(x)
print(y)

print('=== len ====')

print(x)
xx = len(x)
print(xx)
print('=' * 10)
print(x2)
xx = len(x2)
print(xx)

print('=== max ====')

print(x)
print(max(x))
print('=' * 10)
print(x2)
print(max(x2))

print('=== min ====')

print(x)
print(min(x))
print('=' * 10)
print(x2)
print(min(x2))

print('=== sorted ====')

print(z)
print(sorted(z))
print('=' * 10)
print(x2)
print(sorted(x2))
print(sorted(x2, reverse = True))