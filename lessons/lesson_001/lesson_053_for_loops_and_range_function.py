
#sum all numbers from 1 to max_num
max_num = 5
numbers_start_to_end = range(1,max_num+1)
numbers_end_to_start = range(max_num, 0, -1)
for number in numbers_end_to_start:
    print(number)