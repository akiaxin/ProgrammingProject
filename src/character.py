# CS
class Character:
  def __init__(self, name, health, attack):
      self.name = name
      self.health = health
      self.attack = attack

  def is_alive(self):
      return self.health > 0 

class Player(Character):
  def __init__(self, name):
    super().__init__(name, health=100, attack=10)
    self.inventory = []

class Enemy(Character):
  def __init__(self, name, health, attack):
      super().__init__(name, health, attack)
   