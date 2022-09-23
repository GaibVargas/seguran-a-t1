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

# Retorna a parte ímpar de (n - 1)
def getOddPart(n):
  m = n - 1
  while (m % 2 == 0):
    m //= 2
  return m

def miller_rabbin(n):
  # Verifica casos específicos
  if (n == 2):
    return True
  if (n < 2 or n % 2 == 0):
    return False

  # Escolha aleatória de um número entre 2 e n - 2 para agir como base
  # randint usado para garantir bons números pseudo-aleatórios
  # os métodos contruídos nesse trabalho podem não aprensentar
  # o período ideal para gerar bons números pseudo-aleatórios
  a = randint(2, n - 2)
  # Obtém a parte ímpar de (n - 1)
  m = getOddPart(n)
  # b = (a^m) % n
  b = powerMod(a, m, n)

  # Se b for igual a 1, n pode ser primo
  if (b % n == 1):
    return True

  # Repete teste de primalidade 10 vezes
  for _ in range(10):
    # Se b === -1 mod n, então n é provavelmente primo
    if b % n == n - 1:
      return True
    else:
      b = (b*b) % n
  return False