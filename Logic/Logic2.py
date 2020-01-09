#lone_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count
#towards the sum.


# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
  sum=0
  sum+=a if a not in [b,c] else 0
  sum+=b if b not in [c,a] else 0
  sum+=c if c not in [a,b] else 0
  return sum

#lucky_sum

# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values
#to its right do not count. So for example, if b is 13, then both b and c do not count.


# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
  sum=0
  if a==13:
    sum=0
  elif b==13:
    sum=a
  elif c==13:
    sum=a+b
  else:
    if 13 not in [a,b,c]:
      sum=a+b+c
  return sum

 #no_teen_sum
  
#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- 
#then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes
#in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the
#teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  
  return fix_teen(a)+fix_teen(b)+fix_teen(c)
  
def fix_teen(n):
  return n if n not in [13,14,17,18,19] else 0


# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds 
#up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
#Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper 
#"def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().


# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10


def round_sum(a,  b, c):
  return round10(a)+round10(b)+round10(c)

def round10(num):
  n = num % 10
  if n >= 5:
    return (num - n + 10)
  else:
    return (num - n)
  
  
