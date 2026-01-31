
print("Example 1: Print only odd numbers")
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

print()


print("Example 2: Skip the number 3")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print()

print("Example 3: Print only consonants")
word = "hello"
for letter in word:
    if letter in "aeiou":
        continue
    print(letter)