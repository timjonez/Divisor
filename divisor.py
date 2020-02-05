#Program to return all divisors of any given numer

usr_number = int(input("Enter a number:"))

limit = list(range(1,usr_number+1))

for n in limit:
	if usr_number%n == 0:
		print (n)
