n = int(input("Enter the value of n: "))

# matrix = n*[n*[0]] --> wrong method
matrix = [[0 for j in range(n)] for i in range(n)]  #correct method
matrix1 = [[0 for j in range(n)] for i in range(n)]
# print(matrix)

l=[]
def call(a,b):
	if a==0:
		l.append(1)
		if(b==0):
			l.append(2)
		if(b==(n-1)):
			l.append(3)
		if(b>0 and b<(n-1)):
			l.append(2)
			l.append(3)
	if a==(n-1):
		l.append(0)
		if b==(n-1):
			l.append(3)
		if b==0:
			l.append(2)
		if(b>0 and b<(n-1)):
			l.append(2)
			l.append(3)
	if (a>0 and a<(n-1)):
		l.append(0)
		l.append(1)
		if b==0:
			l.append(2)
		if (b>0 and b<(n-1)):
			l.append(2)
			l.append(3)
		if (b==(n-1)):
			l.append(3)
	return (l)

def up(a,b):
	matrix[a][b]=matrix[a-1][b]
	matrix[a-1][b]=' '

def down(a,b):
	matrix[a][b]=matrix[a+1][b]
	matrix[a+1][b]=' '

def right(a,b):
	matrix[a][b]=matrix[a][b+1]
	matrix[a][b+1]=' '

def left(a,b):
	matrix[a][b]=matrix[a][b-1]
	matrix[a][b-1]=' '


def print_board():
    print('\n')
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end = "\t")
        print('\n')

def check():
    if matrix == matrix1:
        print("Congrats!")
        exit(0)

import random
data = list(range(1, n**2))
random.shuffle(data)
data.append(' ')
# print(data)

a = 0
for i in range(0, n):
    for j in range(0, n):
        # print(i, j)
        matrix[i][j] = data[a]
        # print(matrix)
        a = a + 1
        # print(a)
print_board()


data1 = list(range(1, n**2))
data1.append(' ')

b = 0
for i in range(0, n):
    for j in range(0, n):
        matrix1[i][j] = data1[b]
        b = b + 1
# print(matrix1)
print("Move the empty space to up, down, left, or right")
# print(matrix.index(1)) --> didn't work!!
# val = " "
# l = [(index, row.index(val)) for index, row in enumerate(matrix) if val in row]
# print(l)
a = b = n-1
l1 = []
while True:
    ch = int(input('Enter 0 for Up, 1 for Down, 2 for Right, 3 for Left : '))
    l1 = call(a, b)
    if ch in l1:
        if ch == 0:
            up(a, b)
            a = a - 1
            print_board()
            check()
        elif ch == 1:
            down(a, b)
            a = a + 1
            print_board()
            check()
        elif ch == 2:
            right(a, b)
            b = b + 1
            print_board()
            check()
        elif ch == 3:
            left(a, b)
            b = b - 1
            print_board()
            check()
        else:
            print("Wrong Move!")
    else:
        print("Wrong Move!")

    l1[:] = []
