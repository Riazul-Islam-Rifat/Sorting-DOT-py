
def sortArray(nums):

    if len(nums) > 1:
        mid = len(nums) // 2
        left_part = nums[:mid]
        right_part = nums[mid:len(nums)]

        # Recursively calling the sortArray function
        sortArray(left_part)
        sortArray(right_part)

        # Initializing three variables
        i = j = k = 0

        # Comparing and merging
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                nums[k] = left_part[i]
                i += 1

            else:
                nums[k] = right_part[j]
                j += 1

            k += 1

        # This part will be executed when there will be some elements left in left_part List
        while i < len(left_part):
            nums[k] = left_part[i]
            i += 1
            k += 1

        # This part will be executed when there will be some elements left in right_part List
        while j < len(right_part):
            nums[k] = right_part[j]
            j += 1
            k += 1

    return nums


print(sortArray([7,8,1,0,2,33,5]))

