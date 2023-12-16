'''
#Here is a simple task. Take an array/tuple of unique positive integers, and two additional positive integers. Here's an example below: 
 
arr = (3,5,7,1,6,8,2,4) 
n = 3 # span length 
q = 13 # weight threshold 
 
Try to re-arrange arr so that the sum of any n consecutive values does not exceed q. 
 
solver(arr,n,q) ## one possible solution: (4,7,1,5,6,2,3,8) 
 
Did you succeed? Great! Now teach a computer to do it. 
Technical Details 
 
    All test inputs will be valid 
    All test cases will have 0 or more possible solutions 
    If a test case has no solution, return an empty array/tuple. Otherwise, return a valid solution 
    Test constraints: 
        2 <= n <= 6 
        4 <= arr length < 12 
        n < arr length 
        Every value in arr will be less than q 
        11 fixed tests, 25 random tests
'''
def solver(arr, n, q):
    if len(arr) < n:
        return []
    sorted_arr = sorted(arr, reverse=True) 
    result = [sorted_arr[0]] 
    for i in range(1, len(sorted_arr)):
        j = 0
        while j < len(result) - n + 1:
            subset = result[j:j+n]
            if sum(subset) + sorted_arr[i] <= q:
                result = result[:j] + [sorted_arr[i]] + result[j:]
                break
            j += 1
        if j == len(result) - n + 1:
            return [] 
    return tuple(result)
