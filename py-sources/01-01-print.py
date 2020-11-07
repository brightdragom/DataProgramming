#만든 날짜 : 2020.11.03
#제목 : print() 함수
#만든이 : 김광용
#print() 함수 : 출력

my_string = "DSAC Module1 DATA Programming - 선문대학교"
message = "Hi ! Have great day"

line = " = " * 5
price = 20000

print("1. 문자열 연습입니다.")  #""
print("=================")

print('2. 문자열 연습입니다.')   # ''
print("=================")

print('''3. 문자열
연습
입니다''') #''' '''
print('''4. "문자열"
연습
입니다''')# '''   "" '''
print("""3. 문자열
연습
입니다""") #""

print("\n")
print("\n")
print("\n")

print(my_string)
print("\n")

print("Hello ? my name is ","python", "and 20"+"years")
print("안녕하세요? 제 이름은" + "파이썬이고", 20 ,"세입니다.")
print("\n")

print("안녕하세요? 제 이름은\n", "\"파이썬\" 입니다.", "c:\\aaa\\bbb\\")
print("\n")

print(line)
print("\n")
print(my_string, "\n")
print("===============")
print(message * 3,"\n")

print("상품의 가격은 %s원 입니다" %price) # , 구문자 없음
