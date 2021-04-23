def mod(MyList=[],*args):
    MyList1=[]
    [MyList1.append(i.lower() if type(i)==str else i) for i in MyList]
    my_dict={i:MyList1.count(i) for i in MyList1}
    for i in my_dict.values():
        if i % 2 == 0:
            a="true"
            break
        else:
            a="false"
    return  a
print (mod([3, 2, "two", "apple", "Apple","apple"]))