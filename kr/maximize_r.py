import re



fin=open("input.txt")
fout=open("output.txt",'w')


test_case=fin.readline()
test_case=int(test_case)
for i in range(0,test_case):
    i,j=0,0
    flag1=0
    c=0
    kid=[]
    flag=1
    data=fin.readline()
    data=data[:-1]
    data=list(data)
    n=len(data)
    
    for x in range(0,n):
        if(data[x]=='K'):
            
            kid.append(x)
    
    m=len(kid)
    for y in range(0,m-1):
        
        temp=(kid[y+1]-kid[y])-1
        #print temp
        if(temp>=2):
            #do nothongs
            flag1=1
        else:
            if(flag==1):
            
                i=kid[y]
                j=kid[y+1]
                flag=2
            else:
                if(j==kid[y]):
                    j=kid[y+1]
                else:
                    i=kid[y]
                    j=kid[y+1]
    if(flag1==1 and(i==0 and j==0)):
        for y in range (0,n):
            if(data[y]=='K'):
                data[y]='R'
                break;
    else:        
        for t in range(i,j+1):
            if(data[t]=='K'):
                data[t]='R'
            else:
                data[t]='k'
    
    for t in range(0,n):
        if(data[t]=='R'):
            c=c+1
           
    
    fout.write("%d \n" % c)
     
            
            
        
                
              
