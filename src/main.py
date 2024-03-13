# Pygame images: https://www.youtube.com/watch?v=Lw8ndzcWFFw
# CZ: main story logic || SK: pygame || CS: game functions logic

import random, sys, time, pygame

from game_functions import enemy_encounter, bear, orca, chloe, inv
from pygame.locals import QUIT
from character import Player
from locations import explore
from shared_functions import print_delay
from game_functions import enemy_encounter
from Seal import Seal
from Background import Background

delay = 0.05

# Pygame initialization/setup
pygame.init()

startScreen = True

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()

  # Display
  renderBackground = Background.setScreen.blit(Background.oceanSize,
                                          (Background.xpos, Background.ypos))
  renderSeal = Background.setScreen.blit(Seal.sealSize,
                                         (Seal.xpos, Seal.ypos))
  pygame.display.update()

  # main logic
  def start():
    yes_fish = False
    from game_functions import enemy_encounter, bear, orca, inv
    global player
    print_delay("Welcome to the coolest game ever!", delay)
    time.sleep(.8)
    if True:
      player_name = input("\nEnter your character's name: ")
    time.sleep(.5)
    player_name = player_name.upper()
    print_delay("\nWelcome, " + str(player_name) + "!", delay)
    # time.sleep(.9)
    # print_delay(
    #     "You are a seal. You were swimming back from vacation with your family...", delay
    # )
    # time.sleep(1.9)
    # print_delay("... when suddenly there was a big storm, and you got swept away :(", delay)
    # time.sleep(1.7)
    # print_delay(
    #     "\nYou have been separated from your family and need to find your way back.", delay
    # )
    # time.sleep(1.7)
    print_delay(
        "\nYou are currently in the middle of the ocean, and you need to find your "
        + "way back to the shore.", delay)
    time.sleep(0.25)
    renderSeal = Background.setScreen.blit(Seal.sealSize,
       (Seal.xpos, Seal.ypos))
    return Player(player_name)

  player = start()

  print(" ")
  print_delay(
      "Press 1 to try and find the shore, or press 2 to explore the ocean.",
      delay)
  time.sleep(.5)
  choice = input("What do you want to do? ")

  def inv():
    file = open("inventory.txt")
    content = file.readlines()
    print(content[0])
    file.close()

  # finding a fish :)
  def ff():
    got_fish = False
    while True:
      inv = open("inventory.txt", "a")
      inv.write("fish" + "\n")
      inv.close()
      print_delay("Yay! You found a fish!", delay)
      return False

  def lakes_swim(lake):
    print_delay(
        "You cautiously enter the hole and look around." +
        "As you turn your head to look behind you," +
        "a giant piece of ice comes and hits you in the head!!!", delay)
    time.sleep(0.5)
    print("You died!")
    sys.exit()

  def main_path():
    print_delay(
        "You're walking along the main path and see a cave..." +
        "It seems like something is inside the cave", delay)
    time.sleep(.5)
    print_delay(
        "Press 1 to go in the cave, or press 2 to continue on the main path",
        delay)

  def lake_ice(lake):
    print_delay(
        "You slowly climb on top of the frozen lake..." +
        "And start to waddle across...", delay)
    breaks = random.random()
    if breaks >= .9:
      print_delay("The ice broke under your blubburous body!", delay)
      print_delay("YOU DIED!", delay)
      sys.exit()
    elif breaks <= .9:
      print_delay("You safely made it across the ice!", delay)
      print_delay(
          "You come across a curving path." +
          " As you walk along the path, it starts to get darker and starts snowing.",
          delay)
      time.sleep(0.5)
      print_delay(
          "After a while, you come across a set of footsteps." +
          " Diverging of the main path.", delay)
      footsteps = input(
          "Do you want follow the footsteps? press 1 for yes and 2 for no: ")
      if footsteps == "2":
        main_path()
      if footsteps == "1":
        print_delay(
            "You follow the footsteps and find a small cabin in the woods.",
            delay)
        print_delay(
            "Inside you see a warm fireplace, and a delicious looking fish.",
            delay)
        cabin = input(
            "Do you want to enter the cabin? press 1 for yes and 2 for no: ")
        if cabin == "2":
          print_delay("You decide to return to the main path.", delay)
          main_path()
        if cabin == "1":
          print_delay(
              "You enter the cabin and find a warm fireplace." +
              "\nYou sit down and eat a delicious looking fish.", delay)
          print("YOU ATE THE FISH AND HEALED 30 HEALTH")
          player.health = player.health + 30
          print_delay(
              "The fire is so warm and nice, you end up falling asleep...",
              delay)
          print_delay(
              "When you wake up there is an angry looking man in the cabin.",
              delay)
          inv()
          print_delay("The man wants to know where his fish went", delay)
          print_delay("REMINDER: YOU ATE THE FISH", delay)
          if yes_fish == True:
            fish = input("Offer him your fish? (y/n): ")
            if fish == "y" or fish == "yes":
              print_delay(
                  "The man thanks you for the fish and gives you a rusty axe in return.",
                  delay)
              print_delay("DAMAGE +5", delay)
              player.attack = player.attack + 5
            if fish == "n" or fish == "no":
              print_delay("The man is offended and attacks you.", delay)
              enemy_encounter(player, [chloe])
              print_delay("You defeated the man!", delay)
              print_delay("He dropped a battle axe!", delay)
              print_delay("DAMAGE +15", delay)
              player.attack = player.attack + 15

  def right():
    print_delay("\nYou come across a large frozen lake...", delay)
    time.sleep(0.5)
    print_delay(
        "As you look around, you find a large hole in the middle of the lake "
        + "that leads to a way into the water...\n", delay)
    time.sleep(0.5)
    lake = input(
        "Do you choose to go into the water and swim across?" +
        " If not, you will have to go around the hole on the ice. (y/n)")

    if lake == "y" or lake == "yes":
      lakes_swim(lake)
    if lake == "n" or lake == "no":
      lake_ice(lake)

  def ocean():
    choice_ocean = ''
    x = 0
    print_delay("\nYou chose to explore the ocean.", delay)
    fish_chance = random.random()
    if fish_chance >= .3:
      ff()
      yes_fish = True
    bleh = random.random()
    if bleh >= .5:  # 50% chance to find an orca buddy :D
      print_delay("You are swimming in the ocean...", delay)
      print_delay("When suddenly an orca tries to eat you!", delay)
      enemy_encounter(player, [orca])
      print_delay("Press 1 to keep exploring, press 2 to return to shore",
                  delay)
      choice_ocean = input("What do you want to do? ")
    else:
      print_delay("The ocean is too vast... you don't find anything.", delay)
      print_delay("Press 1 to keep exploring, press 2 to return to shore",
                  delay)
      choice_ocean = input("What do you want to do? ")
      x += 1

    if choice_ocean == "1":
      ocean()
    if choice_ocean == "2":
      shore()

  def shore():
    print_delay("\nYou choose to find the shore.", delay)
    time.sleep(0.8)
    print_delay("\nYou are searching for the shore...", delay)
    time.sleep(0.7)
    print_delay(
        "\nAs you come up for air, you see the outline of an island! " +
        "You swim towards it.", delay)
    time.sleep(0.9)
    print_delay(
        "\nWhen you get to the shore, you see a landscape swept with trees...."
        + " it appears to be a forest!", delay)
    time.sleep(1.5)
    print_delay(
        "\nYou go into the woods to explore...when you come across a pebbled path.",
        delay)
    time.sleep(0.98)
    print_delay(
        "\nYou follow the path and come across a fork! You can either go left or right.",
        delay)
    time.sleep(0.6)

    # second choice
    print_delay("\nTo go left, press 3. To go right, press 4.", delay)
    lr = input("\nWhich way do you want to go? ")
    if lr == "3":
      print_delay("\nAfter a while, you come across a large bustling city...",
                  delay)
      time.sleep(1.5)
      print_delay("\nYou decide to explore the city...", delay)
      time.sleep(0.5)
      print_delay(
          "\nYou come across a quaint shop with a sign that says: " + " " +
          "WELCOME TO THE SHOP OF MAGICAL WONDERS." + " " +
          " A sign with very small text says:" +
          " we specialize in (eating) seals", delay)
      time.sleep(.7)
      l_fight = input("Would you like to enter? (y/n) ")
      if l_fight == "y" or l_fight == "yes":
        print_delay("You enter the shop, and everyone falls silent...\n",
                    delay)
        print_delay(
            "Suddenly the shopkeeper tries to kill you! You have to fight him!",
            delay)
        enemy_encounter(player, [bear])
        if player.is_alive():
          print_delay("You have decided to exit the city and go the other way",
                      delay)
          right()

      if l_fight == "n" or l_fight == "no":
        print_delay("You are walking away from the shop...", delay)
        time.sleep(0.5)
        print_delay("When you hear a voice behind you...", delay)
        print_delay("'YOU THINK YOU CAN RUN!?'", delay)
        print_delay("You have to fight him!", delay)
        enemy_encounter(player, [bear])
        if player.is_alive():
          print_delay("You have decided to exit the city and go the other way",
                      delay)
          right()
    if lr == "4":
      right()

  if choice == "1":
    shore()

  if choice == "2":
    ocean()

  print("After a very long time.... of 1 day....")
  print_delay("You have finally found the shore again!", delay)
  print(
      "You look sadly across the flat surface of the water, when you hear a faint cry..."
  )
  print("you look ahead... and you find your family crying out to you!!!")
  print("You are so happy to see them again!" +
        "You have finally found your way back home!")
  print("You have completed the game!")

  # def inv():
  #  file = open("inventory.txt")
  #  content = file.readlines()
  #  print(content[0])

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    pygame.display.update()

start()
