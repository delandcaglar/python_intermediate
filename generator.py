import sys

# Generator


def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

print(sum(g))
print(sorted(g))

def countdown(num):
    print('starting')
    while num>0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

value = next(cd)
print(value)


def firstn(n):
    nums = []
    num = 0
    while num<n:
        nums.append(num)
        num+=1
    return nums


print(firstn(10))


def firstn_generator(n):
    num = 0
    while num<n:
        yield (num)
        num+=1

print("haha")
print(sum(firstn_generator(10)))
elma =(firstn_generator(10))


print(next(elma))
print(next(elma))
print(next(elma))
print(next(elma))

print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(100000)))

def fibonacci(limit):
    a,b, = 0,1
    while a<limit:
        yield a
        a, b = b , a+b

fib = fibonacci(30)

for i in fib:
    print(i)


mygenerator = (i for i in range(10) if i % 2 == 0)
print(list(mygenerator))
# for i in mygenerator:
#     print(i)
    
mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)
















