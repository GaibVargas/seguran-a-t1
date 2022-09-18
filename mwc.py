from math import floor
from time import sleep

bit_length = 32
m = 2**32
a = 16807

def mwc():
  mwc.value = (a*mwc.value + mwc.c) % m
  mwc.c = floor((a*mwc.value + mwc.c) / m)
  return mwc.value

def getRandIntBetween(max, min):
  return floor(mwc() * (max - min + 1)) + min

mwc.value = int(input("Enter a number to be seed: "))
mwc.c = 1

for i in range(10):
  # result = getRandIntBetween(2**bit_length - 1, 2**(bit_length - 1))
  result = mwc()
  print(f'Random number: {result}')
  print(f'Number of bits: {result.bit_length()}')
  sleep(2)