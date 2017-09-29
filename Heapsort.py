import math as m
class heapsortClass(object):

    def leftChild(self,i):
        return 2*i
    def rightChild(self,i):
        return (2*i)+1

    def minHeapify(self,nums,i,l):
        left=int(self.leftChild(i))
        right=int(self.rightChild(i))
        print (str(left) + " "  + str(right))
        if left<=l and nums[left]<nums[i]:
            largest=left
        else:
            largest=i
        if right<=l and nums[right]<nums[largest]:
            largest=right
        if largest!=i:
            temp=nums[i]
            nums[i]=nums[largest]
            nums[largest]=temp
            self.minHeapify(nums,largest,l)
        return nums

    def buildMinHeap(self,nums,l):
        print ("Length of the nums array is :" +str(l))
        for i in range((l/2),-1,-1):#l/2-1 to get the last parent who is not childless
            self.minHeapify(nums,i,l)
        return nums

    def heapsort(self,nums):
        self.buildMinHeap(nums,len(nums)-1)
        print (nums)
        numsH=[]
        i=len(nums)-1

        while( i>=2):
            temp=nums[1]
            nums[1]=nums[i]
            numsH.append(temp)
            self.minHeapify(nums,1,len(nums)-1)
            i=i-1
        return numsH

        return nums

nums=[int(x) for x in input("Enter the initial array to sort").split()]
o=heapsortClass()
nums=o.heapsort(nums)
print("Sorted array: "+ str(nums))

'''
Best , Average, Worst - O(nlogn)
Inplace
Not much stable
'''
