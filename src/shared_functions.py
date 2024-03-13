# CS
import time

def print_delay(text, delay):
  for char in text:
      print(char, end='', flush=True)
      time.sleep(delay)
  print() 
delay = 0.05