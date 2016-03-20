import re
fin=open("prom_in.py")
fout=open("prom_out.py",'w')
t=fin.readline()
t=int(t)
flag,k=0,0
b_height=[]
while(flag!=t):
    m=fin.readline()
    m=re.findall(r'\d+',m)
    n_boy=m[0]
    n_boy=int(n_boy)
    b_height=fin.readline()
    b_height=re.findall(r'\d+',b_height)
    b_height=list(b_height)
    b_height.sort()
    g_height=fin.readline()
    g_height=re.findall(r'\d+',g_height)
    g_height=list(g_height)
    g_height.sort()
    for  i  in range (0,n_boy):
        if(g_height[i]>=b_height[i]):
            k=k+1
    flag=flag+1 
    if(k==0):
        fout.write("yes\n")
    else:
        fout.write("no\n")      
    
