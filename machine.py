from state import State
from machine_io import load_machine

class Machine:
	name = None
	blank = None
	states = []
	finals = []
	alphabet = []
	initial_state = None
	current_state = None

	def __init__(self, filename):

		data = load_machine(filename)

		# Check if data is valid (JSON was correctly parsed)
		if (data is None):
			print(f"JSON data in {filename} is not valid, exiting.")
			exit()

		self.set_header_data(data)

		for state_name in data['transitions']:
			self.states.append(State(state_name, data['transitions'][state_name]))

	def set_header_data(self, data):

		# Check if all necessary data is present.
		self.name = data['name']
		self.blank = data['blank']
		self.alphabet = data['alphabet']
		self.finals = data['finals']
		self.current_state = self.initial_state = data['initial']

	def print_data(self):
		print(f"Machine name: '{self.name}'")
		print(f"Alphabet: {self.alphabet}")

		print("States: [ ", end='')
		for state in self.states:
			print(state.name, end=', ')
		print("]")

		print(f"Initial: {self.initial_state}")

		print("Finals: [ ", end='')
		for final in self.finals:
			print(final, end=', ')
		print("]")

		for state in self.states:
			for action in state.actions:
				print(f"({state.name}, {action.read}) -> ({action.to_state}, {action.write}, {action.action})")

	def start_machine(self, input):
		print('*' * 100)

		# Start looping here.
		# Finite state machine logic creates output from boundaries given by machine data.
