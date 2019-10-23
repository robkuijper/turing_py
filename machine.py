from state import State
from machine_io import load_machine
from validate_machine import *

class Machine:
	name = None
	blank = None
	states = {}
	finals = []
	alphabet = []
	initial_state = None
	current_state = None

	def __init__(self, filename):

		data = load_machine(filename)

		# Try validating the machine data. If unsuccessful, exit.
		if (not validate_machine_data(data)):
			exit()		

		self.set_header_data(data)

		for state_name in data['transitions']:
			self.states[state_name] = State(state_name, data['transitions'][state_name])
		
		# Set the current state using the state list and initial state.
		self.current_state = self.states[self.initial_state]

	def set_header_data(self, data):

		# Check if all necessary data is present.
		self.name = data['name']
		self.blank = data['blank']
		self.alphabet = data['alphabet']
		self.finals = data['finals']
		self.initial_state = data['initial']

	def print_state_action(state, action):
		print(f"({state.name}, {action.read}) -> ({action.to_state}, {action.write}, {action.action})")

	def print_data(self, width):
		print('*' * width)
		print(f"*{self.name.center(width - 2)}*")
		print('*' * width)

		print(f"Alphabet: {self.alphabet}")

		print("States: ", [state for state in self.states])

		print(f"Initial: {self.initial_state}")

		print(f"Finals: {self.finals}")

		for s in self.states:
			for action in self.states[s].actions:
				Machine.print_state_action(self.states[s], action)

		print('*' * width)

	def start_parse(self, input, width):

		# Checking the input string first, seeing if every character is valid.
		for c in input:
			if not c in self.alphabet:
				print(f"Input character {c} is not in machine alphabet, exiting.")
				return

		# Start the actual input parsing.
		i = 0
		while i < len(input):

			# Printing the input string first.
			print(f"[{input[0:i]}<{input[i]}>{input[i+1:]}{self.blank * (30 - len(input))}]", end=' ')

			# Printing the current state and the read character.

			# Checking which action of the current state we need to take.
			for action in self.current_state.actions:
				if (action.read is input[i]):

					# Printing the action that is to be taken.
					Machine.print_state_action(self.current_state, action)

					# If the action is final, return out of the input parsing
					if action.to_state in self.finals:
						return

					# Executing the action.
					input = input[0:i] + action.write + input[i+1:]
					self.current_state = self.states[action.to_state]
					if (action.action == "RIGHT"):
						i += 1
					else:
						i -= 1

					# Breaking out of the action loop.
					break
