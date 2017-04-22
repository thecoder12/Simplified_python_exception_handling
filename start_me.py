from lib.first_call import first_call

f = first_call()
try:
	print('I am starting the call...')
	f.first()
except Exception as e:
	print(e)