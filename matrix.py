start = int(input("Enter the start number: ")) #get the starting number as input from user
end = int(input("Enter the end number: "))# get the ending number as input from user

# Print the header row
print("   ", end="")
for i in range(start, end + 1):
    print(f"{i:4}", end="")
print("\n" + " " * 3 + "*" * 20)

# Print the multiplication table
for i in range(start, end + 1):
    print(f"{i:2} |", end="")
    for j in range(start, end + 1):
        print(f"{i * j:4}", end="")
    print()