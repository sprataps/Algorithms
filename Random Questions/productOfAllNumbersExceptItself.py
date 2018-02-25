'''
Find the product of all numbers in the array except the number at the index i
'''

def product(arr,index):
    product=1
    product1=[0]*(len(arr)+1)
    product1[0]=1

    for i in range(len(arr)-1,-1,-1):
        product*=arr[i]
        product1[i+1]=product
    print(product1)

    product=1
    for i in range(len(arr)):
        product*=arr[i]
        arr[i]=product
    print(arr)

    if index==len(arr):
        return product1[index+1]
    return product1[index+1]*arr[index-2]

arr=[int(x) for x in (input("Enter array: ").split())]
index=int(input("Enter index: ")) #Index of 2 in [1,3,2] is 3
print("Product: ",product(arr,index))
