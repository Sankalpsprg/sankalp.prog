inp = int(input("Enter number of rows you want to print pattern of: "))
for i in range(1, inp+1):
	for j in range(1,i+1):
		print(j, end=" ")
	print()
