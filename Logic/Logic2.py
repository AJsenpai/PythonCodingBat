#lone_sum
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
  sum=0
  sum+=a if a not in [b,c] else 0
  sum+=b if b not in [c,a] else 0
  sum+=c if c not in [a,b] else 0
  return sum
