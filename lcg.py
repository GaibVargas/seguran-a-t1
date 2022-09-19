from time import time

bit_length = 4096
m = (2**bit_length)
a = 16807
c = 0

def lcg():
  lcg.value = (a*lcg.value + c) % m
  return lcg.value

lcg.value = int(input("Enter a seed number: "))

counter = 0
startTime = time()
while True:
  result = lcg()
  if (result.bit_length() >= bit_length):
    print(result)
    print(result.bit_length())
    counter += 1
  if (counter == 10):
    break
print(f"Time: {(time() - startTime) * 1000} ms")