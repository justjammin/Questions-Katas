#QUESTION 5
#Given array1 and array2 populated with numbers, return an array of their intersection. Each value must show the amount of times it shows in both arrays combined. Order does not matter.

#EX. 1
#Input: array1 = [1,2,2,1], array2 = [2,2]
#Output: [2,2]

#EX. 2
#Input: array1 = [4,9,5], array2 = [9,4,9,8,4]
#Output: [4,9]

import time

start = time.process_time_ns()
prices = [12,1,2,15,7,4,30]
buy = min(prices)
buy_day = prices.index(min(prices)) + 1
sell = max(prices)
sell_day = prices.index(max(prices)) + 1

print("I bought on day " + str(buy_day) + " sold on day " + str(sell_day) + " and made " + str((sell - buy)) + " dollars" )



elapsed = (time.process_time_ns() - start)

print(elapsed/1000000000)  