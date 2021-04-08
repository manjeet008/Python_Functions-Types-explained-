# Function with Keyword args
# Function with Positional args
# Function with Arbitrary arguments(*args)
# Function with Keyword Arbitrary arguments(**kwargs)
#..............................................................
# *args Returns a TUPLE
def best1(*args):
    print(args)
    for i in args:
        print(i)
best1(1,2,3,4,5,6,7,8,9,10)
#..............................................................
# **kwargs Returns a DICTIONARY
def best2(**kwargs):
	print(kwargs)
	for k,v in kwargs.items():
		print(k,v)
best2(fname="Manjeet",mname="Singh",lname="Salal")