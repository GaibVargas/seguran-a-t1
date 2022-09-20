from random import randint

def powerMod(base, exp, mod): # Isso aqui deixa as coisas muito rápidas
  # Initialize result
  result = 1

  # Update x if it is more than or
  # equal to p
  base = base % mod
  while (exp > 0):
    
    # If y is odd, multiply
    # x with result
    if (exp & 1):
      result = (result * base) % mod

    # y must be even now
    exp = exp >> 1 # y = y/2
    base = (base * base) % mod

  return result

def getOddPart(n):
  m = n - 1
  while (m % 2 == 0):
    m //= 2
  return m

def miller_rabbin(n):
  if (n == 2):
    return True

  if (n < 2 or n % 2 == 0):
    return False

  a = randint(1, n - 1)
  m = getOddPart(n)
  b = powerMod(a, m, n)

  if (b % n == 1):
    return True

  for _ in range(10):
    if b % n == n - 1:
      return True
    else:
      b = (b*b) % n
  return False