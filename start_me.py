from lib.first_call import first_call

f = first_call()
try:
	f.first()
except Exception as e:
	print(e)