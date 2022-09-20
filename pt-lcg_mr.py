from time import time
from lcg import lcg
from miller_rabin import miller_rabbin

bit_length = 256

lcg.value = int(input("Enter a seed number: "))
startTime = time()
while True:
  number = lcg(2**bit_length)
  if (number.bit_length() >= bit_length):
    is_prime_mr = miller_rabbin(number)
    if (is_prime_mr):
      print(number)
      print(number.bit_length())
      break
print(f"Time: {(time() - startTime) * 1000} ms")
