from machine import Machine

def turing(av):
	if (len(av) < 3):
		if (len(av) < 2):
			print("No machine data given, exiting.")
		else:
			print("No input data given, exiting.")
		return
	machine = Machine(av[1])

	machine.print_data()
	machine.start_machine(av[2])