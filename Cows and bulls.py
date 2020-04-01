import random
import string
def bullcow(userin,randin):
    bull=0
    cow=0
    for x in randin:
        for y in userin:
            f2=randin.find(y)
            f3=userin.index(y)
            #print(f2)
            #print(f3)
            if(f2>-1 and f3>-1):
                if(f2==f3):cow+=1
                if(f2!=f3):bull+=1

            #print(f2)
            #print(f3)
            #if(x==y):
                #cow+=1
            #f1=userin.find(x)
            ##print(f1)
            #if(f1>=1):
                #bull+=1
    #print(cow)
    #print(bull)
    return bull,cow

if __name__=="__main__":
    n=4
    num=''.join(random.choice(string.digits)for i in range(n))
    print(num)
    while(True):
        num2=input('Enter four digit number')
        bull,cow =bullcow(num2,num)
        print(cow/4)
        print(bull/4)
        if (cow/4==4):break