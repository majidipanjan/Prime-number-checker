print("Welcome to prime number checker")
user = int(input("Please enter a number "))
num = 1
display = []
for num in range(1, user):
  remainder = user % num
  num += 1
  if remainder == 0:
    display.append(num)

# print(display)
if len(display) > 2:
  print("It's not a prime number")
elif len(display)<=2:
  print("It's a prime number")




