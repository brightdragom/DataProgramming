# .capitalize() 메소드 : 문자열에만 적용가능, 첫문자만 대문자로
# .title()  : 단어마다 첫글자 대문자
# .upper()  : 모두 대문자
# .lower()  : 모두 소문자
# .swapcase()   : 대소문자 변경

x = 'hello world'
X = 'HELLO WORD'
y = 'how are you?'
Y = 'HOW ARE YOU?'
z = 'I Am Happy.'

print(x)
print(X)
print(y)
print(Y)
print(z)
print('===============')
print(x.upper())
print(X.lower())
print(y.upper())
print(Y.lower())
print(z.swapcase())
print(z.title())
print(z.capitalize())