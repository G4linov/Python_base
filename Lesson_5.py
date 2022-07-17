import sys

gen_odd_num = (num for num in range(0, 50, 2))
list_odd_num =[]
for i in range(0,50,2):
    list_odd_num.append(i)

print(gen_odd_num, type(gen_odd_num), sys.getsizeof(gen_odd_num))
print(list_odd_num, type(list_odd_num), sys.getsizeof(list_odd_num))

print(list_odd_num[10])

for _ in range(11):
    x = next(gen_odd_num)

print(x)
#for el in gen_odd_num:
#    print(el**2)

#for el in list_odd_num:
#    print(el**2)
