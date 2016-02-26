import os

# day
codes = (('.bgd', 'day'), ('.bgn', 'night'), ('.bgmn', 'midnight'))

for css_code, folder in codes:
	print('/*-----------{}------------*/'.format(folder))
	f = os.listdir(folder)
	for n, x in enumerate(f, 1):
		if x != 'Thumbs.db':
			print("{}{} {{ background-image: url({}/{}) !important; }}".format(css_code, n, folder, x))
	print('\n')