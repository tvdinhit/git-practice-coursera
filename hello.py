name = 'Dinh'
def say_hi(name):
	print(f'Hi {name}')



def say_hello(name):
	print(f'Hello {name}')



def say_hiya(name):
	print(f'Hiya {name}')


for func in (say_hi, say_hello, say_hiya):
	func(name)
