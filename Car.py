# Margarita Chistiakova
# 2/15/2023
# Car class exercise (class)

class Car():
  def __init__(self, car_make, car_year, countryofproduction):
    self.make = car_make
    self.year = car_year
    self.countryofproduction = countryofproduction
    

  def drive(self):
    ###This function should not print.  Instead, it should return the value..

    ###Now when you call this function it will return the statement and you can choose to print it from the main program.
    return "You tried to drive in " +  self.make + ". It is driving well."

  def stop(self):
    return "After trying out " + self.make + " you noticed, that " + self.make + " is randomly stopping without a reason. It seems like it needs more gas."

  def product(self):
    return "You heard that models of cars from " + self.countryofproduction + " are very lasting, but this particular " + self.make + " seems to be pretty old."
    
  def get_year(self):
    ###You cannot return with a variable in the middle like you can with print f.  We need to concatenate instead.
    return "The car is a "+ str(self.year) + " model. It is not too old and not so rusty."

  def carbreak(self):
    return "After the check up it turned out that the " + self.make + " car had something wrong with the engine. Please choose another one."

  def donation(self):
    return "This " + self.make + " was donated by the founder of the shop. It looks like a museum exhibit!"