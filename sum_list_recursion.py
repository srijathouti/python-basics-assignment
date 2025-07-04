sum=0
def su(li):
    if not li:
        return 0
    else:
        return li[0]+su(li[1:])   
li=[1,2,3,4,5]
print(su(li))

