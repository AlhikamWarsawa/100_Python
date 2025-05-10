# Conditional Statements, Logical Operators, Code Blocks and Scope
print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to Treasure Island.\nYour Mission is to find the Treasure")
choice = input("left or right ").lower()
if choice == "left":
    choice = input("swim or wait ").lower()
    if choice == "wait":
        choice = input("Which Door? Blue, Red or Yellow ").lower()
        if choice == "yellow":
            print("Congratulation! You Win!")
        elif choice == "red":
            print("You get Burned by Fire.\nGAME OVER")
        elif choice == "blue":
            print("You get Eaten by Beasts\nGAME OVER")
        else:
            print("GAME OVER")
    else:
        print("Attacked by Trout.\nGAME OVER")
else:
    print("Fall Into a Hole.\nGAME OVER")