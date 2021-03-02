numbers= [1,2,3,4,5,6]

*begining, last = numbers
print(begining)
print(last)


begining, *last = numbers
print(begining)
print(last)



begining, *middle,secondlast,last = numbers
print(begining)
print(middle)
print(secondlast)
print(last)


my_tuple= (1,2,3)
myset= (4,5,6)

new_list = [*my_tuple, *myset]
print(new_list)

dict_a = {'a':1,'b':2}
dict_b = {'c':3,'d':4}
my_dict = {**dict_a, **dict_b}
print(my_dict)


