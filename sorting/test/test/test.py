# def rotLeft(a, d):
#     final_list = []
#     count = 1
#     while count <= a:
#         final_list.append ( count )
#         count += 1
#     final_list.rotate ( d )
#     return final_list


def rotate_org(l, y):
    if len(l) == 0:
        print("lolo")
        return l
    print("bakalim")
    print(l)
    y = -y % len(l)
    return l[y:]+ l[:y]

# print("ilk")
# print(rotate_org([1,2,3,4,5],2))


def rotate1(a, d):
    final_list = []
    count = 1
    while count <= a:
        final_list.append ( count )
        count += 1
    l = final_list
    if len ( l ) == 0:
        return l
    d = -d % len ( l )
    return l[d:] + l[:d]

print("ikinci")
print(rotate1(5,4))

def rotate2(a, d):
    # sola kaydirma kodu
    final_list = []
    count = 1
    while count <= a:
        final_list.append ( count )
        count += 1
    l = final_list
    if len ( l ) == 0:
        return l
    print(d)
    d = d % len ( l )
    return l[d:] + l[:d]

print("uc")
print(rotate2(5,4))

print(-11 % len ( [1,2,3,4,5] ))

