class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        head = 0
        tail = len(numbers) - 1
        
        # Loop until head is less than or equal to tail
        while head <= tail:
            # Calculate the sum of numbers at head and tail positions
            pair_sum = numbers[head] + numbers[tail]
            # If sum is less than target, move head pointer to right
            if pair_sum < target:
                head = head + 1
            # If sum is greater than target, move tail pointer to left
            elif pair_sum > target:
                tail = tail - 1
            # If sum equals target, return indices of the two numbers
            else:
                return [head + 1, tail + 1]
        
        # If no pair is found, return [-1, -1]
        return [-1, -1]