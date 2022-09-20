a = 16807
c = 0

def lcg(m):
  lcg.value = (a*lcg.value + c) % m
  return lcg.value