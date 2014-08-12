import string
from random import choice
from sys import argv 

class Passgen:
	def __init__(self):
		pass
	def main(self,length,kind):
		cara=''
		if kind=='num':
			cara=string.digits
		elif kind=='alpha':
			cara=string.ascii_letters+string.digits
		elif kind=='all':
			cara=string.ascii_letters + string.punctuation  + string.digits
		password =  "".join(choice(cara) for x in range(int(length)))
		return password

if __name__ == '__main__':
	script,length,kind=argv
	print Passgen().main(length,kind)

