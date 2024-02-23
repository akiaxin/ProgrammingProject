import sys
import time

import pygame
from pygame.locals import QUIT

from character import Player
from game_functions import enemy_encounter, manage_inventory
from locations import explore


pygame.init()

width, height = 500, 500
backgroundColor = 33,33,33
screen = pygame.display.set_mode((width, height))

# while True:
#   screen.fill(backgroundColor)

#   pygame.display.set_mode((500,660))
#   pygame.display.set_caption("Welcome to the coolest game ever!")
#   loadSeal = pygame.image.load("Seal.png")
#   screen.blit(loadSeal, (50, 50))
#   pygame.display.update()
def start():
  print("Welcome to the coolest game ever!")
  time.sleep(.8)
  while True:
    player_name = input("\nEnter your character's name: ")
    if len(player_name) <= 10:
      break
    else:
      print("Name must be 10 characters or less!")
  time.sleep(.5)
  player_name = player_name.upper()
  print("\nWelcome, " + str(player_name) + "!")
  time.sleep(.9)
  print(
      "You are a seal. You were swimming back from vacation with your family..."
  )
  time.sleep(1.9)
  print("... when suddenly there was a big storm, and you got swept away :(")
  time.sleep(1.7)
  print(
      "\nYou have been separated from your family and need to find your way back."
  )
  time.sleep(1.7)
  print(
      "\nYou are currently in the middle of the ocean, and you need to find your "
      + "\nway back to the shore.")

  return Player(player_name)
player = start()


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


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
  pygame.display.update()
