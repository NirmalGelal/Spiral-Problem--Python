def find(a,b):

    if(s>=a and s>=b):
        if(a>b):
            n=a
        else:
            n=b

        if(a==1 and b==1):
            return 1
        if n%2==0:
            count=n**2
            i,j=n,1
            while count!=1:
                if i>j:
                    if(a==i and b==j):
                        return count
                    count=count-1
                    j=j+1
                else:
                    if(a==i and b==j):
                        return count
                    count=count-1
                    i=i-1
        else:
            i,j=1,n
            count=n**2
            while count!=1:
                if i<j:
                    if a==i and b==j:
                        return count
                    count=count-1
                    i=i+1
                else:
                    if a==i and b==j:
                        return count
                    count=count-1
                    j=j-1
    else:
        print("Out of the box")

s = int(input("Enter table size: "))
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(find(x,y))


