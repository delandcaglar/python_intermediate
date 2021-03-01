from itertools import groupby



# src = inspect.getsource(groupby)

n = 7
c = [1,2,1,2,1,3,2,5]

def claculate_doubles(ar):
    end_pairs = 0
    final_end_pair = 0
    for key, group in groupby( sorted( ar ) ):
        sayi = 0
        for element in (ar):
            if element == key:
                sayi += 1

        print("kopya cikti")
        print ( sayi )
        if sayi ==1:
            print("pair yok ")
            end_pairs = 0
        else:
            if sayi % 2 == 0:
                end_pairs = sayi /2
            else:
                end_pairs = (sayi - 1) /2
        print(f"su anki deger {final_end_pair} ,{end_pairs}")
        final_end_pair = final_end_pair + end_pairs
    return final_end_pair

    # print (group)
    # print (len(list(group)))

print(claculate_doubles(c))


# ans = 0
# for val in [len(list(group)) for key, group in groupby(sorted(c))]:
#     ans = ans + val/2
# print (ans)
#
# ar = [1,2,1,2,1,3,2]