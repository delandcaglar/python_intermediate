def print_name(name):
    print(name)
print_name('Alex')

def foo(a,b,c,d=7):
    print(a,b,c, d)
# Default arguments mut be at the end of the function.
foo(a=1,b=2,c=3)



def foo_v1(a,b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

# If you mark your parameter with one star any number of positional arguments.
# If you mark your parameter with two starts any number of key word arguments are allowed.


foo_v1(1,2,3,4,5, six=6, seven=7)


def foo_v1_1(a, b, *, c, d):
    print ( a, b, c,d )


foo_v1_1 ( 1, 2, c=3, d=4)



def foo_v1_2(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo_v1_2 ( 1, 2, 3, last=100)



def foo_v1_3(a,b,c):
    print(a,b,c)

my_list = [0,1,2]
# If the lenght of the list is matching with the argument numbers, it works.
print("bakalim")
foo_v1_3(0,1,2)
foo_v1_3(*my_list)
my_dict={'a':1,'b':2,'c':3}
# Keys and lenght must match the number of parameters for dictionaries.
foo_v1_3(**my_dict)


def foo_v1_4():
    global number
    x = number
    number = 3
    print(f'number inside function: {x}')

number = 0

foo_v1_4()
print(number)

def foo_v1_5(a_list):
    a_list += [222,313,434]
    #a_list = a_list + [222, 313, 434]
    # second method does not change global my_list


my_list = [1,2,3]
foo_v1_5(my_list)
print(my_list)











