def generate_doc(obj):
	'''
	Generates a document for provided object.
	'''

	attrs = ['	| '+'`'+k+'`'+' |'+'\n' for k, v in vars(obj).items() if not (k.startswith('_') or callable(v))]
	attrs_table = f'''

	| Attributes |
	|:----------:|
	{''.join(attrs)}
	'''

	methods = ['	| '+'`'+x+'`'+' |'+'\n' for x in dir(obj) if not x.startswith('_') and x.startswith('fetch')]
	methods_table = f'''

	| Methods |
	|:-------:|
	{''.join(methods)}
	'''


	doc = f'''
	# `simplegithub.{type(obj).__name__}`

	{obj.__doc__}

	## Attributes
	{attrs_table}

	## Methods
	{methods_table}
	'''

	return doc