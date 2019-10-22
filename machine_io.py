import json
import os.path

def load_machine(filename):
	
	if not (os.path.exists(filename)):
		print(f"The file '{filename}' does not exist.")
		exit()

	try:
		with open(filename) as file:
			data = json.load(file)
			return (data)
	except:
		return (None)
