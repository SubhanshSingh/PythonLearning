# Going to write a simple pattern display program 

'''
1
1 2
1 2 3
'''

# # Displaying a simple pattern using nested loops  with another approach 
# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()  # Move to the next line after each row

# writing similar program in a different way
for i in range(1, 4):
    print(' '.join(str(j) for j in range(1, i + 1)))  # Join numbers with space and print

#  now i want to display the same pattern in different order also explain the steps what i am doing here        
'''
1 2 3
1 2
1
'''
for i in range(3, 0, -1):  # Start from 3 down to 1
    print(' '.join(str(j) for j in range(1, i + 1)))  # Join numbers with space and print now    


# want to display it with different approach
for i in range(3, 0, -1):  # Start from 3 down to 1
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Move to the next line after each row

'''

* * * * *
* * * *
* * *
* *
*    

'''    
# Displaying a pattern with stars in descending order
for i in range(1, 6):  # Start from 5 down to 1
    print('* ' * (6 - i))  # Print stars with space, multiplying by the current row

print"Making changes here on github to see if it triggeres the job on Jenkins or not")

