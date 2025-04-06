# Binary search exercise

array1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def BinarySearch(ar, number):
    startIndex = 0
    endIndex = len(ar) - 1
    
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2
        
        if ar[midIndex] == number:
            return f"number found at index of {midIndex}"
        
        elif number > ar[midIndex]:
            startIndex = midIndex + 1
        else:
            endIndex = midIndex - 1
    
    return "number not found"

print(BinarySearch(array1, 49))
