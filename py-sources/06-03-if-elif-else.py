# if elif else

age = int(input("please input your age! : "))

if age >= 65 or age < 8:
    price = 0
elif age >= 20:
    price = 500
else :
    price = 300
print(age , ' ', price)