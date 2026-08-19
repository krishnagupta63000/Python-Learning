s = int(input("Enter The Number of Seconds: "))

h = s//3600 #hours
s = s%3600 #remaining seconds

m = s//60 #mins
s = s%60

print("")