import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

def print_name():
    print('Alex')

@start_end_decorator
def add5(x):
    return x+ 5

# print_name = start_end_decorator(print_name)

print(help(add5))
print(add5.__name__)

#
# result = add5(10)
# print(result)
#
# print_name()



# Second example
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator_repeat

def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signiture = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signiture})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


print("__________________")
@debug
#@repeat(num_times=3)
@start_end_decorator
def greet(name):
    greeting = (f'Hello {name}')
    print(greeting)
    return greeting
    
greet('Alex')


class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args , **kwargs):
        print("Hi there")
        self.num_calls +=1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('hello')

say_hello()
say_hello()
say_hello()

# debug, timer, check, register plug ins, cash the returns values, or update the state