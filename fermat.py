from random import randint

# retorna (base^exp) % mod
def powerMod(base, exp, mod): # Torna a operação de exponenciação mais rápida
  # Inicia o resultado
  result = 1
  base = base % mod

  while (exp > 0):
    # Se exp é impar, o resultado é multiplicado pela base
    if (exp & 1):
      result = (result * base) % mod
    # exp é dividido por 2
    exp = exp >> 1
    base = (base * base) % mod

  return result

def fermat(n):
  # Verifica casos específicos
  if (n == 2):
    return True
  if (n < 2 or n % 2 == 0):
    return False
  
  # Faz a verificação de Fermat 10 vezes
  for _ in range(10):
    # Escolha aleatória de um número entre 2 e n - 2 para agir como base
    # randint usado para garantir bons números pseudo-aleatórios
    # os métodos contruídos nesse trabalho podem não aprensentar
    # o período ideal para gerar bons números pseudo-aleatórios
    a = randint(2, n - 2)
    # Calcula (a^(n-1)) % n
    aux = powerMod(a, n - 1, n)
    # Caso (a^(n-1)) % n != 1, n não é primo
    # conforme o teste de primalidade de Fermat
    if (aux != 1):
      return False
  # Após 10 testes, se aux != 1 para todos esses casos
  # n é provavelmente primo
  return True