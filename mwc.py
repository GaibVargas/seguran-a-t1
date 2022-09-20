from math import floor

a = 16807

def mwc(m):
  mwc.value = (a*mwc.value + mwc.c) % m
  mwc.c = floor((a*mwc.value + mwc.c) / m)
  return mwc.value