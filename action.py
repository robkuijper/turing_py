class Action:
	def __init__(self, data):
		self.read = data['read']
		self.write = data['write']
		self.action = data['action']
		self.to_state = data['to_state']
		