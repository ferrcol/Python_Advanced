print ("Lambda function in Python")

#Square number

square = lambda x: x**2

print(f"Square of 2: {square(2)}")
print(f"Square of 5: {square(5)}")

#Use of map() and lambda

numbers = [1,2,3,4]
squares = list(map(lambda x:x**2, numbers))

print(f"Squares of {numbers}: {squares}")

#Use of filter() and lambda

evens= list(filter(lambda x:x %2 ==0, numbers))

print(f"Even numbers of {numbers}: {evens}")