'''Write a program to input an integer N from user and print pascal triangle up to N rows.
input - 3
Output 1:
1 0 0
1 1 0
1 2 1
'''


rows = 3

for i in range(rows):

    for j in range(i+1):

        print(i," ", end="")


    print()