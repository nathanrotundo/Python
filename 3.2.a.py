bottles = 99

while bottles > 0:
    if bottles == 1:
        print(f" {bottles} bottle of beer on the wall,\n{bottles} bottle of beer.")
        print("Take it down and pass it around,\nno more bottles of beer on the wall!")
    else:
        print(f"{bottles} bottles of beer on the wall,\n{bottles} bottles of beer.")
        print(f"Take one down and pass it around,\n{bottles-1} {'bottle' if bottles-1 == 1 else 'bottles'} of beer on the wall.")

    bottles -= 1
    print() 