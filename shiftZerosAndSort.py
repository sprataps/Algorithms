def sort(arr):
    z=0
    nz=0
    while(z<len(arr) and nz<len(arr)):
        if arr[z]!=0:
            z+=1
        elif arr[z]==0:
            if arr[nz]==0:
                nz+=1
            else:
                arr[nz],arr[z]=arr[z],arr[nz]
                nz+=1
                z+=1
    print(arr)

def sortII(arr):
    z=0
    nz=0
    while(nz<len(arr) and z<len(arr)):
        while(arr[z]!=0):
            z+=1
        nz=z+1
        while(arr[nz]==0):
            nz+=1
        arr[nz],arr[z]=arr[z],arr[nz]
        nz+=1
        z+=1
    print(arr)
arr=[1,9,8,4,0,0,2,7,0,6,0,9]
sortII(arr)
