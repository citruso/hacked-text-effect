import time
import os

def run(string, max):
  running = string[:]
  while True:
    if len(running) < max:
      running = ' ' + running
      print(running)
      time.sleep(0.05)
      os.system('cls')
    else:
      while len(string) < len(running):
        running = running[1:]
        print(running)
        time.sleep(0.05)
        os.system('cls')

run('hello world', 80)
