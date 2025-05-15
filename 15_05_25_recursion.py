#number matching frequency
def count(x, lst):
    if not lst:
        return 0
    return (lst[0] == x) + count(x, lst[1:])

def print_freq(lst, n, d=None):
    if d is None:
        d = []
    if not lst:
        return
    if lst[0] not in d:
        freq = count(lst[0], a)  
        if freq == n:
            print(lst[0])
        d.append(lst[0])
    print_freq(lst[1:], n, d)

a = [2, 4, 6, 3, 3, 2, 6, 1, 2, 3, 6, 6, 5]
n = int(input("Enter the frequency to match: "))
print(f"Numbers that appear exactly {n} times:")
print_freq(a, n)


#2nd code
#freq number 
#functional recursion
def count_k(lst):
    if not lst:
        return 0
    if lst[0]==6:
        return 1+count_k(lst[1:])
    else:
        return  count_k(lst[1:])
lst=[2,3,3,6,5,5,9,8,8,4,6,6]
count=count_k(lst)
print(count)


#2
def freq(a,x,i=0):
    if(i==len(a)):
        return 0
    if(a[i]==x):
        return 1+freq(a,x,i+1)
    else:
        return freq(a,x,i+1)
a=[3,3,5,6,4,5,5,2,2,9,9]
x=3
print(freq(a,x))

#parameterized recusion
def freq(a,x,i=0,c=0):
    if(i==len(a)):
        return c
    if(a[i]==x):
        return freq(a,x,i+1,c+1)
    else:
        return freq(a,x,i+1,c)
a=[2,3,3,6,5,5,9,8,8,4,6,6]
x=3
print(freq(a,x))

#dictionary
def value(x,f,d,i=0):
    if(i==len(x)):
        return "not found"
    if(d[x[i]]==f):
        return x[i]
    return value(x,f,d,i+1)
def freq_d(x,f,d={},i=0):
    if(i==len(x)):
        return value(list(d.keys()),f,d)
    if(x[i] not in d):
        d[x[i]]=1
    else:
        d[x[i]]+=1
    return freq_d(x,f,d,i+1)
a=[2,3,3,6,5,5,9,8,8,4,6,6]
x=3
print(freq(a,x))


#3rd code
#subset
#printing all subsets 

def subset(x,s=[],i=0):
    if(i==len(x)):
        print(s)
        return
    subset(x,s+[x[i]],i+1)
    subset(x,s,i+1)
a=[2,3,4]
subset(a)

#4th code
#subset sum
# subset sum

def sub_set(x,k,s=[],i=0,):
    if(i==len(x)):
        if(k==0):
            print(s)
            
        return 
    
    if(x[i]<=k):
        sub_set(x,k-x[i],s+[x[i]],i+1)
    sub_set(x,k,s,i+1)
a=[1,4,5,8]
k=9
sub_set(a,k)

#2
def sub_set(x,k,i=0):
    if(k==0):
        return True
    if(i==0):
        return False
    if(x[i-1]>k):
        return sub_set(x,k,i-1) 
    return sub_set(x,k-x[i-1],i-1) or sub_set(x,k,i-1)
a = [2,4,6,8]
k = 13
print(sub_set(a, k,len(a)))


#5thcode
#minimum numbers of the sum
def sub_set(a,k,s=0,i=0,m=999999):
    if i == len(a):
        if k==0:
            if s<m:
                m=s
        return m
    if a[i]<=k:
        m=sub_set(a,k-a[i],s+1,i+1,m)
    m=sub_set(a,k,s,i+1,m)
    return m
a=[2,3,4,5]
k=9
print(sub_set(a, k))


#6thcode
#larger even small odd numbers in array
#2
l=list(map(int,input().split()))
even=0
odd=999999
for i in l:
        if i%2==0 and i>even:
            even=i
        elif i%2!=0 and i<odd:
                odd=i
print("largest even:",even,"\nsmallest odd:",odd)

#2
def leso(a):
    le,so=0,0
    for i in a:
        if i%2==0:
            if le==0 or i>le:
                le=i
        else:
            if so==0 or i<so:
                so=i
    return le,so
a=list(map(int,input().split()))
print(leso(a))















        
        
        

        
        
    




