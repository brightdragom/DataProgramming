# if문
# 조건문 mun % x -> #mun이 x로 나눠지지 않으면 참

x = 7

if x % 2 != 0:
    print("참")
else:
    print('거짓')
print('=' * 20)
print("\n")

if x % 2 == 0:
    print("참")
else:
    print('거짓')
print('=' * 20)
print("\n")

num = 5

if num % 2:
    print('True')   #python에서 True = 1을 의미, Fales는 0을 의미
else :
    print("False")


print("-----")
print('홀수' if num % 2 != 0 else '짝수')