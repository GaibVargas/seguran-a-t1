from time import time
from lcg import lcg
from fermat import fermat

bit_length = 4096

lcg.value = int(input("Enter a seed number: "))
startTime = time()
while True:
  number = lcg(2**bit_length)
  if (number.bit_length() >= bit_length):
    is_prime_fermat = fermat(number)
    if (is_prime_fermat):
      print(number)
      print(number.bit_length())
      break
print(f"Time: {(time() - startTime) * 1000} ms")
