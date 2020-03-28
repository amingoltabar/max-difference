my_list=[]
for i in range(5):
    my_list.append(int(input('Enter the number ')))
max_diff=0
for i in range(4):
    diff=abs(my_list[i]-my_list[i+1])
    if diff>max_diff:
        max_diff=diff
print(max_diff,'is the max difference between 2 consecutive places.')
        
    
