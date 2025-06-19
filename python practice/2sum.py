# brute force

def twosum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if((nums[i]+nums[j])==target):
                return [i,j]
            
list = [2, 7, 11, 15]
tar = 9

print(twosum(list, tar))

# optimal solution

def twoSum(arr, target):
    # Create a set to store the elements
    s = set()

    # Iterate through each element in the array
    for num in arr:
      
        # Calculate the complement that added to
        # num, equals the target
        complement = target - num

        # Check if the complement exists in the set
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False

print(twoSum(list, 13))