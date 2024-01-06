def printing_designs(unprinted, completed):
	while unprinted:
		current = unprinted.pop()
		print(f"Printing model: {current.title()}")
		completed.append(current)

unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
printed_designs = []
printing_designs(unprinted_models, printed_designs)