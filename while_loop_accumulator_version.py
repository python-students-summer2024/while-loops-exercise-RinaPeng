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
    while num_bottles > 0:
        if num_bottles > 1:
            print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
            num_bottles -= 1
            if num_bottles > 1:
                print(f"Take one down, pass it around, {num_bottles} bottles of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            break

if __name__ == "__main__":
    bottles = get_starting_number()
    sing(bottles)
