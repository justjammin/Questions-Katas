#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Ex 1: 
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

#Ex 2:
#Input: nums = [3,3], target = 6
#Output: [0,1]
import time

start = time.process_time_ns()
target = 9
nums = [3,2,15,7]
indices = []
for num in nums:
  noname = target - num
  if noname in nums:
    indices.append(nums.index(num))
    indices.append(nums.index(noname))
    break
else:
  indices = []
print(indices)



elapsed = (time.process_time_ns() - start)

print(elapsed/1000000000)  