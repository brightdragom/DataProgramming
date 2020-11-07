#dict { } type : 중괄호 - dictionary
#Key : Value

dt = {'교수':'반기철','지역':'전주','기간':5}
dt1 = {'학교':'한국대',"교육내용" : "DSACM1", "종목":"python"}
dt2 = {'grade':4, '결과' : 'Good' , "Phone" : "010-****-****"}

print("\n")
print(dt)
print(dt1)
print(dt2)
print("\n")

print('학   교 : ', dt1['학교'])
print('교육내용 : ', dt1['교육내용'])
print('종   목 : ', dt1['종목'])
print('학   년 : ', dt2['grade'])
print('결   과 : ', dt2['결과'])
print('휴대전화 : ', dt2['Phone'])
