from math import floor
from time import time

bit_length = 4096
m = 2**bit_length
a = 16807

def mwc():
  mwc.value = (a*mwc.value + mwc.c) % m
  mwc.c = floor((a*mwc.value + mwc.c) / m)
  return mwc.value

mwc.value = int(input("Enter a number to be seed: "))
mwc.c = 1

counter = 0
startTime = time()
while True:
  result = mwc()
  if (result.bit_length() >= bit_length):
    print(result)
    print(result.bit_length())
    counter += 1
  if (counter == 10):
    break
print(f"Time: {(time() - startTime) * 1000} ms")