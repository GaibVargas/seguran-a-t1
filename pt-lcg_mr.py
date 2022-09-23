from time import time
from lcg import lcg
from miller_rabin import miller_rabbin

bit_length = 4096

# Define seed para o algoritmo LCG através do input do usuário
lcg.value = int(input("Enter a seed number: "))
# Inicia temporizador para capturar as métricas medidas
startTime = time()
# Enquanto não achar um provavel primo, faça:
while True:
  # Gera um número aleatório de no máximo bit_length bits
  number = lcg(2**bit_length)
  # Caso o número gerado tenha o número de bits desejado é feito o teste de primalidade
  if (number.bit_length() >= bit_length):
    # Verifica a primalidade do número gerado
    is_prime_mr = miller_rabbin(number)
    if (is_prime_mr):
      # Informa ao usuário o número que provavelmente é primo e sua quantia de bits
      print(number)
      print(number.bit_length())
      break
# Tempo decorrido para se encontrar o provavel primo
print(f"Time: {(time() - startTime) * 1000} ms")
