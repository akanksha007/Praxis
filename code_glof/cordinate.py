def ycoordinate(N,S):
    k=0
    for t in range(0,N):
        k=k+S[t][1];
        k=k/N;

    for i in range(0,9):
        first_derivative=second_derivative=third_derivative=0;
        for t in range(0,N):
            
            x=S[t][0]
            y=S[t][1]
            a=y-k
            c=k*k-2*k*y+x*x+y*y
            first_derivative+=-a/((x*x+a*a)**0.5)
            second_derivative+=x*x/pow(c,1.5)
            third_derivative+=3*x*x*a/pow(c,2.5)
        
        a=third_derivative/2
        b=second_derivative-third_derivative*k;    #a,b,c are constant
        c=first_derivative-second_derivative*k+a*k*k
        k=(-b+((b*b-4*a*c)**0.5))/third_derivative
    
    return k;

input_array=[]
line = raw_input("Enter the no. of houses")
n_house=int(line)
print "Enter the x and y cordinate for each house in a new line"
for i in range(0,n_house):
    input_array.append([])
for i in range(0,n_house):
    user_input=raw_input()
    input_array[i]=map(float,user_input.split())
print "The ycordinate where you should place your restaurant is:",ycoordinate(n_house,input_array) 
