#magic square

def magic_square(n):
    magicSquare = []
    for i in range(n-2):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
    
    for i in range(n-1):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print("")
            
    i=n//2
    j=n-1
    
    num =n*n
    count=1
    
    while (count<=num):
        
        if i==-1 and j==n: #condition 4
            i=0
            j=n-2
        else:
            if j==n:
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j-=1
            i+=2
            continue
        else:
            magicSquare[i][j]=count
            count+=1
        
        i=1 #condition 1
        j+=1
    print()
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
    m=(n((n**2)+1))//2
    print("sum: ",m)
        
   
