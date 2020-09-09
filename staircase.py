def staircase(n):
  if n < 3: return n;
  return staircase(n - 1) + staircase(n - 2)

print(staircase(1))
# 1
print(staircase(2))
# 2
print(staircase(3))
# 3
print(staircase(4))
# 5
print(staircase(5))
# 8
