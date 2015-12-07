#Kollin Schalhamer
#Dr. Neumann
#CIS-125
#4 DEcember 2015
#EuclidGCD.py

def gCd(x, y):
    print("X=",x,"Y=",y)
    if y==0:
        return x
    else:
        return gCd(y,x%y)


def main():
    x=252
    y=105
    print("GCD of",x,",",y,"=",gCd(x,y))
    
    
if __name__=="__main__":
    main()
    