import itertools
chrs = raw_input("enter the characters")
minlength = input("enter the minimum length")
maxlength = input("enter the maximum length")
output  = open('output.txt' , 'w+')
for i in range(minlength,maxlength+1):
	for xs in itertools.product(chrs, repeat=i):
  		words =  ''.join(xs)
		output.write("%s\n" %words)
	
output.close()
print "Word list Document created"
