score1 = int(input("Enter your Korean grade : "))
score2 = int(input("Enter your English grade : "))
score3 = int(input("Enter your Math grade : "))

total_score = score1 + score2 + score3
avg = total_score / 3
if avg >= 90:
    result = 'A'
elif avg >= 80:
    result = 'B'
elif avg >= 70:
    result = 'C'
elif avg >= 60:
    result = 'D'
else :
    result = 'F'
print('당신의 총점은 ',total_score,'이고 평균 점수는 ',avg,'이며, 학점은 ',result,'입니다. \n내년에 다시만나요 ^^')