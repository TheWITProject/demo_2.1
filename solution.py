import random

# You can skip Zoo if in a crunch for time
# and return to this later to demonstrate greater hierarchy.
class Zoo:
  ''' represents an entire zoo '''

  def __init__(self):
    self.catalog = {}

  def add_animal(self, animal):
    if self.catalog[animal.species]:
      self.catalog[animal.species] = []
    species_in_catalog = self.catalog.get(animal.species)
    species_in_catalog.append(animal)


class Animal:
  ''' represents a single animal '''

  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.noise = '???'
    self.weight = random.randint(5, 500) 

  def make_noise(self):
    print(f"{self.name} says {self.noise}")

  def print_weight_in_lbs(self):
    print(f"{self.name} weighs {self.weight} pounds")

  def print_weight_in_kgs(self):
    weight_in_kg = self._convert_to_kg()
    print(f"{self.name} weighs {weight_in_kg} kilograms")
  
  def _convert_to_kg(self):
    lb_in_kg = 0.453592
    weight_in_kg = weight / lb_in_kg
    return lb_in_kg

    # Errors
    # - weight is undefined
    # - weight should be multiplied by lb_in_kg
    # - we return lb_in_kg, not weight_in_kg


class Cow(Animal):
  ''' represents a single cow '''

  count_of_cows = 0

  def __init__(self, name, color_spots):
    Cow.count_of_cows += 1
    Animal.__init__(self, name, 'Cow')
    self.noise = 'Moo'
    self.color_spots = color_spots

  def grazes(self):
    print(f"{self.name} grazes")


class Pig(Animal):
  ''' represents a single pig '''

  count_of_pigs = 0

  def __init__(self, name, pet_spider):
    Pig.count_of_pigs += 1
    Animal.__init__(self, name, 'Pig')
    self.noise = 'Oink'
    self.pet_spider = pet_spider

  def roll_in_sty(self):
    print(f"{self.name} rolls in their sty")
