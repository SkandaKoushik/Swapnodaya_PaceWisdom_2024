import random, time

from naive_search import naive_search
from binary_search import binary_search


length = 10000

sorted_list = set()
for _ in range(length):
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))


start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
end = time.time()
print('\nNaive Search Time: ', (end - start), 'seconds')


start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print('Binary Search Time: ', (end - start), 'seconds \n')



