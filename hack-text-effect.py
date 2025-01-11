import random
import string
import time
import os

os.system('cls')

def hackEffect(size):
  block = string.ascii_letters + string.digits
  return ''.join(random.choice(block) for _ in range(size))

def hack(text):
  block = string.ascii_letters + string.digits
  for x in range(len(text)+1):
    print(text[:x] + ''.join(random.choice(block) for _ in range(len(text)))[x:])
    time.sleep(0.15)
    os.system('cls')
  print(text)

hack('hello world')
