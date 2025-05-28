class Method_variables:
	a=10 #static variables 
	def __init__(self,x): # constructor
		print("this is constructor method ")
		self .x=x #instance variable 
	def instance_method(self):
		print("this is the instance method ")
		print("static variable is : ",self.a)
		print("instance variable is : ",self.x)
	@classmethod 
	def class_method(cls):
		print("this is class level method ")
		print("static variable is : ",cls.a)
		d="MO"
		print("local variable is : ",d)
	@staticmethod 
	def static_method():
		print("this is static method ")
		d="ADMO"
		print("local variable is : ",d)
m=Method_variables("admou")
m.instance_method()
m.class_method()
m.static_method()