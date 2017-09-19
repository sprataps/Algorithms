'''
Kadane's Algorithm
'''

def maximumSum():
    x=int(input("Enter the number of test cases: "))
    for i in range(x):
        min_neg=-100000000
        sum_highest=0
        flag=0
        arr=[int(x) for x in (input().split())]
        local_sum=arr[0]
        global_sum=arr[0]
        for i in range(1,len(arr)):
            local_sum=max(arr[i],local_sum+arr[i])
            global_sum=max(local_sum,global_sum)
        print(global_sum)

maximumSum()
