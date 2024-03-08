# Pygame images: https://www.youtube.com/watch?v=Lw8ndzcWFFw
# CZ: main story logic || SK: pygame || CS: game functions logic

import random, sys, time, pygame
from game_functions import enemy_encounter, bear, orca, manage_inventory
from pygame.locals import QUIT
from character import Player
from locations import explore
from shared_functions import print_delay
from game_functions import enemy_encounter
delay = 0.05

# Pygame initialization/setup
pygame.init()
pygame.image.load("wave(AH).png")

# Display
def display_screen():
  width, height = 500, 500
  backgroundColor = 33,33,33
  xpos = width/2
  ypos = height/2

  screen = pygame.display.set_mode((width, height))
  loadSeal = pygame.image.load("Seal(AH).png")
  screen.blit(loadSeal, (xpos, ypos))
  pygame.display.set_caption("Seal Game")
  
while True:
  width, height = 500, 500
  xpos = width/2
  ypos = height/2
  
  display_screen()
  pygame.display.update()
  
  for event in pygame.event.get():
    if(event.type == pygame.KEYDOWN):
      if event.key == pygame.K_w:
        ypos += 10
      if event.key == pygame.K_a:
        xpos -= 10
      if event.key == pygame.K_s:
        ypos -= 10
      if event.key == pygame.K_d:
        xpos += 10

  # main logic
  def start():
    from game_functions import enemy_encounter, bear, orca, manage_inventory
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
    time.sleep(1.5)
  
    return Player(player_name)
  player = start()

  print(" ")
  print_delay("Press 1 to try and find the shore, or press 2 to explore the ocean.",delay)
  time.sleep(.5)
  choice = input("What do you want to do? ")
  
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
    print_delay("You cautiously enter the hole and look around." +
       "As you turn your head to look behind you," +
       "a giant piece of ice comes and hits you in the head!!!", delay)
    time.sleep(0.5)
    print("You died!")
    sys.exit()

  def lake_ice(lake):
    print_delay("You slowly climb on top of the frozen lake..." + "And start to waddle across...", delay)
    breaks = random.random()
    if breaks >= .5:
      print_delay("The ice broke under your blubburous body!", delay)
      print_delay("YOU DIED!", delay)
      sys.exit()
    elif breaks <= .5:
      print_delay("You safely made it across the ice!", delay)
      print_delay("You come across a curving path."+
             " As you walk along the path, it starts to get darker and snowing", delay)
      time.sleep(0.5)
      print_delay("After a while, you come across a set of footsteps." +
           " Diverging of the main path.", delay)
      footsteps = input("Do you want follow the footsteps? press 1 for yes and 2 for no")
      if footsteps == "1":
        print("You follow the footsteps and find a small cabin in the woods.")
        print("Inside you see a warm fireplace, and a delicious looking fish.")
        cabin = input("Do you want to enter the cabin? press 1 for yes and 2 for no"")
       
     
  
  def ocean():
    choice_ocean = ''
    x = 0
    print_delay("\nYou chose to explore the ocean.", delay)
    fish_chance = random.random()
    if fish_chance >= .3:
      ff()
    bleh = random.random()
    if bleh >= .5: # 50% chance to find an orca buddy :D
      print_delay("You are swimming in the ocean...", delay)
      print_delay("When suddenly an orca tries to eat you!", delay)
      enemy_encounter(player, [orca])
      print_delay("Press 1 to keep exploring, press 2 to return to shore", delay)
      choice_ocean = input("What do you want to do? ")
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
    print_delay("\nAs you come up for air, you see the outline of an island! " + 
          "You swim towards it.", delay)
    time.sleep(0.9)
    print_delay("\nWhen you get to the shore, you see a landscape swept with trees...." + 
          " it appears to be a forest!", delay)
    time.sleep(1.5)
    print_delay("\nYou go into the woods to explore...when you come across a pebbled path.", delay)
    time.sleep(0.98)
    print_delay("\nYou follow the path and come across a fork! You can either go left or right.", delay)
    time.sleep(0.6)

    # second choice
    print_delay("\nTo go left, press 3. To go right, press 4.", delay)
    lr = input("\nWhich way do you want to go? ")
    if lr == "3":
       print_delay("\nAfter a while, you come across a large bustling city...", delay)
       time.sleep(1.5)
       print_delay("\nYou decide to explore the city...", delay)
       time.sleep(0.5)
       print_delay(
           "\nYou come across a quaint shop with a sign that says: " + " " +
         "WELCOME TO THE SHOP OF MAGICAL WONDERS." + " " + " A sign with very small text says:"+
         " we specialize in (eating) seals", delay)
       time.sleep(.7)
       l_fight = input("Would you like to enter? (y/n) ")
       if l_fight == "y" or l_fight == "yes":
         print_delay("You enter the shop, and everyone falls silent...\n", delay)
         print_delay("Suddenly the shopkeeper tries to kill you! You have to fight him!", delay)
         enemy_encounter(player, [bear])
         if player.is_alive():
           print_delay("You have decided to exit the city and go the other way", delay)
       if l_fight == "n" or l_fight == "no":
        print_delay("You are walking away from the shop...", delay)
        time.sleep(0.5)
        print_delay("When you hear a voice behind you...", delay)
        print_delay("Did you think you could just walk away from the shop?-Storekeeper", delay)
        print_delay("You have to fight him!", delay)
        enemy_encounter(player, [bear])
    if lr == "4":
       print_delay("\nYou come across a large frozen lake...", delay)
       time.sleep(0.5)
       print_delay("As you look around, you find a large hole in the middle of the lake " + 
       "that leads to a way into the water...\n", delay)
       time.sleep(0.5)
       lake = input("Do you choose to go into the water and swim across?" +
                    " If not, you will have to go around the hole on the ice. (y/n)")
    
       if lake == "y" or lake == "yes":
        lakes_swim(lake)
       if lake == "n" or lake == "no":
        lake_ice(lake)

      
  if choice == "1":
    shore()
      
  if choice == "2":
    ocean()
  
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