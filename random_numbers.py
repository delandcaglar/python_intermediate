import  random
import secrets

a = random.uniform(1,10)
print(a)
a = random.normalvariate(0,1)
print(a)
mylist = list("ABCDEFG")
print(mylist)
a = random.sample(mylist,3)
print(a)
# her birinden sadece bir tane olmak uzere 3 tanesi

# secrets module true random number verir

a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)

mylist= list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

import numpy as np

a = np.random.rand(3)
print(a)

a = np.random.randint(0,10,(3,4))
print(a)

arr= np.array([[2, 7, 3],
 [2, 9, 1],
 [0, 2, 8]],
)
print(arr)
print("newww")
np.random.shuffle(arr)
print(arr)





