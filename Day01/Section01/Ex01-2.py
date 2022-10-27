'''
Ex01-2.py
'''
'''
%d, %s, %c를 활용하여 print문으로 데이터를 출력하는 방법
%d : 숫자 데이터
%s : 문자열 데이터
%c : 문자 하나 데이터
'''
print("올해는 %d년 입니다." % 2022)
print("올해는 %d년, 내년은 %d년 입니다." % (2022, 2023))
print("나는 %s 을 공부 합니다." % 'Python')
print("나는 %s과 %s를 공부 합니다." % ('Python', 'Java'))
print("Python 은 %c로 시작 합니다." % 'P')
print("Python 은 %c로 시작 하고, %c로 끝 납니다." % ('P', 'n'))

'''
{} 를 활용하여 데이터의 종류에 상관 없이 print 문으로 표형이 가능.
'''
print("올해는 {}년 입니다.".format(2022))
print("올해는 {}년, 내년은 {}년 입니다.".format(2022, 2023))
print("나는 {}을 공부 합니다.".format('파이썬'))
print("나는 {}과 {}를 탑니다.".format('지하철', '버스'))