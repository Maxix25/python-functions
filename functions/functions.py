import sys
import time
# Delay Print
def printf(sentence: str):
    # Print one character at a time
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    print()
def option(range2:int):
	while True:
		try:
			choice = int(input("Enter a option: "))
		except ValueError:
			print("You entered a non valid character...")
			continue
		if choice > range2:
			print("That's not a valid answer...")
			continue
		else:
			return choice