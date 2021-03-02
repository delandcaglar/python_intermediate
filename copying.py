import copy


org = [0,1,2,3,4]
cpy = org
cpy[0]= -10
print(cpy)
print(org)
print("_________")

org = [0,1,2,3,4]
cpy = copy.copy(org)
# If there is one level it is allright however if there is 2 level depth then the one at the below i snecessary
cpy[0]= -10
print(cpy)
print(org)
print("_________")


org = [[0,1,2,3,4],[0,16,25,33,2]]
cpy = copy.deepcopy(org)
cpy[0][1]= -10
print(cpy)
print(org)
print("_________")

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age = age

class Company:
    def __init__(self,boss,employee):
        self.boss = boss
        self.employee = employee



p1 = Person('Alex',27)
p2 = Person('Joe',88)

company = Company(p1,p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)


