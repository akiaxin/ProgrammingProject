import random

def explore():
  locations = ["your mom's basement", "under the living room couch", 
               "an abandoned castle", "a dark forest"]

  location = random.choice(locations)
  print("You enter " + location)
  