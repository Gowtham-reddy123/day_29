number=int(input("enter number of primes below 100 : "))
a=[]
for x in range(2,101):
	total=0
	for y in range(1,x+1):
		if x % y == 0:
			total=total+1
	if total==2:
		a.append(x)
		if number==len(a):
			break
print(a)