def validate_machine_data(data):
	errors = []

	# If data has not been set, it means the JSON was not parsed correctly.
	if (data is None):
		print(f"JSON data is not valid, exiting.")
		return (False)

	# Check if all machine header variables are set correctly.
	if not data['name']:
		errors.append("HEADER_ERROR: name not set.")
	if not data['alphabet']:
		errors.append("HEADER_ERROR: alphabet not set.")
	if not data['blank']:
		errors.append("HEADER_ERROR: blank not set.")
	if not data['states']:
		errors.append("HEADER_ERROR: states not set.")
	if not data['initial']:
		errors.append("HEADER_ERROR: initial not set.")

	# Preliminary error check.
	# If the header is not formatted correctly, we don't even want to check the rest.
	if (errors):
		for e in errors:
			print(e)
		return (False)

	# Check if all final states are valid.
	if not data['finals']:
		errors.append("HEADER_ERROR: finals not set.")
	else:
		for f in data['finals']:
			if not f in data['states']:
				errors.append(f"STATE_ERROR: final {f} not a defined state.")

	# Check if all transitions states are valid.
	if not data['transitions']:
		errors.append("HEADER_ERROR: transitions not set.")
	else:
		for s in data['transitions']:
			if not s in data['states']:
				errors.append(f"STATE_ERROR: transition {s} not a defined state.")
			else:
				for i, t in enumerate(data['transitions'][s]):
					if not t['read']:
						errors.append(f"TRANSITION_ERROR: {s}{i} read not set.")
					elif not t['read'] in data['alphabet']:
						errors.append(f"TRANSITION_ERROR: {s}{i} read {t['read']} not in alphabet.")

					if not t['to_state']:
						errors.append(f"TRANSITION_ERROR: {s}{i} to_state not set.")
					elif not t['to_state'] in data['states']:
						errors.append(f"TRANSITION_ERROR: {s}{i} to_state {t['to_state']} not a valid state.")

					if not t['write']:
						errors.append(f"TRANSITION_ERROR: {s}{i} write not set.")
					elif not t['write'] in data['alphabet']:
						errors.append(f"TRANSITION_ERROR: {s}{i} write {t['write']} not in alphabet.")

					if not t['action']:
						errors.append(f"TRANSITION_ERROR: {s}{i} action not set.")
					elif (t['action'] != "LEFT" and t['action'] != "RIGHT"):
						errors.append(f"TRANSITION_ERROR: {s}{i} action {t['action']} not valid.")


	# Error printing if errors exist.
	# If they do, return False; errors have been encountered in the machine data.
	if (errors):
		for e in errors:
			print(e)
		return (False)

	# Everything checks out, return True.
	return (True)
