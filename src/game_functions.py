# CS
import random, time
from character import Character, Enemy, Player
from shared_functions import print_delay
delay = 0.05


def enemy_encounter(player, enemies):
  for enemy in enemies:
    time.sleep(1)
    print_delay("\nA wild " + str(enemy.name) + " appeared!", delay)
    time.sleep(.5)

    print_delay("Prepare for battle!", delay)
    time.sleep(.5)
    if player.is_alive() and enemy.is_alive():
      time.sleep(.8)
      print("\n" + player.name + " HP: " + str(player.health) + " vs " 
      + enemy.name + " HP: " + str(enemy.health))

    
    while player.is_alive() and enemy.is_alive():
      action = input("\nEnter '1' to attack or '2' to escape: ") #  add a heal function with the fish

    
      if action == "1":
        player_attack(player, enemy)
        print("\n" + player.name + " HP: " + str(player.health) + " vs " 
          + enemy.name + " HP: " + str(enemy.health))
        if not enemy.is_alive():
          print_delay("\nYou defeated the " + enemy.name + "!", delay)
          return
        else:
          enemy_attack(player, enemy)
          print("\n" + player.name + " HP: " + str(player.health) + " vs " 
            + enemy.name + " HP: " + str(enemy.health))
          if not player.is_alive():
            print_delay("You have been defeated by the " + enemy.name + "!", delay)
            return

      
      elif action == "2":
        escape_attempt = random.choice([True, False])
        if escape_attempt:
          print_delay("You manged to escape! You live in fear of the day you encounter " + 
              "the magnificent " + enemy.name + "again...", delay)
          return
        else:
          print_delay("The " + enemy.name + " caught up to you! Maybe do some more cardio!", delay)
          time.sleep(1)
          enemy_attack(player, enemy)
      else:
          print_delay("Invalid choice. Try again.", delay)


orca = Enemy(name="ORCA", health=random.randint(50,70), attack=random.randint(15,30))

bear = Enemy(name="LOAF", health=random.randint(30,50), attack=random.randint(10,20))

chloe = Enemy(name="CHLOE", health=random.randint(100,1000),
attack=random.randint(100,500))



def player_attack(player, enemy):
  hit_chance = random.random()  
  if hit_chance >= 0.2:  # 80% chance to hit
    damage = random.randint(player.attack - 2, player.attack + 3)
    enemy.health -= damage
    if enemy.health < 0:
      enemy.health = 0
    time.sleep(1)
    print_delay("You attacked the " + enemy.name + " and did " + str(damage) + " damage!", delay)
  else:
    time.sleep(1)
    print_delay("You missed the " + enemy.name + "!", delay)


def enemy_attack(player, enemy):
  hit_chance = random.random()
  if hit_chance >= 0.3:  # 70% chance to hit
    damage = random.randint(enemy.attack - 5, enemy.attack + 4)
    player.health -= damage
    if player.health < 0:
      player.health = 0
    time.sleep(1)
    print_delay("The " + enemy.name + " attacked you and did " + str(damage) + " damage!", delay)
  else:
    time.sleep(1)
    print_delay("The " + enemy.name + " missed the attack!", delay)
  if not player.is_alive():
    print_delay("You have been defeated!", delay)


def manage_inventory(player):
  print("Inventory:")
  for item in player.inventory:
    print("- " + item)