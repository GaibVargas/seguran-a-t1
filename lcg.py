# Definição de constantes do algoritmo
a = 16807
c = 0

# lcg.value atua como seed e como próximos valores gerados
# Recebe como argumento o número que limita o valor máximo
def lcg(m):
  lcg.value = (a*lcg.value + c) % m
  return lcg.value