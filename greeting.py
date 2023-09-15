# greeting.py
#name = input("Enter your name: ")
#print(f"Hello dear {name}!")

# greeting.py
import sys

if len(sys.argv) != 2:
    print("Usage: python greeting.py <name>")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello dear {name}!")


