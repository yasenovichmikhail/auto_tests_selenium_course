word = 'Hello'
numbers = [1, 14, 5, 9, 12]
words = ['one', 'two', 'three', 'four', 'five', 'six']



# Списочное выражение	                        Результирующий список
# [0 for i in range(10)]	                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [i ** 2 for i in range(1, 8)]	                [1, 4, 9, 16, 25, 36, 49]
# [i * 10 for i in numbers]	                    [10, 140, 50, 90, 120]
# [c * 2 for c in word]	                        ['HH', 'ee', 'll', 'll', 'oo']
# [m[0] for m in words]	                        ['o', 't', 't', 'f', 'f', 's']
# [i for i in numbers if i < 10]	            [1, 5, 9]
# [m[0] for m in words if len(m) == 3]	        ['o', 't', 's']
# if / else
# [i if i > 5 else 100 for i in range(10)]      [100, 100, 100, 100, 100, 100, 6, 7, 8, 9]
# [i if i > 5 else i * 2 for i in range(10)]    [0, 2, 4, 6, 8, 10, 6, 7, 8, 9]