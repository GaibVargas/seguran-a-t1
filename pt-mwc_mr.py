from mwc import mwc
from miller_rabin import miller_rabbin

bit_length = 40

mwc.value = int(input("Enter a seed number: "))
mwc.c = 1
while True:
  number = mwc(2**bit_length)
  if (number.bit_length() >= bit_length):
    is_prime_mr = miller_rabbin(number)
    if (is_prime_mr):
      print(number)
      print(number.bit_length())
      break

# counter = 0
# startTime = time()
# while True:
#   result = lcg()
#   if (result.bit_length() >= bit_length):
#     print(result)
#     print(result.bit_length())
#     counter += 1
#   if (counter == 10):
#     break
# print(f"Time: {(time() - startTime) * 1000} ms")
