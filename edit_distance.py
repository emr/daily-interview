def matchStrings(s1, s2):
  groups = []
  currentGroup = ''
  i = 0
  for c1 in s1:
    c2 = s2[i]
    while c1 != c2:
      i += 1
      c2 = s2[i]
    else:
      currentGroup += c1
    else:
      groups.append(currentGroup)
      currentGroup = ''
  return groups

print(matchStrings('biting', 'sitting'))
# 2

