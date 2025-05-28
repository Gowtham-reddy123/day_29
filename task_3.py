class Local:
	def localvariable(self):
		a="Sri"
		b="Good Will"
		c="Python"
		d="Django"
		e=a+b	
		f=c+d
		print(e)			
		print(f)
	def local(self):
		print(self)
		print()
l=Local()
l.localvariable()
l.local()