days,window_size = raw_input().split()
days = int(days)
window_size = int(window_size)
upvote_count = raw_input()
input_array = map(int, upvote_count.split())
#x and y are used to maintain the indices for the list
x,y = 0,len(input_array)-window_size

#loop till the subranges based on window_size is matched
while(x != y + 1):
    temp = x
    nonincreasing_subrange,nondecreasing_subrange = 0,0
    
    # loop to find all the upvotes in the given subrange
    while(temp != x + window_size - 1):
    
        # loop to find all the non-decreasing upvotes in the given subrange
        for i in range(temp,x + window_size):
            if(i == x + window_size - 1):
                break;
            else:
                if(input_array[i] <= input_array[i+1]):
                    nondecreasing_subrange = nondecreasing_subrange + 1
                else:
                    break
         # loop to find all the non-increasing upvotes in the given subrange       
        for i in range(temp,x + window_size):
            if(i == x + window_size - 1):
                break;
            else:
                if(input_array[i] >= input_array[i+1]):
                    nonincreasing_subrange = nonincreasing_subrange + 1
                else:
                    break
        
        temp = temp + 1
    print nondecreasing_subrange-nonincreasing_subrange
        
    x = x + 1
    
            
