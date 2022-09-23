from math import floor

# Constante multiplicativa
a = 16807

# mwc.value atua como seed e como próximos valores gerados
# mwc.c é o equivalente da contante c no algoritmo LCG
  # por padrão é iniciado em 1
# Recebe como argumento o número que limita o valor máximo
def mwc(m):
  # Gera o valor aleatório
  mwc.value = (a*mwc.value + mwc.c) % m
  # Calcula novo fator de soma
  mwc.c = floor((a*mwc.value + mwc.c) / m)
  return mwc.value