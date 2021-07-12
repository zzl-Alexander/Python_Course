# coding=utf-8
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值:", mylist)
    return

mylist = [10, 20]
changeme(mylist)
print("函数外取值:", mylist)
