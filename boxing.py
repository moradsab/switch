import random
while True:
  try:
    user_input=input("please enter boxing punch between 1-6 ")
    user_input=int(user_input)
    if user_input in range(1,7):
      break
    else:
      raise ValueError()
  except ValueError:
    print("invalid input")

machine_input=random.randint(1,4)
print(machine_input)

if user_input>machine_input:
  print("you win")
elif user_input%2 != machine_input%2:
  print("you win")
else:
  print("you lose")
