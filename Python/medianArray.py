def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        combinedArray = mergeArrays(nums1, nums2)
        countSort(combinedArray)
        middlePt = int(len(combinedArray) / 2) - 1
        median = 0.0
        if middlePt % 2 == 1:
            median = combinedArray[middlePt]
        elif middlePt % 2 == 0:
            median = (combinedArray[middlePt] + combinedArray[middlePt + 1]) / 2  
        return median

##helper function to merge two arrays
def mergeArrays(nums1: list[int], nums2: list[int])-> list[int]:
        return nums1 + nums2

#helper function to sort the merged array (counting sort)
def countSort(numbers: list[int]):
       totalSize = len(numbers)
       resultingOutput = [0] * totalSize
       initialCount = [0] * 10
       for i in range(0, totalSize):
              initialCount[numbers[i]] += 1
       for i in range(1, 10):
              initialCount[i] += initialCount[i - 1]
       i = totalSize - 1
       while i >= 0:
              resultingOutput[initialCount[numbers[i]] - 1] = numbers[i]
              initialCount[numbers[i]] -= 1
              i -=1
       for i in range(0, totalSize):
              numbers[i] = resultingOutput[i]
              
def main():
    # print(mergeArrays([1, 3], [2]))
    # print(countSort([4, 2, 2, 8, 3, 3, 1]))
    print(findMedianSortedArrays([1, 3], [2]))    


if __name__ in "__main__":
      main()