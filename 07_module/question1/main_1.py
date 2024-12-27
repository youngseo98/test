import team_module 

print(f'안녕하세요, {team_module.company}입니다.')

print(team_module.introduce())
print(team_module.introduce_developer())

import attendance_module

print(attendance_module.record_attendance('다람쥐','9:00'))
print(attendance_module.record_leave('다람쥐', '18:00'))

from task_module import start_task, complete_task

print(start_task('코드 리뷰'))
print(complete_task('코드 리뷰'))

import statistics

A = [10, 12, 8, 15, 9]

print(statistics.mean(A)) 

count = 0
for x in A:
    if x > statistics.mean(A):
        count += 1




print(f'평균 업무량보다 많이 처리한 날 : {count}')

import numpy

list = [1, 5, 6, 15, 61, 54, 14]

print(numpy.mean(list))








