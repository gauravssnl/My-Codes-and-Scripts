with open('requirements.txt') as f:
	with open('requirements_without_version.txt', 'w') as g:
		for line in f:
			data = line[:line.index('=')]
			data += '\n'
			print(data)
			g.write(data)