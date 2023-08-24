import math
def findMedianSortedArrays(self,nums1: list[int], nums2: list[int]) -> float:
        #call my helper function to merge the two arrays
        combinedArray = mergeArrays(nums1, nums2)
        #after the arrays are merged, use the counting sort function
        mergeSort(combinedArray)
        median = 0
        #Conditionals: If the length of the combined array is even return the sum of the index (middle pt) plus its point after
        if len(combinedArray) % 2 == 0:
            median = (combinedArray[round(len(combinedArray) // 2) - 1] + combinedArray[round(len(combinedArray) // 2)]) / 2
        #If it is odd, just return the middle of the array
        elif len(combinedArray) % 2 == 1:
               median = combinedArray[math.floor(len(combinedArray) // 2)]        
        return median

##helper function to merge two arrays
def mergeArrays(nums1: list[int], nums2: list[int])-> list[int]:
        return nums1 + nums2

#helper function to sort the merged array (merge sort)
def mergeSort(numbers: list[int]):
      if(len(numbers)) > 1:
            middlept = len(numbers) // 2
            leftHalf =  numbers[:middlept]
            rightHalf = numbers[middlept:]
            mergeSort(leftHalf)
            mergeSort(rightHalf)
            i = j = k = 0
            while i < len(leftHalf) and j < len(rightHalf):
                  if leftHalf[i] < rightHalf[j]:
                        numbers[k] = leftHalf[i]
                        i +=1
                  else:
                        numbers[k] = rightHalf[j]
                        j+=1
                  k += 1
            while i < len(leftHalf):
                  numbers[k] = leftHalf[i]
                  i += 1
                  k += 1
            while j < len(rightHalf):
                  numbers[k] = rightHalf[j]
                  j +=1 
                  k +=1    
              
def main():
    # print(mergeArrays([1, 3], [2]))
    # print(countSort([4, 2, 2, 8, 3, 3, 1]))
    print(findMedianSortedArrays([1, 3], [2]))    


if __name__ in "__main__":
      main()