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

def fermat(n):
  if (n == 2):
    return "Primo"

  if (n < 2 or n % 2 == 0):
    return "Composto"
  
  for _ in range(10):
    a = randint(1, n - 2)
    aux = powerMod(a, n - 1, n)
    if (aux != 1):
      return "Composto"
  return "Provavelmente é primo"

# 47362882341088596725068562696893704769436677460225591859092704246296157080253 pseudo-primo
# 561 pseudo-primo
print(fermat(97))