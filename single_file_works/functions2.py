# countdown
def countdown(num):
    for i in range(num, 0-1, -1):
        print(i)
countdown(5)

# print and return
def prnret(a,b):
    print(a)
    return b
prnret(1,3)

# first plus length
def firaddlen(list):
    sum=list[0]+len(list)
    print(sum)
    return sum
firaddlen([1,2,3])
blist=[1,2,3,4,5]
firaddlen(blist)

# values greater than second
def newList(list):
    if(len(list)<2):
        return False
    newArr = [item for item in list if item > list[1]]
    print(newArr)

newList([3])
newList([5,2,3,2,1,4])

# this length, that value
list=[]
def thisnthat(s,v):
    for i in range(s):
        list.append(v)
    return list
print(thisnthat(4,7))
