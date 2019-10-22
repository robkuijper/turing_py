import sys
from turing import turing

def print_help():
	print("usage: ft_turing [-h] jsonfile input\n\n")
	print("positional arguments:\n")
	print("\tjsonfile\t\tjson description of the machine")
	print("\tinput\t\tinput of the machine")
	print("optional arguments:\n")
	print("\t-h, --help\t\tshow this help message and exit")

if __name__ == '__main__':
	ac = len(sys.argv)

	if (ac < 2) or (sys.argv[1] == "-h") or (sys.argv[1] == "--help"):
		print_help()
	else:
		turing(sys.argv)