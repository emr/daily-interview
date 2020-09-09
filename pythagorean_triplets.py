def findPythagoreanTriplets(nums):
  numsLen = len(nums)
  nums.sort()
  for i, b in enumerate(nums):
    for j, a in enumerate(nums[i:numsLen]):
      for c in nums[j:numsLen]:
        if a*a + b*b == c*c:
          return True
  return False

print(findPythagoreanTriplets([1, 2, 3, 5]))
# False

print(findPythagoreanTriplets([1, 2, 3, 4, 5]))
# False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
