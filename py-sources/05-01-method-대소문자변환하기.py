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
print(x.upper(), ' - x upper()')
print(X.lower(), ' - x lower()')
print(y.upper(), ' - y upper()')
print(Y.lower(), ' - y lower()')
print(z.swapcase(), ' - z swapcase()')
print(z.title(), ' - z title()')
print(z.capitalize(), ' - z capitalize()')