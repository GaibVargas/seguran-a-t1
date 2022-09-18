from math import floor
from time import sleep

bit_length = 32
m = (2**31) - 1
a = 16807
c = 0

def lcg():
  lcg.value = (a*lcg.value + c) % m
  return lcg.value/m

def getRandIntBetween(max, min):
  return floor(lcg() * (max - min + 1)) + min

lcg.value = int(input("Enter a number to be seed: "))

for i in range(10):
  result = getRandIntBetween(2**bit_length - 1, 2**(bit_length - 1))
  print(f'Random number: {result}')
  print(f'Number of bits: {result.bit_length()}')
  sleep(2)