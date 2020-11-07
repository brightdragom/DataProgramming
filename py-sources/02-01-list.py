#만든 날짜 : 2020.11.03
#제목 : list[] type : 대괄호
#만든이 : 김광용
#list[] type : 대괄호

lst = [1, 2, 3, 'a', 'b', 'c']
lst11 = ['jj', 'gg', 1, 2, 3, 'a','b','c']

print(lst)
print(lst11)
print("\n")

lst2 = [5,6,7,'t','n','k']
lst3 = [30, 60, 50,"국어", "영어", "수학"]

print(lst2)
print(lst3)
print("\n")

lst.append(4) #추가
print(lst)
lst.insert(2, 100) #중간 삽입
print(lst)
lst.remove(100) #원하는 값 찾아 삭제
print(lst)
del lst[3]
print(lst)