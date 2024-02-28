# Pygame images: https://www.youtube.com/watch?v=Lw8ndzcWFFw
# CS, CZ
import random
import sys
import time

#pygame import
import pygame
from pygame.locals import QUIT

from character import Player
from game_functions import enemy_encounter, manage_inventory
from locations import explore

# Pygame initialization/setup
pygame.init()

scrWidth, scrHeight = 500, 500
backgroundColor = 33,33,33

screen = pygame.display.set_mode((scrWidth, scrHeight))
img = pygame.image.load('Seal.png')
pygame.display.set_caption('Welcome to fishfishifhs')

while True:
  screen.fill(backgroundColor)

  pygame.display.set_mode((500,660))
  pygame.display.set_caption("Seal Game")
  loadSeal = pygame.image.load("Seal.png")
  screen.blit(loadSeal, (100, 100))
  pygame.transform.scale(loadSeal, (300, 100))
  pygame.display.update()
  break


def print_delay(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 
delay = 0.05

# Story
def start():
  print_delay("Welcome to the coolest game ever!", delay)
  time.sleep(.8)
  while True:
    player_name = input("\nEnter your character's name: ")
    if len(player_name) <= 10:
      break
    else:
      print("Name must be 10 characters or less!")
  time.sleep(.5)
  player_name = player_name.upper()
  print_delay("\nWelcome, " + str(player_name) + "!", delay)
  time.sleep(.9)
  print_delay(
      "You are a seal. You were swimming back from vacation with your family...", delay
  )
  time.sleep(1.9)
  print_delay("... when suddenly there was a big storm, and you got swept away :(", delay)
  time.sleep(1.7)
  print_delay(
      "\nYou have been separated from your family and need to find your way back.", delay
  )
  time.sleep(1.7)
  print_delay(
      "\nYou are currently in the middle of the ocean, and you need to find your "
      + "\nway back to the shore.", delay)
  time.sleep(1.5)

  return Player(player_name)
  
player = start()
print(" ")
print_delay("Press 1 to try and find the shore, or press 2 to explore the ocean.",delay)
time.sleep(.5)
choice = input("What do you want to do? ")

def ff():
  got_fish = False
  while True:
    inv = open("inventory.txt", "a")
    inv.write("fish")
    inv.close()
    print_delay("Yay! You found a fish!", delay)
    return False

def ocean():
  choice_ocean = ''
  x = 0
  print_delay("\nYou chose to explore the ocean.", delay)
  fish_chance = random.random()
  if fish_chance >= .5:
    print_delay("You found a fish!", delay)
    ff()
    print_delay("Press 1 to keep exploring, press 2 to return to shore", delay)
  else:
    print_delay("The ocean is too vast... you don't find anything.", delay)
    print_delay("Press 1 to keep exploring, press 2 to return to shore", delay)
    choice_ocean = input("What do you want to do? ")
    x+=1

  if choice_ocean == "1":
    ocean()
  if choice_ocean == "2":
     shore()

def shore():
  print_delay("\nYou choose to find the shore.", delay)
  time.sleep(0.8)
  print_delay("\nYou are searching for the shore...", delay)
  time.sleep(0.7)
  print_delay("\nAs you come up for air, you see the outline of an island!" + 
        "You swim towards it", delay)
  time.sleep(0.9)
  print_delay("\nWhen you get to the shore, you see the landscape swept with trees...." + 
        " it appears to be a forest!", delay)
  time.sleep(1.5)
  print("\nYou go into the woods to explore...when you come across a pebbled path.")
  time.sleep(0.98)
  print("\nYou follow the path and come across a fork! You can either go left or right.")
  time.sleep(0.6)
  print("\nTo go left, press 1. To go right, press 2.")
  choice_shore = input("\nWhich way do you want to go? ")

if choice == "1":
  shore()
 if choice_shore == "1":
   print("\nAfter a while, you come across a large bustling city..." )
   time.sleep(1.5)
   print("\nYou decide to explore the city...")
   time.sleep(0.5)
   print(
       "\nYou come across a large building with a sign that says: " + 
     "WELCOME TO THE SHOP OF MAGICAL WONDERS." + " A sign with very small text says"+
     "\n we specialize in (eating) seals")
     


if choice == "2":
  ocean()
  if x >= 2:
    orca = random.random()
    if orca >= .01:
      enemy_encounter(player)

def main():
 while player.is_alive():
   print("\nOptions:")
   print("1. Explore")
   print("2. Fight")
   print("3. Inventory")
   print("4. Quit")

   time.sleep(.9)
   choice = input("\nEnter your choice: ")

   if choice == "1":
     explore()
   elif choice == "2":
     enemy_encounter(player)
   elif choice == "3":
     manage_inventory(player)
   elif choice == "4":
     print("Thank you for playing!")
     break
   else:
     print("Invalid choice. Try again.")

 if __name__ == "__main__":
     main()

def inv():
 file = open("inventory.txt")
 content = file.readlines()
 print(content[0])

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
  pygame.display.update()
