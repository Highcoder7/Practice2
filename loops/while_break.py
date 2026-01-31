
import numbers


c = 0
while True:
    print(c)
    c += 1
    if c == 5:
        break


while True:
    user_input = input("Enter smth: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

nums = [2, 4, 6, 7, 8, 10]
index = 0
while index < len(nums):
    if nums[index] == 7:
        print("Found 7!")
        break
    index += 1