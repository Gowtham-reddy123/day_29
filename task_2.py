class Gowtham :
	phone="sm"#static variable
	
	def Instagram(cls):
		print("you are using Gowtham mobile",cls.phone)
class Aditya :
	def Instagram(cls):
		print("Aditya is using Gowtham",Gowtham.phone)
G=Gowtham()
G.Instagram()
A=Aditya()
A.Instagram()