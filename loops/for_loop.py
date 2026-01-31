phones = ["apple", "samsung", "xiaomi", "oneplus", "nokia"]
for x in phones:
  print(x)


for x in "Serikzhan":
    print(x)


phones = ["apple", "samsung", "xiaomi", "oneplus", "nokia"]
for x in phones:
  print(x)
  if x == "xiaomi":
    break
  
phones = ["apple", "samsung", "xiaomi", "oneplus", "nokia"]
for x in phones:
  if x == "xiaomi":
    continue
  print(x)

for x in range(5):
    print(x)

for x in range(2, 10):
    print(x)

for x in range(2, 20, 3):
    print(x)

for x in range(6):
    print(x)
else:
        print("Loop is over")


adj = ["green", "yellow", "blackred"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

