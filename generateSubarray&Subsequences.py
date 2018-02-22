'''
Print all subarrays
'''


def printSubarrays(arr):

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])
            print("\n",end="")

arr=[1,2,3,4]
n=len(arr)
print("All non-empty Subarray")

printSubarrays(arr)

def printSubsequences(arr):
    for i in range(len(arr)):
        print(arr[i])
        for j in range(i+1,len(arr)):
            print(arr[i],arr[j])
            if j!=i+1:
                print(arr[i:j+1])
printSubsequences(arr)
