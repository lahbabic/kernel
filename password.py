import sys

def password():
	if len(sys.argv) < 2:
		exit()
	if "aaaa8" == sys.argv[1]:
		print(0)
		return 0
	else:
		print(1)
		return 1

password()