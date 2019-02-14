# There are 2 sorted arrays A and B of size n each.
# Write an algorithm to find the median of the array obtained
# after merging the above 2 arrays(i.e. array of length 2n).
# The complexity should be O(log(n)).


def getMedian(arr1, arr2, n):
    total = []
    i, j = 0
    while i < n and j < n:
        if expression:
            pass


# Driver code to test above function
ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
    print("Median is ", getMedian(ar1, ar2, n1))
else:
    print("Doesn't work for arrays of unequal size")
