# 문자 정렬 메소드
# .center()
# .ljust()
# .rjust()

k = 'python'

print(k)
k1 = k.center(20)
k2 = k.ljust(20)
k3 = k.rjust(20)

# 공백 * 채우기
k22 = k.center(20, '*')
k33 = k.ljust(20, '*')
k44 = k.rjust(20, '*')

print(k1," _ k.center(20)")
print(k2," _ k.ljust(20)")
print(k3," _ k.rjust(20)")
print(k22," _ k.center(20, '*')")
print(k33," _ k.ljust(20, '*')")
print(k44," _ k.rjust(20, '*')")