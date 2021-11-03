#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#Ex. 1
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]

#Ex. 2
#Input: nums = [-7,-3,2,3,11]
#Output: [4,9,9,49,121]

nums = [anything]
squares = []

for num in nums:
  squared = num**2
  squares.append(squared)
  continue
squares.sort()
print(squares)


