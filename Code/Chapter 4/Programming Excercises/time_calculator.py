def main():
	seconds = int(input('Enter seconds: '))
    
	if seconds < 86400:
		if seconds < 3600:
			if seconds < 60:
				print(seconds, 'seconds.')
			else:
				seconds = seconds / 60
		else:
			seconds = seconds / 3600
	else:
		seconds = seconds / 86400
	print(seconds)

main()
