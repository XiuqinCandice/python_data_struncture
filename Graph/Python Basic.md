
#  第一章 
# 1) reverse three digits

def reverse(x):
    res = 0
    while x > 0:
        res = res*10+x%10
        x = x // 10
    print(res)
reverse(123)

def reverse(x):
    x = str(x)
    print(int(x[::-1]))
reverse(123)

# 2) swap two variables
# use variables
def swap(x,y):
    z = x
    x = y
    y = z
    print(x,y)
# no variables
def swap(x,y):
    print('x=%s,y=%s' %(x,y))
    x = x+y
    y = x-y
    x = x-y
    print('after swapping x=%s,y=%s' %(x,y))
swap(12,23)

# no variabkes
def swap(x,y):
    x = x*y
    y = x/y
    x = x/y
    print(x,y)
swap(-2,-5)

# no variables
# the bitwise XOR operator can be used to swap two variables. 
# XOR of two numbers x and y returns a number which has all the bits as 1 wherever bits of x and y differ
# for example, XOR of 10 (in binary 1010) and 5 (in binary 0101) is 1111
# 7 (0111) and 5(0101) is (0010)

def swap(x,y):
    x = x^y
    y = x^y
    x = x^y
    print(x,y)
swap(12,45)

#################################################################
# 第二章
# 廖雪峰
# Loops, function, Objected-oriented Programming (OOP) 
# if, for, while, function definition, parameters, OOP, class
# Class, Instance, 比如student 类，实例是类创建出来的具体的对象


#################################################################3
#第三章
# In cs, a data structure is a data organization, management, and storage format that enables efficient access and modification
# A data structure is a collection of data values, the relationships among them, and the functions or operations can be applied to the data
# Array, LinkedList, Stack, Queue, Binary Tree, Binary Search Tree, Heap, Hash, Graph, Matrix, Misc, Advanced Data Structure
# 1. 线性数据结构 Linear Data Structure (Array, LinkedList, Stack, Queue)
Array: used to store homogeneous elements at contiguous locations, size of array must be provided 
Big O (time complexity):
Access time: O(1) : because elements are stored at contiguous locations
Search time: 
    O(n) : for sequential Search
    O(log n) for binary Search
Insertion time: O(n) the worst case occus when insertion happens at the beginning of an array and requires shifting all the elements
Deletion Time: O(n) the worst case occurs when deletion happens at the beginning of an array and requires shifting all the elements

--------------------------------------------------------------------------
List

List is like arrays, but doesn't need to be homogenous, a single list can contain strings, integers, objects, list can also be used for implementing stacks and queues. List are mutable
Tuple is immutable python objects, faster than list
list, tuple, dict, class, int, float are data types not data structures
data structure is a collection of data types
list comprehension
# a list of list multiplication table
a = 5
table = [[a,b,a*b] for b in range(1,11)]
result:
[[5, 1, 5], [5, 2, 10], [5, 3, 15], [5, 4, 20], [5, 5, 25], [5, 6, 30], [5, 7, 35], [5, 8, 40], [5, 9, 45]]
filter(func,iterables)
import functools
Apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value
functools.reduce(function,iterables) 
list '+' operator : concatenate two lists into a single list
a = [1] b = [2] c = a+b = [1,2]
space seperated: print(*c) or for i in c: print(i, end = ' ')
list '*' multiple the list n times and return a single list
a = [0] a*3 = [0,0,0]
index(ele,beg,end): beg and end are optional, ele is the index of first occurence of element, after beg and before end, works the same as slice
a = [1,2,3]
del lis[1:2] deletes elements in range from index a to be,works the same as slice
del a to delete the whole list
a = [1,3]
a.pop(i): deletes the elements at the position i
a.insert(v,x) insert element v at the position x 
a.remove(v) remove element v the first occurrence of the number mentioned in the arguments
a.sort() sort the list in ascending order
a.sort(reverse=True) sort the list in descending order
a.reverse() to reverse the list
reversed(a) it return a list_reverseiterator object
extend(b): this function is used to extend the list with elements present in another list. This function takes another list as its arguments
a = [1,2,3]
b = [4,5,6]
a.extend(b) --> [1,2,3,4,5,6]
a.clear() to delete all list contents 


-------------------------------------------------------
Tuples
similar to list on indexing, nested objects and repetition, but immutable
tuple1+tuple2 for concatenation
tuple3 = (tuple1,tuple2) nested Tuples
tuple5 = tuple1*5
slicing is the same as list
del tuple to delete a tuple, it has no clear() function as list
use list(a) or tuple(a) to convert list to tuple to tuple to list
a+b when b only has one element,should express as (x,)
a = (1,2,3)
b = (4,)

-------------------------------------------------------
Set 
set is unordered
set class represents the mathematical notion of a set
it is used when checking whether a specific element is in the set
it is based on a data structure hash table {}
since it is undered, we cannot use index like in the list
a = set([1,2,3])
a --> {1,2,3}
a.add(v) add element v to the set, time complexity O(1) on average, O(n) is the worst case
It is based on hash table, if multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List
set is implemeted using dummy variables using dictionary,keys being the member to the time complexity
UNION:
set1.union(set2) union() function or | operator, duplicates are removed
time complexity is O(len(set1))+O(len(set2))
Intersection:
set1.intersection(set2) or set1 & set2, time complexity is O(min(len(s1),len(s2))
Difference:
set1.difference(set2) or set1 - set2, time complexity is O(len(set1))
Clearing sets:
set1.clear() method to empty the whole set, the empty set will be set()
del set1 is to delete, print(set1) again, it will be undefined

----------------------------------------------------------------------
Array in python
Use when we only have to manipute one specific data type values

array(datatype, value list)
array('i',[1,2,3]) int array list
'f': float, 'd': double float, 'u': unicode character,...
like list: append(),insert(v,x): insert value at position x

import array
arr = array.array('i',[1,2,3])
print('The array is: ', end = ' ')
for i in range(arr):
    print(i, end=' ') # space seperated
arr.pop()
arr.remove()
index()
reverse()
arr.typecode: return the data type like 'i'
arr.itemsize: return size in bytes of a single array element
arr.buffer_info(): return a tuple like(a,b), a is the address in which array is stored, b is the number of elements
arr.count(x)
arr.extend(x)
arr.fromlist(list): append a list in the argument to the end of array, but can only apply with the same datatype
arr.tolist(): transform an array into a list
------------------------------------------------------------------
# array arrangement and rearrangement
# Given an array of N elements,(O-N-1), elements not present will be -1 in the array, rearrange an array such that arr[i] = i
# eg. arr = {-1,-1,3,2} -> [-1,-1,2,3] or {0,3,1,2} -> [0,1,2,3]
# use hashset
# 1) store all number into a hashset
# 2) if in the set, A[i] = i, else A[i] = -1
def rearrange(arr):
    set_arr = set(arr) # get the set, no repetitive elements in the set
    for i in range(len(arr)):
        if i in set_arr: 
            if arr[i] != i:
                arr[i] = i
        else:
            arr[i] = -1
    return arr
arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrange(arr))
# Time Complexity = O(n)

------------------------------------------------------------------
# Array Rotation: Write a function rotates arr[] of size n by d elements
# 1,2,3,4,5,6,7 -> 3,4,5,6,7,1,2
def rotate(arr,d,n):
    d = d%n
    arr = arr[d:n]+arr[:d]
    print(arr)
# Time complexity: O(n)
arr = [1,2,3,4,5,6,7]
rotate(arr,2,7)

# Program to cyclically rotate an array by one
# 周期性运转
arr = [1,2,3,4,5] -> [5,1,2,3,4]

def cyc_rotate(arr):
    n = len(arr)
    x = arr[n-1] #顺时针赋值要注意，list可能要reverse后反向逆时针赋值
    for i in range(n-1,0,-1): # use reverse list, otherwise the result will be [5,1,1,1,1]
        arr[i] = arr[i-1]
    arr[0] = x
    return arr
arr = [1,2,3,4,5]
# 4->5, 3->4,2->3,1->2 逆时针从队伍最后向前赋值
print(cyc_rotate(arr))
-----------------------------------------
'linear search', time complexity is O(n)
binday logarithm: log base is 2
binary search: 
    * search x in the sorted array
    * compare x with the 'middle element'
    * if x == mid, return mid index
    * else if x > mid, x lie in right half subarry
    * else recur for the left half
# find x index in arr, l is the left index, r is the right index, return the index of x in arr if present, else -1

1) recursive approach:

def binarySearch (arr, l, r, x):
    if r >= l:
        mid = (l+r)//2 # or mid = l+(r-l)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binarySearch(arr,mid+1,r,x)
        else:
            return binarySearch(arr,l,mid-1,x)
    else:
        return -1
arr = [2,3,4,10,40]
print('index:%d' %binarySearch(arr,0,len(arr)-1,10))

2) iterative approach

def binarySearch(arr, l, r, x):

    while r >= l:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
----------------------------------------------------------------
Search an element in a sorted and rotated array
an element index in a 'sorted array' can be found in O(log n) via binary search
e.g. rotate an ascending order sorted array at some pivot unknown beforehand, 1 2 3 4 5 become 3 4 5 1 2

# The main idea for finding pivot is for a ascending sorted array is to divide the array into two sub arrays and call binary search
# find the pivot, where the next element is smaller than it
# if element is greater than 0th element, then search is in the left array
# else it is in the right array
# use binary search based on the criteria above find the element index, if not in the array, return -1
# time complexity: O(logn)
def pivotBinarySearch(arr,n,x):
    #n is the size of arr
    pivot = findPivot(arr,0,n-1)
    # If we didn't find a pivot,  
    # then array is not rotated at all 
    if pivot == -1: 
        return binarySearch(arr, 0, n-1, x)
    if arr[pivot] == x:
        return pivot
    # if we find a pivot, first compare with pivot 
    # if not the pivot, we compare x with the arr[0]
    if x >= arr[0]:
        return binarySearch(arr,0,pivot-1,x)
    return binarySearch(arr,pivot+1,n-1,x)

def findPivot(arr,l,r):

    # base case
    if r < l: 
        return -1 # no pivot, sorted array
    if r == l:
        return l # only one element
    mid = (l+r)//2
    # where l != r
    if mid < r and arr[mid] > arr[mid+1]:
        return mid
    if mid > l and arr[mid] < arr[mid-1]:
        return mid-1
    if arr[l] >= arr[mid]:
        return findPivot(arr,l,mid-1)
    return findPivot(arr,mid+1,r) # unrotated array will keep call this one


def binarySearch(arr,l,r,x):

    if l <= r:
        mid = (l+r)//2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binarySearch(arr,mid+1,r,x)
        else: 
            return binarySearch(arr,l,mid-1,x)
    else:
        return -1
          

# Rotated array
arr1 = [5,6,7,8,9,10,11,12,1,2,3,4] 
n1 = len(arr1)
assert(pivotBinarySearch(arr1, n1, 3) == 10)
assert(pivotBinarySearch(arr1, n1, 4) == 11)
assert(pivotBinarySearch(arr1, n1, 7) == 2)
# Find element that doesn't exist
assert(pivotBinarySearch(arr1, n1, 520) == -1)


# Test with a sorted array, not rotated
arr2 = [1,2,3,4,5]
n2 = len(arr2)
assert(pivotBinarySearch(arr2, n2, 1) == 0)
assert(pivotBinarySearch(arr2, n2, 5) == 4)
# Find element that doesn't exist
assert(pivotBinarySearch(arr2, n2, 520) == -1)


# Test array with one element
arr3 = [1]
n3 = len(arr3)
# Find the only element
assert(pivotBinarySearch(arr3, n3, 1) == 0)
# Find element that doesn't exist
assert(pivotBinarySearch(arr3, n3, 520) == -1)

# Test array with two elements rotated
arr4 = [3,2]
n4 = len(arr4)
assert(pivotBinarySearch(arr4, n4, 3) == 0)
assert(pivotBinarySearch(arr4, n4, 2) == 1)
assert(pivotBinarySearch(arr4, n4, 520) == -1)

# Test array with two elements, not rotated
arr5 = [2,3]
n5 = len(arr5)
assert(pivotBinarySearch(arr5, n5, 3) == 1)
assert(pivotBinarySearch(arr5, n5, 2) == 0)
assert(pivotBinarySearch(arr5, n5, 520) == -1)

# Test empty array
arr6 = []
n6 = len(arr6)
assert(pivotBinarySearch(arr6, n6, 520) == -1)

-----
Search an element in an sorted array
Improved Solution
1) mid = (l+r)/2
2) if arr[mid] == x, return mid
3) elif arr[l,...,mid] is sorted
    a) if lies in [l,...mid-1], recur in here
    b) else recur for arr[mid+1, r]
4) else arr[mid,...,h] must be sorted   
    a) if lies in [mid+1,...,r], recur in here
    b) else recur [l,mid-1]

def findSortedArray(arr,l,r,x):
    if l > r:
        return -1 # x not found in the aray
    mid = (l+r)//2
    if arr[mid] == x:
        return mid # found mid, mid is the arrya
    if arr[mid] >= arr[l]: # [l,...mid] is sorted
        if x >= arr[l] and x < arr[mid]: #x lies in the range
            return findSortedArray(arr,l,mid-1,x)
        else:
            return findSortedArray(arr,mid+1,r,x) # the other range
    else: # if [l,..mid] is not sorted, [mid+1,r] must be sorted
        if x > arr[mid] and x <= arr[r]:
            return findSortedArray(arr, mid+1,r,x) # lies in the range
        else:
            return findSortedArray(arr,l,mid-1,x)
    
# Driver program 
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 4
i = findSortedArray(arr, 0, len(arr)-1, key) 
if i != -1: 
    print ("Index: %d"%i) 
else: 
    print ("Key not found") 

-----------------------------------------------------------
Given an array A[] and a number x, check if pair in A[] with sum as x 
'''
# Method 1: O(n^2)
def pair_has_sum(A,x):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i] + A[j] == x:
                return A[i],A[j]
    return -1
# test 1
A = [1, 4, 45, 6, 10, -8] 
x = 16
assert(pair_has_sum(A,x)== (6,10))
# test 2
A = [0, -1, 2, -3, 1] 
x = -2
assert(pair_has_sum(A,x)== (-3,1))

# 







        

