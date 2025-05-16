#1stcode
#getting profit of selling-buying
#a=[13,14,2,5,18,1,4]
a=[4,5,6,2,3,14,5,6,4]
b=a[0]
max_profit = 0
for i in a:
    if i<b:
        b=i
    profit = i-b
    if profit > max_profit:
        max_profit = profit
print(max_profit)


#2nd code
#sum of numbers in an array  where 1 is in matrix
ip = [8, 7, 6, 5, 2]
a = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]


for row in a:
    total = 0  
    for i in range(len(row)):
        if row[i] == 1:
            total += ip[i]  
    print(total)  

#3rd code
#number of paths to reach junction point
def rat(a,i,j,n):
    count=0
    if(a[i][j]==0 or i==n or j==n):
        return 0
    if(i==n-1 and j==n-1 and a[i][j]==1):
        return 1
    
    return rat(a,i,j+1,n)+rat(a,i+1,j,n)
    
a = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
n = len(a)
total_paths = rat(a, 0, 0, n)
print("Total paths from top-left to bottom-right:", total_paths)

#2
def rat(a,i,j,n):
    
    if i==n or j==n or a[i][j] == 0:
        return 0

    if i==n-1 and j==n-1:
        return 1

    right_paths = rat(a, i, j + 1, n)
    down_paths = rat(a, i + 1, j, n)

    return right_paths + down_paths

a = [
    [1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1]
]

n = len(a)
total_paths = rat(a, 0, 0, n)
print("Total paths from top-left to bottom-right:", total_paths)


#4th code
'''if 1 is along with another 1 as top or bottom or left or right is a land connecting and surrounded
by water is island, print the how many islands are there'''
def land(a, i, j, n):
    # Base conditions: out of bounds or water or already visited
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] == 0 or a[i][j] == 2:
        return

    # Mark the land as visited
    a[i][j] = 2

    # Visit all four directions
    land(a, i - 1, j, n)  # up
    land(a, i + 1, j, n)  # down
    land(a, i, j - 1, n)  # left
    land(a, i, j + 1, n)  # right

a = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]

n = 5
c = 0

# Traverse the matrix to count islands
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            land(a, i, j, n)
            c += 1

print("Number of islands:", c)

#2
def land(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    land(a,i-1,j,n)
    land(a,i,j-1,n)
    land(a,i+1,j,n)
    land(a,i,j+1,n)
a = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
n=5
c=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            land(a,i,j,n)
            c=c+1            
print(c)

#5th code
#to print the unburn trees
def burn(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    burn(a,i-1,j,n)
    burn(a,i,j-1,n)
    burn(a,i+1,j,n)
    burn(a,i,j+1,n)
a = [[1,0,0,1,1,1],
     [1,1,1,0,0,0],
     [0,0,1,1,1,1],
     [1,1,1,0,0,0],
     [0,0,0,0,0,1],
     [1,0,0,1,0,0]]
n=6
unburn=0
i=3
j=6
burn(a,i-1,j-1,n)
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            unburn=unburn+1            
print(unburn)


#6th code
#frog doesn't go to upwards and left it is in 2,3 position ,print how may paths are required to reach the junction point.
def frog(n,i,j,blocked):
    #if i<0 or j<0 or i>=n or j>=n:
    if(i==n or j==n or(i+1,j+1) in blocked):
        return 0
    
    if i==n-1 and j==n-1:
        return 1
    return frog(n,i+1,j,blocked) + frog(n,i,j+1,blocked)
n=5
a,b=(2,3)
blocked=[(2,1),(4,1),(5,2),(3,5)]
print(frog(n,a-1,b-1,blocked))

#7th code
#printing the binary numbers from 0 to the number
def allbinary(a, n, s=''):
    if a == -1:
        return a
    if len(s) == n:
        print(s)
        return a - 1
    a = allbinary(a, n, s + '0')
    if a != -1:
        a = allbinary(a, n, s + '1')
    return a
a = 5  # Number of binary strings to print
n = 4  # Length of binary strings
allbinary(a, n)


#8th code
#backraking
def paranth(n, opened = 0, closed = 0, s = ''):
    if opened > n or closed > n or closed > opened:
        return
    if opened == closed == n:
        print(s)
    paranth(n, opened+1, closed,s+'(')
    paranth(n, opened, closed+1, s+')')

paranth(5)