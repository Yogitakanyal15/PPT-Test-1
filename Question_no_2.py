def repeating(str):
  for i in s:
    n=s[i+1:]
    for j in n:
      if (i==j):
        return i
  return -1
s='leetcode'
print(repeating s)
