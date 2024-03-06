# CS
import random, time
from character import Character, Enemy, Player

def enemy_encounter(player, enemies):
  for enemy in enemies:
    time.sleep(1)
    print("\nA wild " + str(enemy.name) + " appeared!")
    time.sleep(.5)

    print("Prepare for battle!")
    time.sleep(.5)
    while player.is_alive() and enemy.is_alive():
      time.sleep(.8)
      print("\n" + player.name + " HP: " + str(player.health) + " vs " 
      + enemy.name + " HP: " + str(enemy.health))

    action = input("\nEnter '1' to attack or '2' to run: ")

    if action == "1":
      player_attack(player, enemy)
      if not enemy.is_alive():
        print("\nYou defeated the " + enemy.name + "!")
      else:
        enemy_attack(player, enemy)
        if not player.is_alive():
          print("You have been defeated by the" + enemy.name + "!")
    elif action == "2":
      escape_attempt = random.choice([True, False])
      if escape_attempt:
        print("You manged to escape! You live in fear of the day you encounter " + 
              "the magnificent " + enemy.name + "again...")
        return
      else:
        print("The " + enemy.name + " caught up to you! Maybe do some more cardio!")
        time.sleep(1)
        enemy_attack(player, enemy)
    else:
        print("Invalid choice. Try again.")


orca = Enemy(name="ORCA", health=random.randint(50,70), attack=random.randint(15,30))

bear = Enemy(name="LOAF", health=random.randint(30,50), attack=random.randint(10,20))

chloe = Enemy(name="CHLOE", health=random.randint(100,1000),
              attack=random.randint(100,500))


def player_attack(player, enemy):
  hit_chance = random.random()  
  if hit_chance >= 0.2:  # 80% chance to hit
    damage = random.randint(player.attack - 2, player.attack + 3)
    enemy.health -= damage
    time.sleep(1)
    print("You attacked the " + enemy.name + " and did " + str(damage) + " damage!")
  else:
    time.sleep(1)
    print("You missed the " + enemy.name + "!")


def enemy_attack(player, enemy):
  hit_chance = random.random()
  if hit_chance >= 0.3:  # 70% chance to hit
    damage = random.randint(enemy.attack - 5, enemy.attack + 4)
    player.health -= damage
    time.sleep(1)
    print("The " + enemy.name + " attacked you and did " + str(damage) + " damage!")
  else:
    time.sleep(1)
    print("The " + enemy.name + " missed the attack!")
  if not player.is_alive():
    print("You have been defeated!")


def manage_inventory(player):
  print("Inventory:")
  for item in player.inventory:
    print("- " + item)