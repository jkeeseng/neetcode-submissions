class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array,L,M,R):
            Left, right = array[L:M+1], array[M+1:R+1]
            i,j,k = 0,0,L
            while i < len(Left) and j < len(right):
              if Left[i] <= right[j]:
                  array[k] = Left[i]
                  i += 1
              else:
                  array[k] = right[j]
                  j += 1 
              k += 1
            while i < len(Left):
                array[k] = Left[i]
                i += 1
                k += 1
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        def mergesort(array, L, R):
            if L >= R:
               return 
            M = (L + R) // 2
            mergesort(array,L,M)
            mergesort(array,M+1,R)
            merge(array,L,M,R)
        mergesort(nums,0,len(nums)-1)
        return nums 
