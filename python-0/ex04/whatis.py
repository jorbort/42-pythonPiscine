import sys

try:
	if len(sys.argv) > 2:
		raise AssertionError("Assertionerror: more than one argument provided")
	if len(sys.argv) == 2:
		if sys.argv[1].isdigit():
			num = int(sys.argv[1])
			print("I'm Even.") if num % 2 == 0 else print("I'm Odd.")
		else:
			raise AssertionError("Assertionerror: argument is not an integer")
except AssertionError as error:
	print(error)