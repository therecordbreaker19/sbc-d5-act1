numbers = []

for i in range(4):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    
print("DISPLAYED NUMBERS: ", numbers)

bossing = input("Naa si Bossing Jared? (naa/wala): ")

if bossing.lower() == 'naa':
    removed_number = numbers.pop(0)
    print(f"Naa si Bossing Jared. Removed the first number: {removed_number}")
else:
    removed_number = numbers.pop()
    print(f"Wala si Bossing Jared. Removed the last number: {removed_number}")

print("Updated list after removal:", numbers)
