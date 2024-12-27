
####################################################

# 1. import 구문 사용

# our_class.py 모듈을 가져와서
# 선생님 이름과 학생수를 출력하고
# study() 함수와 lecture() 함수를 호출하고
# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해보자


####################################################

# import our_class

# print(our_class.teacher_name, our_class.student_count)
# print(our_class.student_count)
# our_class.study()
# our_class.lecture()

# menus = ['돈까스', '제육볶음', '제육덮밥', '짜장면', '피자']

# print(our_class.go_lunch(menus))
################################################################################
# 2.from- import 구문 사용

# from our_class import teacher_name, student_count, study, lecture

# print(teacher_name, student_count)
# study()
# lecture()


# menus = ['돈까스', '제육볶음', '제육덮밥', '짜장면', '처음처럼']

# from our_class import go_lunch

# print(go_lunch(menus))


# from our_class import teacher_name, student_count, study, lecture, go_lunch

# print(teacher_name, student_count)
# study()
# lecture()
# print(go_lunch(menus))

###############################################################################

# 3. 패키지 내의 모듈 import

import our_class_dir.official.official_module
from our_class_dir.unofficial.unofficial_module import study, go_lunch
# 선생님 이름과 학생 수를 출력하고

print(our_class_dir.official.official_module.teacher_name)
print(our_class_dir.official.official_module.student_count)


# study() 함수와 lecture() 함수를 호출하고 
study()
our_class_dir.official.official_module.lecture()

# 먹고싶은 메뉴명이 5개 담긴 menus 배열을 만들어서

menus = ['돈까스', '제육볶음', '제육덮밥', '짜장면', '처음처럼']

print(go_lunch(menus))


