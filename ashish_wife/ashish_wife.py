"""
Little Ashish had no interest in studying ever in his life. So, he always wanted to marry as soon as possible, and kept forcing his parents to get him married. He thought his married life was going to be fun. But, well, surprise, surprise... it's not - not for him, at least.

Fulfilling the demands of his wife is a huge problem for him. She wants costumes, a lot of them - and it's getting impossible for Ashish to buy her all the clothes she asks for. Fortunately, for Ashish, he knows that out of n dresses, his wife only needs x different type of dresses. Now Ashish doesn't want to spend and waste a lot of time on this whole thing - so the only strategy he's decided to follow is to not follow any strategy - that is to say, he gets all the n dresses, and gifts them to his wife for her to figure out how many different dresses has he managed to bring.

Given the number of dresses, n, number of dresses he has to select, x - find out what his wife feels for him.

Input format:
In the first line, tc will denote the number of test cases. The next line will contain the number of total dresses, and the number of dresses he has to select for his wife. After which, there will be n integers, denoting the price of each dress.

Output format:
If the wife had asked for x dresses, and she got EXACTLY x dresses, print "Perfect husband", if it's more than what she had asked for, print "Lame husband", if it's less than what she had demanded for, print "Bad husband."

Constraints:
1 <= Test cases <= 50
1 <= N <= 13000
1 <= X <= 13000
1 <= Price <= 109 
"""
import re
fin=open("input.txt")
fout=open("output.txt",'w')
test_case=fin.readline()
test_case=int(test_case)

for i in range (0,test_case):
    data=fin.readline()
    data=re.findall(r'\d+',data)
    data=list(data)
    total_dress=int(data[0])
    demand=int(data[1])
    if(demand!=total_dress):
        y=fin.readline()
        fout.write("lame husband \n")
    else:
        y=fin.readline()
        fout.write("Perfect husband \n")
        
    
