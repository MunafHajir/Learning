"""
Geek likes this girl Garima from his neighborhood, and wants to impress her so that she may go on a date with him. Garima is a Perfectionist and likes only PERFECT things .This makes Geek really nervous, and so Geek asks for your Help.!
Geek has baked a cake for Garima, which is basically an array of Numbers. Garima will take only a Perfect Piece of the cake.
A Perfect Piece is defined as - a subarray such that the difference between the minimum and the maximum value in that range is at most 1. Now, Since garima just loves cake, She wants a Perfect Piece Of Maximum length possible. Help Geek go on a date.!

Input
The first line of the input contains an integer T denoting the number of test cases.

The first line of each test case contains an integer n-denoting the length of the array.
The second line contains n space separated integers -denoting the cake
Output
For each testcase, output a single line containing the maximum Possible length of the subarray which is a Perfect piece
"""

"""
Example:

Input:

4
8 8 8 8
5
1 2 3 3 2
11
5 4 5 5 6 7 8 8 8 7 6

Output:
4
4
5
"""


import numpy as np
a = [5,4,5,5,6,7,8,8,8,7,6]
max_diff = 1
sub_arrays = [x for x in [a[i:j] for i in range(len(a)) for j in range(i+1, len(a))] if (max(x)-min(x) <= max_diff)]
max_sub_array = sub_arrays[np.argmax([len(sa) for sa in sub_arrays])]
print(max_sub_array)
print(len(max_sub_array))
