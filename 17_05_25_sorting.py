#total codes based on bubble sort
#1st code
#bubble sort using sliding window
a= list(map(int,input().split()))
c=0#comparision count
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        c=c+1
        if a[i]>a[i+1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)
print(c)


#2code kth largets value
arr = list(map(int, input().split()))
k = int(input("Enter k: "))
c = 0
for j in range(len(arr) - 1):
    flag = False
    for i in range(len(arr) - 1 - j):
        c += 1
        if arr[i] > arr[i + 1]:
            flag = True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if not flag:
        break

print( arr)
print( arr[-k])



#3rd code
# given k value only k value elements get unsort of first k value and last k value middle elements should sort
arr=[5,2,3,8,1,6,7]
k=2
for j in range(len(arr)-2*k-1):
    f=False
    for i in range(k,len(arr)-k-1-j):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            f=True
    if f==False:
        break
print(arr)

#4th code
#sorting alphabets
a= input().split()
c=0#comparision count
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        c=c+1
        if a[i]>a[i+1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)
print(c)



#5th code
#sorting second element in every set
a= [[2, 3], [5, 1], [1, 4], [2, 7], [1, 3]]

for j in range(len(a) - 1):
    f = False
    for i in range(len(a) - 1 - j):
        if a[i][1] > a[i + 1][1]:  
            a[i], a[i + 1] = a[i + 1], a[i]
            f = True
    if not f:
        break

print(a)



#6th code
# sort in alphabetical order if two words are same till second letter print them as it is

a = ['zebra', 'cat', 'apple', 'car']
c = 0  # comparison count
for j in range(len(a) - 1):
    f = False
    for i in range(len(a) - 1 - j):
        c += 1
        # Only swap if the first 2 letters are different AND word[i] > word[i+1]
        if a[i][:2] != a[i + 1][:2] and a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            f = True
    if not f:
        break

print("Sorted list:", a)
print("Comparisons:", c)

#2
a = ['zebra', 'cat', 'apple', 'car']
for i in range(len(a) - 1):  
    f = False
    for j in range(len(a) - 1 - i):
        if a[j][0] > a[j + 1][0]:
            a[j], a[j + 1] = a[j + 1], a[j]
            f = True
        elif a[j][0] == a[j + 1][0] and a[j][1] > a[j + 1][1]: 
            a[j], a[j + 1] = a[j + 1], a[j]
            f = True
    if f == False:
        break
print(a)


#7th code
#sorting sets as prime number in it , in any index
def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            return i
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)



#8th code
# an apple a day keeps doctor away sort this statement as lendth of the words an print output as statement
a = "An apple a day keeps doctor away".split(' ')
b=[]
for i in a:
    b.append(len(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(' '.join(a))


#9th code
#bucket sorting
#printing the numbers according their frequency
a=[3,5,4,4,5,6,7,7,8,8,7,6,4,1,1,2,8,8]
d={}
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(d)
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
print(b)
for i in d.items():
    b[i[1]].append(i[0])
print(b)
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)



#10th code
#imp
'''using key -sort method'''
def qwe(x):
    return x[1]
a=[[2, 3],[5, 1],[1, 4],[2, 7],[1, 3]]
a.sort(key=qwe)
print(a)

def qwe(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            return i
    return 0
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3],[10]]
a.sort(key=qwe)
print(a)
