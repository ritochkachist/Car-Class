# Margarita Chistiakova
# 2/15/2023
# Car class exercise (main file with code)

restart = 1
while restart == 1:
  from Car import Car
    
  car1 = Car("Ford", 2006, "the US")
  car2 = Car("BMW", 2014, "Germany")
  car3 = Car("Tesla", 2020, "The US")
  car4 = Car("Toyota", 2004, "Japan")
  car5 = Car("Suzuki", 2013, "Japan")
  car6 = Car("Lada", 1998, "Russia")
    
  print("Hello! Welcome to our car resail shop!")
  print(f"""
  We have the following models of cars at the moment:
  1. Ford, manufactured in {car1.countryofproduction}
  2. BMW, manufactured in {car2.countryofproduction}
  3. Suzuki, manufactured in {car5.countryofproduction}
  4. Toyota, manufactured in {car4.countryofproduction}
  5. Tesla, manufactured in {car3.countryofproduction}
  6. Lada, manufactured in {car6.countryofproduction}""")
      
  print("""
  What option interested you the most? Please type your answer in this format:
  * car1
  * car2
  * car3
  * car4
  * car5
  * car6
  """)
  choice = input()
  ###Remember that all input is string
  if choice == "car1":
    print(car1.carbreak())
  elif choice == "car2":
    print(car2.drive())
  elif choice == "car3":
    print(car3.stop())
  elif choice == "car4":
    print(car4.product())
  elif choice == "car5":
    print(car5.get_year())
  elif choice == "car6":
    print(car6.donation())
  else:
    print("There is no such car. Please restart the program.")
    exit()

  print("Do you want to restart the program? 1 for 'Yes' and 2 for 'No'")
  restart = int(input())

print("Have you chosen anything? Please enter 1 for 'Yes' and 2 for 'No'")
answer = int(input())
if answer == 1:
  print("Which car did you like the most? Please enter the name of the model of the car you chose.")
  car = input()
  print(f"Great! My congratulations on puchasing this {car}!")
else:
  print("Thank you for coming! Have a good day!")

# Professor! Thank you so much for your help!
