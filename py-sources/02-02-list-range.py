# range( )
# range ( start, stop, [step] ) _ start 생략가능(0번) 인덱스번호,
# step-1까지 : 종료 인덱스번호의 자료 , step : 기본 1(증가), -1(감소)

lst = list(range(5))
lst2 = list(range(0,5))
lst3 = list(range(1,5))
lst33 = list(range(-5, 5))

print(lst)
print(lst2)
print(lst3)
print(lst33)
print('=' * 20)

lst4 = list(range(1,6))
lst5 = list(range(3,6))
lst6 = list(range(0,10,2))
lst7 = list(range(1,10,2))
lst8 = list(range(0,10,3))
lst88 = list(range(-5,10,3))

print(lst4)
print(lst5)
print(lst6)
print(lst7)
print(lst8)
print(lst88)