def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
        except ValueError:
            pass
        print("Please enter a valid number (1 or greater).")

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i > 2:
                print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")

if __name__ == "__main__":
    bottles = get_starting_number()
    sing(bottles)
