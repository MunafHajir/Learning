'''
Sorting all array elements except one
Given an array A positive integers, sort the array in ascending order such that element at index K in unsorted array stays unmoved and all other elements are sorted.

Examples:

Input : arr[] = {10, 4, 11, 7, 6, 20}
            k = 2;
Output : arr[] = {4, 6, 11, 7, 10, 20}

Input : arr[] = {30, 20, 10}
         k = 0
Output : arr[] = {30, 10, 20}
'''

l = [2,1,5,4,7]
s = []
i = 0

key = 1

if key in l:
    i = l.index(key)
    print(i)
    
    for j in range(len(l)):
        
        if j == i:
            continue
            
        else:
            s.append(l[j])
            
    print(sorted(s))
    s.insert(i , key)
    print(s)
        
else:
    print(sorted(l))
