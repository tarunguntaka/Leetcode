


def binary_search(x,t):
    l = 0
    r = len(x)
    mid = (l+r)//2

    while l<=r:
        if x[mid]==t:
            return mid
        elif t < x[mid]:
            r = mid - 1
        else:
            l = mid + 1 
        
    return -1 

print(binary_search([1,2,3,4,5,6,7],4))
