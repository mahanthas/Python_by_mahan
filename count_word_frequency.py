list1 = ['one','two','one','three','four','three','five','two','five']
list2 = set(list1)
list3 = list(list2)
print(list3)

def count_word():
    mydict = dict()
    count = [0] * len(list3)
    for i in range(len(list3)):
        for j in range(len(list1)):
            if list1[j] == list3[i]:
                count[i] += 1
        mydict[list3[i]] = count[i]
    print(mydict)

count_word()
