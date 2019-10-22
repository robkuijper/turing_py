from action import Action

class State:

	def __init__(self, name, data):
		self.name = name
		self.actions = []

		for a in data:
			self.actions.append(Action(a))
